#!/usr/bin/env python3
"""
UDI and EUDAMED Compliance Checker - Unique Device Identification and Database Compliance

This script helps assess UDI and EUDAMED compliance requirements.
"""

import json
import datetime
from typing import List, Dict, Optional


class UDIComplianceChecker:
    """
    UDI and EUDAMED Compliance Checking Class
    """
    
    def __init__(self):
        self.udi_requirements = {
            "udi_assignment": {
                "title": "UDI Assignment",
                "requirements": [
                    "Basic UDI-DI assigned",
                    "UDI-DI assigned to each device variant",
                    "UDI-PI assigned per device level",
                    "UDIs obtained from authorized issuing entity",
                    "UDI format complies with standards"
                ]
            },
            "labeling": {
                "title": "UDI Labeling",
                "requirements": [
                    "UDI carrier on device label",
                    "UDI carrier on all higher-level packaging",
                    "UDI-AIDC format correct",
                    "UDI-HRI readable",
                    "Human-readable format correct"
                ]
            },
            "eudamed": {
                "title": "EUDAMED Registration",
                "requirements": [
                    "Actor registration completed",
                    "Device registration completed",
                    "UDI-DI registered in EUDAMED",
                    "Certificate registration completed",
                    "Clinical investigation registration (if applicable)"
                ]
            },
            "record_keeping": {
                "title": "Record Keeping",
                "requirements": [
                    "UDI records maintained",
                    "Device history records updated",
                    "Traceability procedures established",
                    "Records available for competent authorities"
                ]
            }
        }
    
    def assess_compliance(self, compliance_data: Dict) -> Dict:
        """
        Assess UDI and EUDAMED compliance
        
        Args:
            compliance_data: Dictionary with compliance status
        
        Returns:
            Compliance assessment results
        """
        total_requirements = 0
        compliant_requirements = 0
        findings = []
        
        for area, data in self.udi_requirements.items():
            area_data = compliance_data.get(area, {})
            for req in data["requirements"]:
                total_requirements += 1
                status = area_data.get(req, "unknown")
                
                if status == "compliant":
                    compliant_requirements += 1
                elif status in ["non-compliant", "partial"]:
                    findings.append({
                        "requirement": req,
                        "status": status,
                        "area": data["title"]
                    })
        
        compliance_percentage = (compliant_requirements / total_requirements) * 100 if total_requirements > 0 else 0
        
        return {
            "assessment_date": datetime.datetime.now().isoformat(),
            "total_requirements": total_requirements,
            "compliant_requirements": compliant_requirements,
            "compliance_percentage": round(compliance_percentage, 2),
            "overall_status": self._determine_status(compliance_percentage),
            "findings": findings,
            "recommendations": self._generate_recommendations(findings)
        }
    
    def _determine_status(self, percentage: float) -> str:
        """
        Determine compliance status
        
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
        Generate recommendations
        
        Args:
            findings: List of non-compliant items
        
        Returns:
            List of recommendations
        """
        recommendations = []
        
        if not findings:
            recommendations.append("UDI/EUDAMED compliance appears satisfactory")
            return recommendations
        
        recommendations.append("Priority actions:")
        for finding in findings:
            recommendations.append(f"  - {finding['requirement']} ({finding['area']})")
        
        recommendations.append("\nGeneral recommendations:")
        recommendations.append("1. Verify UDI assignment with authorized issuing entity")
        recommendations.append("2. Update labeling to include UDI carriers")
        recommendations.append("3. Complete EUDAMED registration")
        recommendations.append("4. Establish traceability procedures")
        
        return recommendations
    
    def generate_udi_implementation_timeline(self) -> List[Dict]:
        """
        Generate UDI implementation timeline based on device class
        
        Returns:
            List of implementation milestones
        """
        return [
            {
                "phase": "Phase 1 - UDI Foundation",
                "activities": [
                    "Determine Basic UDI-DI structure",
                    "Assign UDI-DIs to device variants",
                    "Obtain UDI codes from issuing entity",
                    "Develop UDI database procedures"
                ],
                "applicable_to": "All device classes"
            },
            {
                "phase": "Phase 2 - Labeling Update",
                "activities": [
                    "Update device labels with UDI carrier",
                    "Update packaging labels",
                    "Verify AIDC and HRI formats",
                    "Test UDI readability"
                ],
                "applicable_to": "Class III, IIb, IIa, Is, Im (phased)"
            },
            {
                "phase": "Phase 3 - EUDAMED Registration",
                "activities": [
                    "Register as Actor in EUDAMED",
                    "Register devices with UDI-DIs",
                    "Upload certificate information",
                    "Maintain registration updates"
                ],
                "applicable_to": "All device classes (when EUDAMED available)"
            },
            {
                "phase": "Phase 4 - Integration",
                "activities": [
                    "Integrate UDI into QMS",
                    "Update traceability procedures",
                    "Train personnel on UDI requirements",
                    "Conduct internal audit"
                ],
                "applicable_to": "All device classes"
            }
        ]


def main():
    """
    Example usage of UDIComplianceChecker
    """
    checker = UDIComplianceChecker()
    
    # Example compliance data
    compliance_data = {
        "udi_assignment": {
            "Basic UDI-DI assigned": "compliant",
            "UDI-DI assigned to each device variant": "compliant",
            "UDI-PI assigned per device level": "partial",
            "UDIs obtained from authorized issuing entity": "compliant",
            "UDI format complies with standards": "compliant"
        },
        "labeling": {
            "UDI carrier on device label": "partial",
            "UDI carrier on all higher-level packaging": "non-compliant",
            "UDI-AIDC format correct": "compliant",
            "UDI-HRI readable": "compliant",
            "Human-readable format correct": "compliant"
        },
        "eudamed": {
            "Actor registration completed": "compliant",
            "Device registration completed": "partial",
            "UDI-DI registered in EUDAMED": "partial",
            "Certificate registration completed": "compliant",
            "Clinical investigation registration (if applicable)": "compliant"
        }
    }
    
    # Assess compliance
    result = checker.assess_compliance(compliance_data)
    print("UDI/EUDAMED Compliance Assessment:")
    print(json.dumps(result, indent=2))
    
    # Generate implementation timeline
    print("\nUDI Implementation Timeline:")
    timeline = checker.generate_udi_implementation_timeline()
    print(json.dumps(timeline, indent=2))


if __name__ == "__main__":
    main()