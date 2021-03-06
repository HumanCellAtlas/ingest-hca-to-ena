#!/usr/bin/env bash
cd /data/Regev-ICA/data/bone-marrow/fastqs


# ls MantonBM4_*L001*I1*.fastq.gz | xargs cat >> MantonBM4_HiSeq_L001_I1_001.fastq.gz
cat MantonBM4_HiSeq_1_S25_L001_I1_001.fastq.gz MantonBM4_HiSeq_2_S26_L001_I1_001.fastq.gz MantonBM4_HiSeq_3_S27_L001_I1_001.fastq.gz MantonBM4_HiSeq_4_S28_L001_I1_001.fastq.gz MantonBM4_HiSeq_5_S29_L001_I1_001.fastq.gz MantonBM4_HiSeq_6_S30_L001_I1_001.fastq.gz MantonBM4_HiSeq_7_S31_L001_I1_001.fastq.gz MantonBM4_HiSeq_8_S32_L001_I1_001.fastq.gz > ../fastq-concat/MantonBM4_HiSeq_L001_I1_001.fastq.gz

# ls MantonBM4_*L001*R1*.fastq.gz | xargs cat >> MantonBM4_HiSeq_L001_R1_001.fastq.gz
cat MantonBM4_HiSeq_1_S25_L001_R1_001.fastq.gz MantonBM4_HiSeq_2_S26_L001_R1_001.fastq.gz MantonBM4_HiSeq_3_S27_L001_R1_001.fastq.gz MantonBM4_HiSeq_4_S28_L001_R1_001.fastq.gz MantonBM4_HiSeq_5_S29_L001_R1_001.fastq.gz MantonBM4_HiSeq_6_S30_L001_R1_001.fastq.gz MantonBM4_HiSeq_7_S31_L001_R1_001.fastq.gz MantonBM4_HiSeq_8_S32_L001_R1_001.fastq.gz > ../fastq-concat/MantonBM4_HiSeq_L001_R1_001.fastq.gz

cat MantonBM4_HiSeq_1_S25_L001_R2_001.fastq.gz MantonBM4_HiSeq_2_S26_L001_R2_001.fastq.gz MantonBM4_HiSeq_3_S27_L001_R2_001.fastq.gz MantonBM4_HiSeq_4_S28_L001_R2_001.fastq.gz MantonBM4_HiSeq_5_S29_L001_R2_001.fastq.gz MantonBM4_HiSeq_6_S30_L001_R2_001.fastq.gz MantonBM4_HiSeq_7_S31_L001_R2_001.fastq.gz MantonBM4_HiSeq_8_S32_L001_R2_001.fastq.gz > ../fastq-concat/MantonBM4_HiSeq_L001_R2_001.fastq.gz

cat MantonBM4_HiSeq_1_S25_L002_I1_001.fastq.gz MantonBM4_HiSeq_2_S26_L002_I1_001.fastq.gz MantonBM4_HiSeq_3_S27_L002_I1_001.fastq.gz MantonBM4_HiSeq_4_S28_L002_I1_001.fastq.gz MantonBM4_HiSeq_5_S29_L002_I1_001.fastq.gz MantonBM4_HiSeq_6_S30_L002_I1_001.fastq.gz MantonBM4_HiSeq_7_S31_L002_I1_001.fastq.gz MantonBM4_HiSeq_8_S32_L002_I1_001.fastq.gz > ../fastq-concat/MantonBM4_HiSeq_L002_I1_001.fastq.gz

cat MantonBM4_HiSeq_1_S25_L002_R1_001.fastq.gz MantonBM4_HiSeq_2_S26_L002_R1_001.fastq.gz MantonBM4_HiSeq_3_S27_L002_R1_001.fastq.gz MantonBM4_HiSeq_4_S28_L002_R1_001.fastq.gz MantonBM4_HiSeq_5_S29_L002_R1_001.fastq.gz MantonBM4_HiSeq_6_S30_L002_R1_001.fastq.gz MantonBM4_HiSeq_7_S31_L002_R1_001.fastq.gz MantonBM4_HiSeq_8_S32_L002_R1_001.fastq.gz > ../fastq-concat/MantonBM4_HiSeq_L002_R1_001.fastq.gz

cat MantonBM4_HiSeq_1_S25_L002_R2_001.fastq.gz MantonBM4_HiSeq_2_S26_L002_R2_001.fastq.gz MantonBM4_HiSeq_3_S27_L002_R2_001.fastq.gz MantonBM4_HiSeq_4_S28_L002_R2_001.fastq.gz MantonBM4_HiSeq_5_S29_L002_R2_001.fastq.gz MantonBM4_HiSeq_6_S30_L002_R2_001.fastq.gz MantonBM4_HiSeq_7_S31_L002_R2_001.fastq.gz MantonBM4_HiSeq_8_S32_L002_R2_001.fastq.gz > ../fastq-concat/MantonBM4_HiSeq_L002_R2_001.fastq.gz

cat MantonBM3_HiSeq_1_S17_L003_I1_001.fastq.gz MantonBM3_HiSeq_2_S18_L003_I1_001.fastq.gz MantonBM3_HiSeq_3_S19_L003_I1_001.fastq.gz MantonBM3_HiSeq_4_S20_L003_I1_001.fastq.gz MantonBM3_HiSeq_5_S21_L003_I1_001.fastq.gz MantonBM3_HiSeq_6_S22_L003_I1_001.fastq.gz MantonBM3_HiSeq_7_S23_L003_I1_001.fastq.gz MantonBM3_HiSeq_8_S24_L003_I1_001.fastq.gz  >  ../fastq-concat/MantonBM3_HiSeq_L003_I1_001.fastq.gz

cat MantonBM3_HiSeq_1_S17_L003_R1_001.fastq.gz MantonBM3_HiSeq_2_S18_L003_R1_001.fastq.gz MantonBM3_HiSeq_3_S19_L003_R1_001.fastq.gz MantonBM3_HiSeq_4_S20_L003_R1_001.fastq.gz MantonBM3_HiSeq_5_S21_L003_R1_001.fastq.gz MantonBM3_HiSeq_6_S22_L003_R1_001.fastq.gz MantonBM3_HiSeq_7_S23_L003_R1_001.fastq.gz MantonBM3_HiSeq_8_S24_L003_R1_001.fastq.gz  >  ../fastq-concat/MantonBM3_HiSeq_L003_R1_001.fastq.gz

cat MantonBM3_HiSeq_1_S17_L003_R2_001.fastq.gz MantonBM3_HiSeq_2_S18_L003_R2_001.fastq.gz MantonBM3_HiSeq_3_S19_L003_R2_001.fastq.gz MantonBM3_HiSeq_4_S20_L003_R2_001.fastq.gz MantonBM3_HiSeq_5_S21_L003_R2_001.fastq.gz MantonBM3_HiSeq_6_S22_L003_R2_001.fastq.gz MantonBM3_HiSeq_7_S23_L003_R2_001.fastq.gz MantonBM3_HiSeq_8_S24_L003_R2_001.fastq.gz  >  ../fastq-concat/MantonBM3_HiSeq_L003_R2_001.fastq.gz

cat MantonBM3_HiSeq_1_S17_L004_I1_001.fastq.gz MantonBM3_HiSeq_2_S18_L004_I1_001.fastq.gz MantonBM3_HiSeq_3_S19_L004_I1_001.fastq.gz MantonBM3_HiSeq_4_S20_L004_I1_001.fastq.gz MantonBM3_HiSeq_5_S21_L004_I1_001.fastq.gz MantonBM3_HiSeq_6_S22_L004_I1_001.fastq.gz MantonBM3_HiSeq_7_S23_L004_I1_001.fastq.gz MantonBM3_HiSeq_8_S24_L004_I1_001.fastq.gz > ../fastq-concat/MantonBM3_HiSeq_L004_I1_001.fastq.gz

cat MantonBM3_HiSeq_1_S17_L004_R1_001.fastq.gz MantonBM3_HiSeq_2_S18_L004_R1_001.fastq.gz MantonBM3_HiSeq_3_S19_L004_R1_001.fastq.gz MantonBM3_HiSeq_4_S20_L004_R1_001.fastq.gz MantonBM3_HiSeq_5_S21_L004_R1_001.fastq.gz MantonBM3_HiSeq_6_S22_L004_R1_001.fastq.gz MantonBM3_HiSeq_7_S23_L004_R1_001.fastq.gz MantonBM3_HiSeq_8_S24_L004_R1_001.fastq.gz > ../fastq-concat/MantonBM3_HiSeq_L004_R1_001.fastq.gz

cat MantonBM3_HiSeq_1_S17_L004_R2_001.fastq.gz MantonBM3_HiSeq_2_S18_L004_R2_001.fastq.gz MantonBM3_HiSeq_3_S19_L004_R2_001.fastq.gz MantonBM3_HiSeq_4_S20_L004_R2_001.fastq.gz MantonBM3_HiSeq_5_S21_L004_R2_001.fastq.gz MantonBM3_HiSeq_6_S22_L004_R2_001.fastq.gz MantonBM3_HiSeq_7_S23_L004_R2_001.fastq.gz MantonBM3_HiSeq_8_S24_L004_R2_001.fastq.gz > ../fastq-concat/MantonBM3_HiSeq_L004_R2_001.fastq.gz

