#!/usr/bin/env python3
"""
QMS Audit Expert - Example Script

This script provides utilities for QMS audit management, including:
- Audit planning tools
- Nonconformity tracking
- Audit report generation
"""

import json
import datetime
from typing import List, Dict, Optional


class AuditManager:
    """
    QMS Audit Management Class
    """
    
    def __init__(self):
        self.audits = []
        self.nonconformities = []
    
    def create_audit_plan(self, audit_name: str, scope: str, 
                         criteria: str, auditors: List[str],
                         start_date: str, end_date: str) -> Dict:
        """
        Create a new audit plan
        
        Args:
            audit_name: Name/title of the audit
            scope: Scope description
            criteria: Audit criteria (e.g., ISO 13485:2016)
            auditors: List of auditor names
            start_date: Audit start date (YYYY-MM-DD)
            end_date: Audit end date (YYYY-MM-DD)
        
        Returns:
            Dictionary containing audit plan details
        """
        audit_plan = {
            "audit_id": f"AUD-{datetime.datetime.now().strftime('%Y%m%d%H%M')}",
            "audit_name": audit_name,
            "scope": scope,
            "criteria": criteria,
            "auditors": auditors,
            "start_date": start_date,
            "end_date": end_date,
            "status": "planned",
            "created_at": datetime.datetime.now().isoformat()
        }
        self.audits.append(audit_plan)
        return audit_plan
    
    def add_nonconformity(self, audit_id: str, clause: str, 
                         description: str, severity: str,
                         evidence: str, area: str) -> Dict:
        """
        Add a nonconformity to an audit
        
        Args:
            audit_id: ID of the audit
            clause: ISO 13485 clause reference
            description: Description of nonconformity
            severity: Severity level (Major/Minor/Observation)
            evidence: Evidence reference
            area: Area/process affected
        
        Returns:
            Dictionary containing nonconformity details
        """
        nonconformity = {
            "nc_id": f"NC-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}",
            "audit_id": audit_id,
            "clause": clause,
            "description": description,
            "severity": severity,
            "evidence": evidence,
            "area": area,
            "status": "open",
            "created_at": datetime.datetime.now().isoformat(),
            "corrective_action": None,
            "target_date": None,
            "verification_date": None,
            "verified": False
        }
        self.nonconformities.append(nonconformity)
        return nonconformity
    
    def update_corrective_action(self, nc_id: str, action: str, 
                                responsible: str, target_date: str) -> bool:
        """
        Update corrective action for a nonconformity
        
        Args:
            nc_id: Nonconformity ID
            action: Corrective action description
            responsible: Responsible person
            target_date: Target completion date
        
        Returns:
            True if updated successfully, False otherwise
        """
        for nc in self.nonconformities:
            if nc["nc_id"] == nc_id:
                nc["corrective_action"] = {
                    "action": action,
                    "responsible": responsible,
                    "target_date": target_date
                }
                nc["status"] = "in_progress"
                return True
        return False
    
    def verify_corrective_action(self, nc_id: str, verification_date: str,
                                verified: bool, remarks: str = "") -> bool:
        """
        Verify corrective action effectiveness
        
        Args:
            nc_id: Nonconformity ID
            verification_date: Date of verification
            verified: Whether action was effective
            remarks: Additional remarks
        
        Returns:
            True if verified successfully, False otherwise
        """
        for nc in self.nonconformities:
            if nc["nc_id"] == nc_id:
                nc["verification_date"] = verification_date
                nc["verified"] = verified
                nc["verification_remarks"] = remarks
                nc["status"] = "closed" if verified else "reopened"
                return True
        return False
    
    def generate_audit_report(self, audit_id: str) -> Dict:
        """
        Generate audit report
        
        Args:
            audit_id: ID of the audit
        
        Returns:
            Dictionary containing audit report
        """
        audit = next((a for a in self.audits if a["audit_id"] == audit_id), None)
        if not audit:
            return None
        
        audit_ncs = [nc for nc in self.nonconformities if nc["audit_id"] == audit_id]
        
        report = {
            "audit_id": audit_id,
            "audit_name": audit["audit_name"],
            "scope": audit["scope"],
            "criteria": audit["criteria"],
            "auditors": audit["auditors"],
            "audit_period": f"{audit['start_date']} to {audit['end_date']}",
            "report_date": datetime.datetime.now().isoformat(),
            "summary": {
                "total_nc": len(audit_ncs),
                "major_nc": len([nc for nc in audit_ncs if nc["severity"] == "Major"]),
                "minor_nc": len([nc for nc in audit_ncs if nc["severity"] == "Minor"]),
                "observations": len([nc for nc in audit_ncs if nc["severity"] == "Observation"])
            },
            "nonconformities": audit_ncs,
            "conclusions": "Audit completed successfully" if not audit_ncs else "Corrective actions required",
            "recommendations": ["Implement corrective actions", "Schedule follow-up audit"]
        }
        
        return report
    
    def get_open_nonconformities(self) -> List[Dict]:
        """
        Get all open nonconformities
        
        Returns:
            List of open nonconformities
        """
        return [nc for nc in self.nonconformities if nc["status"] != "closed"]


def main():
    """
    Example usage of AuditManager
    """
    # Initialize audit manager
    manager = AuditManager()
    
    # Create an audit plan
    audit_plan = manager.create_audit_plan(
        audit_name="QMS Internal Audit Q2 2026",
        scope="All manufacturing processes and quality management system",
        criteria="ISO 13485:2016",
        auditors=["John Smith", "Jane Doe"],
        start_date="2026-06-01",
        end_date="2026-06-03"
    )
    print(f"Created audit plan: {audit_plan['audit_id']}")
    
    # Add a nonconformity
    nc = manager.add_nonconformity(
        audit_id=audit_plan["audit_id"],
        clause="4.2.4",
        description="Document control procedure not followed for work instruction WI-005",
        severity="Minor",
        evidence="Observed during document review on 2026-06-01",
        area="Document Control"
    )
    print(f"Added nonconformity: {nc['nc_id']}")
    
    # Update corrective action
    manager.update_corrective_action(
        nc_id=nc["nc_id"],
        action="Review and update document control procedure, train relevant personnel",
        responsible="Quality Manager",
        target_date="2026-06-15"
    )
    print("Updated corrective action")
    
    # Generate report
    report = manager.generate_audit_report(audit_plan["audit_id"])
    print("\nAudit Report:")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()