Reviewed Preprint

v2 • February 7, 2025

Revised by authors

Reviewed Preprint

v1 • December 2, 2024

# Computational and Systems Biology

# AI-enabled Alkaline-resistant Evolution of Protein to Apply in Mass Production

Liqi Kang, Banghao Wu, Bingxin Zhou, Pan Tan, Yun (Kenneth) Kang, Yongzhen Yan, Yi Zong, Shuang Li, Zhuo Liu , Liang Hong

School of Physics and Astronomy, Shanghai Jiao Tong University, Shanghai, China • School of Life Sciences and Biotechnology, Shanghai Jiao Tong University, Shanghai, China • Institute of Natural Sciences, Shanghai Jiao Tong University, Shanghai, China • Shanghai National Centre for Applied Mathematics (SJTU Center), MOE-LSC, Shanghai Jiao Tong University, Shanghai, China • Shanghai Artificial Intelligence Laboratory, Shanghai, China • Changchun GeneScience Pharmaceuticals Co., Ltd, Changchun, China • Zhangjiang Institute for Advanced Study, Shanghai Jiao Tong University, Shanghai, China

https://en.wikipedia.org/wiki/Open\_access

Copyright information

# eLife Assessment

This important work demonstrates the application of Pro-PRIME, a large language model, to engineer VHH antibodies with enhanced stability for extreme industrial environments. The evidence is convincing, showing through two rounds of design and experimental validation that AI-guided approaches can outperform traditional rational design methods. The solid methodology and results establish a foundation for further exploration of LLM-assisted protein engineering.

https://doi.org/10.7554/eLife.102788.2.sa2

# Abstract

Artificial intelligence (AI) models have been used to study the compositional regularities of proteins in nature, enabling it to assist in protein design to improve the efficiency of protein engineering and reduce manufacturing cost. However, in industrial settings, proteins are often required to work in extreme environments where they are relatively scarce or even non-existent in nature. Since such proteins are almost absent in the training datasets, it is uncertain whether AI model possesses the capability of evolving the protein to adapt extreme conditions. Antibodies are crucial components of affinity chromatography, and they are hoped to remain active at the extreme environments where most proteins cannot tolerate. In this study, we applied an advanced large language model (LLM), the Pro-PRIME model, to improve the alkali resistance of a representative antibody, a VHH antibody capable of binding to growth hormone. Through two rounds of design, we ensured that the selected mutant has enhanced functionality, including higher thermal stability, extreme pH resistance and stronger affinity, thereby validating the generalized capability of the LLM in meeting specific demands. To the best of our knowledge, this is the first LLM-designed protein product, which is successfully applied in mass production.

# 1. Introduction

Protein engineering, situated at the nexus of molecular biology, bioinformatics, and biotechnology, focuses on the design of proteins to introduce novel functionalities or enhance existing attributes[1 -3 ]. With the exponential growth of biological data and computational power, protein engineering has experienced a significant shift towards advanced computational methodologies, particularly deep learning, to expedite the design process and unravel complex protein-function relationships[4 -9 ]. However, a significant challenge in industrial protein engineering is designing proteins with inherent resistance to extreme conditions, such as high temperature and extreme pH environments (acidic or alkaline)[10 , 11 ]. Unlike proteins in natural ecosystems, those used in industrial processes often encounter harsh physical and chemical conditions, necessitating exceptional resilience to maintain functionality[12 , 13 ]. Previous efforts to enhance protein resistance have often relied on rational design and mutant library screening. These methods are typically labor-intensive, inefficient, and yield limited improvements[14 -17 ]. Consequently, the industrial demand for proteins resilient to harsh environments poses a notable absence within the training datasets of Artificial Intelligence (AI) models. Exploring whether AI can achieve the evolution of protein resistance to extreme environments is crucial for broadening protein applications and improving modification efficiency.

Recent advances in large-scale protein language models (LLMs) have enabled zero-shot predictions of protein mutants based on self-supervised learning from natural protein sequences[18 -21 ]. Although AI-guided protein design has been applied to predict the mutants with greater thermostability and higher activity[22 -24 ], it is unexplored whether these models based on the natural protein information can find the mutants that adapt the unnatural extreme environments, such as the alkaline solution with the pH value higher than 13.

Here, we employed a LLM (large language model) developed by our group, the Pro-PRIME model[25 ], to predict dozens of mutants of a nano-antibody against growth hormone (a VHH antibody), and examined their fitness, including alkali resistance and thermostability, to evaluate their performance under extreme environments. We utilized the Pro-PRIME model to score saturated single-point mutations of the VHH in a zero-shot setting, and selected the top 45 mutants for experimental testing. Some mutants exhibited improved alkali resistance, while others demonstrated higher thermal stability or affinity. Subsequently, we fine-tuned the Pro-PRIME model to predict dozens of multi-point mutations. As a result, we obtained three multi-point mutants with enhanced alkali resistance, higher thermostability, as well as strong affinity to the targeted protein. Also, the dynamic binding capacity of the selected mutant did not show significant decline after more than 100 cycles, making it suitable for practical application in industrial production. The selected mutant has been used in practical production and lower the cost for over one million dollars in a year. To the best of our knowledge, this is the first protein product developed by a LLM that has been successfully applied in mass production. Due to the Pro-PRIME model’s ability to achieve precise predictions of multi-point mutations with reliance on a small amount of experimental data, our two-round design process involved experimental validation of only 65 mutants in two months, demonstrating remarkable high efficiency. Furthermore, we performed a systematic analysis of these findings and determined that the model can yield more valuable predictive outcomes while remaining consistent with rational design principles. Specifically, within the framework of multi-point combinations, the model’s incorporation of negative single-point mutations into the combinatorial space led to exceptional results, showcasing its capacity to capture epistatic interactions. Notably, in striving for global optimum, deep learning methods offer distinct advantages over traditional rational design approaches.

# 2. Results and Discussion

# 2.1. Wet experimental testing of single-point mutants

Currently, the prevailing approach in protein engineering involves rational design or highthroughput screening to identify positive single-point mutations, followed by their combination into more effective multi-point mutations through greedy search methods[26 ]. However, these approaches are inclined to trap in a local optimum and unable to avoid the negative epistasis[27 , 28 ]. To overcome these limitations, we employed the Pro-PRIME model to screen single-point mutations in the first round, enabling rapid inference of scores for saturated mutations. An efficient strategy involves validating only a select number of top-ranked mutants, thereby saving considerable time and reducing economic costs compared to rational design and high-throughput experiment. Moreover, we posit that deep learning models can capture nuanced features during training, and recommend single-point mutations that expert experience may not cover. These mutants expand possibilities for subsequent combination of multi-point mutations and mitigate the risk of converging into local optima.

Specifically, we made use of the Pro-PRIME model to score the single-site saturated mutants, and selected the top 45 single-point mutants of the VHH antibody for testing. Pro-PRIME is a deep learning-based methodology developed to guide protein engineering, utilizing masked language modeling (MLM) and multi-task learning to study and comprehend the semantic and grammatical features inherent in protein sequences, and further capture the temperature traits associated with these sequences. A higher score corresponds to a greater appearance probability of the residue at this site in the Pro-PRIME model[25 ]. The alkali resistance of a mutant was determined by its half maximal effective concentration (EC50) after treatment with alkali. A lower EC50 represents that antibodies have stronger affinity. Firstly, the 45 single-point mutants were treated with 0.3 M NaOH for 24 hours, and evaluated by their thermal stability and affinity. The results revealed that 15 mutants exhibited higher alkali resistance, and 35 mutants displayed higher melting temperatures $( \mathrm { T } _ { \mathrm { m } } ) ( \mathsf { F i g u r e } \imath \mathsf { A } \sqsubseteq )$ . We also noted that 8 out of 45 single-site mutants designed by Pro-PRIME showed improved affinity as compared to the WT before alkali treatment (Figure S1). It is worth noting that six mutants (A57D, A15P, V113D, P117Q, R20T, and L12K) exhibited enhancements in all three properties, i.e., higher alkali resistance, greater thermal stability, and stronger affinity before alkali treatment. Additionally, eight mutants (P29T, N85Q, G134R, N78S, R110E, L49V, T58K, and W112F) exhibited improved alkali resistance and $\mathrm { T } _ { \mathrm { m } } ,$ albeit at the moderate cost of affinity. This trade-off is acceptable, as excessively high affinity could complicate the separation of growth hormone from the VHH. Furthermore, we subjected single-point mutants with remarkable alkali resistance to treatment with 0.5 M NaOH, and measured their affinity after 24 hours. Our findings demonstrated that four mutants (L49V, A15P, W112F, and R20T) exhibited higher affinity than the wild type following the same treatment protocol (Figure 1B ). Interestingly, these four single-point mutations all showed improvements in $\mathrm { T } _ { \mathrm { m } } ,$ and their affinities before alkali treatment were either similar to or lower than those of the wild type. However, this does not imply that enhancing thermal stability will concurrently improve alkali resistance. The spearman correlation between the EC50 values after 0.3 M NaOH treatment and $\mathrm { T _ { m } }$ values of single-point mutants is -0.29, indicating that these two properties of the antibody are only weakly correlated (Figure S3). Therefore, achieving multi-point mutants that enhance both alkali resistance and thermal stability remains a challenge.

# 2.2. Multi-point mutation design driven by experimental data

In the process of combining multiple single-site mutations, common greedy algorithms typically proceed by sequentially adding the most effective single-point mutations and gradually increasing the number of stacked mutations. However, this approach often demonstrates low efficiency and

![](images/d498b037f447ea3eb95f4d18c6b9e66763eb59ac11b4d115937edda5244d8da5.jpg)  
Figure 1.

The experimental results from two rounds of design. (A) Experimental results of single-point mutants. The melting temperatures of mutants are shown as red squares. The affinity of mutants after treatment with 0.3 M NaOH for 24 hours are shown as blue bars. (B) Experimental results of multi-point mutants and single-point mutants. The melting temperatures of mutants are shown as red squares. The affinity of single-point mutants after treatment with 0.5 M NaOH for 24 hours are shown as blue bars, while those of multi-point mutants are shown as green bars. The affinity values were normalized in the graph, with the wild-type EC50 set as 1.

is susceptible to becoming trapped in local optima. Importantly, the most effective multi-point mutations in practical scenarios may not necessarily include the most effective single-point mutations[28 ]. Moreover, in the traditional approach of incrementally stacking mutations from single points to multiple points, only paths that yield better results at each step are retained[27 ]. Nevertheless, combinations that are discarded due to decreased effectiveness may significantly enhance performance in subsequent stacking step, a phenomenon unforeseeable in traditional methods.

Although the model inference is fast, it is not feasible to explore all possible mutations when designing multi-point mutants due to the exponential increase in the number of potential combinations. To manage this challenge, we constructed a mutant library based on a two-stage design process. In the first stage, we scored all single-point mutations using the model, and in the second stage, we combined experimentally validated single-point mutations to create the multipoint mutant library. This approach ensures that even when designing multi-point mutants (e.g., five-point mutants), the number of mutants to score remains in the millions, which is computationally efficient and practical. The number of single-point mutations selected for the multi-point mutant library is a key factor influencing both the computational load and the scope of the design space. To maintain a balance between efficiency and accuracy, we limited the number of single-point mutations to between 30 and 50. This strategic approach allows us to achieve both scalability and precision in our protein engineering tasks.

To better search the global optimium, we chose the Pro-PRIME model to predict the results of multi-point mutants due to its remarkable performance on the design of diverse proteins[25 ]. We trained two Pro-PRIME models using the alkali resistance and $\mathrm { T _ { m } }$ data of single-point mutants, respectively, to score these two properties of mutants. During the prediction of multi-point mutations, we prioritized mutants with higher alkali resistance scores while ensuring $\mathrm { T _ { m } }$ scores were not lower than those of the wild type. Ultimately, we selected 20 multi-point mutants for experimentation (see details in Supporting Information, SI). Experimental results indicated that the alkali resistance of five multi-point mutants (A57D;P29T, A57D;D114Y;W112F, A15P;R20T, A15P;P117Q, and A57D;G134R;D114Y) surpassed that of the best single-point mutant. The $\mathrm { T } _ { \mathrm { m } }$ of multi-point mutants was generally higher, with the highest (P29T;A15P) exceeding that of the wild type by approximately $1 0 ~ ^ { \circ } \mathrm { C }$ (Figure 1B ). Although we did not optimize for the affinity of the VHH antibody, certain multi-point mutants (A15P;R20T, A15P;G134R, and P29T;G134R) exhibited affinity levels close to or even exceeding those of the wild type (Figure S2). Although experimental results from single-point mutations suggested that simultaneously improving the alkali resistance and thermal stability of VHH might be challenging, we successfully designed multi-point mutants that balance multiple properties. This demonstrates the excellent multi-objective optimization capability of the Pro-PRIME model.

Note that we employed different strategies for designing single-point and multi-point mutants, specifically using a zero-shot approach for single-point mutations and fine-tuning the model for multi-point mutations. These choices were made based on the distinct characteristics of the two tasks and the availability of experimental data. For single-point mutations, the number of possible mutations is relatively limited, and at the outset, there were no experimental data available. In such cases, the zero-shot setting was chosen because it allows the model to predict the fitness of mutants based solely on the information learned during pre-training on a large protein sequence dataset. Since single-point mutations are computationally manageable, this approach was deemed appropriate to generate initial predictions for protein engineering. However, when designing multi-point mutants, the situation changes significantly. The potential combinations of mutations increase exponentially, and without prior data, it becomes computationally infeasible to evaluate every possible combination within a reasonable timeframe. Moreover, by the time we reached the multi-point mutation design stage, experimental data for several single-point mutations had already been obtained. This data enabled us to fine-tune the model to better capture the specific structural and functional features that contribute to protein stability and resistance, especially in the context of multiple interacting mutations. Fine-tuning improves the model’s accuracy by adjusting its parameters to align more closely with the experimental data, ensuring that the predicted multi-point mutants are more likely to meet the desired engineering goals. After the second round of design, the fitness of the mutants was further improved. In improving alkali resistance, experimental results showed that 15 of the 45 designed mutants exhibited positive responses, yielding a success rate of 30%, close to the 35% success rate achieved in the second round. Compared to the wild type, the best single-point mutant improved alkali resistance by approximately 44.7%, while the best multi-point mutant achieved a 67.7% increase. For thermal stability enhancement, the success rate in the first round was 77.8%, rising to 100% in the second round. The top single-point mutant exhibited a $\mathrm { T _ { m } }$ increase of $6 . 3 7 ^ { \circ } \mathrm { C }$ over the wild type, while the best multi-point mutant had a $\mathrm { T } _ { \mathrm { m } }$ increase of $1 0 . 0 2 ^ { \circ } \mathrm { C }$ . We also tested the performance of the zeroshot approach for multi-point mutants, and the results showed that this method did not yield satisfactory predictions. The Spearman correlation coefficient between the zero-shot predictions and experimental results for multi-point mutants was -0.71, indicating a significant discrepancy. This further highlights the importance of fine-tuning the model for multi-point mutations, as the fine-tuned model provided more accurate and reliable results. In summary, the choice of zero-shot for single-point mutations and fine-tuning for multi-point mutations was driven by practical considerations regarding computational feasibility and the availability of experimental data. Finetuning the model significantly enhances its predictive performance, particularly for complex multi-point mutations where multiple residues interact. We believe this strategy strikes an optimal balance between computational efficiency and predictive accuracy, making it well-suited for practical protein engineering applications.

# 2.3. Complex epistatic effects generated by the combination of single-point mutations

To understand the principle of the evolution, we analyzed the improvement in multi-point mutants across three different indicators. As illustrated in Figure 2B , the evolution of thermal stability in the second round was successful, with nearly all multi-point mutants exhibiting an increase in $\mathrm { T _ { m } }$ compared to the best single-point mutant they contain. Three multi-point mutants demonstrated higher affinity than the wild type, but only P29T and G134R exhibited positive epistasis, resulting in the creation of a double-point mutant with superior affinity. Although A15P;R20T and A15P;G134R showed higher affinity than the wild type, these combinations did not contribute to affinity improvement because the A15P single-point mutation they contained exhibited stronger affinity compared to these double-point mutants.

As shown in Figure 2A , single-point mutations produced complex results during the combination process due to epistatic effects, which were unpredictable using traditional methods. A57D;P29T exhibited remarkably high alkali resistance, despite A57D and P29T being negative mutants individually. This “double negative yields positive” phenomenon also occurred in terms of affinity, where the EC50 value of P29T;G134R was approximately one-third of that of the wild type, despite both P29T and G134R caused a decrease in affinity individually, with the EC50 value of P29T being larger than that of the wild type by a factor of five. These mutation pairs are distantly located on the VHH antibody structure, making it challenging to infer the reasons for the enhanced properties after combination (Figure 3B ). Not all combinations resulted in improved mutant effects. For instance, while A15P showed high affinity and alkali resistance, adding R20T or P29T led to decrease in affinity or alkali resistance, respectively. Additionally, combining A15P with P117Q, two single mutations capable of individually enhancing affinity, resulted in a decrease in affinity.

In traditional methods, only positive single-point mutations are selected to compose the multipoint mutants and negative single-point mutations are typically avoided in multi-point combinations. However, the number of negative mutations often far exceeds that of positive mutations, thus limiting the sequence space that can be explored by traditional methods. Large

![](images/ee1468ffe7c8009e134ef58400ff34f1a30333fe5b32701792237ff7d51461db.jpg)

<details>
<summary>heatmap</summary>

| Category | Subgroup | Value 1 | Value 2 | Value 3 | Value 4 | Value 5 |
|---|---|---|---|---|---|---|
| affinity after alkali treatment | A57D;P29T | 0.32 | A57D 1.54 | P29T 1.21 | A15P 0.61 | A15P R20T 0.84 |
| affinity after alkali treatment | A15P;R20T | 0.37 | A15P 0.61 | R20T 0.84 | P29T 1.21 | A15P 0.61 |
| affinity after alkali treatment | P29T;A15P | 1.24 | P29T 1.21 | A15P 0.61 | A57D 1.54 | A57D D114Y W112F 0.70 |
| affinity before alkali treatment | P29T;G134R | 0.33 | P29T 5.35 | G134R 1.35 | A15P 0.17 | A15P R20T 0.64 |
| affinity before alkali treatment | A15P;R20T | 0.51 | A15P 0.17 | R20T 0.64 | A15P 0.17 | A15P P117Q 0.44 |
| affinity before alkali treatment | A15P;P117Q | 1.37 | A15P 0.17 | P117Q 0.44 | A57D 0.19 | A57D D114Y W112F 1.70 |
| affinity before alkali treatment | A57D;D114Y;W112F | 8.93 | A57D 0.19 | D114Y 1.25 | A57D D114Y;W112F | A57D;D114Y;W112F |
| Tm | A57D;D114Y;W112F | 47.6°C | A57D 43.3°C | D114Y 40.0°C | W112F 43.3°C | Tm 43.3°C |
| Tm | A57D;D114Y;W112F | 52.0°C | P29T 43.3°C | A15P 43.5°C | P29T 43.3°C | A57D 43.3°C |
| Tm | P29T;A15P | 50.7°C | A57D 43.3°C | P29T 43.3°C | A57D 43.3°C | A57D G34R 42.7°C |
| Tm | A57D;P29T | 50.6°C | A57D 43.3°C | G34R 42.7°C | P117Q 43.4°C | A57D;G134R;P117Q;R110E |
| Tm | A57D;G134R;P117Q;R110E | - | - | - | - | - |
The chart displays a heatmap of pairwise similarity scores between two sets of data points for each group, with values ranging from - to +52.0°C, based on the color scale from high to low fitness. The color intensity indicates the strength of the variable (e.g., high fitness = high, low fitness = low). The legend uses red for high fitness and blue for low fitness.
</details>

![](images/9572f9fad8223d9e77643d2cc969b7d93efe1ad3fa2cfc548d814ee9e7e565f7.jpg)

![](images/814ce64509f00c7123fc87fa1995958fa99cdd60cd135aca92bffe929e981836.jpg)

<details>
<summary>bar</summary>

| Category | Value |
|---|---|
| W112F | 4 |
| D114Y | 4 |
| L49V | 3 |
| R110E | 11 |
| R20T | 2 |
| P117Q | 3.5 |
| G134R | 8.5 |
| A15P | 5 |
| P29T | 3.5 |
| A57D | 13 |
</details>

Figure 2.

Schematic diagram illustrating the combined effects of single-point mutations. The colors (outer contours representing multipoint mutations and inner solid circles representing the included single-point mutations) and numerical values represent the EC50 values after alkali treatment with 0.5 M NaOH for 24 hours, the EC50 values before alkali treatment, and the ${ \sf T } _ { \sf m }$ values. Blue indicates mutations inferior to the wild type, while red indicates mutations superior to the wild type. The EC50 values before and after alkali treatment are normalized, with the wild type set to 1. (B) Experimental elvalutation of multi-point mutations. Different colors represent the proportions of improvement or decline in ${ \sf T } _ { \sf m } ,$ affinity, and alkali resistance of multipoint mutations compared to the corresponding best single-point mutations they include. (C) Distribution of the occurrences of single-point mutations included in the 20 multi-point mutation variants. The length of the bar represents the frequency of occurrence of each mutation.

![](images/1826227d958874aafaf7bebb7bcfbc071e5101e18f2187b42c3eba41fba4ddc3.jpg)

<details>
<summary>bar</summary>

| Category | Fraction of small bands |
|---|---|
| WT | 61 |
| L49V | 23 |
| G134R | 23 |
| A15P | 24 |
| N78S | 29 |
| P29T | 29 |
| P117Q | 38 |
| W112F | 38 |
| L12K | 39 |
| A57D | 40 |
| R20T | 46 |
| A57D:G134R:D114Y | 13 |
| A57D:G134R:R110E | 21 |
| P29T:G134R | 25 |
| A57D:R110E | 25 |
| A57D:G134R:R110E:L49V | 27 |
| A57D:G134R:R110E:D114Y | 28 |
| A57D:G134R:R110E:W112F | 28 |
| P29T:A15P | 28 |
| A57D:G134R:W112F | 29 |
| A57D:G134R | 30 |
| A57D:G134R:P17Q:R110E | 32 |
| A57D:R110E:W112F | 32 |
| A57D:P17Q:R110E | 35 |
| A57D:R110E:L49V | 38 |
| A57D:D114Y:W112F | 42 |
| A57D:R110E:D114Y | 43 |
| A57D:P29T | 44 |
</details>

![](images/27cf732d4f21ac756e5066674236cc1ef8e5571bc9e0b59a5064e296f4837087.jpg)

<details>
<summary>natural_image</summary>

3D protein structure diagram with labeled residues G134, P29, and A57 (no text or symbols beyond labels)
</details>

![](images/9334978354e76c8d2e79e912274493085d9f17ca02a763caf2763773d354d3fa.jpg)

<details>
<summary>text_image</summary>

C
A15P
R20T
P29T
L49V
14 15 16 17 18 19 20 21 28 29 30 48 49 50
VHH ... Q A G G S L R L ... M P E ... L L A ...
7EH3 ... Q A G G S L R L ... R T F ... F V A ...
4TV5 ... Q A G G S L R L ... R T L ... F V A ...
5IMK ... Q A G G S L R L ... R T F ... F V A ...
6WAQ ... Q A G G S L R L ... R T F ... F V A ...
</details>

Figure 3.

(A) The SDS-PAGE experimental results depict the proportion of small bands observed after alkali treatment for multi-point mutations and certain single-point mutations exhibiting relatively higher alkali resistance. (B) Structure of the VHH antibody.

(C) The multiple sequence alignment of the VHH and several homologous sequences.

language models can leverage negative mutations to generate positive multi-point mutants, surpassing the capabilities of rational design and significantly expanding the design space in protein engineering. Therefore, the Pro-PRIME method manifests significant advantages in exploring sequence space, being less susceptible to local optima, and having greater potential to find the global optimum. As depicted in Figure 2C , the 20 multi-point mutations we identified consisted of combinations of nine different single-point mutations. Although the distribution was biased, we incorporated some negative mutations that experts might consider disadvantageous, implying that the Pro-PRIME method balances the exploitation of local optima and the exploration of global optimum.

# 2.4. Reevaluating the AI predictions from a rational design perspective

In addition to interpret the multi-point mutations based on the single-site mutations, we investigated the design of VHH antibodies from a rational design perspective to understand the AI predictions. The experimental results from SDS-PAGE revealed a significant degradation of the VHH antibody following alkali treatment, with small bands accounting for up to 61.1%. This phenomenon could be attributed to the poor alkali resistance of the VHH antibody.

Mass spectrometry analysis identified specific breakage sites at Q2, Q4, G9, G10, G16, S22, S23, S26, A57, N78, N85, F101, and G134, highlighting these as ideal targets for rational design. Introducing mutations at these sites to prevent the breakdown of VHH antibodies could effectively enhance their alkali resistance. The predictions of the Pro-PRIME model align with this rationale, with 4 out of the top 10 performing single-point mutations occurring at these breakpoint sites. Experimental evidence showed that our single-point mutations could effectively reduce the proportion of small bands, and not all positive mutations locate at the breakage sites, such as P29T and A15P (Figure 3A ). Mutations identified by the model at other locations may have non-local effects, contributing to overall protein stability. In the second round of experiments, multi-point mutants exhibited an overall lower proportion of small bands, reaching as low as 13.6% (A57D;G134R;D114Y), though we did not use the experimental results of SDS-PAGE to train the model and make predictions. Thus, the improvement in the second round suggests a positive correlation between the alkali resistance of the VHH antibody and the degree of breakage after alkali treatment. Employing a rational design approach, it is plausible to identify single-point mutants with improved alkali resistance at these breakpoints. However, determining the optimal mutated residues requires conducting multiple single-point saturation mutation experiments, which is time consuming and costly. Deep learning methods can directly predict mutation types at each site, enhancing design efficiency while remaining aligned with rational design principles.

Furthermore, we analyzed the VHH antibody and homologous sequences from the perspective of evolutionary sequence alignment (Figure 3C ). The results revealed that some critical singlepoint mutations (P29T, L49V) changed original residues to more conservative ones, aligning with the “consensus sequence” method commonly used in rational design[29 ]. The Pro-PRIME model’s ability to predict such mutations is expected, given its training set contains information from homologous proteins. However, the advantage of deep learning methods extends beyond providing suggestions aligned with rational design principles; they can predict mutations contrary to expert experience. For instance, both A15 and R20 are conservative residues according to homologous sequence alignment (see Figure 3C ). Moreover, mutating A15 to proline reduces hydrogen bonds, and changing R20 to threonine contradicts empirical physicochemical properties, since arginine is more likely to form salt bridges and hydrogen bonds, benefiting stability. However, both A15P and R20T contribute to increased alkali resistance and play positive roles in subsequent multi-point combinations. This exceptional capability beyond the traditional rationaldesign principles expands the exploration space of deep learning models, aiding to approach the global optimum.

In order to gain deeper insights into the mechanisms by which the identified mutations enhance protein properties, we performed molecular dynamics (MD) simulations on the best alkaliresistant mutant. The simulation results revealed several key observations that help explain the observed improvements in protein stability and alkali resistance. As shown in Figure S4A, the twopoint mutant of A57D;P29T has a $\mathrm { T _ { m } }$ increase of around 8 °C and a much stronger binding affinity than the WT. Our analysis of the MD trajectories indicates that the A57D;P29T mutant has a more rigid structure than that of WT due to its lower root mean squared deviation (RMSD) of protein (Figure S4B). Furthermore, we calculated the root mean squared fluctuation (RMSF) for each residue, and realized that the mutant displayed less fluctuation at residue 29 but similar flexibility at residue 57. Interestingly, residues at positions 10, 108 and 118 which spatially distant from residues 29 and 57 in the mutant exhibited remarkable weakened fluctuations than those in the WT (Figure S1C), implying a more rigid structure of the mutant contributing to its improved resistance on high temperature and strong alkalinity. However, Figure S4D shows the AlphaFold3 predicted structures of the WT and the mutant are quite similar. To unveil the origin of change on structural flexibility, we computed the intramolecular interactions, such as salt bridges and hydrogen bonds for both WT and the mutant. We observed that the mutations increased the number of hydrogen bonds between the mutation sites and the rest of the protein (Figure S4E). However, the overall structure of the mutant did not show significant changes, which is also evident from the solvent-accessible surface area (SASA) analysis (Figure S4F). We also analyzed changes in salt bridges and found that although residue 57 mutated to Histidine, no new salt bridges were formed. Additionally, RMSF results showed that residues 10, 108, and 118 became more rigid, but further analysis revealed that there were no significant changes in hydrogen bonds or other interactions in these regions. Taken together, these findings suggest that the enhanced alkali resistance of the mutant is likely due to an overall increase in protein stability, rather than a dramatic change in its structural conformation. The MD simulation results, which are detailed in Figure S4, provide a deeper understanding of how specific mutations can improve protein properties and offer valuable insights for future protein engineering applications.

# 2.5. Improved acid and salt resistance simultaneously

According to the rational design principles, a protein with enhanced intramolecular interactions can resist various stress, including high temperature, strong alkali, strong acid, concentrated salt, etc.[30 , 31 ] Hence, we expected that the mutants with higher thermal stability and alkali resistance can tolerate acidic and saline environments as well. We evaluated the binding affinity of the mutants to the target protein under elution with saline (1 M NaCl) or acidic (20 mM citric acid) solutions to characterize their salt-induced and acid-induced dissociation abilities.

Additionally, we assessed the acid resistance of the mutants by measuring their affinity after a 48- hour treatment with 1 M ethanoic acid (see details in SI). Figure 4 shows the acid and salt resistance of the selected multi-point mutants with higher thermal stability and stronger alkali resistance. It is noteworthy that the Pro-PRIME model can provide us the mutants, such as A57D;P29T and A15P;R20T, with strong resistance on acid and salt (Figure 4A ) as well as high temperature and alkali resistance (Figure 2B ). Our design enhances protein stability while retaining other properties such as affinity, thereby endowing the mutant with the potential for application in industrial production.

# 2.6. Application in industrial production

The Pro-PRIME method can predict multi-site mutants using a small amount of experimental data, and the entire design process can be completed within two months. This method has the potential to empower industrial production due to its relatively low economic and time costs. Our mutants have already been widely applied in the purification process of growth hormones. Figure 4B shows the ratio of the residual dynamic binding capacity (DBC) after 0.5 M NaOH treatment for 6 hours and 24 hours to the residual DBC before treatment for various mutants and the wild type. The wild type experienced a 74.1% loss in the residual DBC after 6 hours of alkali treatment, and

![](images/85758413f89c57d544a7f2771a5ce938d06363e5013fa21f2edd16e180b9d94d.jpg)  
Figure 4.   
(A) The tolerance of acid dissociation and salt dissociation, and the acid resistance of multi-point mutations with strong alkali resistance. All EC50 values are normalized, with the wild type set to 1. (B) Experiment results of residual dynamic binding capacity (DBC) at 10% breakthrough. The bars represent the ratio of the residual DBC after 0.5 M NaOH treatment for 6 hours and 24 hours to the residual DBC before treatment for multi-site mutants and the wild type. (C) Yield in affinity chromatography and the corresponding number of cycles. This figure illustrates the variation in yield during affinity chromatography across multiple cycles.

only retained 15.2% of its residual DBC after 24 hours of alkali treatment. In contrast, the designed multi-site mutants retained 60-90% of their residual DBC after 6 hours of alkali treatment, and even after 24 hours of treatment, some mutants maintained over 50% of their residual DBC, which is remakably more stable than the wild type in the alkaline environment of industrial production. Figure 4C shows the variation in yield during affinity chromatography across multiple cycles after employing our mutant. After more than 140 cycles, the yield of our mutant did not exhibit a significant downward trend. In contrary, the binding affinity of wild type is unable to sustain after 60 cycles. Therefore, our designed mutants maintain activity after more cycles of reuse compared to the wild type, substaintially reducing the production cost of growth hormones. Consequently, the selected mutant designed by the LLM has been applied in mass production scale up to 5,000 liters.

# 3. Conclusions

Through two rounds of evolution, we successfully designed a VHH antibody with strong resistance to extreme environments and enhanced affinity using the Pro-PRIME model. Although rare case can tolerate the extreme pH and saline conditions in our pre-training dataset, the Pro-PRIME model showed impressive performance after supervised learning with limited data, especially on capturing the epistatic effects. The analysis of these 65 mutants revealed that the Pro-PRIME model is adept at exploring the large space of protein fitness, being less susceptible to local optima, and having greater potential to find the global optimum. Our efficient method of designing mutants that consider multiple properties improvement holds promise for industrial application of proteins. Specifically, the VHH antibody has been deployed in practical production and significantly enhancing the efficiency of the entire production line after our design. While the Pro-PRIME model itself has been reported[25 ], this work demonstrates its first-time application to the challenge of designing proteins with alkali resistance and other extreme properties that are not found in natural proteins, nor have previous studies addressed or provided data for such applications. This shift from optimizing existing protein properties to engineering entirely new, unnatural traits is a significant advance in the field. This study shows that the AI models, such as Pro-PRIME, can not only guide the evolution of protein thermal stability, enzymatic activity, ligand affinity but also enable to develop the mutants adapting the harsh unnatural environments, such as extreme pH and concentrated salt, largely expanding its application. The novelty of this work lies in the ability to design and engineer proteins with novel properties, specifically alkali resistance, which is an unprecedented achievement in AI-assisted protein engineering. The great potential of AI model is expected to significantly accelerate the development of proteins for diverse applications in medicine, agriculture, bioengineering, etc.

# Data availability

Data will be made available on request.

# Acknowledgements

This work was supported by the National Natural Science Foundation of China (12204302), the Computational Biology Program of Shanghai Science and Technology Commission (23JS1400600), the Shanghai Pujiang Program (Grant No. 22PJ1406900), the Startup Fund for Young Faculty at SJTU (SFYF at SJTU), the Oceanic Interdisciplinary Program of Shanghai Jiao Tong University (Project No. SL2022MS018), the Natural Science Foundation of Shanghai (Grant No. 23ZR1431700), Shanghai Jiao Tong University Scientific and Technological Innovation Funds (21×010200843),

Science and Technology Innovation Key R&D Program of Chongqing (CSTB2022TIAD-STX0017), the Student Innovation Center at Shanghai Jiao Tong University, and Shanghai Artificial Intelligence Laboratory.

# Additional information

# CRediT authorship contribution statement

Liqi Kang: Writing – original draft, Data curation, Conceptualization, Methodology. Banghao Wu: Data curation, Methodology. Bingxin Zhou: Writing – review & editing. Pan Tan: Writing – review & editing. Yun (Kenneth) Kang: Data curation. Yongzhen Yan: Data curation. Yi Zong: Data curation. Shuang Li: Data curation. Zhuo Liu: Writing – review & editing, Supervision. Liang Hong: Writing – review & editing, Supervision.

# Additional files

Supporting information

# References

[1] Lovelock S.L., Crawshaw R., Basler S., Levy C., Baker D., Hilvert D., Green A.P. 2022) The road to fully programmable protein catalysis Nature 606:49–58   
Tokuriki N., Tawfik D.S. 2009) Protein dynamism and evolvability Science 324:203–207[2]   
[3] Lutz S., Iamurri S.M. 2018) Protein engineering: past, present, and future Protein Engineering: Methods and Protocols :1–12   
[4] Narayanan H., Dingfelder F., Butté A., Lorenzen N., Sokolov M., Arosio P. 2021) Machine learning for biologics: opportunities for protein engineering, developability, and formulation Trends in pharmacological sciences 42:151–165   
[5] Jang W.D., Kim G.B., Kim Y., Lee S.Y. 2022) Applications of artificial intelligence to enzyme and pathway design for metabolic engineering Current Opinion in Biotechnology 73:101–107   
[6] Qiu Y., Wei G.-W. 2023) Artificial intelligence-aided protein engineering: from topological data analysis to deep protein language models Briefings in Bioinformatics 24   
[7] Zhou Z., Zhang L., Yu Y., Wu B., Li M., Hong L., Tan P. 2024) Enhancing efficiency of protein language models with minimal wet-lab data through few-shot learning Nature Communications 15   
[8] Tan Y., Li M., Tan P., Zhou Z., Yu H., Fan G., Hong L. 2023) PETA: Evaluating the impact of protein transfer learning with sub-word tokenization on downstream applications arXiv   
[9] Li M., Kang L., Xiong Y., Wang Y.G., Fan G., Tan P., Hong L. 2023) SESNet: sequence-structure feature-integrated deep learning method for data-efficient protein engineering Journal of Cheminformatics 15:1–13   
[10] Pinney M.M., Mokhtari D.A., Akiva E., Yabukarski F., Sanchez D.M., Liang R., Doukov T., Martinez T.J., Babbitt P.C., Herschlag D. 2021) Parallel molecular mechanisms for enzyme temperature adaptation Science 371   
Jaenicke R. 1991) Protein stability and molecular adaptation to extreme conditons[11] European Journal of Biochemistry 202:715–728   
[12] Reetz M.T., Sun Z., Qu G. 2023) Enzyme engineering: selective catalysts for applications in biotechnology, organic chemistry, and life science John Wiley & Sons   
Xia Y., Li X., Yang L., Luo X., Shen W., Cao Y., Peplowski L., Chen X. 2021) Development of[13] thermostable sucrose phosphorylase by semi-rational design for efficient biosynthesis of alpha-D-glucosylglycerol Applied Microbiology and Biotechnology 105:7309–7319   
Minakuchi K., Murata D., Okubo Y., Nakano Y., Yoshida S. 2013) Remarkable alkaline stability[14] of an engineered protein A as immunoglobulin affinity ligand: C domain having only one amino acid substitution Protein Science 22:1230–1238

Linhult M., Gülich S., Gräslund T., Simon A., Karlsson M., Sjöberg A., Nord K., Hober S. 2004)[15] Improving the tolerance of a protein a analogue to repeated alkaline exposures using a bypass mutagenesis approach, Proteins: structure, function and bioinformatics 55:407–416   
Gülich S., Linhult M., Ståhl S., Hober S. 2002) Engineering streptococcal protein G for[16] increased alkaline stability Protein engineering 15:835–842   
Palmer B., Angus K., Taylor L., Warwicker J., Derrick J.P. 2008) Design of stability at extreme[17] alkaline pH in streptococcal protein G Journal of biotechnology 134:222–230   
[18] Madani A., Krause B., Greene E.R., Subramanian S., Mohr B.P., Holton J.M., Olmos J.L., Xiong C., Sun Z.Z., Socher R. 2023) Large language models generate functional protein sequences across diverse families Nature Biotechnology :1–8   
Hie B., Ellen D. Zhong, Berger B., Bryson B. 2021) Learning the language of viral evolution[19] and escape Science 371:284–288 https://doi.org/10.1126/science.abd7331   
Rao R.M., Liu J., Verkuil R., Meier J., Canny J., Abbeel P., Sercu T., Rives A. 2021) MSA[20] transformer, International Conference on Machine Learning Pmlr :8844–8856   
[21] Rives A., Meier J., Sercu T., Goyal S., Lin Z., Liu J., Guo D., Ott M., Zitnick C.L., Ma J. 2021) Biological structure and function emerge from scaling unsupervised learning to 250 million protein sequences Proceedings of the National Academy of Sciences 118   
[22] Blaabjerg L.M., Kassem M.M., Good L.L., Jonsson N., Cagiada M., Johansson K.E., Boomsma W., Stein A., Lindorff-Larsen K. 2023) Rapid protein stability prediction using deep learning representations Elife 12   
Wang S., Tang H., Zhao Y., Zuo L. 2022) BayeStab: Predicting effects of mutations on protein[23] stability with uncertainty quantification Protein Science 31   
Li F., Yuan L., Lu H., Li G., Chen Y., Engqvist M.K., Kerkhoven E.J., Nielsen J. 2022) Deep learning-[24] based k cat prediction enables improved enzyme-constrained model reconstruction Nature Catalysis 5:662–672   
Jiang F., Li M., Dong J., Yu Y., Sun X., Wu B., Huang J., Kang L., Pei Y., Zhang L. 2024) A general [25] temperature-guided language model to design proteins of enhanced stability and activity Science Advances 10   
Weiß M.S., Bornscheuer U.T., Höhne M. 2018) Solid-phase agar plate assay for screening[26] amine transaminases Protein Engineering: Methods and Protocols :283–296   
Khersonsky O., Lipsh R., Avizemer Z., Ashani Y., Goldsmith M., Leader H., Dym O., Rogotner S.,[27] Trudeau D.L., Prilusky J. 2018) Automated design of efficient and functionally diverse enzyme repertoires Molecular cell 72:178–186   
Weinreich D.M., Delaney N.F., DePristo M.A., Hartl D.L. 2006) Darwinian evolution can follow[28] only very few mutational paths to fitter proteins science 312:111–114   
Sternke M., Tripp K.W., Barrick D. 2019) Consensus sequence design as a general strategy to[29] create hyperstable, biologically active proteins Proceedings of the National Academy of Sciences 116:11275–11284

Wijma H.J., Floor R.J., Janssen D.B. 2013) Structure-and sequence-analysis inspired[30] engineering of proteins for enhanced thermostability Current opinion in structural biology 23:588–594

Xu Z., Cen Y.-K., Zou S.-P., Xue Y.-P., Zheng Y.-G. 2020) Recent advances in the improvement [31] of enzyme thermostability by structure modification Critical reviews in biotechnology 40:83– 98

# Author information

Liqi Kang†

School of Physics and Astronomy, Shanghai Jiao Tong University, Shanghai, China ORCID iD: 0009-0004-2427-5807

†These authors contributed equally to this work.

Banghao Wu †

School of Life Sciences and Biotechnology, Shanghai Jiao Tong University, Shanghai, China

†These authors contributed equally to this work.

Bingxin Zhou

Institute of Natural Sciences, Shanghai Jiao Tong University, Shanghai, China, Shanghai National Centre for Applied Mathematics (SJTU Center), MOE-LSC, Shanghai Jiao Tong University, Shanghai, China

ORCID iD: 0000-0002-3897-9766

Pan Tan

Shanghai Artificial Intelligence Laboratory, Shanghai, China

Yun (Kenneth) Kang

Changchun GeneScience Pharmaceuticals Co., Ltd, Changchun, China

Yongzhen Yan

Changchun GeneScience Pharmaceuticals Co., Ltd, Changchun, China

Yi Zong

Changchun GeneScience Pharmaceuticals Co., Ltd, Changchun, China

Shuang Li

Changchun GeneScience Pharmaceuticals Co., Ltd, Changchun, China

Zhuo Liu

Institute of Natural Sciences, Shanghai Jiao Tong University, Shanghai, China, Shanghai National Centre for Applied Mathematics (SJTU Center), MOE-LSC, Shanghai Jiao Tong University, Shanghai, China, Zhangjiang Institute for Advanced Study, Shanghai Jiao Tong University, Shanghai, China, Shanghai Artificial Intelligence Laboratory, Shanghai, China

ORCID iD: 0000-0001-9202-0516

For correspondence: judeliu@sjtu.edu.cn

# Liang Hong

School of Physics and Astronomy, Shanghai Jiao Tong University, Shanghai, China, Institute of Natural Sciences, Shanghai Jiao Tong University, Shanghai, China, Shanghai National Centre for Applied Mathematics (SJTU Center), MOE-LSC, Shanghai Jiao Tong University, Shanghai, China, Zhangjiang Institute for Advanced Study, Shanghai Jiao Tong University, Shanghai, China, Shanghai Artificial Intelligence Laboratory, Shanghai, China

For correspondence: hongl3liang@sjtu.edu.cn

# Editors

Reviewing Editor

# Martin Graña

Institut Pasteur de Montevideo, Montevideo, Uruguay

Senior Editor

# David Ron

University of Cambridge, Cambridge, United Kingdom

# Joint Public Review:

Summary:

In this manuscript, the model's capacity to capture epistatic interactions through multi-point mutations and its success in finding the global optimum within the protein fitness landscape highlights the strength of deep learning methods over traditional approaches.

Strengths:

It is impressive that the authors used AI combined with limited experimental validation to achieve such significant enhancements in protein performance. Besides, the successful application of the designed antibody in industrial settings demonstrates the practical and economic relevance of the study. Overall, this work has broad implications for future AIguided protein engineering efforts.

Reviewing Editor's comments on revised version:

The authors extensively addressed conceptual and methodological points raised by reviewers, as well as constructive comments to clarify the narrative. Consequently, the manuscript experienced a qualitative jump on clarity and appeal for the eLife readership.

https://doi.org/10.7554/eLife.102788.2.sa1

# Author response:

The following is the authors’ response to the original reviews.

Reviewer #1 (Public review):

(1) Summary:

In this manuscript, the model's capacity to capture epistatic interactions through multipoint mutations and its success in finding the global optimum within the protein fitness landscape highlights the strength of deep learning methods over traditional approaches.

We thank the reviewer for his/her recognition of our model’s potential and advantages.

# (2) Strengths:

It is impressive that the authors used AI combined with limited experimental validation to achieve such significant enhancements in protein performance. Besides, the successful application of the designed antibody in industrial settings demonstrates the practical and economic relevance of the study. Overall, this work has broad implications for future AI-guided protein engineering efforts.

We are thankful for the editor’s appreciation on our work, especially acknowledged the practical application of our model.

# (3) Weaknesses:

However, the authors should conduct a more thorough computational analysis to complement their manuscript. While the identification of improved multi-point mutants is commendable, the manuscript lacks a detailed investigation into the mechanisms by which these mutations enhance protein properties. The authors briefly mention that some physicochemical characteristics of the mutants are unusual, but they do not delve into why these mutations result in improved performance. Could computational techniques, such as molecular dynamics simulations, be employed to explore the effects of these mutations?

We thank the reviewer for this good question, which allows us to provide a deeper investigation into the mechanisms by which the mutations significantly enhance the alkaliresistance of proteins. By following the reviewer’s suggestion, we have expanded our analysis by incorporating molecular dynamics (MD) simulations to understand the impact of the mutations. As an example, we focused on the representative alkali-resistant mutant, A57D;P29T, and examined its MD simulation results. As shown in Figure S4A, the two-point mutant of A57D;P29T has a Tm increase of around 8 ℃ and a much stronger binding affinity than the WT. Our analysis of the MD trajectories indicates that the A57D;P29T mutant has a more rigid structure than that of WT due to its lower root mean squared deviation (RMSD) of protein (Figure S4B). Furthermore, we calculated the root mean squared fluctuation (RMSF) for each residue, and realized that the mutant displayed less fluctuation at residue 29 but similar flexibility at residue 57. Interestingly, residues at positions 10, 108 and 118 which spatially distant from residues 29 and 57 in the mutant exhibited remarkable weakened fluctuations than those in the WT (Figure S4C), implying a more rigid structure of the mutant contributing to its improved resistance on high temperature and strong alkalinity. However, Figure S4D shows the AlphaFold3 predicted structures of the WT and the mutant are quite similar.

To unveil the origin of change on structural flexibility, we computed the intramolecular interactions, such as salt bridges and hydrogen bonds for both WT and the mutant. We observed that the mutations increased the number of hydrogen bonds between the mutation sites and the rest of the protein (Figure S4E). However, the overall structure of the mutant did not show significant changes, which is also evident from the solvent-accessible surface area (SASA) analysis (Figure S4F). We also analyzed changes in salt bridges and found that although residue 57 mutated to Histidine, no new salt bridges were formed. Additionally, RMSF results showed that residues 10, 108, and 118 became more rigid, but further analysis revealed that there was no significant change in hydrogen bonds or other interactions in these regions. Overall, the MD results suggest that more hydrogen bonds introduced by the mutations of A57D;P29T stabilize the protein, leading to the enhanced alkali resistance observed in the mutant. These results are now presented in Figure S4 and discussed in detail in the revised manuscript.

Specifically, we have added the following discussion in the main text:

“In order to gain deeper insights into the mechanisms by which the identified mutations enhance protein properties, we performed molecular dynamics (MD) simulations on the best alkali-resistant mutant. The simulation results revealed several key observations that help explain the observed improvements in protein stability and alkali resistance. As shown in Figure S4A, the two-point mutant of A57D;P29T has a Tm increase of around 8℃ and a much stronger binding affinity than the WT. Our analysis of the MD trajectories indicates that the A57D;P29T mutant has a more rigid structure than that of WT due to its lower root mean squared deviation (RMSD) of protein (Figure S4B). Furthermore, we calculated the root mean squared fluctuation (RMSF) for each residue, and realized that the mutant displayed less fluctuation at residue 29 but similar flexibility at residue 57. Interestingly, residues at positions 10, 108 and 118 which spatially distant from residues 29 and 57 in the mutant exhibited remarkable weakened fluctuations than those in the WT (Figure S1C), implying a more rigid structure of the mutant contributing to its improved resistance on high temperature and strong alkalinity. However, Figure S4D shows the AlphaFold3 predicted structures of the WT and the mutant are quite similar. To unveil the origin of change on structural flexibility, we computed the intramolecular interactions, such as salt bridges and hydrogen bonds for both WT and the mutant. We observed that the mutations increased the number of hydrogen bonds between the mutation sites and the rest of the protein (Figure S4E). However, the overall structure of the mutant did not show significant changes, which is also evident from the solvent-accessible surface area (SASA) analysis (Figure S4F). We also analyzed changes in salt bridges and found that although residue 57 mutated to Histidine, no new salt bridges were formed. Additionally, RMSF results showed that residues 10, 108, and 118 became more rigid, but further analysis revealed that there were no significant changes in hydrogen bonds or other interactions in these regions. Taken together, these findings suggest that the enhanced alkali resistance of the mutant is likely due to an overall increase in protein stability, rather than a dramatic change in its structural conformation. The MD simulation results, which are detailed in Figure S4, provide a deeper understanding of how specific mutations can improve protein properties and offer valuable insights for future protein engineering applications.”

And we also included the following content in the SI:

“Molecular Dynamics (MD) simulations

The initial structures for molecular dynamics (MD) simulations of both the wild type and the mutant were predicted using AlphaFold3. To simulate experimental conditions, each protein was placed in a cubic water box containing 0.1 M NaCl. The CHARMM27 force field and the TIP4P water model were applied throughout the simulations. After an initial energy minimization of 50,000 steps, the systems were heated and equilibrated for 1 ns in the NVT ensemble at 300 K followed by an additional 1 ns in the NPT ensemble at 1 atm. The production phase then involved 200-ns simulations with periodic boundary conditions, using a 2 fs integration time step. The LINCS algorithm was used to constrain covalent bonds involving hydrogen atoms, while Lennard-Jones interactions were cut off at 10 Å. Electrostatic interactions were computed with the particle mesh Ewald method, using a 10 Å cutoff and a grid spacing of approximately 1.6 Å with a fourth-order spline. Temperature and pressure were regulated by the velocity rescaling thermostat and Parrinello-Rahman algorithm, respectively. All simulations were performed using GROMACS 2020.4 software

packages. Both systems have reached equilibrium according to the analyses of root mean squared deviation (RMSD).”

(4) Additionally, the authors claim that their method is efficient. However, the selected VHH is relatively short (<150 AA), resulting in lower computational costs. It remains unclear whether the computational cost of this approach would still be acceptable when designing larger proteins (>1000 AA). Besides, the design process involves a large number of prediction tasks, including the properties of both single-site saturation and multi-point mutants. The computational load is closely tied to the protein length and the number of mutation sites. Could the authors analyze the model's capability boundaries in this regard and discuss how scalable their approach is when dealing with larger proteins or more complex mutation tasks?

In our prior work, we have demonstrated that our method is applicable to larger proteins as well [Jiang et al., Sci. Adv. 10, eadr2641 (2024)]. For instance, when engineering a protein with 1000 amino acids, inferring the fitness of one million mutants using the model on a single 4090 GPU takes approximately 20 hours. However, it remains infeasible to explore all possible mutations when designing multi-point mutants due to the vast space. To address this challenge, we propose the design of a reliable mutant library. In the first round of experiments, we used the model to score all single-point mutations, and then constructed the multi-point mutant library by combining experimentally tested single-point mutations. In this way, even when designing five-point mutants, we only need to score on the order of millions of mutants, making the inference process time-efficient and fully acceptable. As a result, the number of single-point mutations selected for combination into the multi-point mutant library becomes a crucial parameter that affects both inference time and scope. We limited the number of single-point mutations to between 30 and 50 to strike a balance between efficiency and accuracy.

These results are discussed in the revised manuscript. Specifically, we have added the following discussion at the section 2.2 in the main text:

“Although the model inference is fast, it is not feasible to explore all possible mutations when designing multi-point mutants due to the exponential increase in the number of potential combinations. To manage this challenge, we constructed a mutant library based on a twostage design process. In the first stage, we scored all single-point mutations using the model, and in the second stage, we combined experimentally validated single-point mutations to create the multi-point mutant library. This approach ensures that even when designing multipoint mutants (e.g., five-point mutants), the number of mutants to score remains in the millions, which is computationally efficient and practical. The number of single-point mutations selected for the multi-point mutant library is a key factor influencing both the computational load and the scope of the design space. To maintain a balance between efficiency and accuracy, we limited the number of single-point mutations to between 30 and 50. This strategic approach allows us to achieve both scalability and precision in our protein engineering tasks.”

# Reviewer #2 (Public review):

In this paper, the authors aim to explore whether an AI model trained on natural protein data can aid in designing proteins that are resistant to extreme environments. While this is an interesting attempt, the study's computational contributions are weak, and the design of the computational experiments appears arbitrary.

The reviewer’s comments give us an opportunity to further state the novelty of this study. Despite the AI model has been reported in our previous work [Sci. Adv. 10, eadr2641 (2024)], the unnatural physicochemical properties of proteins, to the best of our knowledge, have

never been predicted using AI models. Our preceding work [Sci. Adv. 10, eadr2641 (2024)] has demonstrated that the large language model can predict the performances of the mutants on thermostability, catalytic activity, and binding affinity, etc. However, whether the AI models are able to evaluate the unnatural properties of the mutants remains unexplored. Our work has shown that AI models trained on the natural proteins can be used to design the mutants that resistant extreme conditions, such as strong alkalinity, substantially expanding the application of AI for bioengineering. Moreover, our design of the computational experiments was driven by the nature of the task and the availability of experimental data. We employed different strategies for designing single-point and multi-point mutants, specifically using a zero-shot approach for single-point mutations to overcome the challenge of rare data and fine-tuning the model for multi-point mutations to leverage the experimental data of singlepoint mutations.

(1) The writing throughout the paper is poor. This leaves the reader confused.

The manuscript has been revised accordingly, and we would like to address the reader’s questions if anything is confused.

(2) The main technical issue the authors address is whether AI can identify protein mutations that adapt to extreme environments based solely on natural protein data. However, the introduction could be more concise and focused on the key points to better clarify the significance of this question.

We thank the reviewer for this comment. We have revised the manuscript, particularly the introduction, where we focused on the research questions, methods, and main findings, while removing excessive background information to improve the manuscript’s conciseness and clarity.

“Protein engineering, situated at the nexus of molecular biology, bioinformatics, and biotechnology, focuses on the design of proteins to introduce novel functionalities or enhance existing attributes[1-3]. With the exponential growth of biological data and computational power, protein engineering has experienced a significant shift towards advanced computational methodologies, particularly deep learning, to expedite the design process and unravel complex protein-function relationships[4-9]. However, a significant challenge in industrial protein engineering is designing proteins with inherent resistance to extreme conditions, such as high temperature and extreme pH environments (acidic or alkaline)[17, 18]. Unlike proteins in natural ecosystems, those used in industrial processes often encounter harsh physical and chemical conditions, necessitating exceptional resilience to maintain functionality[19, 20]. Previous efforts to enhance protein resistance have often relied on rational design and mutant library screening. These methods are typically labor-intensive, inefficient, and yield limited improvements[23-26]. Consequently, the industrial demand for proteins resilient to harsh environments poses a notable absence within the training datasets of Artificial Intelligence (AI) models. Exploring whether AI can achieve the evolution of protein resistance to extreme environments is crucial for broadening protein applications and improving modification efficiency.

Recent advances in large-scale protein language models (LLMs) have enabled zero-shot predictions of protein mutants based on self-supervised learning from natural protein sequences. Although AI-guided protein design has been applied to predict the mutants with greater thermostability and higher activity[34-36], it is unexplored whether these models based on the natural protein information can find the mutants that adapt the unnatural extreme environments, such as the alkaline solution with the pH value higher than 13.

Here, we employed a LLM (large language model) developed by our group, the Pro-PRIME model[27], to predict dozens of mutants of a nano-antibody against growth hormone (a VHH antibody), and examined their fitness, including alkali resistance and thermostability, to evaluate their performance under extreme environments.

We utilized the Pro-PRIME model to score saturated single-point mutations of the VHH in a zero-shot setting, and selected the top 45 mutants for experimental testing. Some mutants exhibited improved alkali resistance, while others demonstrated higher thermal stability or affinity. Subsequently, we fine-tuned the Pro-PRIME model to predict dozens of multi-point mutations. As a result, we obtained three multi-point mutants with enhanced alkali resistance, higher thermostability, as well as strong affinity to the targeted protein. Also, the dynamic binding capacity of the selected mutant did not show significant decline after more than 100 cycles, making it suitable for practical application in industrial production. The selected mutant has been used in practical production and lower the cost for over one million dollars in a year. To the best of our knowledge, this is the first protein product developed by a LLM that has been successfully applied in mass production. Due to the Pro-PRIME model's ability to achieve precise predictions of multi-point mutations with reliance on a small amount of experimental data, our two-round design process involved experimental validation of only 65 mutants in two months, demonstrating remarkable high efficiency. Furthermore, we performed a systematic analysis of these findings and determined that the model can yield more valuable predictive outcomes while remaining consistent with rational design principles. Specifically, within the framework of multi-point combinations, the model's incorporation of negative single-point mutations into the combinatorial space led to exceptional results, showcasing its capacity to capture epistatic interactions. Notably, in striving for global optimum, deep learning methods offer distinct advantages over traditional rational design approaches.”

(3) The authors did not develop a new model but instead used their previously developed Pro-PRIME model. This significantly weakens the novelty and contribution of this work.

While it is true that the Pro-PRIME model was previously developed, the novelty and contribution of this work lie in its novel application to design proteins with properties that are not naturally found or are rare in nature. In our original work, the Pro-PRIME model was used to optimize proteins for existing, well-established properties, such as thermal stability, enzymatic activity, and affinity. However, in this study, we extended the model’s capabilities to design proteins that exhibit resilience to extreme environments, such as high pH— properties that are not inherently present in most natural proteins. To our knowledge, no existing model has addressed the challenge of engineering alkali-resistant proteins, nor is there relevant dataset available for training such models.

This shift from optimizing existing characteristics to engineering entirely new properties represents a significant step forward in the field of protein design. By focusing on the design of proteins that can survive and function in harsh, unnatural environments, we have demonstrated the broader applicability of the Pro-PRIME model beyond its initial scope. This expansion of the model's application is a novel contribution that has the potential to accelerate the development of proteins for industrial, agricultural, and biotechnological applications.

Thus, while the Pro-PRIME model itself is not new, its application to the new challenge of engineering proteins with alkali resistance and other novel properties significantly enhances the impact and novelty of this work. Moreover, this work is groundbreaking not only in terms of the model’s novel application but also because no previous studies have specifically targeted alkali resistance or provided data for training models on such extreme properties. Therefore, our approach is unique, marking a new direction in protein engineering.

We have made the following revisions to the conclusions section of the manuscript:

“Through two rounds of evolution, we successfully designed a VHH antibody with strong resistance to extreme environments and enhanced affinity using the Pro-PRIME model. Although rare case can tolerate the extreme pH and saline conditions in our pre-training dataset, the Pro-PRIME model showed impressive performance after supervised learning with limited data, especially on capturing the epistatic effects. The analysis of these 65 mutants revealed that the Pro-PRIME model is adept at exploring the large space of protein fitness, being less susceptible to local optima, and having greater potential to find the global optimum. Our efficient method of designing mutants that consider multiple properties improvement holds promise for industrial application of proteins. Specifically, the VHH antibody has been deployed in practical production and significantly enhancing the efficiency of the entire production line after our design. While the Pro-PRIME model itself has been reported, this work demonstrates its first-time application to the challenge of designing proteins with alkali resistance and other extreme properties that are not found in natural proteins, nor have previous studies addressed or provided data for such applications. This shift from optimizing existing protein properties to engineering entirely new, unnatural traits is a significant advance in the field. This study shows that the AI models, such as Pro-PRIME, can not only guide the evolution of protein thermal stability, enzymatic activity, ligand affinity, etc., but also enable to develop the mutants adapting the harsh unnatural environments, such as extreme pH and concentrated salt, largely expanding its application. The novelty of this work lies in the ability to design and engineer proteins with novel properties, specifically alkali resistance, which is an unprecedented achievement in AIassisted protein engineering. The great potential of AI model is expected to significantly accelerate the development of proteins for diverse applications in medicine, agriculture, bioengineering, etc.”

(4) The computational experiments are not well-justified. For instance, the authors used a zero-shot setting for single-point mutation experiments but opted for fine-tuning in multiple-point mutation experiments. There is no clear explanation for this discrepancy. How does the model perform in zero-shot settings for multiple-point mutations? How would fine-tuning affect single-point mutation results? The choice of these strategies seems arbitrary and lacks sufficient discussion.

We appreciate the reviewer’s comment regarding the use of zero-shot and fine-tuning settings for single-point and multi-point mutation experiments, and we are grateful for the opportunity to further clarify this aspect of our work.

In the first round of design, we used the zero-shot approach for single-point mutations because the number of possible single-point mutations is limited, and no prior experimental data was available. In the absence of relevant data, the zero-shot approach allows the model to make predictions based on the learned sequence patterns from the pre-trained protein language model. Given that single-point mutations are relatively fewer in number and computationally feasible to evaluate, the zero-shot approach was deemed appropriate for this task.

However, when it comes to designing multi-point mutants, the number of potential combinations increases exponentially, making it computationally impractical to explore all possible mutations in a reasonable timeframe. Furthermore, since we had already obtained some experimental data for single-point mutations in the first round, we fine-tuned the model with this data in the second round to improve the accuracy of predictions for multipoint mutants. Fine-tuning helps the model better capture the specific features that contribute to protein functionality, which are critical when dealing with multi-point mutations where multiple residues interact. This allows the model to produce more reliable and targeted predictions for multi-point mutants, ultimately leading to better design outcomes.

Regarding the model's performance in zero-shot settings for multi-point mutations, we tested this approach, and the results did not align well with the experimental data for multi-point mutants. Specifically, the Spearman correlation coefficient between the zero-shot predictions and experimental results was -0.71, indicating that zero-shot predictions for multi-point mutations were not as accurate as those from the fine-tuned model.

In summary, the choice of using zero-shot for single-point mutations and fine-tuning for multi-point mutations was driven by the nature of the task and the availability of experimental data. Fine-tuning the model improves its predictive performance, especially for more complex multi-point mutation tasks. We have now clarified these choices in the manuscript and have added further discussion on the trade-offs between zero-shot and finetuning approaches.

Specifically, we have added the following discussion at the section 2.2 in the main text:

“Note that we employed different strategies for designing single-point and multi-point mutants, specifically using a zero-shot approach for single-point mutations and fine-tuning the model for multi-point mutations. These choices were made based on the distinct characteristics of the two tasks and the availability of experimental data. For single-point mutations, the number of possible mutations is relatively limited, and at the outset, there were no experimental data available. In such cases, the zero-shot setting was chosen because it allows the model to predict the fitness of mutants based solely on the information learned during pre-training on a large protein sequence dataset. Since single-point mutations are computationally manageable, this approach was deemed appropriate to generate initial predictions for protein engineering. However, when designing multi-point mutants, the situation changes significantly. The potential combinations of mutations increase exponentially, and without prior data, it becomes computationally infeasible to evaluate every possible combination within a reasonable timeframe. Moreover, by the time we reached the multi-point mutation design stage, experimental data for several single-point mutations had already been obtained. This data enabled us to fine-tune the model to better capture the specific structural and functional features that contribute to protein stability and resistance, especially in the context of multiple interacting mutations. Fine-tuning improves the model’s accuracy by adjusting its parameters to align more closely with the experimental data, ensuring that the predicted multi-point mutants are more likely to meet the desired engineering goals. After the second round of design, the fitness of the mutants was further improved. In improving alkali resistance, experimental results showed that 15 of the 45 designed mutants exhibited positive responses, yielding a success rate of 30%, close to the 35% success rate achieved in the second round. Compared to the wild type, the best singlepoint mutant improved alkali resistance by approximately 44.7%, while the best multi-point mutant achieved a 67.7% increase. For thermal stability enhancement, the success rate in the first round was 77.8%, rising to 100% in the second round. The top single-point mutant exhibited a Tm increase of 6.37°C over the wild type, while the best multi-point mutant had a Tm increase of 10.02°C. We also tested the performance of the zero-shot approach for multipoint mutants, and the results showed that this method did not yield satisfactory predictions. The Spearman correlation coefficient between the zero-shot predictions and experimental results for multi-point mutants was -0.71, indicating a significant discrepancy. This further highlights the importance of fine-tuning the model for multi-point mutations, as the finetuned model provided more accurate and reliable results. In summary, the choice of zeroshot for single-point mutations and fine-tuning for multi-point mutations was driven by practical considerations regarding computational feasibility and the availability of experimental data. Fine-tuning the model significantly enhances its predictive performance, particularly for complex multi-point mutations where multiple residues interact. We believe this strategy strikes an optimal balance between computational efficiency and predictive accuracy, making it well-suited for practical protein engineering applications.”

https://doi.org/10.7554/eLife.102788.2.sa0