# SRS – SOFTWARE REQUIREMENTS SPECIFICATION

#    **Functional Requirements (WHAT system must do)**

        FR-1: Repository Management

            System must list all repositories the user has access to

            System must support multiple repositories

        FR-2: Permission Validation

            System must check GitHub permissions before any action

            System must block action if permission is insufficient

        FR-3: Branch Management

            Create a new branch from default branch

            Prevent duplicate branch creation

        FR-4: Merge Management

            Merge source branch into target branch

            Handle merge conflicts safely

        FR-5: Deployment Trigger

            Deployment must start only after successful merge

            Deployment must be automated using CI/CD

        FR-6: Audit Safety (basic)

            System must return clear success or failure messages
    
#    **Non-Functional Requirements (HOW it should behave)**

        Secure (no hardcoded secrets)

        Scalable (supports many repos)

        Reliable (no direct server access from user)

        Simple UI/API for beginners