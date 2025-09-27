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
├── backend/              # FastAPI service
│   ├── app/              # Your FastAPI application code
│   │   ├── api/          # API routes
│   │   ├── core/         # Config, startup, shutdown
│   │   ├── models/       # Pydantic models & DB models
│   │   ├── services/     # Business logic
│   │   └── main.py       # FastAPI entry point
│   ├── tests/            # Backend tests
│   ├── requirements.txt  # Python dependencies
│   └── Dockerfile        
│
├── frontend/             # Node.js + React service
│   ├── server/           # Node.js server (API proxy, auth, etc.)
│   │   ├── routes/       
│   │   ├── middleware/   
│   │   ├── utils/        
│   │   └── index.js      # Node.js entry point
│   ├── client/           # React app
│   │   ├── public/       
│   │   ├── src/          
│   │   │   ├── components/
│   │   │   ├── pages/
│   │   │   ├── hooks/
│   │   │   ├── context/
│   │   │   └── index.jsx
│   ├── package.json
│   └── Dockerfile
│
├── docker-compose.yml    # To spin up backend + frontend together
└── README.md


$ python -m pip install "fastapi[standard]"

cd backend && poetry run uvicorn app.main:app --reload