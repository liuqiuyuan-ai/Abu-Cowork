#!/usr/bin/env python3
"""
FDA Pathway Analyzer - Medical Device Regulatory Pathway Assessment Tool

This script helps determine the appropriate FDA regulatory pathway for medical devices.
"""

import json
import datetime
from typing import List, Dict, Optional


class FDAPathwayAnalyzer:
    """
    FDA Regulatory Pathway Analysis Class
    """
    
    def __init__(self):
        self.pathways = {
            "510k": {
                "name": "510(k) Clearance",
                "description": "For devices substantially equivalent to legally marketed devices",
                "classification": ["Class II", "Some Class I"],
                "review_time": "90-180 days",
                "requirements": ["Substantial equivalence demonstration", "Performance data", "Labeling"]
            },
            "PMA": {
                "name": "Premarket Approval",
                "description": "For high-risk Class III devices",
                "classification": ["Class III"],
                "review_time": "6-12+ months",
                "requirements": ["Clinical trials", "Safety/effectiveness data", "Manufacturing info"]
            },
            "DeNovo": {
                "name": "De Novo Classification",
                "description": "For novel devices without predicates",
                "classification": ["Class I/II (novel)"],
                "review_time": "150 days",
                "requirements": ["Safety/effectiveness data", "Risk analysis"]
            },
            "IDE": {
                "name": "Investigational Device Exemption",
                "description": "For clinical investigation of devices",
                "classification": ["All classes"],
                "review_time": "30 days",
                "requirements": ["Clinical protocol", "IRB approval", "Safety plan"]
            }
        }
    
    def analyze_pathway(self, product_info: Dict) -> Dict:
        """
        Analyze product information and recommend FDA pathway
        
        Args:
            product_info: Dictionary containing product details
        
        Returns:
            Dictionary with pathway recommendations
        """
        recommendations = []
        classification = product_info.get('classification', 'Unknown')
        is_novel = product_info.get('is_novel', False)
        has_predicate = product_info.get('has_predicate', False)
        risk_level = product_info.get('risk_level', 'medium')
        
        if classification == 'Class III':
            recommendations.append({
                "pathway": "PMA",
                "reason": "High-risk devices require PMA approval",
                "confidence": "High"
            })
        elif classification == 'Class II':
            if is_novel and not has_predicate:
                recommendations.append({
                    "pathway": "DeNovo",
                    "reason": "Novel device without predicate requires De Novo",
                    "confidence": "High"
                })
            else:
                recommendations.append({
                    "pathway": "510k",
                    "reason": "Class II device with predicate",
                    "confidence": "High"
                })
        elif classification == 'Class I':
            if product_info.get('requires_fda_clearance', False):
                recommendations.append({
                    "pathway": "510k",
                    "reason": "Certain Class I devices require 510(k)",
                    "confidence": "Medium"
                })
            else:
                recommendations.append({
                    "pathway": "Exempt",
                    "reason": "Most Class I devices are exempt",
                    "confidence": "High"
                })
        
        if product_info.get('needs_clinical_trials', False):
            recommendations.append({
                "pathway": "IDE",
                "reason": "Clinical investigation required before marketing",
                "confidence": "High"
            })
        
        return {
            "analysis_date": datetime.datetime.now().isoformat(),
            "product_info": product_info,
            "recommendations": recommendations,
            "next_steps": self._generate_next_steps(recommendations)
        }
    
    def _generate_next_steps(self, recommendations: List) -> List[str]:
        """
        Generate recommended next steps based on pathway analysis
        
        Args:
            recommendations: List of pathway recommendations
        
        Returns:
            List of recommended actions
        """
        steps = []
        pathways = [r['pathway'] for r in recommendations]
        
        if '510k' in pathways:
            steps.append("Identify predicate devices and gather comparison data")
            steps.append("Prepare 510(k) submission package")
            steps.append("Submit to FDA for clearance")
        
        if 'PMA' in pathways:
            steps.append("Develop clinical trial plan")
            steps.append("Conduct clinical investigations")
            steps.append("Prepare comprehensive PMA application")
        
        if 'DeNovo' in pathways:
            steps.append("Prepare De Novo request with safety/effectiveness data")
            steps.append("Consider pre-submission meeting with FDA")
        
        if 'IDE' in pathways:
            steps.append("Prepare IDE application")
            steps.append("Obtain IRB approval")
            steps.append("Submit IDE to FDA")
        
        steps.append("Review FDA guidance documents for your product type")
        steps.append("Consider consulting FDA-registered regulatory expert")
        
        return steps
    
    def get_pathway_details(self, pathway_code: str) -> Optional[Dict]:
        """
        Get detailed information about a specific pathway
        
        Args:
            pathway_code: Pathway code (510k, PMA, DeNovo, IDE)
        
        Returns:
            Dictionary with pathway details or None
        """
        return self.pathways.get(pathway_code)
    
    def generate_submission_checklist(self, pathway_code: str) -> List[str]:
        """
        Generate submission checklist for a specific pathway
        
        Args:
            pathway_code: Pathway code
        
        Returns:
            List of submission requirements
        """
        checklists = {
            "510k": [
                "Cover letter",
                "Table of contents",
                "Indications for use",
                "510(k) summary or statement",
                "Substantial equivalence comparison",
                "Performance data",
                "Biocompatibility data (if applicable)",
                "Software validation (if applicable)",
                "Labeling",
                "Sterilization validation (if applicable)",
                "User fee payment"
            ],
            "PMA": [
                "Application form",
                "Summary of safety/effectiveness",
                "Clinical investigation reports",
                "Non-clinical laboratory studies",
                "Manufacturing information",
                "Device description",
                "Labeling",
                "Risk analysis",
                "Software documentation",
                "PMA supplement (if applicable)",
                "User fee payment"
            ],
            "DeNovo": [
                "De Novo request form",
                "Indications for use",
                "Safety and effectiveness data",
                "Risk analysis",
                "Benefit-risk assessment",
                "Proposed classification",
                "Labeling",
                "User fee payment"
            ],
            "IDE": [
                "IDE application form",
                "Investigational plan",
                "Investigator's brochure",
                "IRB approval letter",
                "Manufacturing information",
                "Labeling",
                "Safety monitoring plan",
                "Informed consent form"
            ]
        }
        
        return checklists.get(pathway_code, [])


def main():
    """
    Example usage of FDAPathwayAnalyzer
    """
    analyzer = FDAPathwayAnalyzer()
    
    # Example product information
    product_info = {
        "product_name": "Cardiac Monitoring Device",
        "classification": "Class II",
        "intended_use": "Continuous monitoring of cardiac rhythm",
        "is_novel": False,
        "has_predicate": True,
        "risk_level": "medium",
        "requires_fda_clearance": True,
        "needs_clinical_trials": False
    }
    
    # Analyze pathway
    result = analyzer.analyze_pathway(product_info)
    print("FDA Pathway Analysis Results:")
    print(json.dumps(result, indent=2))
    
    # Get pathway details
    print("\n510(k) Pathway Details:")
    details = analyzer.get_pathway_details("510k")
    print(json.dumps(details, indent=2))
    
    # Generate submission checklist
    print("\n510(k) Submission Checklist:")
    checklist = analyzer.generate_submission_checklist("510k")
    for i, item in enumerate(checklist, 1):
        print(f"{i}. {item}")


if __name__ == "__main__":
    main()