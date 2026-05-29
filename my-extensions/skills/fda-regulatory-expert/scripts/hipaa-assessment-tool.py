#!/usr/bin/env python3
"""
HIPAA Assessment Tool - Health Insurance Portability and Accountability Act Compliance

This script helps assess compliance with HIPAA Privacy and Security Rules.
"""

import json
import datetime
from typing import List, Dict


class HIPAAAssessmentTool:
    """
    HIPAA Compliance Assessment Class
    """
    
    def __init__(self):
        self.hipaa_requirements = {
            "privacy_rule": {
                "title": "HIPAA Privacy Rule",
                "requirements": [
                    "Notice of Privacy Practices (NPP)",
                    "Individual rights (access, amendment, accounting)",
                    "Uses and disclosures of PHI",
                    "Business Associate Agreements (BAAs)",
                    "Minimum necessary standard",
                    "Breach notification"
                ]
            },
            "security_rule": {
                "title": "HIPAA Security Rule",
                "requirements": [
                    "Risk assessment",
                    "Administrative safeguards",
                    "Physical safeguards",
                    "Technical safeguards",
                    "Access controls",
                    "Audit logs",
                    "Encryption",
                    "Incident response"
                ]
            },
            "breach_notification": {
                "title": "Breach Notification Rule",
                "requirements": [
                    "Immediate breach assessment",
                    "Individual notification (without unreasonable delay)",
                    "HHS notification (within 60 days)",
                    "Media notification (if 500+ individuals affected)",
                    "Breach documentation"
                ]
            }
        }
    
    def assess_compliance(self, assessment_data: Dict) -> Dict:
        """
        Assess HIPAA compliance based on provided data
        
        Args:
            assessment_data: Dictionary with compliance status for each requirement
        
        Returns:
            Dictionary with compliance assessment results
        """
        total_requirements = 0
        compliant_requirements = 0
        findings = []
        
        for area, data in self.hipaa_requirements.items():
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
            recommendations.append("HIPAA compliance appears satisfactory")
            return recommendations
        
        recommendations.append("Immediate action items:")
        for finding in findings:
            if finding["status"] == "non-compliant":
                recommendations.append(f"- Address: {finding['requirement']} ({finding['area']})")
        
        recommendations.append("\nGeneral recommendations:")
        recommendations.append("1. Conduct regular risk assessments")
        recommendations.append("2. Maintain up-to-date BAAs with all business associates")
        recommendations.append("3. Implement ongoing staff training")
        recommendations.append("4. Establish incident response procedures")
        recommendations.append("5. Regularly review and update policies")
        
        return recommendations
    
    def generate_baa_template(self) -> str:
        """
        Generate a basic BAA template
        
        Returns:
            BAA template string
        """
        template = """BUSINESS ASSOCIATE AGREEMENT

This Business Associate Agreement ("Agreement") is entered into between:

[Covered Entity Name], a [State] [Type of Entity] ("Covered Entity")
and
[Business Associate Name], a [State] [Type of Entity] ("Business Associate")

1. DEFINITIONS
   - Protected Health Information (PHI)
   - Covered Entity
   - Business Associate
   - Breach

2. OBLIGATIONS OF BUSINESS ASSOCIATE
   a. Maintain confidentiality of PHI
   b. Use PHI only as permitted
   c. Implement safeguards
   d. Report breaches
   e. Disclose PHI only as required

3. OBLIGATIONS OF COVERED ENTITY
   a. Notify Business Associate of restrictions
   b. Provide necessary information

4. TERMINATION
   a. Termination upon breach
   b. Return or destruction of PHI

5. MISCELLANEOUS
   a. Governing law
   b. Entire agreement

IN WITNESS WHEREOF, the parties execute this Agreement.

___________________________
[Covered Entity Representative]
[Date]

___________________________
[Business Associate Representative]
[Date]
"""
        return template


def main():
    """
    Example usage of HIPAAAssessmentTool
    """
    tool = HIPAAAssessmentTool()
    
    # Example assessment data
    assessment_data = {
        "privacy_rule": {
            "Notice of Privacy Practices (NPP)": "compliant",
            "Individual rights (access, amendment, accounting)": "compliant",
            "Uses and disclosures of PHI": "compliant",
            "Business Associate Agreements (BAAs)": "partial",
            "Minimum necessary standard": "compliant",
            "Breach notification": "compliant"
        },
        "security_rule": {
            "Risk assessment": "compliant",
            "Administrative safeguards": "compliant",
            "Physical safeguards": "compliant",
            "Technical safeguards": "compliant",
            "Access controls": "compliant",
            "Audit logs": "non-compliant",
            "Encryption": "compliant",
            "Incident response": "compliant"
        }
    }
    
    # Perform assessment
    result = tool.assess_compliance(assessment_data)
    print("HIPAA Compliance Assessment Results:")
    print(json.dumps(result, indent=2))
    
    # Generate BAA template
    print("\nBAA Template:")
    print(tool.generate_baa_template())


if __name__ == "__main__":
    main()