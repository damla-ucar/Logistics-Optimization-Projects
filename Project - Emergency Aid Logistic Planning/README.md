# 🚨 Logistics Planning for Emergency Aid Distribution Centers

This project focuses on designing a **logistics optimization model** to plan the placement of emergency aid distribution centers in disaster-affected regions.  
Developed as part of coursework in Distribution Logistics, Bilkent University.

Natural disasters often strike unexpectedly, making **fast and effective aid distribution** critical. By strategically locating temporary aid centers, we can **maximize population coverage**, **reduce total transportation distances**, and operate efficiently within real-world constraints.

---

## 🧩 **Problem Overview**
The project addresses three real-world logistics scenarios:
1. **Full coverage**: Place as many centers as needed so that every affected district is within a given radius.
2. **Maximize coverage under budget constraints**: Place at most 4 centers to cover as many people as possible.
3. **Minimize total distance**: Place at most 4 centers to reduce overall distance from districts to centers.

Each was tested for coverage radii of **2km, 3km, 4km, 5km, and 6km**.

Centers must also be located near major roads or transportation hubs to ensure supply accessibility.

---

## **Methodology**
- Built **mixed-integer programming (MIP)** models using **Gurobi**.
- Explored trade-offs between number of centers, coverage radius, and total distance.
- Analyzed sensitivity of results to radius changes.
- Focused on **population coverage**, **logistics feasibility**, and **cost-effectiveness**.

---

## **Key Findings & Insights**
- Larger radii reduce the number of centers required for complete coverage.
- With only 4 centers allowed, increasing radius can significantly improve population coverage.
- Some scenarios yield multiple equally optimal solutions, allowing flexibility in site choice.
- Minimizing distance helps speed up delivery and reduce operational cost.

Even when resources are limited, data-driven optimization improves aid delivery efficiency.

---

## **Repository Contents**
- `Code/`: Python notebooks implementing optimization models (with Gurobi) for all three scenarios.
- **Note**: Only the **2km and 3km radius cases** are included in this repo for demonstration.
- `Report.pdf`:  Contains full methodology, visualizations, and analysis.

📌 *The raw data has been omitted due to confidentiality.*

---

## ✅ **Conclusion**
This project demonstrates how **optimization modeling** and **logistics planning** can save lives in disaster response by improving speed, coverage, and resource allocation.  
It highlights the value of **data-driven decision-making** in humanitarian logistics.


