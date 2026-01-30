# SYSTEM DESIGN (ARCHITECT VIEW)

# High-Level Architecture (HLD)

            User (API / Bot)
                ↓
            Automation Backend (FastAPI)
                ↓
            Permission Engine
                ↓
            GitHub API
                ↓
            GitHub Actions (CI/CD)
                ↓
            Server (Deploy)


# 🧠 MENTAL MODEL 

User → Backend → Permission Check → GitHub → CI/CD → Server
