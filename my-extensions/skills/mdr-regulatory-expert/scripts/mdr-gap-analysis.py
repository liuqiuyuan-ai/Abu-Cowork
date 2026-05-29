#!/usr/bin/env python3
"""
MDR Gap Analysis Tool - EU MDR 2017/745 Compliance Gap Assessment

This script helps assess compliance with EU MDR 2017/745 requirements.
"""

import json
import datetime
from typing import List, Dict, Optional


class MDRGapAnalyzer:
    """
    MDR Compliance Gap Analysis Class
    """
    
    def __init__(self):
        self.mdr_requirements = {
            "article_10": {
                "title": "Article 10 - Responsibilities of Manufacturers",
                "requirements": [
                    "Quality management system established",
                    "Risk management system implemented",
                    "Technical documentation prepared",
                    "Declaration of conformity issued",
                    "CE marking applied",
                    "Registration in EUDAMED",
                    "Post-market surveillance system established"
                ]
            },
            "annex_i": {
                "title": "Annex I - General Safety and Performance Requirements (GSPR)",
                "requirements": [
                    "Device meets general safety requirements",
                    "Risk management documented",
                    "Clinical benefits outweigh residual risks",
                    "Device performs as intended",
                    "Side-effects acceptable",
                    "Information provided to users"
                ]
            },
            "annex_ii": {
                "title": "Annex II - Technical Documentation",
                "requirements": [
                    "Device description and specification",
                    "Design and manufacturing information",
                    "GSPR checklist completed",
                    "Benefit-risk analysis documented",
                    "Risk management file complete",
                    "Clinical evaluation conducted",
                    "Labeling and IFU prepared"
                ]
            },
            "annex_iii": {
                "title": "Annex III - Technical Documentation on Post-Market Surveillance",
                "requirements": [
                    "PMS plan developed",
                    "Serious incident reporting procedures",
                    "Trend reporting procedures",
                    "Field safety corrective actions procedures",
                    "Periodic safety update reports"
                ]
            },
            "annex_xiv": {
                "title": "Annex XIV - Clinical Evaluation and PMCF",
                "requirements": [
                    "Clinical evaluation plan prepared",
                    "Literature search conducted",
                    "Clinical data analysis performed",
                    "Clinical evaluation report prepared",
                    "PMCF plan developed",
                    "PMCF evaluation reports prepared"
                ]
            }
        }
    
    def assess_compliance(self, assessment_data: Dict) -> Dict:
        """
        Assess MDR compliance based on provided data
        
        Args:
            assessment_data: Dictionary with compliance status for each requirement
        
        Returns:
            Dictionary with compliance assessment results
        """
        total_requirements = 0
        compliant_requirements = 0
        findings = []
        
        for area, data in self.mdr_requirements.items():
            for req in data["requirements"]:
                total_requirements += 1
                status = assessment_data.get(area, {}).get(req, "unknown")
                
                if status == "compliant":
                    compliant_requirements += 1
                elif status in ["non-compliant", "partial"]:
                    findings.append({
                        "requirement": req,
                        "status": status,
                        "area": data["title"]
                    })
        
        compliance_percentage = (compliant_requirements / total_requirements) * 100
        
        return {
            "assessment_date": datetime.datetime.now().isoformat(),
            "total_requirements": total_requirements,
            "compliant_requirements": compliant_requirements,
            "compliance_percentage": round(compliance_percentage, 2),
            "overall_status": self._determine_overall_status(compliance_percentage),
            "findings": findings,
            "recommendations": self._generate_recommendations(findings)
        }
    
    def _determine_overall_status(self, percentage: float) -> str:
        """
        Determine overall compliance status
        
        Args:
            percentage: Compliance percentage
        
        Returns:
            Status string
        """
        if percentage >= 90:
            return "Compliant"
        elif percentage >= 70:
            return "Partially Compliant"
        else:
            return "Non-Compliant"
    
    def _generate_recommendations(self, findings: List) -> List[str]:
        """
        Generate improvement recommendations
        
        Args:
            findings: List of non-compliant items
        
        Returns:
            List of recommendations
        """
        recommendations = []
        
        if not findings:
            recommendations.append("MDR compliance appears satisfactory")
            recommendations.append("Continue monitoring regulatory updates")
            return recommendations
        
        # Group findings by area
        areas = {}
        for finding in findings:
            area = finding["area"]
            if area not in areas:
                areas[area] = []
            areas[area].append(finding["requirement"])
        
        recommendations.append("Priority action items:")
        for area, items in areas.items():
            recommendations.append(f"  {area}:")
            for item in items:
                recommendations.append(f"    - {item}")
        
        recommendations.append("\nGeneral recommendations:")
        recommendations.append("1. Develop comprehensive compliance roadmap")
        recommendations.append("2. Engage Notified Body early for guidance")
        recommendations.append("3. Update technical documentation to MDR format")
        recommendations.append("4. Strengthen clinical evaluation if needed")
        recommendations.append("5. Establish robust PMS system")
        
        return recommendations
    
    def generate_classification_checklist(self, device_info: Dict) -> List[Dict]:
        """
        Generate classification decision checklist
        
        Args:
            device_info: Dictionary with device characteristics
        
        Returns:
            List of classification considerations
        """
        checklist = []
        
        # Duration
        duration = device_info.get("duration", "transient")
        duration_map = {
            "transient": "Rule 1-5 (typically)",
            "short_term": "Rule 6-10",
            "long_term": "Rule 11-13",
            "permanent": "Rule 11-13"
        }
        checklist.append({
            "criterion": "Device Duration",
            "value": duration,
            "applicable_rules": duration_map.get(duration, "Review Annex VIII")
        })
        
        # Invasiveness
        invasive = device_info.get("invasive", False)
        checklist.append({
            "criterion": "Invasive Device",
            "value": invasive,
            "applicable_rules": "Rule 6-8 for invasive devices"
        })
        
        # Active device
        active = device_info.get("active", False)
        checklist.append({
            "criterion": "Active Device",
            "value": active,
            "applicable_rules": "Rule 9-13 for active devices"
        })
        
        # Software
        software = device_info.get("software", False)
        checklist.append({
            "criterion": "Software Device",
            "value": software,
            "applicable_rules": "MDCG 2019-11 for software"
        })
        
        return checklist


def main():
    """
    Example usage of MDRGapAnalyzer
    """
    analyzer = MDRGapAnalyzer()
    
    # Example assessment data
    assessment_data = {
        "article_10": {
            "Quality management system established": "compliant",
            "Risk management system implemented": "compliant",
            "Technical documentation prepared": "partial",
            "Declaration of conformity issued": "non-compliant",
            "CE marking applied": "non-compliant",
            "Registration in EUDAMED": "partial",
            "Post-market surveillance system established": "partial"
        },
        "annex_i": {
            "Device meets general safety requirements": "compliant",
            "Risk management documented": "compliant",
            "Clinical benefits outweigh residual risks": "compliant",
            "Device performs as intended": "compliant",
            "Side-effects acceptable": "compliant",
            "Information provided to users": "compliant"
        },
        "annex_ii": {
            "Device description and specification": "compliant",
            "Design and manufacturing information": "compliant",
            "GSPR checklist completed": "partial",
            "Benefit-risk analysis documented": "compliant",
            "Risk management file complete": "compliant",
            "Clinical evaluation conducted": "partial",
            "Labeling and IFU prepared": "compliant"
        }
    }
    
    # Perform assessment
    result = analyzer.assess_compliance(assessment_data)
    print("MDR Compliance Gap Analysis Results:")
    print(json.dumps(result, indent=2))
    
    # Generate classification checklist
    print("\nClassification Checklist:")
    device_info = {
        "duration": "long_term",
        "invasive": True,
        "active": False,
        "software": False
    }
    checklist = analyzer.generate_classification_checklist(device_info)
    print(json.dumps(checklist, indent=2))


if __name__ == "__main__":
    main()