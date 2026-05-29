#!/usr/bin/env python3
"""
Document Control Audit Tool

This script audits document control compliance against ISO 13485 requirements.

Usage:
    python document-control-audit.py --docs-dir <path> [--output <path>]
"""

import os
import sys
import argparse
import json
from pathlib import Path
from typing import Dict, List
from datetime import datetime


class DocumentControlAuditor:
    """Audits document control compliance."""

    def __init__(self, docs_dir: str):
        """Initialize auditor with document directory."""
        self.docs_dir = Path(docs_dir)
        self.findings = []
        self.compliance_score = 0

    def audit(self) -> Dict:
        """Run document control audit."""
        print(f"Auditing document control in: {self.docs_dir}")

        if not self.docs_dir.exists():
            print(f"ERROR: Directory not found: {self.docs_dir}")
            return {}

        # Audit document control requirements
        self._audit_document_approval()
        self._audit_document_version_control()
        self._audit_document_distribution()
        self._audit_document_review()
        self._audit_obsolete_documents()
        self._audit_document_retention()
        self._audit_external_documents()

        # Calculate compliance score
        self._calculate_compliance_score()

        # Generate audit report
        report = self._generate_report()

        return report

    def _audit_document_approval(self):
        """Audit document approval process."""
        print("\nAuditing document approval...")

        # Check for approval signatures
        approval_found = False
        for file_path in self.docs_dir.rglob('*.md'):
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read().lower()
                    if 'approval' in content or 'approved by' in content or 'signature' in content:
                        approval_found = True
                        break
            except Exception:
                continue

        if not approval_found:
            self.findings.append({
                "requirement": "4.2.4 - Document Approval",
                "finding": "Documents lack approval signatures or approval documentation",
                "severity": "MAJOR",
                "recommendation": "Implement document approval process with signatures"
            })
        else:
            print("✓ Document approval process found")

    def _audit_document_version_control(self):
        """Audit document version control."""
        print("Auditing document version control...")

        # Check for version information
        version_found = False
        for file_path in self.docs_dir.rglob('*.md'):
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read().lower()
                    if 'version' in content or 'revision' in content:
                        version_found = True
                        break
            except Exception:
                continue

        if not version_found:
            self.findings.append({
                "requirement": "4.2.4 - Version Control",
                "finding": "Documents lack version control information",
                "severity": "MAJOR",
                "recommendation": "Implement version control for all documents"
            })
        else:
            print("✓ Version control found")

    def _audit_document_distribution(self):
        """Audit document distribution control."""
        print("Auditing document distribution...")

        # Check for distribution lists or access control
        distribution_found = False
        for file_path in self.docs_dir.rglob('*.md'):
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read().lower()
                    if 'distribution' in content or 'access control' in content:
                        distribution_found = True
                        break
            except Exception:
                continue

        if not distribution_found:
            self.findings.append({
                "requirement": "4.2.4 - Document Distribution",
                "finding": "Document distribution control not documented",
                "severity": "MINOR",
                "recommendation": "Document distribution list and access control procedures"
            })
        else:
            print("✓ Distribution control found")

    def _audit_document_review(self):
        """Audit document review process."""
        print("Auditing document review process...")

        # Check for review schedules or procedures
        review_found = False
        for file_path in self.docs_dir.rglob('*.md'):
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read().lower()
                    if 'review' in content and ('periodic' in content or 'annual' in content):
                        review_found = True
                        break
            except Exception:
                continue

        if not review_found:
            self.findings.append({
                "requirement": "4.2.4 - Document Review",
                "finding": "Document review process not documented",
                "severity": "MINOR",
                "recommendation": "Establish periodic document review schedule"
            })
        else:
            print("✓ Document review process found")

    def _audit_obsolete_documents(self):
        """Audit obsolete document control."""
        print("Auditing obsolete document control...")

        # Check for obsolete document handling
        obsolete_found = False
        for file_path in self.docs_dir.rglob('*.md'):
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read().lower()
                    if 'obsolete' in content or 'superseded' in content:
                        obsolete_found = True
                        break
            except Exception:
                continue

        if not obsolete_found:
            self.findings.append({
                "requirement": "4.2.4 - Obsolete Documents",
                "finding": "Obsolete document control not documented",
                "severity": "MINOR",
                "recommendation": "Document obsolete document identification and control procedures"
            })
        else:
            print("✓ Obsolete document control found")

    def _audit_document_retention(self):
        """Audit document retention requirements."""
        print("Auditing document retention...")

        # Check for retention periods
        retention_found = False
        for file_path in self.docs_dir.rglob('*.md'):
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read().lower()
                    if 'retention' in content or 'retention period' in content:
                        retention_found = True
                        break
            except Exception:
                continue

        if not retention_found:
            self.findings.append({
                "requirement": "4.2.5 - Record Retention",
                "finding": "Document retention period not documented",
                "severity": "MAJOR",
                "recommendation": "Document retention periods (minimum device lifetime)"
            })
        else:
            print("✓ Document retention found")

    def _audit_external_documents(self):
        """Audit external document control."""
        print("Auditing external document control...")

        # Check for external document handling
        external_found = False
        for file_path in self.docs_dir.rglob('*.md'):
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read().lower()
                    if 'external' in content and ('document' in content or 'standard' in content):
                        external_found = True
                        break
            except Exception:
                continue

        if not external_found:
            self.findings.append({
                "requirement": "4.2.4 - External Documents",
                "finding": "External document control not documented",
                "severity": "MINOR",
                "recommendation": "Document external document identification and control procedures"
            })
        else:
            print("✓ External document control found")

    def _calculate_compliance_score(self):
        """Calculate overall compliance score."""
        # Total requirements audited
        total_requirements = 7

        # Count findings by severity
        major_findings = len([f for f in self.findings if f['severity'] == 'MAJOR'])
        minor_findings = len([f for f in self.findings if f['severity'] == 'MINOR'])

        # Calculate score (100 - major*20 - minor*10)
        self.compliance_score = max(0, 100 - (major_findings * 20) - (minor_findings * 10))

    def _generate_report(self) -> Dict:
        """Generate audit report."""
        report = {
            "audit_date": datetime.now().isoformat(),
            "audited_directory": str(self.docs_dir),
            "compliance_score": self.compliance_score,
            "total_findings": len(self.findings),
            "major_findings": len([f for f in self.findings if f['severity'] == 'MAJOR']),
            "minor_findings": len([f for f in self.findings if f['severity'] == 'MINOR']),
            "findings": self.findings,
            "recommendations": self._generate_recommendations()
        }

        return report

    def _generate_recommendations(self) -> List[str]:
        """Generate recommendations based on findings."""
        recommendations = []

        if self.compliance_score < 70:
            recommendations.append(
                "CRITICAL: Document control system requires immediate attention and improvement"
            )

        major_findings = [f for f in self.findings if f['severity'] == 'MAJOR']
        if major_findings:
            recommendations.append(
                f"Address {len(major_findings)} major findings before certification audit"
            )

        minor_findings = [f for f in self.findings if f['severity'] == 'MINOR']
        if minor_findings:
            recommendations.append(
                f"Address {len(minor_findings)} minor findings to improve compliance"
            )

        if self.compliance_score >= 90:
            recommendations.append(
                "Document control system is well-implemented. Focus on continuous improvement"
            )

        return recommendations


def print_audit_report(report: Dict):
    """Print formatted audit report."""
    print("\n" + "="*80)
    print(" DOCUMENT CONTROL AUDIT REPORT")
    print("="*80)
    print(f"\nAudit Date: {report['audit_date']}")
    print(f"Audited Directory: {report['audited_directory']}\n")

    # Compliance Score
    print("-" * 80)
    print(" COMPLIANCE SCORE")
    print("-" * 80)
    compliance_score = report['compliance_score']
    print(f"Compliance Score: {compliance_score}%")

    if compliance_score >= 90:
        print("Status: EXCELLENT ✓")
    elif compliance_score >= 70:
        print("Status: GOOD ✓")
    elif compliance_score >= 50:
        print("Status: NEEDS IMPROVEMENT ⚠")
    else:
        print("Status: CRITICAL ✗")

    # Summary
    print("\n" + "-" * 80)
    print(" SUMMARY")
    print("-" * 80)
    print(f"Total Findings: {report['total_findings']}")
    print(f"Major Findings: {report['major_findings']}")
    print(f"Minor Findings: {report['minor_findings']}")

    # Findings
    if report['findings']:
        print("\n" + "-" * 80)
        print(" FINDINGS")
        print("-" * 80)
        for i, finding in enumerate(report['findings'], 1):
            print(f"\n{i}. {finding['requirement']}")
            print(f"   Severity: {finding['severity']}")
            print(f"   Finding: {finding['finding']}")
            print(f"   Recommendation: {finding['recommendation']}")

    # Recommendations
    if report['recommendations']:
        print("\n" + "-" * 80)
        print(" RECOMMENDATIONS")
        print("-" * 80)
        for i, rec in enumerate(report['recommendations'], 1):
            print(f"{i}. {rec}")

    print("\n" + "="*80)
    print(" END OF AUDIT REPORT")
    print("="*80 + "\n")


def save_audit_report(report: Dict, output_path: str):
    """Save audit report to JSON file."""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2)
    print(f"Audit report saved to: {output_path}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Document Control Audit Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        '--docs-dir',
        required=True,
        help='Directory containing documents to audit'
    )
    parser.add_argument(
        '--output',
        help='Output file path for JSON report (optional)'
    )

    args = parser.parse_args()

    # Run audit
    auditor = DocumentControlAuditor(args.docs_dir)
    report = auditor.audit()

    # Print report
    print_audit_report(report)

    # Save report if output path specified
    if args.output:
        save_audit_report(report, args.output)

    return 0


if __name__ == '__main__':
    sys.exit(main())