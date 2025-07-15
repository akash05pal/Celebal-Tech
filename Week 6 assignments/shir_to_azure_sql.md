# Configure Self-hosted Integration Runtime (SHIR) for Local to Azure SQL Data Load

1. Install SHIR on your local server (download from Azure Data Factory > Integration Runtimes > New > Self-hosted).
2. Register the SHIR with your Azure Data Factory instance using the authentication key.
3. In ADF, create a Linked Service for your on-premises database using the SHIR.
4. Create a Linked Service for your Azure SQL Database.
5. Build a pipeline with a Copy Data activity:
   - Source: On-premises DB (via SHIR Linked Service)
   - Sink: Azure SQL DB (via Azure SQL Linked Service)
6. Publish and trigger the pipeline. 