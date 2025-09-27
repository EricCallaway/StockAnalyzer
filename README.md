# StockAnalyzer

# Virtual Environment
$ bash venv_stock

This will activate your virtual environment for the stock analysis project.

# DataPipeline Directory
## Data Ingestion
This directory is where all the data ingestion processes will happen. This includes external API's, manual uploads of data and any other ingress into the system.

## Data Transformation
This directory is where all the data transformation/processing will happen.

## Data Orchestration
This direcotry is responsible for handling all of the orchestration of the data. Processes will rely on logic within this directory retrieve data for the rest of the system to use.
This will act as an internal API to the rest of the system.


project-root/
├── data/                 # Data warehouse and processing
│   ├── warehouse/        # Data warehouse tables and schemas
│   │   ├── raw/          # Raw data storage
│   │   ├── staging/      # Staging tables
│   │   └── marts/        # Business logic marts
│   ├── dbt/              # dbt project
│   │   ├── models/       # dbt models
│   │   ├── seeds/        # Reference data
│   │   ├── tests/        # dbt tests
│   │   ├── macros/       # dbt macros
│   │   └── dbt_project.yml
│   └── scripts/          # Data processing scripts
│
├── services/
│   ├── backend/          # FastAPI service (API only)
│   │   ├── app/          # FastAPI application code
│   │   │   ├── api/      # API routes
│   │   │   ├── core/     # Config, startup, shutdown
│   │   │   ├── models/   # Pydantic models & DB models
│   │   │   ├── services/ # Business logic
│   │   │   └── main.py   # FastAPI entry point
│   │   ├── tests/        # Backend API tests
│   │   ├── requirements.txt # Python dependencies
│   │   └── Dockerfile    
│   │
│   ├── data_pipeline/    # Airflow service (DAGs + Python modules)
│   │   ├── dags/         # Airflow DAG definitions
│   │   │   ├── stock_data_pipeline.py
│   │   │   └── data_quality_checks.py
│   │   ├── modules/      # Reusable Python modules
│   │   │   ├── data_ingestion/ # Data ingestion components
│   │   │   │   └── integrations/ # External API integrations
│   │   │   ├── data_transformation/ # Data transformation logic
│   │   │   └── data_orchestration/ # Workflow orchestration & distribution
│   │   │       ├── connectors/ # Database & external system connectors
│   │   │       └── workflows/ # Data distribution workflows
│   │   ├── tests/        # Data pipeline tests
│   │   ├── requirements.txt # Airflow + pipeline dependencies
│   │   ├── airflow.cfg   # Airflow configuration
│   │   └── Dockerfile    # Airflow server containerization
│   │
│   └── frontend/         # Node.js + React service
│       ├── server/       # Node.js server (API proxy, auth, etc.)
│       │   ├── routes/   
│       │   ├── middleware/
│       │   ├── utils/    
│       │   └── index.js  # Node.js entry point
│       ├── client/       # React app
│       │   ├── public/   
│       │   ├── src/      
│       │   │   ├── components/
│       │   │   ├── pages/
│       │   │   ├── hooks/
│       │   │   ├── context/
│       │   │   └── index.jsx
│       │   ├── package.json
│       │   └── Dockerfile
│       └── Makefile      # Frontend build commands
│
├── docker-compose.yml    # To spin up backend + frontend together
└── README.md


$ python -m pip install "fastapi[standard]"


# Start Fast API Server
cd /backend
poetry run uvicorn app.main:app --reload

# Start Node JS Server
cd frontend/server/
node index.js

# Start React Dev Server
cd frontend/client/
npm start

cd backend && poetry run uvicorn app.main:app --reload