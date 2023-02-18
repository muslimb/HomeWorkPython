library(rlang)
library(tidyverse)
library(DESeq2)
library(clusterProfiler)
library(tximport)
library(rhdf5)
sample_names <- c(paste0("WT", 1:2), paste0("GM", 1:2))
run_names <- c("oxygen1",
               "oxygen2",
               "bioxygen1",
               "bioxygen2")
kallisto_dirs <- paste0("./", run_names)

samples <- data.frame(sample = sample_names,
                      condition = c(rep("WT", 2), rep("GM", 2)),
                      path = kallisto_dirs)
files <- file.path(samples$path, "abundance.h5")
txi <- tximport(files, type = 'kallisto', txOut = T)

ddsTxi <- DESeqDataSetFromTximport(txi,
                                   colData = samples,
                                   design = ~ condition)

dds <- ddsTxi[rowSums(counts(ddsTxi)) >= 10]
dds$condition <- relevel(dds$condition, ref = 'WT')

dds <- DESeq(dds)

res <- results(dds, name = 'condition_GM_vs_WT')
res[order(res$pvalue),]
sum(res$pvalue < 0.05, na.rn=TRUE)

library(pheatmap)
ntd <- normTransform(dds)

select <- order(rowMeans(counts(dds, normalized=TRUE)),
                decreasing = TRUE)[1:100]
df <- as.data.frame(colData(dds)[, "condition"])
pheatmap(assay(ntd)[select,], cluster_rows = T, show_rownames = T,
         cluster_cols = T, annotation_col=df)

plotPCA(ntd)

sign_results <- res %>%
  as.data.frame %>%
  rownames_to_column("gene_name") %>%
  mutate(ens_id = str_replace(gene_name, "_mRNA", "")) %>%
  filter(pvalue < .1)

sign_up <- sign_results %>% filter(log2FoldChange > 0)
sign_dw <- sign_results %>% filter(log2FoldChange < 0)

library(org.Sc.sgb.db)

KEGG_enrich <- enrichKEGG(sign_dw$ens_id, organism = "sce")
GO_enrich <- enrichGO(sign_up$ens_id, OrgDb = "org.Sc.sgd.db", ont = "ALL")

barplot(KEGG_enrich)
dotplot(GO_enrich)
