# AI-Powered Retail Decision Support System

## Overview
This project presents an AI-powered decision support system designed to help
retail business owners make informed, data-driven decisions.

Unlike traditional analytics dashboards, the system integrates multiple AI
modules and presents insights in a business-friendly manner through a chatbot
and dashboard interface.

The system focuses on explanation and recommendation rather than prediction
alone.

---

## Project Objectives
- Analyze customer behavior inside retail stores
- Support inventory and staffing decisions
- Measure customer satisfaction and business performance
- Translate AI outputs into actionable business insights

---

## System Components
- Computer Vision for foot traffic analysis
- Sales forecasting using POS data
- Customer segmentation based on purchasing behavior
- Sentiment analysis of customer reviews
- Business KPI aggregation
- AI chatbot for natural language interaction

---

## Repository Structure
```
ai-retail-decision-support-system/
│
├── data/
│   ├── outputs/
│   ├── processed/
│   └── raw/
│       ├── customer_segmentation/
│       ├── cv_foot_traffic/
│       ├── inventory/
│       ├── reviews_analysis/
│       ├── sales_forecasting/
│       └── yolo/
│
├── modules/
│   ├── cv_foot_traffic/
│   │   ├── notebook.ipynb
│   │   ├── model.py
│   │   └── output_generator.py
│   │
│   ├── sales_forecasting/
│   │   ├── notebook.ipynb
│   │   ├── forecast_model.py
│   │   └── output_generator.py
│   │
│   ├── inventory_management/
│   │   ├── notebook.ipynb
│   │   ├── inventory_logic.py
│   │   ├── stock_generation.py
│   │   └── output_generator.py
│   │
│   ├── customer_segmentation/
│   │   ├── notebook.ipynb
│   │   ├── output_generator.py
│   │   └── segmentation_model.py
│   │
│   ├── review_analysis/
│   │   ├── notebook.ipynb
│   │   ├── output_generator.py
│   │   └── topic_model.py
│   │
│   └── chatbot/
│       ├── intents.json
│       ├── chatbot.py
│       └── response_logic.py
│
├── dashboard/
│   └── app.py
│
├── schemas/
│   ├── cv_foot_traffic_schema.json
│   ├── sales_forecasting_schema.json
│   ├── customer_segmentation_schema.json
│   └── review_analysis_schema.json
│
├── docs/
│   ├── architecture.txt
│   ├── business_kpis.md
│   ├── system_architecture.md
│   ├── project_overview.md
│   └── evaluation_plan.md 
│
├── README.md
└── requirements.txt

```
---

## Documentation
Detailed documentation can be found in the `docs/` directory:
- System architecture
- Business KPIs
- Evaluation plan
- Project overview

---

## Team Workflow
Each AI module is developed independently.
All module outputs must follow predefined schemas to ensure smooth integration.

---

## Disclaimer
This project is developed for academic purposes.
Business impact metrics are indicative and based on historical or simulated data.
