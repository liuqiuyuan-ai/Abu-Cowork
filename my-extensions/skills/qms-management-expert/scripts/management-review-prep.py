#!/usr/bin/env python3
"""
Management Review Preparation Tool

This script compiles inputs for management review meetings per ISO 13485 Clause 5.6.

Usage:
    python management-review-prep.py --data-dir <path> [--output <path>]
"""

import os
import sys
import argparse
import json
from pathlib import Path
from typing import Dict, List
from datetime import datetime, timedelta


class ManagementReviewPreparer:
    """Prepares management review input package."""

    def __init__(self, data_dir: str):
        """Initialize preparer with data directory."""
        self.data_dir = Path(data_dir)
        self.inputs = {}

    def prepare(self) -> Dict:
        """Prepare management review input package."""
        print(f"Preparing management review from: {self.data_dir}")

        if not self.data_dir.exists():
            print(f"WARNING: Data directory not found: {self.data_dir}")
            print("Generating template input package...")

        # Collect all required inputs per ISO 13485 Clause 5.6.2
        self._collect_audit_results()
        self._collect_customer_feedback()
        self._collect_process_performance()
        self._collect_product_conformity()
        self._collect_capa_status()
        self._collect_previous_review_actions()
        self._collect_qms_changes()
        self._collect_improvement_recommendations()
        self._collect_regulatory_changes()
        self._collect_resource_needs()

        # Generate input package
        package = self._generate_package()

        return package

    def _collect_audit_results(self):
        """Collect audit results (internal and external)."""
        print("\nCollecting audit results...")

        self.inputs['audit_results'] = {
            'internal_audits': {
                'scheduled': 4,
                'completed': 0,
                'findings': {
                    'major': 0,
                    'minor': 0,
                    'observations': 0
                }
            },
            'external_audits': {
                'scheduled': 1,
                'completed': 0,
                'findings': {
                    'major': 0,
                    'minor': 0,
                    'observations': 0
                }
            },
            'trends': [],
            'effectiveness': 'Not assessed'
        }

        # Try to load audit data
        audit_file = self.data_dir / 'audit_data.json'
        if audit_file.exists():
            try:
                with open(audit_file, 'r', encoding='utf-8') as f:
                    audit_data = json.load(f)
                    self.inputs['audit_results'].update(audit_data)
            except Exception as e:
                print(f"Warning: Could not load audit data: {e}")

    def _collect_customer_feedback(self):
        """Collect customer feedback and complaint data."""
        print("Collecting customer feedback...")

        self.inputs['customer_feedback'] = {
            'complaints_received': 0,
            'complaints_closed': 0,
            'complaints_open': 0,
            'customer_satisfaction_score': 0,
            'feedback_trends': [],
            'recurring_issues': []
        }

        # Try to load complaint data
        complaint_file = self.data_dir / 'complaint_data.json'
        if complaint_file.exists():
            try:
                with open(complaint_file, 'r', encoding='utf-8') as f:
                    complaint_data = json.load(f)
                    self.inputs['customer_feedback'].update(complaint_data)
            except Exception as e:
                print(f"Warning: Could not load complaint data: {e}")

    def _collect_process_performance(self):
        """Collect process performance data."""
        print("Collecting process performance data...")

        self.inputs['process_performance'] = {
            'processes_monitored': 0,
            'processes_meeting_criteria': 0,
            'processes_not_meeting_criteria': 0,
            'cycle_times': {},
            'efficiency_metrics': {},
            'trends': []
        }

        # Try to load process data
        process_file = self.data_dir / 'process_data.json'
        if process_file.exists():
            try:
                with open(process_file, 'r', encoding='utf-8') as f:
                    process_data = json.load(f)
                    self.inputs['process_performance'].update(process_data)
            except Exception as e:
                print(f"Warning: Could not load process data: {e}")

    def _collect_product_conformity(self):
        """Collect product conformity data."""
        print("Collecting product conformity data...")

        self.inputs['product_conformity'] = {
            'products_tested': 0,
            'products_passed': 0,
            'products_failed': 0,
            'nonconformities': 0,
            'yield_rate': 0,
            'trends': []
        }

        # Try to load product data
        product_file = self.data_dir / 'product_data.json'
        if product_file.exists():
            try:
                with open(product_file, 'r', encoding='utf-8') as f:
                    product_data = json.load(f)
                    self.inputs['product_conformity'].update(product_data)
            except Exception as e:
                print(f"Warning: Could not load product data: {e}")

    def _collect_capa_status(self):
        """Collect CAPA status and effectiveness."""
        print("Collecting CAPA status...")

        self.inputs['capa_status'] = {
            'capa_open': 0,
            'capa_closed': 0,
            'capa_overdue': 0,
            'effectiveness_verified': 0,
            'effectiveness_pending': 0,
            'average_closure_days': 0,
            'recurrence_prevented': 0
        }

        # Try to load CAPA data
        capa_file = self.data_dir / 'capa_data.json'
        if capa_file.exists():
            try:
                with open(capa_file, 'r', encoding='utf-8') as f:
                    capa_data = json.load(f)
                    self.inputs['capa_status'].update(capa_data)
            except Exception as e:
                print(f"Warning: Could not load CAPA data: {e}")

    def _collect_previous_review_actions(self):
        """Collect status of actions from previous management review."""
        print("Collecting previous review actions...")

        self.inputs['previous_review_actions'] = {
            'actions_assigned': 0,
            'actions_completed': 0,
            'actions_in_progress': 0,
            'actions_overdue': 0,
            'actions': []
        }

        # Try to load previous review data
        review_file = self.data_dir / 'previous_review.json'
        if review_file.exists():
            try:
                with open(review_file, 'r', encoding='utf-8') as f:
                    review_data = json.load(f)
                    self.inputs['previous_review_actions'].update(review_data)
            except Exception as e:
                print(f"Warning: Could not load previous review data: {e}")

    def _collect_qms_changes(self):
        """Collect changes affecting the QMS."""
        print("Collecting QMS changes...")

        self.inputs['qms_changes'] = {
            'organizational_changes': [],
            'process_changes': [],
            'product_changes': [],
            'regulatory_changes': [],
            'other_changes': []
        }

        # Try to load change data
        change_file = self.data_dir / 'change_data.json'
        if change_file.exists():
            try:
                with open(change_file, 'r', encoding='utf-8') as f:
                    change_data = json.load(f)
                    self.inputs['qms_changes'].update(change_data)
            except Exception as e:
                print(f"Warning: Could not load change data: {e}")

    def _collect_improvement_recommendations(self):
        """Collect improvement recommendations."""
        print("Collecting improvement recommendations...")

        self.inputs['improvement_recommendations'] = {
            'process_improvements': [],
            'product_improvements': [],
            'system_improvements': [],
            'resource_improvements': []
        }

        # Try to load improvement data
        improvement_file = self.data_dir / 'improvement_data.json'
        if improvement_file.exists():
            try:
                with open(improvement_file, 'r', encoding='utf-8') as f:
                    improvement_data = json.load(f)
                    self.inputs['improvement_recommendations'].update(improvement_data)
            except Exception as e:
                print(f"Warning: Could not load improvement data: {e}")

    def _collect_regulatory_changes(self):
        """Collect applicable new or revised regulatory requirements."""
        print("Collecting regulatory changes...")

        self.inputs['regulatory_changes'] = {
            'new_requirements': [],
            'revised_requirements': [],
            'upcoming_deadlines': [],
            'compliance_status': 'Not assessed'
        }

        # Try to load regulatory data
        regulatory_file = self.data_dir / 'regulatory_data.json'
        if regulatory_file.exists():
            try:
                with open(regulatory_file, 'r', encoding='utf-8') as f:
                    regulatory_data = json.load(f)
                    self.inputs['regulatory_changes'].update(regulatory_data)
            except Exception as e:
                print(f"Warning: Could not load regulatory data: {e}")

    def _collect_resource_needs(self):
        """Collect resource needs and allocation."""
        print("Collecting resource needs...")

        self.inputs['resource_needs'] = {
            'personnel_needs': [],
            'equipment_needs': [],
            'facility_needs': [],
            'training_needs': [],
            'budget_needs': []
        }

        # Try to load resource data
        resource_file = self.data_dir / 'resource_data.json'
        if resource_file.exists():
            try:
                with open(resource_file, 'r', encoding='utf-8') as f:
                    resource_data = json.load(f)
                    self.inputs['resource_needs'].update(resource_data)
            except Exception as e:
                print(f"Warning: Could not load resource data: {e}")

    def _generate_package(self) -> Dict:
        """Generate management review input package."""
        package = {
            "preparation_date": datetime.now().isoformat(),
            "data_source": str(self.data_dir),
            "review_period": "Last Quarter",
            "inputs": self.inputs,
            "summary": self._generate_summary(),
            "recommendations": self._generate_recommendations()
        }

        return package

    def _generate_summary(self) -> Dict:
        """Generate summary of inputs."""
        summary = {
            "audit_health": "Not assessed",
            "customer_satisfaction": "Not assessed",
            "process_effectiveness": "Not assessed",
            "product_quality": "Not assessed",
            "capa_effectiveness": "Not assessed",
            "overall_qms_health": "Not assessed"
        }

        # Assess audit health
        if 'audit_results' in self.inputs:
            audit = self.inputs['audit_results']
            total_findings = (audit['internal_audits']['findings']['major'] +
                            audit['internal_audits']['findings']['minor'] +
                            audit['external_audits']['findings']['major'] +
                            audit['external_audits']['findings']['minor'])
            if total_findings == 0:
                summary['audit_health'] = "Excellent"
            elif total_findings < 5:
                summary['audit_health'] = "Good"
            else:
                summary['audit_health'] = "Needs Improvement"

        # Assess customer satisfaction
        if 'customer_feedback' in self.inputs:
            satisfaction = self.inputs['customer_feedback']['customer_satisfaction_score']
            if satisfaction >= 4.5:
                summary['customer_satisfaction'] = "Excellent"
            elif satisfaction >= 4.0:
                summary['customer_satisfaction'] = "Good"
            elif satisfaction >= 3.5:
                summary['customer_satisfaction'] = "Satisfactory"
            else:
                summary['customer_satisfaction'] = "Needs Improvement"

        # Assess CAPA effectiveness
        if 'capa_status' in self.inputs:
            capa = self.inputs['capa_status']
            if capa['capa_overdue'] == 0 and capa['effectiveness_pending'] == 0:
                summary['capa_effectiveness'] = "Excellent"
            elif capa['capa_overdue'] == 0:
                summary['capa_effectiveness'] = "Good"
            else:
                summary['capa_effectiveness'] = "Needs Improvement"

        return summary

    def _generate_recommendations(self) -> List[str]:
        """Generate recommendations based on inputs."""
        recommendations = []

        # Audit recommendations
        if 'audit_results' in self.inputs:
            audit = self.inputs['audit_results']
            if audit['internal_audits']['completed'] < audit['internal_audits']['scheduled']:
                recommendations.append(
                    "Complete remaining scheduled internal audits"
                )

        # CAPA recommendations
        if 'capa_status' in self.inputs:
            capa = self.inputs['capa_status']
            if capa['capa_overdue'] > 0:
                recommendations.append(
                    f"Address {capa['capa_overdue']} overdue CAPA items"
                )

        # Customer feedback recommendations
        if 'customer_feedback' in self.inputs:
            feedback = self.inputs['customer_feedback']
            if feedback['customer_satisfaction_score'] < 4.0:
                recommendations.append(
                    "Investigate customer satisfaction concerns and implement improvements"
                )

        # Process performance recommendations
        if 'process_performance' in self.inputs:
            process = self.inputs['process_performance']
            if process['processes_not_meeting_criteria'] > 0:
                recommendations.append(
                    f"Address {process['processes_not_meeting_criteria']} processes not meeting criteria"
                )

        return recommendations


def print_package(package: Dict):
    """Print formatted management review input package."""
    print("\n" + "="*80)
    print(" MANAGEMENT REVIEW INPUT PACKAGE")
    print("="*80)
    print(f"\nPreparation Date: {package['preparation_date']}")
    print(f"Review Period: {package['review_period']}\n")

    # Summary
    print("-" * 80)
    print(" SUMMARY")
    print("-" * 80)
    summary = package['summary']
    for key, value in summary.items():
        print(f"{key.replace('_', ' ').title()}: {value}")

    # Audit Results
    if 'audit_results' in package['inputs']:
        print("\n" + "-" * 80)
        print(" AUDIT RESULTS")
        print("-" * 80)
        audit = package['inputs']['audit_results']
        print(f"Internal Audits: {audit['internal_audits']['completed']}/{audit['internal_audits']['scheduled']} completed")
        print(f"  Findings: {audit['internal_audits']['findings']['major']} major, {audit['internal_audits']['findings']['minor']} minor")
        print(f"External Audits: {audit['external_audits']['completed']}/{audit['external_audits']['scheduled']} completed")
        print(f"  Findings: {audit['external_audits']['findings']['major']} major, {audit['external_audits']['findings']['minor']} minor")

    # Customer Feedback
    if 'customer_feedback' in package['inputs']:
        print("\n" + "-" * 80)
        print(" CUSTOMER FEEDBACK")
        print("-" * 80)
        feedback = package['inputs']['customer_feedback']
        print(f"Complaints: {feedback['complaints_received']} received, {feedback['complaints_closed']} closed")
        print(f"Customer Satisfaction: {feedback['customer_satisfaction_score']}/5.0")

    # CAPA Status
    if 'capa_status' in package['inputs']:
        print("\n" + "-" * 80)
        print(" CAPA STATUS")
        print("-" * 80)
        capa = package['inputs']['capa_status']
        print(f"CAPA Items: {capa['capa_open']} open, {capa['capa_closed']} closed, {capa['capa_overdue']} overdue")
        print(f"Effectiveness: {capa['effectiveness_verified']} verified, {capa['effectiveness_pending']} pending")

    # Recommendations
    if package['recommendations']:
        print("\n" + "-" * 80)
        print(" RECOMMENDATIONS")
        print("-" * 80)
        for i, rec in enumerate(package['recommendations'], 1):
            print(f"{i}. {rec}")

    print("\n" + "="*80)
    print(" END OF INPUT PACKAGE")
    print("="*80 + "\n")


def save_package(package: Dict, output_path: str):
    """Save package to JSON file."""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(package, f, indent=2)
    print(f"Input package saved to: {output_path}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Management Review Preparation Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        '--data-dir',
        required=True,
        help='Directory containing QMS data files'
    )
    parser.add_argument(
        '--output',
        help='Output file path for JSON package (optional)'
    )

    args = parser.parse_args()

    # Prepare package
    preparer = ManagementReviewPreparer(args.data_dir)
    package = preparer.prepare()

    # Print package
    print_package(package)

    # Save package if output path specified
    if args.output:
        save_package(package, args.output)

    return 0


if __name__ == '__main__':
    sys.exit(main())