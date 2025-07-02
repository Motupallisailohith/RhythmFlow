# RhythmFlow

A comprehensive data pipeline showcasing real-time and batch processing with Kafka, Spark Streaming, dbt, Docker, Airflow, Terraform, and Google Cloud Platform.

## Description

### Objective

RhythmFlow is designed to simulate a music streaming service (like Spotify) by generating and processing real-time user event data. This data, including song listens, website navigation, and user authentication, is consumed by a robust data pipeline. Real-time processing is performed, with data periodically stored in a data lake (every two minutes). Subsequently, an hourly batch job transforms this data to create analytics-ready tables for a dashboard. The project aims to derive insights into metrics such as popular songs, active users, and user demographics.

### Dataset

The project utilizes [Eventsim](https://github.com/Interana/eventsim), a program that generates realistic, albeit fake, event data for a music streaming website. The Docker image for Eventsim is sourced from [viirya's maintained fork](https://github.com/viirya/eventsim). Eventsim leverages a [subset of 10,000 songs](http://millionsongdataset.com/pages/getting-dataset/#subset) from the [Million Songs Dataset](http://millionsongdataset.com) to simulate user interactions.

### Tools & Technologies

* **Cloud Platform:** [Google Cloud Platform (GCP)](https://cloud.google.com)
* **Infrastructure as Code:** [Terraform](https://www.terraform.io)
* **Containerization:** [Docker](https://www.docker.com), [Docker Compose](https://docs.docker.com/compose/)
* **Stream Processing:** [Apache Kafka](https://kafka.apache.org), [Apache Spark Streaming](https://spark.apache.org/docs/latest/streaming-programming-guide.html)
* **Orchestration:** [Apache Airflow](https://airflow.apache.org)
* **Data Transformation:** [dbt (data build tool)](https://www.getdbt.com)
* **Data Lake:** [Google Cloud Storage (GCS)](https://cloud.google.com/storage)
* **Data Warehouse:** [Google BigQuery](https://cloud.google.com/bigquery)
* **Data Visualization:** [Looker Studio (formerly Data Studio)](https://datastudio.google.com/overview)
* **Programming Language:** [Python](https://www.python.org)

### Architecture

![RhythmFlow Architecture](https://github.com/Motupallisailohith/RhythmFlow/blob/main/RhythmFlow.png)
*Figure 1: High-level architectural overview of the RhythmFlow data pipeline.*

### Final Result

![Dashboard Example](https://github.com/Motupallisailohith/RhythmFlow/blob/main/images/RhythFlow_Dashboard.png)
*Figure 2: Example dashboard visualizing processed music streaming data.*

## Setup

**WARNING:** Running this project will incur charges on your Google Cloud Platform account. New GCP accounts may be eligible for $300 in free credits.

### Prerequisites

To set up and run RhythmFlow, ensure you have the following in place:

* **Google Cloud Platform Account:**
    * [GCP Account and Access Setup](setup/gcp.md)
    * [gcloud CLI alternate installation method - Windows](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/week_1_basics_n_setup/1_terraform_gcp/windows.md#google-cloud-sdk)
* **Terraform:**
    * [Terraform Setup Guide](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/week_1_basics_n_setup/1_terraform_gcp/windows.md#terraform)


### Debugging

If you encounter any issues during setup or operation, refer to the [debug guide](setup/debug.md).

### Future Enhancements

There are many opportunities to enhance this project:

* **Managed Infrastructure:**
    * Utilize Cloud Composer for Airflow orchestration.
    * Integrate with Confluent
