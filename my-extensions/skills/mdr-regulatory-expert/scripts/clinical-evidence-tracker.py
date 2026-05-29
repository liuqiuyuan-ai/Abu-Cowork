#!/usr/bin/env python3
"""
Clinical Evidence Tracker - MDR Clinical Evaluation and PMCF Monitoring

This script helps track clinical evidence requirements and PMCF activities.
"""

import json
import datetime
from typing import List, Dict, Optional


class ClinicalEvidenceTracker:
    """
    Clinical Evidence Requirement Tracking Class
    """
    
    def __init__(self):
        self.evidence_types = {
            "literature": {
                "name": "Literature Review",
                "description": "Systematic review of published clinical data",
                "requirements": [
                    "Search protocol documented",
                    "Multiple databases searched",
                    "Inclusion/exclusion criteria defined",
                    "Quality appraisal conducted",
                    "Results synthesized",
                    "Gap analysis performed"
                ]
            },
            "clinical_investigation": {
                "name": "Clinical Investigation",
                "description": "Clinical data from conducted investigations",
                "requirements": [
                    "Clinical investigation plan",
                    "Ethics committee approval",
                    "Competent authority notification",
                    "Informed consent obtained",
                    "Data collection completed",
                    "Statistical analysis performed"
                ]
            },
            "pmcf": {
                "name": "Post-Market Clinical Follow-up",
                "description": "Ongoing clinical data collection post-market",
                "requirements": [
                    "PMCF plan developed",
                    "PMCF activities defined",
                    "PMCF evaluation report prepared",
                    "Results integrated into CER",
                    "Conclusions documented"
                ]
            }
        }
    
    def assess_evidence_adequacy(self, evidence_data: Dict) -> Dict:
        """
        Assess adequacy of clinical evidence
        
        Args:
            evidence_data: Dictionary with evidence status for each type
        
        Returns:
            Dictionary with assessment results
        """
        total_requirements = 0
        met_requirements = 0
        gaps = []
        
        for evidence_type, data in self.evidence_types.items():
            type_data = evidence_data.get(evidence_type, {})
            for req in data["requirements"]:
                total_requirements += 1
                status = type_data.get(req, "not_met")
                
                if status == "met":
                    met_requirements += 1
                else:
                    gaps.append({
                        "type": data["name"],
                        "requirement": req,
                        "status": status
                    })
        
        adequacy_percentage = (met_requirements / total_requirements) * 100 if total_requirements > 0 else 0
        
        return {
            "assessment_date": datetime.datetime.now().isoformat(),
            "total_requirements": total_requirements,
            "met_requirements": met_requirements,
            "adequacy_percentage": round(adequacy_percentage, 2),
            "adequacy_status": self._determine_adequacy_status(adequacy_percentage),
            "evidence_gaps": gaps,
            "recommendations": self._generate_recommendations(gaps)
        }
    
    def _determine_adequacy_status(self, percentage: float) -> str:
        """
        Determine evidence adequacy status
        
        Args:
            percentage: Adequacy percentage
        
        Returns:
            Status string
        """
        if percentage >= 90:
            return "Adequate"
        elif percentage >= 70:
            return "Partially Adequate"
        else:
            return "Inadequate - Additional Evidence Required"
    
    def _generate_recommendations(self, gaps: List) -> List[str]:
        """
        Generate recommendations to address evidence gaps
        
        Args:
            gaps: List of evidence gaps
        
        Returns:
            List of recommendations
        """
        recommendations = []
        
        if not gaps:
            recommendations.append("Clinical evidence appears adequate")
            recommendations.append("Continue PMCF activities as planned")
            return recommendations
        
        recommendations.append("Actions to address evidence gaps:")
        
        # Group by evidence type
        by_type = {}
        for gap in gaps:
            etype = gap["type"]
            if etype not in by_type:
                by_type[etype] = []
            by_type[etype].append(gap["requirement"])
        
        for etype, requirements in by_type.items():
            recommendations.append(f"\n{etype}:")
            for req in requirements:
                recommendations.append(f"  - {req}")
        
        return recommendations
    
    def create_pmcf_activity_tracker(self, activities: List[Dict]) -> Dict:
        """
        Create PMCF activity tracking report
        
        Args:
            activities: List of PMCF activities
        
        Returns:
            Tracking report dictionary
        """
        completed = 0
        in_progress = 0
        planned = 0
        
        for activity in activities:
            status = activity.get("status", "planned")
            if status == "completed":
                completed += 1
            elif status == "in_progress":
                in_progress += 1
            else:
                planned += 1
        
        return {
            "report_date": datetime.datetime.now().isoformat(),
            "total_activities": len(activities),
            "completed": completed,
            "in_progress": in_progress,
            "planned": planned,
            "completion_percentage": round((completed / len(activities) * 100) if activities else 0, 2),
            "activities": activities
        }
    
    def generate_cer_update_checklist(self) -> List[Dict]:
        """
        Generate checklist for CER update requirements
        
        Returns:
            List of CER update triggers
        """
        return [
            {
                "trigger": "New clinical data available",
                "action": "Review and integrate new data into CER",
                "timeline": "As soon as data available"
            },
            {
                "trigger": "Post-market surveillance data",
                "action": "Update benefit-risk assessment",
                "timeline": "During PSUR preparation"
            },
            {
                "trigger": "PMCF results",
                "action": "Document PMCF evaluation in CER",
                "timeline": "After each PMCF activity"
            },
            {
                "trigger": "Significant design changes",
                "action": "Assess impact on clinical evaluation",
                "timeline": "Before implementing change"
            },
            {
                "trigger": "Competent authority request",
                "action": "Provide updated CER",
                "timeline": "As specified by authority"
            }
        ]


def main():
    """
    Example usage of ClinicalEvidenceTracker
    """
    tracker = ClinicalEvidenceTracker()
    
    # Example evidence data
    evidence_data = {
        "literature": {
            "Search protocol documented": "met",
            "Multiple databases searched": "met",
            "Inclusion/exclusion criteria defined": "met",
            "Quality appraisal conducted": "met",
            "Results synthesized": "met",
            "Gap analysis performed": "partial"
        },
        "pmcf": {
            "PMCF plan developed": "met",
            "PMCF activities defined": "met",
            "PMCF evaluation report prepared": "not_met",
            "Results integrated into CER": "not_met",
            "Conclusions documented": "not_met"
        }
    }
    
    # Assess evidence adequacy
    result = tracker.assess_evidence_adequacy(evidence_data)
    print("Clinical Evidence Assessment Results:")
    print(json.dumps(result, indent=2))
    
    # Generate CER update checklist
    print("\nCER Update Checklist:")
    checklist = tracker.generate_cer_update_checklist()
    print(json.dumps(checklist, indent=2))


if __name__ == "__main__":
    main()