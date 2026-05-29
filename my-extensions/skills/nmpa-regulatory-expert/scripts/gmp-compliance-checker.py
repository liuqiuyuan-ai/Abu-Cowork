#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NMPA GMP Compliance Checker
用于评估医疗器械和药品生产企业的GMP合规性
"""

import json
from typing import Dict, List, Tuple

class GMPComplianceChecker:
    """GMP合规检查器"""
    
    def __init__(self):
        self.gmp_requirements = {
            'quality_management': {
                'name': '质量管理体系',
                'items': [
                    ('QMS001', '质量方针和目标已制定并传达', '高'),
                    ('QMS002', '质量管理体系文件完整', '高'),
                    ('QMS003', '管理评审程序已建立', '高'),
                    ('QMS004', '内部审核程序已建立', '高'),
                    ('QMS005', '质量负责人已任命', '高'),
                    ('QMS006', '质量手册已批准发布', '中'),
                    ('QMS007', '质量目标可测量并监控', '中')
                ]
            },
            'facility_equipment': {
                'name': '设施与设备',
                'items': [
                    ('FAC001', '厂房布局合理，符合生产流程', '高'),
                    ('FAC002', '洁净区级别符合要求', '高'),
                    ('FAC003', '设备已验证并定期维护', '高'),
                    ('FAC004', '校准程序已建立', '高'),
                    ('FAC005', '环境监测系统运行正常', '中'),
                    ('FAC006', '设备维护记录完整', '中'),
                    ('FAC007', '仓储条件符合要求', '中')
                ]
            },
            'documentation': {
                'name': '文件与记录',
                'items': [
                    ('DOC001', '文件控制程序已建立', '高'),
                    ('DOC002', '批记录完整准确', '高'),
                    ('DOC003', '变更控制程序已建立', '高'),
                    ('DOC004', '记录保存期限符合要求', '高'),
                    ('DOC005', '电子记录符合完整性要求', '中'),
                    ('DOC006', '文件修订历史完整', '中'),
                    ('DOC007', '作废文件已收回', '低')
                ]
            },
            'production_control': {
                'name': '生产与过程控制',
                'items': [
                    ('PRD001', '工艺验证已完成', '高'),
                    ('PRD002', '批生产记录完整', '高'),
                    ('PRD003', '物料追溯系统有效', '高'),
                    ('PRD004', '标签管理程序已建立', '高'),
                    ('PRD005', '中间产品控制到位', '中'),
                    ('PRD006', '设备清洁验证已完成', '中'),
                    ('PRD007', '返工与回收程序已建立', '中')
                ]
            },
            'quality_control': {
                'name': '质量控制与保证',
                'items': [
                    ('QC001', '检验程序已建立', '高'),
                    ('QC002', '实验室设备已校准', '高'),
                    ('QC003', '成品放行程序已建立', '高'),
                    ('QC004', '不合格品处理程序已建立', '高'),
                    ('QC005', '投诉处理程序已建立', '高'),
                    ('QC006', 'CAPA系统有效运行', '高'),
                    ('QC007', '供应商质量评估程序已建立', '中')
                ]
            },
            'personnel_training': {
                'name': '人员与培训',
                'items': [
                    ('PER001', '关键岗位人员资质符合要求', '高'),
                    ('PER002', '培训计划已制定', '中'),
                    ('PER003', '培训记录完整', '中'),
                    ('PER004', '人员健康档案已建立', '中'),
                    ('PER005', '洁净区人员着装符合要求', '低'),
                    ('PER006', '新员工入职培训已完成', '低')
                ]
            }
        }
    
    def perform_compliance_check(self, audit_data: Dict) -> Dict:
        """执行GMP合规检查"""
        results = {
            'audit_scope': audit_data.get('audit_scope', 'full'),
            'audit_date': audit_data.get('audit_date', '2026-05-28'),
            'facility_name': audit_data.get('facility_name', '未指定'),
            'overall_score': 0,
            'total_items': 0,
            'compliant_items': 0,
            'findings': [],
            'summary': {
                'quality_management': {'score': 0, 'compliant': 0, 'total': 0},
                'facility_equipment': {'score': 0, 'compliant': 0, 'total': 0},
                'documentation': {'score': 0, 'compliant': 0, 'total': 0},
                'production_control': {'score': 0, 'compliant': 0, 'total': 0},
                'quality_control': {'score': 0, 'compliant': 0, 'total': 0},
                'personnel_training': {'score': 0, 'compliant': 0, 'total': 0}
            }
        }
        
        for category, details in self.gmp_requirements.items():
            category_score = 0
            category_compliant = 0
            category_total = 0
            
            for item_id, item_desc, priority in details['items']:
                category_total += 1
                
                # 检查该项目是否合规（从audit_data获取或默认为未知）
                is_compliant = audit_data.get('findings', {}).get(item_id, 'unknown')
                
                if is_compliant == 'compliant':
                    category_compliant += 1
                    category_score += 1
                    results['compliant_items'] += 1
                elif is_compliant == 'non-compliant':
                    severity = '严重' if priority == '高' else '一般' if priority == '中' else '轻微'
                    results['findings'].append({
                        'item_id': item_id,
                        'description': item_desc,
                        'priority': priority,
                        'severity': severity,
                        'status': '不符合',
                        'recommendation': f'建议立即整改{details["name"]}相关的{item_desc}要求'
                    })
                else:
                    results['findings'].append({
                        'item_id': item_id,
                        'description': item_desc,
                        'priority': priority,
                        'severity': '未知',
                        'status': '待确认',
                        'recommendation': '建议进一步核查'
                    })
                
                results['total_items'] += 1
            
            results['summary'][category]['score'] = category_score
            results['summary'][category]['compliant'] = category_compliant
            results['summary'][category]['total'] = category_total
        
        # 计算总体得分
        if results['total_items'] > 0:
            results['overall_score'] = round(results['compliant_items'] / results['total_items'] * 100, 2)
        
        # 添加合规等级评估
        if results['overall_score'] >= 90:
            results['compliance_level'] = '优秀'
            results['assessment'] = '企业GMP体系运行良好，建议继续保持'
        elif results['overall_score'] >= 75:
            results['compliance_level'] = '良好'
            results['assessment'] = '企业GMP体系基本符合要求，建议针对不符合项进行整改'
        elif results['overall_score'] >= 60:
            results['compliance_level'] = '合格'
            results['assessment'] = '企业GMP体系存在一定差距，需要制定整改计划'
        else:
            results['compliance_level'] = '不合格'
            results['assessment'] = '企业GMP体系存在严重缺陷，需要立即整改'
        
        return results
    
    def generate_audit_report(self, audit_data: Dict) -> str:
        """生成完整的审计报告"""
        results = self.perform_compliance_check(audit_data)
        
        report = {
            'report_title': 'NMPA GMP合规审计报告',
            'report_version': '1.0',
            'audit_info': {
                'facility_name': results['facility_name'],
                'audit_date': results['audit_date'],
                'audit_scope': results['audit_scope']
            },
            'compliance_summary': {
                'overall_score': f"{results['overall_score']}%",
                'compliance_level': results['compliance_level'],
                'assessment': results['assessment'],
                'compliant_items': results['compliant_items'],
                'total_items': results['total_items']
            },
            'category_summary': results['summary'],
            'findings': results['findings'],
            'recommendations': self._generate_recommendations(results)
        }
        
        return json.dumps(report, ensure_ascii=False, indent=2)
    
    def _generate_recommendations(self, results: Dict) -> List[str]:
        """生成改进建议"""
        recommendations = []
        
        if results['overall_score'] < 90:
            # 按严重程度分类不符合项
            critical_issues = [f for f in results['findings'] if f['severity'] == '严重']
            major_issues = [f for f in results['findings'] if f['severity'] == '一般']
            
            if critical_issues:
                recommendations.append(f"发现{len(critical_issues)}项严重不符合项，建议立即整改")
            if major_issues:
                recommendations.append(f"发现{len(major_issues)}项一般不符合项，建议在30天内整改")
            
            recommendations.append("建议制定CAPA计划，明确整改责任人及时限")
            recommendations.append("建议定期进行内部审核，持续改进")
        
        recommendations.append("建议关注NMPA最新GMP要求更新")
        recommendations.append("建议加强员工GMP培训")
        
        return recommendations

def main():
    """示例用法"""
    checker = GMPComplianceChecker()
    
    # 示例审计数据
    audit_data = {
        'facility_name': '示例医疗器械有限公司',
        'audit_date': '2026-05-28',
        'audit_scope': 'full',
        'findings': {
            'QMS001': 'compliant',
            'QMS002': 'compliant',
            'QMS003': 'compliant',
            'FAC001': 'compliant',
            'FAC002': 'non-compliant',  # 洁净区级别不符合
            'FAC003': 'compliant',
            'DOC001': 'compliant',
            'DOC002': 'compliant',
            'PRD001': 'compliant',
            'PRD002': 'compliant',
            'QC001': 'compliant',
            'QC002': 'compliant',
            'QC003': 'compliant',
            'PER001': 'compliant',
            'PER002': 'compliant'
        }
    }
    
    report = checker.generate_audit_report(audit_data)
    print("GMP合规审计报告:")
    print(report)

if __name__ == '__main__':
    main()
