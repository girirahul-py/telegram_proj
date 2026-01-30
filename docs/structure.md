repocontrol/
│
├── app/
│   ├── main.py                # App entry point
│   │
│   ├── core/                  # Core system logic
│   │   ├── config.py          # Config & env
│   │   └── github_client.py   # GitHub API wrapper
│   │
│   ├── services/              # Business logic
│   │   ├── permission.py      # Permission engine
│   │   ├── repo_service.py    # Repo operations
│   │   └── deploy_service.py  # Deployment logic
│   │
│   ├── api/                   # API layer
│   │   ├── routes/
│   │   │   ├── repos.py
│   │   │   ├── branches.py
│   │   │   └── deploy.py
│   │   └── router.py
│   │
│   └── utils/
│       └── responses.py
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── requirements.txt
├── README.md
└── .env
