<h1 align="center"> <p> Rail3D </p></h1>
<h3 align="center">
<a href="" target="_blank">Rail3D: Multi-Context Point Cloud Dataset and New Approach for Railways Semantic Understanding</a>
</h3>

In this paper, we propose the first multi-context point cloud dataset called Rail3D. This dataset covers three countries: Hungary, France, and Belgium, with a total length of almost 5.8 kilometers and approximately 288 million points. It covers the 9 most relevant classes for railway applications: Ground, Vegetation, Rail, Poles, Wires, Signalling, Fenc-es, Installations, and Buildings. Our novel approach employs the LightGBM machine learning model for semantic segmentation, showcasing promising performance on three distinct railway datasets. It achieves significantly higher mean Intersection over Union (IoU) scores compared 3DMASC, but still behind the KPConv performance. The best per-forming model, a fine-tuned KPConv, achieved a mean Intersection over Union (mIoU) of 86%. While ours achieved a mIoU of 71%, outperforming Random Forest with 70%. The Rail3D dataset, publicly available for France and Hungary, will overcomes limitations in existing datasets, fostering the training of more generalizable learning models. We are also looking for feedback from the user community to improve our approach and grow the da-taset with other countries. We recommend evaluating our developed dataset with alterna-tive deep learning methods to assess their performance. Additionally, exploring the de-veloped method in diverse railway contexts by selecting different objects. Future work in-volves the exploration of semantic information within the Rail3D for 3D change detection, aiming to assess the use of semantics for change detection in different railway contexts.

## ⭐ Download

Please fill out this [**Data Request**](https://forms.gle/2iLWQQhhyRfzGrgq5) if you have access to Google Forms. 

Download links will be sent automatically after completing the application.

## 📌 Dataset

This section details the process of creating the datasets and the methods developed. We begin by describing the data specifications, then the used classes, and how the annotation process was performed.
## Dataset specification
The Rail3D dataset is the first multi-context point cloud dataset for railway semantic understanding. It is composed of three distinct datasets from Hungary, France, and Belgium, providing a diverse representation of the railway. We annotated three datasets for rail-way scene understanding: HMLS, SNCF, and INFRABEL. The first two datasets are publicly available and provide a diverse representation of railway environments. The third dataset was provided by Infrabel, the Belgian railway infrastructure manager, under a confidentiality agreement. The datasets were acquired using different LiDAR sensors, en-suring a wide range of point densities and acquisition conditions. This diversity is crucial for developing robust and generalizable models for railway scene understanding. The specifications of each dataset are detailed in the subsections below.
### Hungarian MLS point clouds of railroad environment
This LiDAR dataset represents a collection acquired by the Hungarian State Railways using the mobile mapping system (MMS); Riegl VMX-450 high-density. These LiDAR scans were conducted from a railroad vehicle recording data at a rate of 1.1 million points per second. It exhibited high precision, with an average 3D range accuracy of 3 mm and a maximum threshold of 7 mm, ensuring high-quality data capture. The positional accuracy of the acquired point clouds averaged 3 cm, with a maximum threshold of 5 cm. This dataset not only contain georeferenced spatial information in the form of 3D coordinates but also incorporate intensity and RGB data, enhancing their utility for diverse applica-tions. The datasets adhere to the Hungarian national spatial reference system, designated as EPSG:23700, ensuring their compatibility with regional mapping efforts. Originally, three distinct datasets were thoughtfully selected, each representing different topograph-ical regions within Hungary. The original data can be found at: https://data.mendeley.com/datasets/ccxpzhx9dj/ under CC BY NC 3.0 licence.  

### French MLS point clouds of railroad environment
The SNCF LiDAR dataset is a valuable resource provided by SNCF Reseau, the French state-owned railway company. This dataset comprises approximately 2 kilometers of rail-borne LiDAR data, representing a non-annotated subset of a more extensive collection. The geospatial reference system employed for this dataset is RGF93-CC44 / NGF-IGN69, ensuring its alignment with regional mapping standards and geographic referencing. The dataset is primarily presented in the compressed LAZ format with a total of 16 tiles publicly available under the Open Database License (ODbL). 


### Belgian MLS point clouds of railroad environment
For several years, Infrabel, the Belgian railway infrastructure manager, was using LiDAR technology to acquire data about the country's railway network. The lidar acquisition process involves mounting a Z+F 9012 lidar sensor on the front part of a train (EM202 vehicle) and recording the point cloud data as the train travels along the tracks. The train collects data for every railway line in Belgium at least twice a year. This is highly relevant for 3D detection of change studies, which we will be looking at in our next studies. In ad-dition to LiDAR, 4 cameras are used to capture the colours, 2 at the front and 2 at the back. However, for this application, we only used the point cloud with intensity, and without colours. The point clouds are encoded in LAS format and the coordinates are in Lambert Belge 72. We have chosen three different areas in Belgium; Brussels, mid-way Brussels and Ghent, and the south of Ghent. Each of these contexts presented a different challenge, either in terms of occlusion, complexity, or unbalanced classes. 

## Classes typology
To ensure the comprehensiveness and relevance of the class labels, we conducted a thorough review of existing literature and consulted with railway industry experts. Therefore, we have not limited our analysis to the meaning and geometric appearance of each class, but also its relevance to the railway industry. This resulted in the following list of classes and their corresponding objects as illustrated in Figure 5:
•	Ground (label 1): Represents various ground surfaces, including rough ground, cement, and asphalt.
•	Vegetation (label 2): Covers all types of vegetation present in the railway environment, such as trees, and median vegetation.
•	Rail (label 3): Refers to the physical track structure; rails.
•	Poles (label 4): Includes all types of poles found along the railway, such as catenary poles, and utility poles.
•	Wires (label 5): Covers various overhead wires, including catenary wires, power lines, and communication cables.
•	Signalling (label 6): Represents all types of railway signaling equipment, such as traffic lights, and traffic signs.
•	Fence (label 7): Includes various types of fences and barriers used along the railway, such as security fences, noise insulation panels, and guardrails. 
•	Installation (label 8): Refers to larger structures that are part of the railway infrastructure, such as boxes, and passenger cabins. 
•	Building (label 9): Covers all types of buildings located within the railway corridor, such as houses, warehouses, and stations.


## ⭐ Benchmark

Coming soon...

## ✔ Code

Coming soon...

## ✨ Citation

If you find our work useful in your research, please consider citing:

```
@article{

}
```
## 🙌 Acknowledgements

This study is part of the first author’s Ph.D. thesis. We thank the dataset providers. The original data used in this study are publicly available at: https://ressources.data.sncf.com/explore/dataset/nuage-points-3d for French data, and at https://data.mendeley.com/datasets/ccxpzhx9dj for Hungarian data (accessed on 28 November 2023).

## 🤝 Related Work

1. [KPconv: Flexible and Deformable Convolution for Point Clouds](https://github.com/HuguesTHOMAS/KPConv)



