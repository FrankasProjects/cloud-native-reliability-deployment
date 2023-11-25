# Review Protocol: Systematic Literature Review - Identifying common cloud cost and purchasing models

In the context of the masters' thesis *Evaluating Cost Implications of Cloud-Native Application Characteristics With a Focus on Reliability Aspects* a Systematic literature review (SLR) was conducted to derive common cloud costs, as well as purchasing models used by Cloud service providers (CSPs). The SLR follows the procedure of Kitchenham et al. [1]. The following sections will provide the detailed steps, including search strings, inclusion & exclusion criteria, as well as an overview of the final literature. 

**Table of content:**

 1. [Search Procedure](#item-one)  
     1.1. [ACM Digital Library](#item-two)  
     1.2. [IEEE Xplore](#item-three)  
     1.3. [SpringerLink](#item-four)  
2.  [Selection Criteria](#item-five)
3.  [Inclusion / Exclusion Criteria](#item-six)  
     3.1. [Title-based Filtering](#item-seven)  
     3.2. [Abstract-based Filtering](#item-eight)  
     3.3. [Full-text-based Filtering](#item-nine)  
4. [Snowballing](#item-ten)
5. [Full-text-based Filtering (Detailed Analysis)](#item-eleven)


<a id="item-one"></a>

## 1. Search Procedure

Based on a first unstructured literature search and research articles in the cloud cost area, a search string was developed. Depending on the database used, the search string was adapted according to the search criteria. The following sections display the string, search procedure, and the results for the three databases ACM, IEEE Xplore, and SpringerLink. 

 <a id="item-two"></a>

### 1.1 ACM Digital Library

> [[Abstract: "cloud-computing"] OR [Abstract: "cloud-native"]] AND   
> [[Abstract: "cost-analysis"] OR [Abstract: "cost evaluation"]   
> OR [Abstract: "cost characteristics"] OR [Abstract: "cost characterization"]   
> OR [Abstract: "cost model"] OR [Abstract: "cost models"]   
> OR [Abstract: "cost scheme"] OR [Abstract: "cost schemes"]   
> OR [Abstract: "price model"] OR [Abstract: "pricing model"]   
> OR [Abstract: "price models"] OR [Abstract: "pricing models"]   
> OR [Abstract: "price scheme"] OR [Abstract: "pricing schemes"]   
> OR [Abstract: "price schemes"] OR [Abstract: "pricing scheme"]   
> OR [Abstract: "price evaluation"] OR [Abstract: "price analysis"]   
> OR [Abstract: "pricing analysis"] OR [Abstract: "total cost of ownership"]]  

- **Date of Search:** 23.06.2023
- **Results:** 68
- **Limit by Year:** 68 (earliest 2009)
- **Limit by Publication Type:** 63 (58 Conferences, 5 Journals)

 <a id="item-three"></a>

### 1.2 IEEE Xplore

> (("Abstract":"cloud computing") OR ("Abstract":"cloud-native")) AND   
> (("Abstract":"cost analysis") OR ("Abstract":"cost evaluation")   
> OR ("Abstract":"cost charac*")   
> OR ("Abstract":"cost model*") OR ("Abstract":"cost scheme*")   
> OR ("Abstract":"pric* model*") OR ("Abstract":"pric* scheme*")   
> OR ("Abstract":"pric* evaluation") OR ("Abstract":"price analysis")   
> OR ("Abstract":"total cost of ownership"))  

- **Date of Search:** 23.06.2023
- **Results:** 348
- **Limit by Year:** 348 (earliest 2008)
- **Limit by Publication Type:** 340 (293 Conferences, 47 Journals)

 <a id="item-four"></a>

### 1.3 SpringerLink

> 1. with the exact phrase: cost analysis, where the title contains: cloud computing

- Results: 65
- Eingrenzung nach Jahr: 2006-2023: 65
- Articles: 29
- Conference Paper: 21
- Conference Proceedings: 2
- Results: 52 (springer_1)


> 2. with the exact phrase: cost analysis, where the title contains: cloud-native

- Results: 3 
- Eingrenzung nach Jahr: 2006-2023: 3
- Article: 1
- Conference Paper: 1
- Result: 2


> 3. with the exact phrase: pricing model, where the title contains: cloud computing

- Results: 244
- Eingrenzung nach Jahr: 2006-2023: 244
- Article: 95
- Conference Paper: 87
- Conference Proceeding: 2
- Results: 184


> 4. with the exact phrase: pricing scheme, where the title contains: cloud computing

- Results: 71
- Eingrenzung nach Jahr: 2006-2023: 71
- Conference Paper: 19
- Conference Proceeding: 1

- Results: 56

**SpringerLink total: 294 articles**

<a id="item-five"></a>

## 2. Selection Criteria
According to Kitchenham et al. initial, more liberally study selection criteria are developed with the focus of removing articles that do not adhere to the scientific standard, are duplicates, or not within the investigated timeframe. Content criteria cover the target literature, but are further refined through the inclusion and exclusion criteria developed iteratively in the next section. 

The study selection criteria include the following articles: 
- Studies between 2006 and 2023 (The beginning of cloud computing to date)
- Journal arcticles and conference paper (ensure peer-review process)
- Systematic literature reviews
- Studies with a different focus but at least one section on cloud costs
- Studies that do not cover all existing cloud pricing model / cost types but address specific providers, products or cloud service models and their costs  

The study selection criteria exclude the following articles:  
- Thematic duplicates (paper and journal extensions)
- Informal articles such as keynotes, posters, workshops  

Total of 697 Articles (applied criteria directly at search: year, peer-reviewed)  
Result: After removing 58 duplicates: 697-58 = 639 articles
ResultSet (with duplicates): [1_combined_databases_unfiltered](https://github.com/FrankasProjects/cloud-native-reliability-deployment/blob/main/Systematic%20Literature%20Review/ResultSets/1_combined_databases_unfiltered.csv)
ResultSet (without duplicates): [3_prepared_dataset](https://github.com/FrankasProjects/cloud-native-reliability-deployment/blob/main/Systematic%20Literature%20Review/ResultSets/3_prepared_dataset.csv)

<a id="item-six"></a>

## 3. Inclusion & Exclusion Criteria
Inclusion and exclusion criteria are iteratively developed by first conducting a title and metadata based scan, followed by an abstract scan, and concluded by the full-text scan. All 3 steps, including the derived critera as well as the results are displayed in the following.  

<a id="item-seven"></a>

### 3.1 Title-based filtering
During this step part of the study selection criteria were applied in addition to a first topic-related based filtering.  
The articles matching the following criteria were removed from the resultset:
- Posters, keynotes, workshops and informal articles
- Articles, where the title indicates that the focus is on cloud offerings apart from the public cloud, e.g., hybrid or private cloud
- Conference to journal extensions (keeping one version)

This step removed 130 articles, which results in 509 remaining articles. 
ResultSet: [4_title_based_filtering](https://github.com/FrankasProjects/cloud-native-reliability-deployment/blob/main/Systematic%20Literature%20Review/ResultSets/4_title_based_filtering.csv)

<a id="item-eight"></a>

### 3.2 Abstract-based filtering
During this step a more content-related selection was conducted that excluded the following types of articles:
- Articles which propose new pricing mechanisms, such as dynamic and auction-based mechanisms, or propose approaches to maximize profit on CSP or customer side through **adaptions** of pricing mechanisms (not related to existing mechanisms)
- Articles that focus on routing, networking, and more hardware-related topics and that include cost factors besides the cloud pricing mechanisms
- Articles that were analysing the TCO from the CSPs point of view, and therefore provide insights on the occuring costs of the CSP, suche as hardware, electricity, cooling, etc.
- Articles that investigate the cloud provider market from an economical perspective and thus focus on economic phenomena and not on cloud pricing strategies

This step removed 419 articles, which results in 90 remaining articles. 
ResultSet: [5_abstract_based_filtering](https://github.com/FrankasProjects/cloud-native-reliability-deployment/blob/main/Systematic%20Literature%20Review/ResultSets/5_abstract_based_filtering.csv)

<a id="item-nine"></a>

### 3.3 Full-text filtering
During this step, articles were removed based on their full-text. The most common criteria for articles to be removed from the resultset were the follwoing:
- Articles that were developing their own approach on optimizing cloud costs for either the provider or consumer side 
- Articles that were listing specific cloud costs, for example for EC2 instances, but do not provide information about the price composition, and are therefore outdated

Additioally, the table below displays all articles scanned in this step and provides a short explanation on their inclusion / removal. 

This step removed 51 articles, which results in 39 remaining articles. 
ResultSet (.bib): [6_full_text_based_filtering](https://github.com/FrankasProjects/cloud-native-reliability-deployment/blob/main/Systematic%20Literature%20Review/ResultSets/6_full_text_based_filtering.bib)

<a id="item-ten"></a>

## 4. Snowballing
Based on the resultset of 39 articles, a forward and backward search was conducted that discovered 4 additional articles. 

The final resultset consists of 43 articles.
ResultSet: [7_snowballing](https://github.com/FrankasProjects/cloud-native-reliability-deployment/blob/main/Systematic%20Literature%20Review/ResultSets/7_snowballing.csv)
ResultSet (.bib): [8_final_literatureset](https://github.com/FrankasProjects/cloud-native-reliability-deployment/blob/main/Systematic%20Literature%20Review/ResultSets/8_final_literatureset.bib)

<a id="item-eleven"></a>

## 5. Full-text-based filtering (Detailed Analysis)
This table diplays all papers scanned within step x and provides the reason for inclusion / removal.  
The first column represents for each articles its position within all articles / its position of included or excluded articles.  

Number / (Included / Excluded) | Author | Title | Year | Publication Type | Content | Included | Reason for Inclusion / Removal |
| ----------- | ----------- | ----------- | ----------- | ----------- |----------- | ----------- | ----------- |
| 1 / 1| Arshad et al. | A survey of Cloud computing variable pricing models | 2015 | Conference | The authors outline different pricing schemes used by CSPs. In addition to insights into the structure of static and dynamic pricing mechanisms, an overview of the state of research on variable pricing models is given. | Yes | Cloud pricing models, such as pay-as-you-go pricing and dynamic pricing are explained. | 
| 2 / 1| Keskin and Taskin | A Pricing Model for Cloud Computing Service | 2014 | Conference | The study derives a pricing model from the intersection of cloud switching costs, time-inconsistent discounting, and network externalities. They build on principles of behavioral economics to maximize organization's profits. | No | The authors provide a new pricing model and do not address current pricing mechanisms. | 
| 3 / 2 | Li et al. | Price competition in a duopoly IaaS cloud market | 2014 | Conference | The authors studied pricing issues in a duopoly IaaS cloud market, focussing on subscription-based pricing models in order to accomplish better pricing strategies. | Yes | Insights into the IaaS pricing schemes (at AWS) are provided along with concrete infrastructure options. | 
| 4 / 2|  Emeras et al. | Amazon Elastic Compute Cloud (EC2) versus In-House HPC Platform: A Cost Analysis | 2019 | Journal | The study conducts a cost comparison of running an HPC platform on premises versus on the cloud. Therefore, they calculate the TCO, provide hourly pricing information and compare the in-house results to an architecture based on AWS EC2 instances.| No | The study only contains pricing information relevant for their specific use case an no overview of pricing categories, models, or relevant appraoches. | 
| 5 / 3|  Cong et al. | Personality-Guided Cloud Pricing via Reinforcement Learning | 2020 | Journal | To optimize cost and profit, the authors develop a dynamic pricing scheme and decision-support service based on a reinforcement-technology that incorporates the users' percevied value of cloud services. | Yes | The authors include pricing details on AWS' EC2 pricing scheme. | 
| 6 / 4|  Teramoto and Huang | Pay as You Go in the Cloud: One Watt at a Time | 2012 | Conference | The study proposes a pricing scheme based on the power consumption of the consumed infrastructure in order to better estimate the actual CPU and disk usage to obtain usage-based pricing models. | Yes | The theoretical background contains information on the price composition, specific for EC2 instances. | 
| 7 / 5|  Gohad et al. | Cloud Pricing Models: A Survey and Position Paper | 2013 | Conference | The authors conduct a literature review on various pricing strategies and industry trends based on an Indian case study. In addition, they provide a cross over model that aims to increase profit of providers hosting multi-tenant cloud environments. | Yes | The authors include a detailed overview of various pricing strategies, pricing models and their price composition. Thereby they provide concrete examples on Amazons pricing model but general pricing strategies applicable for multiple providers. | 
| 8 / 6|  Mudali et al. | QoS Aware Heuristic Provisioning Approach for Cloud Spot Instances | 2017 | Conference | The authors study resource provisioning approaches using AWS EC2 instances with spot instance pricing in order to reduce costs. | Yes | The paper provides insights into the pricing model of AWS EC2 spot instances. | 
| 9 / 3|  Alves et al. | CM Cloud Simulator: A Cost Model Simulator Module for Cloudsim | 2016 | Conference | The authors implement a cloud simulator that optimizes the search for cloud instances and prices.  | No | The authors only offer a comparison of AWS, Google, and Azure and their VM instances with a focus on the actual presences that give no insight into the pricing scheme and are quickly outdated.  | 
| 10 / 4|  Alasaad et al. | Prediction-based resource allocation in clouds for media streaming applications | 2012 | Conference | The authors address a cost optimization problem for the resource allocation of media content in the cloud.  | No | The content focuses more on how resource usage can be calculated in the future to reserve sufficient cloud resources and minimize costs. An overview of the different pricing models is not given. |
| 11 / 5|  Mvelase et al. | A comparative analysis of pricing models for enterprise cloud platforms | 2013 | Conference | The authors investigate a enterprise architecture by comparing their pricing model with the AWS EC2 pricing model. | No | The article does not provide insights into cost structures and does adhere to the qualitative standard of the remaining articles. |
| 12 / 6|  Bellur et al. | Cost Optimization in Multi-site Multi-cloud Environments with Multiple Pricing Schemes | 2014 | Conference | The authors address the concept of multi-site and multi-cloud deployments and their challenges regarding different pricing schemes.  | No | First, the paper focuses more on algorithms for deployment on multi-cloud environments, second, the challenges of the resulting pricing are not in the scope of this thesis. |
| 13 / 7|  Samimi and Patel | Review of pricing models for grid & cloud computing | 2011 | Conference | The article deals with the ifrastructure of distributed systems and compares grid and cloud computing. | Yes | The focus is on the pricing models of cloud and grid computing. The authors discuss auction-based pricing models, for example, but also mention different cost factors such as CPU hours or I/O rates as price categories.  |
| 14 / 7|  Filiopoulou et al. | Integrating cost analysis in the cloud: A SoS approach | 2015 | Conference | The authors attempt to create a model for decision support for the cloud that covers economic metrics such as TCO, NPV and ROI to benefit providers, users and brokers.  | No | Costs are covered in this article mainly at the infrastructure level, as well as at the expense level. An attempt is made to determine all costs incurred for all cloud participants, whereby the costs relevant to the thesis that the cloud provider imposes are only a part of the cost model, which is not further elaborated. |
| 15 / 8|  Markus and Kertesz | Simulating IoT Cloud systems: A meteorological case study | 2017 | Conference | The authors compare IoT cloud systems and their costs at 4 cloud providers.  | Yes | Although the comparison of costs only relates to the IoT cloud systems sector, it does provide an insight into their cost categorization, which can also be applied to other sectors. |
| 16 / 9|  Cong et al. | Developing User Perceived Value Based Pricing Models for Cloud Markets | 2018 | Journal | The authors address the issue of price control according to the supply and demand principle. They optimize the maximum profit for the cloud provider by designing prices according to the user perceived value. | Yes | The authors discuss the dynamic pricing model, as well as common pricing models. |
| 17 / 10|  Kandpal et al. | Role of predictive modeling in cloud services pricing: A survey | 2017 | Conference | The authors address the relevance of big data analytics in pricing, providing an overview of predictive modeling approaches and their accuracy.  | Yes | The authors compare different pricing models of AWS and Microsoft Azure. |
| 18 / 11|  Mahajan et al. | Optimal Pricing for Serverless Computing | 2019 | Conference | The authors examine potential cost benefits that can arise in serverless computing. They examine a distribution mechanism by running an application on both VM and serverless systems while maintaining certain availability constraints. They identify an optimum for cloud providers and cloud consumers. | Yes | The article provides an insight into the cost structure of VM and serverless computing and compares the two approaches. |
| 19 / 8|  Murat et al. | OMTiR: Open Market for Trading Idle Cloud Resources | 2014 | Conference | The authors present a market model to increase the attractiveness of the cloud by reducing costs for cloud resources. Their model ist based on an open market strategy that allows users to resell their cloud resources.| No | The model proposes a new market model for the cloud, which is currently not applicable and thus not provide insights into the current pricing schemes of cloud providers. |
| 20 / 12|  Belli et al. | Towards a Cost-Optimized Cloud Application Placement Tool | 2016 | Conference | This research paper addresses the price estimation of cloud resources on multiple cloud providers by combining pricing model approaches.| Yes | This paper provides insights into their approach on abstracting cloud pricing models and parameters, which aligns with the goal os this thesis. |
| 21 / 13|  Boza et al. | Reserved, on demand or serverless: Model-based simulations for cloud budget planning | 2017 | Conference | This research focus on the ideal cloud pricing model also in alignment with the company's size. They propose a model to optimize budget planing for cloud resources that especially small and mid-sized companies benefit from.  | Yes | A overview over different pricing models, including serverless computing pricing is provided. |
| 22 / 14|  Adebayo et al. | Cost-Benefit Analysis of Pricing Models in Cloudlets | 2020 | Conference | The authors' research relates to the domain of cloudlets and how cloud pricing models lend themselves to it.  | Yes | The article displays differneces between cloud pricing strategies such as fixed pricing strategies or dynamic pricing strategies. |
| 23 / 9|  Hanh Le et al. | A Study on BPaaS with TCO Model | 2014 | Conference | The authors conduct a case study to validate a TCO for cloud costs in the domain of BPaaS. | Yes | The article is limitied to the cas of BPaaS cloud computing costs. |
| 24 / 15|  Kandpal and Patel | Pricing model for revenue generation using Recurrent Neural Network for Cloud service provider | 2019 | Conference | The article targets cloud price estimations through the usage of Recurrent Neural Networks.  | Yes | The authors address pricing mechanisms such as on-demand, pay as you go, or auction based pricing. |
| 25 / 16|  Li et al. | Research on Pricing Model of Cloud Storage | 2013 | Conference | The paper addresses the pricing strategies in the domain of private cloud storage. In doing so, they compare products, prices and differentiate them on the basis of the usual pricing strategies.  | Yes | Although most of the research relates to aspects of cloud storage that are less relevant to this thesis, it also includes some aspects for categorizing pricing.  |
| 26 / 17|  Zhang et al. | A Dynamic Pricing Model for Virtual Machines in Cloud Environments | 2020 | Conference | The authors propose a dynamic pricing model for virtual machines that outperforms current fixed pricing schemes in domains such as user satisfaction and cloud provider profits.  | Yes | As a basis for the calculation, the authors differentiate between dynamic and fixed pricing mechanisms, which is relevant for categorization approach of this thesis.  |
| 27 / 10|  Wallace et al. | Applications of neural-based spot market prediction for cloud computing | 2013 | Conference | The paper addresses the topic of spot pricing in the cloud market. The authors use neural networks to predict spot prices of AWS EC2 instances.  | No | AThe paper focuses very much on spot pricing, whereby no cost compositions are provided.   |
| 28 / 18|  Kozhipurath | Cloud Service Costing Challenges | 2012 | Conference | The authors address the challenge of pricing as well as the economic efficiency of using cloud services. They compare infrastructure costs and cloud costing parameters as well as additional benefits that arise alongside the costs. | Yes | In addition to a cost breakdown, the paper also abstracts from specific costs and emphasizes parameters and characteristics in pricing that can be used as a basis for this thesis. |
| 29 / 19|  He et al. | On the Cost–QoE Tradeoff for Cloud-Based Video Streaming Under Amazon EC2's Pricing Models | 2013 | Journal | The authors' paper addresses video service providers, dealing with the selection of pricing models for EC2 instances and the associated complexity. Mathematical optimization is used to optimize procurement costs and revenue.  | Yes | The authors discuss the different pricing scenarios of AWS EC2 instances, as well as their characteristics and parameters that are relevant for the thesis. |
| 30 / 20|  Wang et al. | Revenue maximization with dynamic auctions in IaaS cloud markets | 2013 | Conference | The paper primarily addresses auction procedures for the procurement of EC2 instances. With regard to the revenue maximization of cloud providers, dynamic pricing through auction procedures in response to market events should better reflect prices. | Yes | In addition to the development of the dynamic pricing method, the authors also compare the cost models of EC2 instances. |
| 31 / 11|  Mihailescu and Teo | On Economic and Computational-Efficient Resource Pricing in Large Distributed Systems | 2010 | Conference | The authors develop a dynamic pricing mechanism and compare it with existing pricing models. The main focus is on distributed systems and shared resources and not exclusively on cloud resources.  | No | The research focuses on federates sharing systems, whereby prices are designed independently of specific cloud pricing models but rather from an economic market perspective. |
| 32 / 21|  Martens et al. | Costing of Cloud Computing Services: A Total Cost of Ownership Approach | 2012 | Conference | Martens et al. examine the TCO incurred by cloud providers for offering their services. They identify various pricing schemes and cost types and map these in a TCO model, which is validated using a case study.  | Yes | The cost analysis of cloud providers identifies different types of costs and pricing mechanisms that abstract from concrete costs and provide insights into cost structures.  |
| 33 / 12|  Wahid and Banday | Machine Type Comparative of Leading Cloud Players Based on Performance & Pricing | 2018 | Conference | The paper compares cloud computing services between AWS, Microsoft Azure and the Google Cloud. It compares concrete costs caused by different parameters of compute instances. | No | Although the authors focus on the costs incurred in the cloud, they focus on specific prices and less on cost types. This thesis attempts to refrain from these comparisons in order to create generalizability, abstractability and a more long-term view.  |
| 34 / 13|  Yu | The Cost-Efficient Awareness for Cloud MapReduce | 2015 | Conference | The paper discusses optimizing cost management in cloud-based MapReduce applications, introducing the concept of "Cost-Efficient Awareness" to reduce overall operational costs. | No | It does not deal with specific pricing schemes or types of ksot, but rather approaches to reducing costs.  |
| 35 / 14|  Caton et al.  | Assessing the Current State of AWS Spot Market Forecastability | 2022 | Conference | The paper examines the predictability of spot pricing mechanisms. Using statistical ARIMA models, the authors show that AWS sport pricing is quite predictable and can determine the actual costs well. | No | The object of research is the price determination and prediction of spot pricing mechanisms. Various instance types and models for their price prediction are analyzed, but no conclusions relevant to the thesis are presented with regard to the price structures.  |
| 36 / 15|  Mvelase et al.  | The economics of cloud computing: A review | 2016 | Conference | The authors address relevant decision criteria when considering migrating to the cloud.  | No | The authors focus more on the costs incurred by the client when switching to the cloud, i.e. the associated switching costs, refactoring costs, etc., than cost paradigms within the cloud.  |
| 37 / 16|  Fu et al.  | A differentiated pricing mechanism for idle resources allocation in reservation clouds | 2016 | Conference | The paper focuses on the aspects of SaaS in the cloud. They propose a resource allocation algorithm and a new pricing scheme that should enable optimized resource usage by reducing idle resources. | No | The paper does not provide insights into the pricing scheme of cloud providers but develops a new pricing scheme.   |
| 38 / 17|  Hamad and Fayoumi | Modernization of a Classical Data Center (CDC) vs. Adoption in Cloud Computing Calculate Total Cost of Ownership for Both Cloud and CDC - Jordanian Case Study | 2018 | Conference | Using a case study, the study compares the costs incurred via a TCO approach of cloud computing with on-premises data centers.  | No | Although the authors address the costs incurred in the cloud, they limit themselves to specific prices for selected cloud products that do not provide any insight into cost structures and are also not valid in the long term. |
| 39 / 22|  Wang et al. | When cloud meets eBay: Towards effective pricing for cloud computing | 2012 | Conference | The authors propose an auction model for cloud pricing to reduce manipulation in the spot pricing market.  | Yes | In the introduction and the theoretical section, the authors discuss different cloud pricing models.  |
| 40 / 18|  Mireslami et al. | Minimizing Deployment Cost of Cloud-Based Web Application with Guaranteed QoS | 2015 | Conference | The subject of the research is the optimization of IaaS resource procurement. A model is proposed which is intended to reduce overprovisioned cloud resources but still adhere to QoS requirements. | No | Although the authors select some input parameters, they do so independently of specific product and cost allocations.  |
| 41 / 23|  Zhang et al. | Dynamic optimal resource provisioning for VoD services under Amazon EC2's pricing models | 2014 | Conference | Similar to He et al., the paper addresses the challenges of video service providers to optimally utilize resources in order to fulfill quality of service requirements. | Yes | The authors display and formalise the AWSCEC2 instance pricing strategies.   |
| 42 / 24|  Karthikeyan and Nandhini | Dependent component cost model of legacy application for hybrid cloud | 2016 | Conference | In addition to analyzing various cloud pricing models, the research article addresses the process of hybrid cloud migration. A mathematical approach is proposed to calculate costs for the cloud migration. | Yes | The authors provide a comparison of different cloud models, as well as billing models and a classification of common cloud providers. The categorization is suitable for the strategy of the thesis. |
| 43 / 19|  Hong et al. | Selective commitment and selective margin: Techniques to minimize cost in an IaaS cloud | 2012 | Conference | The research article addresses pricing in the cloud, especially in IaaS computing. They try to optimize pricing for CSP by analyzing the margin in pricing. | No | The focus here is on pricing from a cloud provider perspective and less on the cost types incurred in the cloud. |
| 44 / 20|  Zhang et al. | Online combinatorial double auction for mobile cloud computing markets | 2014 | Conference | The main subject of the paper is the limitations of pricing models in markets such as mobile cloud computing, which is characterized by the dynamic actions of users. To counteract this, the authors develop an auction-based pricing model. | No | The paper addresses a self-developed approach that does not reflect the currently available cloud pricing models.  |
| 45 / 21|  Van Den Bossche et al. | Optimizing IaaS Reserved Contract Procurement Using Load Prediction | 2014 | Conference | In the research article, costs are optimized on the customer side through load prediction. IaaS costs can thus be reduced by means of reserved pricing models and appropriate load prediction. | No | The article focuses mainly on the pricing model of reserved instances, with a particular focus on specific prices from 2014. These are no longer valid and cannot be abstracted / applied for the purpose of this thesis.  |
| 46 / 22|  Nagy and Kovari | Evaluating performance of cloud computing environments | 2013 | Conference | The authors compare the prices of different cloud components and providers. This includes virtual machines, storage options or data transfer prices of common cloud providers such as Azure, AWS, or HP.  | No | The article focuses on specific prices and price differences between the products and providers. A breakdown of specific prices to identify the choice of provider and products is only mentioned as outlook for future work.  |
| 47 / 23|  Lopes et al. | Business-driven capacity planning of a cloud-based it infrastructure for the execution of Web applications | 2010 | Conference | With their paper, the authors address the IaaS area, in particular the pricing model of reserved instances. The aim is to investigate how to provide appropriate resources for web applications with fluctuating workloads.  | No |  In this article, a capacity planning model is created which allocates the capacity based on the information from reservation and on-demand instances and the predicted workload. The paper focuses on model creation and less on the properties of the cloud pricing models. |
| 48 / 24|  Rizou and Polyviou | Towards value-based resource provisioning in the cloud | 2012 | Conference | The aim of the paper is to increase the revenue of cloud providers by introducing value-based pricing strategies. The implementation is proposed as an outlook.  | No | The paper describes various aspects such as resource provisioning strategies, cloud resource architectures and pricing strategies. However, the paper focuses on the provider side, in particular how prices can be set. |
| 49 / 25|  Motta et al. | Cloud Computing: A Business and Economical Perspective | 2012 | Conference | Using an SLR, the paper presents an overview of cloud computing, in particular economic aspects.  | Yes |  The paper also deals with costs, in particular cost models such as tiered pricing which is less frequently addressed in other papers.  |
| 50 / 25|  Meinl et al. | Enabling Cloud Service Reservation with Derivatives and Yield Management | 2010 | Conference | The article examines reservation systems in cloud computing and how the reservation price can be optimized. | No | Apart from a brief introduction to dynamic pricing, there is no further information on the cost structure in cloud computing but rather specific approaches to optimize the reserved pricing mechanism.   |
| 51 / 26|  Kiran et al. | Lambda architecture for cost-effective batch and speed big data processing | 2015 | Conference | The article develops a cloud architecture for processing big data. | No |  When creating the architecture, care was taken to select a cost-optimized approach that applies specifically to this architecture. Only specific prices are compared and no further cost types or structures are analyzed.   |
| 52 / 26|  Choudhary et al. | Enabling Cloud Service Reservation with Derivatives and Yield Management | 2022 | Conference | The article is a comparison or a review of cloud service providers, whereby the different characteristics, pricing models, cloud service models etc. are discussed. | Yes |  The authors compare different pricing models and how these are represented by the usual cloud providers, such as AWS, Oracle or Google.   |
| 53 / 27|  Li et al. | Enabling Cloud Service Reservation with Derivatives and Yield Management | 2009 | Conference | The research article presents an approach to TCO and Utilization cost calculation. | No | The cost analysis is considered holistically and many factors such as power consumption, maintenance costs, etc. are also evaluated, which is outside the scope of the work.  |
| 54 / 28|  Villamizar et al. |E-Clouds: A SaaS Marketplace for Scientific Computing | 2012 | Conference | T | No |   |
| 55 / 29|  Dhirani et al. | Can IoT escape Cloud QoS and Cost Pitfalls | 2018 | Conference | | No |  |


[1]