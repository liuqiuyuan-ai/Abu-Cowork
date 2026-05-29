#!/usr/bin/env python3
"""
QSR Compliance Checker - 21 CFR Part 820 Quality System Regulation Assessment

This script helps assess compliance with FDA Quality System Regulation.
"""

import json
import datetime
from typing import List, Dict


class QSRComplianceChecker:
    """
    QSR Compliance Assessment Class
    """
    
    def __init__(self):
        self.qsr_requirements = {
            "management_controls": {
                "title": "Management Controls (820.20)",
                "requirements": [
                    "Quality policy established and communicated",
                    "Organizational structure defined",
                    "Responsibilities assigned",
                    "Management review conducted",
                    "Quality objectives established"
                ]
            },
            "design_controls": {
                "title": "Design Controls (820.30)",
                "requirements": [
                    "Design planning",
                    "Design inputs",
                    "Design outputs",
                    "Design review",
                    "Design verification",
                    "Design validation",
                    "Design transfer",
                    "Design changes",
                    "Design history file"
                ]
            },
            "document_controls": {
                "title": "Document Controls (820.40)",
                "requirements": [
                    "Document approval before issuance",
                    "Document review and update",
                    "Document revision status identified",
                    "Current documents available at points of use",
                    "Obsolete documents removed"
                ]
            },
            "purchasing_controls": {
                "title": "Purchasing Controls (820.50)",
                "requirements": [
                    "Supplier evaluation and selection",
                    "Purchase orders with requirements",
                    "Receiving inspection",
                    "Supplier quality monitoring"
                ]
            },
            "production_controls": {
                "title": "Production Controls (820.70)",
                "requirements": [
                    "Production and process controls",
                    "Device labeling control",
                    "Device packaging control",
                    "Process validation",
                    "Equipment maintenance"
                ]
            },
            "quality_assurance": {
                "title": "Quality Assurance (820.80)",
                "requirements": [
                    "Inspection and testing",
                    "Acceptance criteria",
                    "Nonconforming product control",
                    "Corrective and preventive actions",
                    "Quality audits"
                ]
            },
            "records": {
                "title": "Records (820.180)",
                "requirements": [
                    "Record maintenance",
                    "Record accessibility",
                    "Record retention",
                    "Record authenticity"
                ]
            }
        }
    
    def assess_compliance(self, assessment_data: Dict) -> Dict:
        """
        Assess QSR compliance based on provided data
        
        Args:
            assessment_data: Dictionary with compliance status for each requirement
        
        Returns:
            Dictionary with compliance assessment results
        """
        total_requirements = 0
        compliant_requirements = 0
        findings = []
        
        for area, data in self.qsr_requirements.items():
            area_findings = []
            area_compliant = 0
            
            for req in data["requirements"]:
                total_requirements += 1
                status = assessment_data.get(area, {}).get(req, "unknown")
                
                if status == "compliant":
                    compliant_requirements += 1
                    area_compliant += 1
                elif status == "non-compliant":
                    area_findings.append({
                        "requirement": req,
                        "status": "non-compliant",
                        "area": data["title"]
                    })
                elif status == "partial":
                    area_findings.append({
                        "requirement": req,
                        "status": "partial",
                        "area": data["title"]
                    })
            
            if area_findings:
                findings.extend(area_findings)
        
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
        Determine overall compliance status based on percentage
        
        Args:
            percentage: Compliance percentage
        
        Returns:
            Overall status string
        """
        if percentage >= 90:
            return "Compliant"
        elif percentage >= 70:
            return "Partially Compliant"
        else:
            return "Non-Compliant"
    
    def _generate_recommendations(self, findings: List) -> List[str]:
        """
        Generate improvement recommendations based on findings
        
        Args:
            findings: List of non-compliant items
        
        Returns:
            List of recommendations
        """
        recommendations = []
        
        if not findings:
            recommendations.append("QSR compliance appears satisfactory")
            recommendations.append("Continue regular audits and monitoring")
            return recommendations
        
        # Group findings by area
        areas = {}
        for finding in findings:
            area = finding["area"]
            if area not in areas:
                areas[area] = []
            areas[area].append(finding["requirement"])
        
        for area, items in areas.items():
            recommendations.append(f"Address non-compliant items in {area}")
            recommendations.append(f"  - {', '.join(items)}")
        
        recommendations.append("\nGeneral recommendations:")
        recommendations.append("1. Conduct regular internal audits")
        recommendations.append("2. Document all corrective actions")
        recommendations.append("3. Train personnel on QSR requirements")
        recommendations.append("4. Prepare for FDA inspection")
        
        return recommendations
    
    def get_qsr_requirements(self) -> Dict:
        """
        Get all QSR requirements
        
        Returns:
            Dictionary of QSR requirements
        """
        return self.qsr_requirements


def main():
    """
    Example usage of QSRComplianceChecker
    """
    checker = QSRComplianceChecker()
    
    # Example assessment data
    assessment_data = {
        "management_controls": {
            "Quality policy established and communicated": "compliant",
            "Organizational structure defined": "compliant",
            "Responsibilities assigned": "compliant",
            "Management review conducted": "compliant",
            "Quality objectives established": "partial"
        },
        "design_controls": {
            "Design planning": "compliant",
            "Design inputs": "compliant",
            "Design outputs": "compliant",
            "Design review": "compliant",
            "Design verification": "compliant",
            "Design validation": "compliant",
            "Design transfer": "compliant",
            "Design changes": "non-compliant",
            "Design history file": "compliant"
        },
        "document_controls": {
            "Document approval before issuance": "compliant",
            "Document review and update": "compliant",
            "Document revision status identified": "compliant",
            "Current documents available at points of use": "compliant",
            "Obsolete documents removed": "compliant"
        }
    }
    
    # Perform assessment
    result = checker.assess_compliance(assessment_data)
    print("QSR Compliance Assessment Results:")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()