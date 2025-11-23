# capstone project

`title:` : InsightFlow
`desc` : AI-Powered Task Management & Insight Dashboard
`concept`: Smart Productivity Analytics & Task Management Platform

## description

A task management web application that also uses machine learning to analyze productivity, predict task delays, and generate automated performance reports.

Ideal for teams, IT companies, or student groups.

## Key Features

1. Task Management (API-driven)

   - Create / update / delete tasks
   - Assign tasks to users
   - Task deadlines, priority
   - Task status tracking
   - Comments & activity logs
   - All endpoints built using FastAPI

2. Data Dashboard

   - Using React (or any frontend)
   - Shows graphs:
   - Tasks completed per user
   - Productivity per week
   - Category-wise task distribution
   - User workload heatmap
   - Data fetched from FastAPI analytics endpoints

3. Machine Learning Insights

   - Predict which tasks may get delayed
   - Identify users with overload
   - Estimate task completion time using ML
   - Clustering to find similar working patterns
   - ML model using:
     - Scikit-Learn
     - Pandas
   - Joblib model saved & loaded in FastAPI

4. Automated Report Generator
   - Weekly PDF/email report for every user:
   - Summary of completed tasks
   - Predicted delays
   - Productivity score
   - Suggestions for improvement
   - Generate PDF via:
     - ReportLab or WeasyPrint
     - Sent via FastAPI scheduled tasks (sta)
