#!/usr/bin/env python3
"""
PMS Reporting Automation Tool - Post-Market Surveillance Report Generation

This script helps generate and manage post-market surveillance reports.
"""

import json
import datetime
from typing import List, Dict, Optional


class PMSReportingTool:
    """
    Post-Market Surveillance Reporting Class
    """
    
    def __init__(self):
        self.psur_sections = {
            "section_1": {
                "title": "Section 1: Device Summary",
                "content": [
                    "Device identification",
                    "Intended purpose",
                    "Device classification",
                    "CE marking date",
                    "Basic UDI-DI"
                ]
            },
            "section_2": {
                "title": "Section 2: PMS Data Summary",
                "content": [
                    "Sales volume data",
                    "Production volume data",
                    "Complaints received",
                    "Incidents reported",
                    "Field safety corrective actions"
                ]
            },
            "section_3": {
                "title": "Section 3: Incident Analysis",
                "content": [
                    "Serious incidents reported",
                    "Non-serious incidents",
                    "Trend analysis",
                    "Root cause analysis",
                    "Corrective actions taken"
                ]
            },
            "section_4": {
                "title": "Section 4: Benefit-Risk Conclusion",
                "content": [
                    "Benefit assessment update",
                    "Risk assessment update",
                    "Benefit-risk ratio conclusion",
                    "Acceptability of residual risks"
                ]
            },
            "section_5": {
                "title": "Section 5: PMCF Conclusions",
                "content": [
                    "PMCF activities completed",
                    "PMCF results summary",
                    "Impact on clinical evaluation",
                    "Recommendations for future PMCF"
                ]
            },
            "section_6": {
                "title": "Section 6: Overall Conclusions",
                "content": [
                    "Overall safety conclusion",
                    "Ongoing risk acceptability",
                    "Effectiveness of preventive measures",
                    "Recommendations for label changes",
                    "Overall benefit-risk conclusion"
                ]
            }
        }
    
    def generate_psur_template(self) -> Dict:
        """
        Generate PSUR template structure
        
        Returns:
            PSUR template dictionary
        """
        template = {
            "document_info": {
                "document_title": "Periodic Safety Update Report",
                "document_number": "[PSUR-XXXX]",
                "revision": "01",
                "date": datetime.datetime.now().isoformat(),
                "author": "[Author Name]",
                "reviewer": "[Reviewer Name]",
                "approver": "[Approver Name]"
            },
            "report_period": {
                "start_date": "[Start Date]",
                "end_date": "[End Date]"
            },
            "sections": {}
        }
        
        for section_id, section_data in self.psur_sections.items():
            template["sections"][section_id] = {
                "title": section_data["title"],
                "status": "draft",
                "content": {},
                "completion_status": "pending"
            }
        
        return template
    
    def assess_pms_system_readiness(self, pms_data: Dict) -> Dict:
        """
        Assess PMS system readiness for MDR compliance
        
        Args:
            pms_data: Dictionary with PMS system status
        
        Returns:
            Readiness assessment results
        """
        readiness_areas = {
            "pms_plan": {
                "title": "PMS Plan",
                "requirements": [
                    "PMS plan developed",
                    "PMS plan approved",
                    "PMS plan implemented",
                    "PMS plan reviewed and updated"
                ]
            },
            "vigilance": {
                "title": "Vigilance System",
                "requirements": [
                    "Serious incident reporting procedures",
                    "Trend reporting procedures",
                    "FSCA procedures",
                    "Vigilance contacts designated"
                ]
            },
            "data_collection": {
                "title": "Data Collection",
                "requirements": [
                    "Complaint handling system",
                    "Sales/production data tracking",
                    "Literature review process",
                    "Proactive data collection"
                ]
            },
            "reporting": {
                "title": "Reporting",
                "requirements": [
                    "PSUR prepared",
                    "PSUR updated as required",
                    "Reports submitted to NB",
                    "Reports archived properly"
                ]
            }
        }
        
        total_requirements = 0
        met_requirements = 0
        gaps = []
        
        for area, data in readiness_areas.items():
            area_data = pms_data.get(area, {})
            for req in data["requirements"]:
                total_requirements += 1
                status = area_data.get(req, "not_met")
                
                if status == "met":
                    met_requirements += 1
                else:
                    gaps.append({
                        "area": data["title"],
                        "requirement": req,
                        "status": status
                    })
        
        readiness_percentage = (met_requirements / total_requirements) * 100 if total_requirements > 0 else 0
        
        return {
            "assessment_date": datetime.datetime.now().isoformat(),
            "total_requirements": total_requirements,
            "met_requirements": met_requirements,
            "readiness_percentage": round(readiness_percentage, 2),
            "readiness_status": self._determine_readiness_status(readiness_percentage),
            "gaps": gaps,
            "recommendations": self._generate_recommendations(gaps)
        }
    
    def _determine_readiness_status(self, percentage: float) -> str:
        """
        Determine PMS readiness status
        
        Args:
            percentage: Readiness percentage
        
        Returns:
            Status string
        """
        if percentage >= 90:
            return "Ready for MDR Compliance"
        elif percentage >= 70:
            return "Partially Ready - Improvements Needed"
        else:
            return "Not Ready - Significant Gaps"
    
    def _generate_recommendations(self, gaps: List) -> List[str]:
        """
        Generate recommendations to address gaps
        
        Args:
            gaps: List of readiness gaps
        
        Returns:
            List of recommendations
        """
        recommendations = []
        
        if not gaps:
            recommendations.append("PMS system appears ready for MDR compliance")
            return recommendations
        
        recommendations.append("Actions to address PMS gaps:")
        
        by_area = {}
        for gap in gaps:
            area = gap["area"]
            if area not in by_area:
                by_area[area] = []
            by_area[area].append(gap["requirement"])
        
        for area, requirements in by_area.items():
            recommendations.append(f"\n{area}:")
            for req in requirements:
                recommendations.append(f"  - {req}")
        
        return recommendations
    
    def generate_serious_incident_report(self, incident_data: Dict) -> Dict:
        """
        Generate serious incident report structure
        
        Args:
            incident_data: Dictionary with incident details
        
        Returns:
            Serious incident report
        """
        return {
            "report_header": {
                "report_number": f"SIR-{datetime.datetime.now().strftime('%Y%m%d%H%M')}",
                "report_date": datetime.datetime.now().isoformat(),
                "incident_type": incident_data.get("incident_type", ""),
                "severity": incident_data.get("severity", "")
            },
            "device_information": {
                "device_name": incident_data.get("device_name", ""),
                "device_model": incident_data.get("device_model", ""),
                "serial_number": incident_data.get("serial_number", ""),
                "lot_number": incident_data.get("lot_number", ""),
                "basic_udi_di": incident_data.get("basic_udi_di", ""),
                "device_manufacture_date": incident_data.get("manufacture_date", "")
            },
            "incident_description": {
                "date_of_incident": incident_data.get("incident_date", ""),
                "place_of_incident": incident_data.get("incident_location", ""),
                "description": incident_data.get("description", ""),
                "patient_outcome": incident_data.get("patient_outcome", "")
            },
            "root_cause_analysis": {
                "investigation_conducted": incident_data.get("investigation_conducted", False),
                "root_cause": incident_data.get("root_cause", ""),
                "contributing_factors": incident_data.get("contributing_factors", [])
            },
            "corrective_actions": {
                "fsca_required": incident_data.get("fsca_required", False),
                "fsca_description": incident_data.get("fsca_description", ""),
                "preventive_actions": incident_data.get("preventive_actions", []),
                "effectiveness_evaluation": incident_data.get("effectiveness_evaluation", "")
            },
            "reporting": {
                "reported_to_authority": incident_data.get("reported_to_authority", False),
                "authority_name": incident_data.get("authority_name", ""),
                "report_date": incident_data.get("authority_report_date", ""),
                "follow_up_required": incident_data.get("follow_up_required", False)
            }
        }


def main():
    """
    Example usage of PMSReportingTool
    """
    tool = PMSReportingTool()
    
    # Generate PSUR template
    print("PSUR Template:")
    template = tool.generate_psur_template()
    print(json.dumps(template, indent=2))
    
    # Assess PMS readiness
    pms_data = {
        "pms_plan": {
            "PMS plan developed": "met",
            "PMS plan approved": "met",
            "PMS plan implemented": "partial",
            "PMS plan reviewed and updated": "not_met"
        },
        "vigilance": {
            "Serious incident reporting procedures": "met",
            "Trend reporting procedures": "met",
            "FSCA procedures": "met",
            "Vigilance contacts designated": "met"
        },
        "data_collection": {
            "Complaint handling system": "met",
            "Sales/production data tracking": "partial",
            "Literature review process": "met",
            "Proactive data collection": "not_met"
        }
    }
    
    print("\nPMS Readiness Assessment:")
    result = tool.assess_pms_system_readiness(pms_data)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()