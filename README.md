초기 개발단계입니다.

백엔드 서버기반이며, FileUpload, Download 모두 가능하고, base64기반 시각화를 위한 base64 Serving API도 제공합니다.

## Index
  - [Overview](#overview) 
  - [Contributing](#contributing)
  - [Authors](#authors)


## Overview
<!-- Write Overview about this project -->
*Based on the present point, deep learning learning in MITS has changed to be based on the whole server side.*

For this reason, file system production became inevitable in the process of building all learning infrastructure, pipelines, and MLOs.
In the process of using media servers such as AWS S3 or GCP storage services, due to legal or cost issues of loading medical data
It had to be self-stored, and it tried to solve the problem based on Binary Chunck storytelling for reasons such as simplification of services and reduction of development craft,
As the answer, we are developing MongoDB's GridFS.


*현 사점을 기준으로 MITS의 딥러닝 학습이 전체 서버사이드 기반으로 바뀌었습니다.*

해당 사유로 학습인프라, 파이프라인, MLOps 등 모두 구축하는 과정에서 파일시스템 제작이 불가피해졌습니다.
AWS S3 혹은 GCP 스토리지 서비스 등등 미디어 서버를 사용하는 과정에선 의료데이터를 적재하는 법률적 문제 혹은 비용적 문제 때문에
자체적으로 스토리징을 해야했으며 서비스의 단순화, 개발공수의 절감등의 사유로 Binary Chunck 스토리징 기반으로 해당 문제를 해결하려 했으며,
그 해답으로 MongoDB의 GridFS를 채택하여 개발중입니다.


## Contributing
<!-- Write the way to contribute -->
I am looking for someone to help with this project. Please advise and point out.  
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code
of conduct, and the process for submitting pull requests to us.

## Authors
  - [Sxngt](https://github.com/sxngt) - **SangHyun Yun** - <sxngt@icloud.com>
