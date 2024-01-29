# Wolfiebot: AI-Powered Virtual Admissions Bot

## Introduction
Wolfiebot is an AI-powered Virtual Admissions Bot developed using OpenAI and Microsoft Azure, designed for Stony Brook University Admissions. It aids high school students with queries about college attendance, application procedures, campus life, education funding, and courses. Wolfiebot is built on LangChain and deployed on Azure, incorporating Azure Web App, Blob Storage, Cognitive Search, Vector Database, and Container Registry.


# Team Members

| Name              | School                           | Email                                 |
|-------------------|----------------------------------|---------------------------------------|
| Arnav Saxena      | Stony Brook University           | arsaxena@cs.stonybrook.edu            |
| Shreepooja Singh  | Stony Brook University           | shreepooja.singh@stonybrook.edu       |
| Prakash Upadhyay  | Stony Brook University           | prakash.upadhyay@stonybrook.edu       |
| Ronald Ngounou    | University of the District of Columbia | ronald.ngounou@yahoo.com        |

## Purpose
The Wolfiebot Virtual Admissions Bot is specifically designed for Stony Brook University to assist in the college admissions process. It serves as an innovative tool for high school students seeking information about college attendance, application procedures, and campus life at Stony Brook University.

## Access Wolfiebot Web Application
Experience the Wolfiebot Web Application, now publicly accessible. Visit here: [Wolfiebot Web App](https://georgehackathonapp.azurewebsites.net/)
s

## Azure Overview
Microsoft Azure, a comprehensive cloud computing platform, provides services such as IaaS, PaaS, and SaaS. It enables efficient application management and deployment across a global network of data centers. Azure organizes services in resource groups for streamlined management.

## Key Azure Services Used
1. **Azure Web App**: Facilitates hosting of web applications and APIs.
2. **Blob Storage**: Stores large amounts of unstructured data, serving the chatbot’s data needs.
3. **Azure Cognitive Search**: Provides a cloud search service, functioning as a vector database for efficient information retrieval.
4. **Azure Container Registry**: Manages Docker container images for chatbot deployment.

## Creating a Resource Group
Resource groups in Azure act as containers for related resources, simplifying management and deployment.

## Blob Storage & Upload
Involves creating a storage account and blob container within the resource group for storing and uploading files using Python.

## Azure Cognitive Search
Setting up a cognitive search service includes selecting pricing tiers and configuring the service using Python SDK for data indexing and retrieval.

## Streamlit Web Application
Details the creation of a Streamlit web application integrated with Azure Cognitive Search, structured for Docker containerization.

## Container Registry & Docker Image
Describes creating an Azure Container Registry and the process of building and pushing the Docker image, including login and environment variable configurations.

## Deploying to Azure Web Service
Outlines the deployment of the Docker image to an Azure Web Service and the setup of a web app with the deployed image, including environment variable configuration and startup command setting.

## Conclusion
Wolfiebot demonstrates successful deployment and interaction with Vector store. Questions are welcomed in the comments, and viewers are invited to subscribe for more insights.














#Introduction: The objective of this project is to create a chatbot using LangChain on Microsoft Azure for Stony Brook University Admissions. Key Microsoft Azure services utilized include Azure Web App, Blob Storage, Cognitive Search, Vector Database, and Container Registry. The final product is a website allowing users to interact with a database, all deployed on Azure. The report includes a code walkthrough and deployment steps.

#Azure Overview: Microsoft Azure is a cloud computing platform offering services like infrastructure as a service (IaaS), platform as a service (PaaS), and software as a service (SaaS). Azure facilitates application management and deployment across Microsoft’s global data center network. An Azure subscription is an agreement with Microsoft for using its cloud platforms or services, billed monthly or pay-as-you-go. Azure organizes services in resource groups, which are containers holding related resources for an Azure solution.

#Key Azure Services Used:

Azure Web App: Hosts web applications, APIs, and mobile backends. Simplifies hosting without infrastructure concerns. Supports deployment as code or Docker container.
Blob Storage: Optimized for storing large amounts of unstructured data, ideal for the chatbot’s data serving needs.
Azure Cognitive Search: A powerful cloud search service for web and mobile applications. Acts as a vector database, aiding the chatbot in efficient information retrieval.
Azure Container Registry: Manages and stores Docker container images, used for deploying the chatbot.
#Creating a Resource Group: The process starts with creating a resource group in Azure. Resource group is a collection of resources (services, databases, virtual machines, etc.) that are managed together. It acts like a container where related resources for an Azure solution are grouped. The group acts as a virtual folder for grouping Azure services.

#Blob Storage & Upload: A storage account is created within the resource group, followed by a blob container setup. The container is set to private access level. We uploaded files to this container using Python, highlighting the use of connection strings and container names.

#Azure Cognitive Search: A new cognitive search service is created within the resource group.We need to carefully select pricing tiers to avoid high costs, hence recommending the free tier. The service is then configured using Python SDK, including creating an index and inserting data from Blob storage.

#Streamlit Web Application: This section walks through the development of a Streamlit web application. It uses Azure Cognitive Search Retriever and other objects like conversation buffer memory. The application code, structured for UI creation, is prepared for Docker containerization.

#Container Registry & Docker Image: A new Azure Container Registry is created. Then building and pushing the Docker image to this registry, including login procedures and setting environment variables is done.

#Deploying to Azure Web Service: The final step involves deploying the Docker image to an Azure Web Service, and creating a web app with the deployed image. The process includes configuring environment variables and ensuring the correct startup commands are set.

#Conclusion: We have successfully demonstrated the deployed chatbot called Wolfiebot and showed its interaction with the Vector store. The presenter encourages questions in the comments and invites viewers to subscribe to the channel.
