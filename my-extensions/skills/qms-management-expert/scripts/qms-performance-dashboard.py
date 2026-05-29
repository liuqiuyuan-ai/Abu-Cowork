#!/usr/bin/env python3
"""
QMS Performance Dashboard

This script generates a comprehensive QMS performance dashboard with key quality indicators.

Usage:
    python qms-performance-dashboard.py --data-dir <path> [--output <path>]
"""

import os
import sys
import argparse
import json
from pathlib import Path
from typing import Dict, List
from datetime import datetime, timedelta


class QMSPerformanceDashboard:
    """Generates QMS performance metrics and dashboard."""

    def __init__(self, data_dir: str):
        """Initialize dashboard with data directory."""
        self.data_dir = Path(data_dir)
        self.metrics = {}

    def generate_dashboard(self) -> Dict:
        """Generate comprehensive QMS performance dashboard."""
        print(f"Generating QMS Performance Dashboard from: {self.data_dir}")

        if not self.data_dir.exists():
            print(f"WARNING: Data directory not found: {self.data_dir}")
            print("Generating template dashboard structure...")

        # Collect metrics from various sources
        self._collect_audit_metrics()
        self._collect_capa_metrics()
        self._collect_complaint_metrics()
        self._collect_training_metrics()
        self._collect_document_control_metrics()
        self._collect_supplier_metrics()

        # Calculate overall QMS health score
        self._calculate_health_score()

        # Generate dashboard report
        dashboard = self._generate_report()

        return dashboard

    def _collect_audit_metrics(self):
        """Collect internal and external audit metrics."""
        self.metrics['audit'] = {
            'internal_audits_completed': 0,
            'internal_audits_scheduled': 4,
            'external_audits_completed': 0,
            'external_audits_scheduled': 1,
            'findings_open': 0,
            'findings_closed': 0,
            'findings_overdue': 0,
            'average_closure_days': 0
        }

        # Try to load audit data if available
        audit_file = self.data_dir / 'audit_data.json'
        if audit_file.exists():
            try:
                with open(audit_file, 'r', encoding='utf-8') as f:
                    audit_data = json.load(f)
                    self.metrics['audit'].update(audit_data)
            except Exception as e:
                print(f"Warning: Could not load audit data: {e}")

    def _collect_capa_metrics(self):
        """Collect CAPA metrics."""
        self.metrics['capa'] = {
            'capa_open': 0,
            'capa_closed': 0,
            'capa_overdue': 0,
            'average_closure_days': 0,
            'effectiveness_verified': 0,
            'effectiveness_pending': 0
        }

        # Try to load CAPA data if available
        capa_file = self.data_dir / 'capa_data.json'
        if capa_file.exists():
            try:
                with open(capa_file, 'r', encoding='utf-8') as f:
                    capa_data = json.load(f)
                    self.metrics['capa'].update(capa_data)
            except Exception as e:
                print(f"Warning: Could not load CAPA data: {e}")

    def _collect_complaint_metrics(self):
        """Collect complaint handling metrics."""
        self.metrics['complaint'] = {
            'complaints_received': 0,
            'complaints_closed': 0,
            'complaints_open': 0,
            'average_closure_days': 0,
            'complaints_per_month': 0,
            'customer_satisfaction_score': 0
        }

        # Try to load complaint data if available
        complaint_file = self.data_dir / 'complaint_data.json'
        if complaint_file.exists():
            try:
                with open(complaint_file, 'r', encoding='utf-8') as f:
                    complaint_data = json.load(f)
                    self.metrics['complaint'].update(complaint_data)
            except Exception as e:
                print(f"Warning: Could not load complaint data: {e}")

    def _collect_training_metrics(self):
        """Collect training and competency metrics."""
        self.metrics['training'] = {
            'training_planned': 0,
            'training_completed': 0,
            'training_completion_rate': 0,
            'employees_trained': 0,
            'total_employees': 0,
            'competency_assessments_completed': 0
        }

        # Try to load training data if available
        training_file = self.data_dir / 'training_data.json'
        if training_file.exists():
            try:
                with open(training_file, 'r', encoding='utf-8') as f:
                    training_data = json.load(f)
                    self.metrics['training'].update(training_data)
            except Exception as e:
                print(f"Warning: Could not load training data: {e}")

    def _collect_document_control_metrics(self):
        """Collect document control metrics."""
        self.metrics['document_control'] = {
            'documents_total': 0,
            'documents_current': 0,
            'documents_obsolete': 0,
            'documents_under_review': 0,
            'average_approval_days': 0,
            'documents_revised_this_quarter': 0
        }

        # Try to load document control data if available
        doc_file = self.data_dir / 'document_data.json'
        if doc_file.exists():
            try:
                with open(doc_file, 'r', encoding='utf-8') as f:
                    doc_data = json.load(f)
                    self.metrics['document_control'].update(doc_data)
            except Exception as e:
                print(f"Warning: Could not load document control data: {e}")

    def _collect_supplier_metrics(self):
        """Collect supplier quality metrics."""
        self.metrics['supplier'] = {
            'suppliers_qualified': 0,
            'suppliers_under_evaluation': 0,
            'supplier_audits_completed': 0,
            'supplier_audits_scheduled': 0,
            'average_quality_rating': 0,
            'suppliers_on_corrective_action': 0
        }

        # Try to load supplier data if available
        supplier_file = self.data_dir / 'supplier_data.json'
        if supplier_file.exists():
            try:
                with open(supplier_file, 'r', encoding='utf-8') as f:
                    supplier_data = json.load(f)
                    self.metrics['supplier'].update(supplier_data)
            except Exception as e:
                print(f"Warning: Could not load supplier data: {e}")

    def _calculate_health_score(self):
        """Calculate overall QMS health score."""
        scores = []

        # Audit health score
        if self.metrics['audit']['internal_audits_scheduled'] > 0:
            audit_score = (self.metrics['audit']['internal_audits_completed'] /
                          self.metrics['audit']['internal_audits_scheduled']) * 100
            scores.append(audit_score)

        # CAPA health score
        if self.metrics['capa']['capa_open'] + self.metrics['capa']['capa_closed'] > 0:
            capa_score = (self.metrics['capa']['capa_closed'] /
                         (self.metrics['capa']['capa_open'] + self.metrics['capa']['capa_closed'])) * 100
            scores.append(capa_score)

        # Training health score
        if self.metrics['training']['training_planned'] > 0:
            training_score = self.metrics['training']['training_completion_rate']
            scores.append(training_score)

        # Document control health score
        if self.metrics['document_control']['documents_total'] > 0:
            doc_score = (self.metrics['document_control']['documents_current'] /
                        self.metrics['document_control']['documents_total']) * 100
            scores.append(doc_score)

        # Calculate average health score
        if scores:
            self.metrics['health_score'] = round(sum(scores) / len(scores), 1)
        else:
            self.metrics['health_score'] = 0

    def _generate_report(self) -> Dict:
        """Generate dashboard report."""
        report = {
            "report_date": datetime.now().isoformat(),
            "data_source": str(self.data_dir),
            "health_score": self.metrics.get('health_score', 0),
            "metrics": self.metrics,
            "recommendations": self._generate_recommendations()
        }

        return report

    def _generate_recommendations(self) -> List[str]:
        """Generate recommendations based on metrics."""
        recommendations = []

        # Audit recommendations
        if self.metrics['audit']['internal_audits_completed'] < self.metrics['audit']['internal_audits_scheduled']:
            recommendations.append(
                f"Complete {self.metrics['audit']['internal_audits_scheduled'] - self.metrics['audit']['internal_audits_completed']} "
                "scheduled internal audits"
            )

        if self.metrics['audit']['findings_overdue'] > 0:
            recommendations.append(
                f"Address {self.metrics['audit']['findings_overdue']} overdue audit findings"
            )

        # CAPA recommendations
        if self.metrics['capa']['capa_overdue'] > 0:
            recommendations.append(
                f"Address {self.metrics['capa']['capa_overdue']} overdue CAPA items"
            )

        if self.metrics['capa']['effectiveness_pending'] > 0:
            recommendations.append(
                f"Verify effectiveness for {self.metrics['capa']['effectiveness_pending']} CAPA items"
            )

        # Training recommendations
        if self.metrics['training']['training_completion_rate'] < 90:
            recommendations.append(
                f"Improve training completion rate (currently {self.metrics['training']['training_completion_rate']}%)"
            )

        # Document control recommendations
        if self.metrics['document_control']['documents_under_review'] > 10:
            recommendations.append(
                f"Review and approve {self.metrics['document_control']['documents_under_review']} pending documents"
            )

        # Overall health score recommendations
        if self.metrics.get('health_score', 0) < 70:
            recommendations.append(
                "QMS health score is below 70%. Prioritize improvement initiatives."
            )
        elif self.metrics.get('health_score', 0) >= 90:
            recommendations.append(
                "QMS health score is excellent. Focus on continuous improvement opportunities."
            )

        return recommendations


def print_dashboard(dashboard: Dict):
    """Print formatted dashboard."""
    print("\n" + "="*80)
    print(" QMS PERFORMANCE DASHBOARD")
    print("="*80)
    print(f"\nReport Date: {dashboard['report_date']}")
    print(f"Data Source: {dashboard['data_source']}\n")

    # Health Score
    health_score = dashboard['health_score']
    print("-" * 80)
    print(" OVERALL QMS HEALTH SCORE")
    print("-" * 80)
    print(f"Health Score: {health_score}%")

    if health_score >= 90:
        print("Status: EXCELLENT ✓")
    elif health_score >= 70:
        print("Status: GOOD ✓")
    elif health_score >= 50:
        print("Status: NEEDS IMPROVEMENT ⚠")
    else:
        print("Status: CRITICAL ✗")

    # Audit Metrics
    print("\n" + "-" * 80)
    print(" AUDIT METRICS")
    print("-" * 80)
    audit = dashboard['metrics']['audit']
    print(f"Internal Audits: {audit['internal_audits_completed']}/{audit['internal_audits_scheduled']} completed")
    print(f"External Audits: {audit['external_audits_completed']}/{audit['external_audits_scheduled']} completed")
    print(f"Findings: {audit['findings_open']} open, {audit['findings_closed']} closed, {audit['findings_overdue']} overdue")

    # CAPA Metrics
    print("\n" + "-" * 80)
    print(" CAPA METRICS")
    print("-" * 80)
    capa = dashboard['metrics']['capa']
    print(f"CAPA Items: {capa['capa_open']} open, {capa['capa_closed']} closed, {capa['capa_overdue']} overdue")
    print(f"Effectiveness: {capa['effectiveness_verified']} verified, {capa['effectiveness_pending']} pending")

    # Complaint Metrics
    print("\n" + "-" * 80)
    print(" COMPLAINT METRICS")
    print("-" * 80)
    complaint = dashboard['metrics']['complaint']
    print(f"Complaints: {complaint['complaints_received']} received, {complaint['complaints_closed']} closed")
    print(f"Average Closure: {complaint['average_closure_days']} days")
    print(f"Customer Satisfaction: {complaint['customer_satisfaction_score']}/5.0")

    # Training Metrics
    print("\n" + "-" * 80)
    print(" TRAINING METRICS")
    print("-" * 80)
    training = dashboard['metrics']['training']
    print(f"Training: {training['training_completed']}/{training['training_planned']} completed")
    print(f"Completion Rate: {training['training_completion_rate']}%")
    print(f"Employees Trained: {training['employees_trained']}/{training['total_employees']}")

    # Document Control Metrics
    print("\n" + "-" * 80)
    print(" DOCUMENT CONTROL METRICS")
    print("-" * 80)
    doc = dashboard['metrics']['document_control']
    print(f"Documents: {doc['documents_total']} total, {doc['documents_current']} current")
    print(f"Under Review: {doc['documents_under_review']}")
    print(f"Average Approval Time: {doc['average_approval_days']} days")

    # Supplier Metrics
    print("\n" + "-" * 80)
    print(" SUPPLIER METRICS")
    print("-" * 80)
    supplier = dashboard['metrics']['supplier']
    print(f"Suppliers: {supplier['suppliers_qualified']} qualified, {supplier['suppliers_under_evaluation']} under evaluation")
    print(f"Audits: {supplier['supplier_audits_completed']}/{supplier['supplier_audits_scheduled']} completed")
    print(f"Average Quality Rating: {supplier['average_quality_rating']}/5.0")

    # Recommendations
    if dashboard['recommendations']:
        print("\n" + "-" * 80)
        print(" RECOMMENDATIONS")
        print("-" * 80)
        for i, rec in enumerate(dashboard['recommendations'], 1):
            print(f"{i}. {rec}")

    print("\n" + "="*80)
    print(" END OF DASHBOARD")
    print("="*80 + "\n")


def save_dashboard(dashboard: Dict, output_path: str):
    """Save dashboard to JSON file."""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(dashboard, f, indent=2)
    print(f"Dashboard saved to: {output_path}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='QMS Performance Dashboard',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        '--data-dir',
        required=True,
        help='Directory containing QMS data files'
    )
    parser.add_argument(
        '--output',
        help='Output file path for JSON dashboard (optional)'
    )

    args = parser.parse_args()

    # Generate dashboard
    dashboard_generator = QMSPerformanceDashboard(args.data_dir)
    dashboard = dashboard_generator.generate_dashboard()

    # Print dashboard
    print_dashboard(dashboard)

    # Save dashboard if output path specified
    if args.output:
        save_dashboard(dashboard, args.output)

    return 0


if __name__ == '__main__':
    sys.exit(main())