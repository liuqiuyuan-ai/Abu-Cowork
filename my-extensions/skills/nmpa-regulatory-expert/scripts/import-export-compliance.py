#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NMPA Import/Export Compliance Tool
用于管理医疗器械和药品的进出口合规
"""

import json
from typing import Dict, List, Optional

class ImportExportCompliance:
    """进出口合规管理工具"""
    
    def __init__(self):
        self.import_requirements = {
            'medical_device': [
                ('IM001', '进口医疗器械注册证', '必须'),
                ('IM002', '医疗器械生产企业许可证', '必须'),
                ('IM003', '产品技术要求', '必须'),
                ('IM004', '注册检验报告', '必须'),
                ('IM005', '说明书和标签', '必须'),
                ('IM006', '原产地证明', '必须'),
                ('IM007', '自由销售证明', '必须'),
                ('IM008', 'CE证书（如适用）', '可选'),
                ('IM009', 'FDA 510(k)（如适用）', '可选'),
                ('IM010', 'GMP证书', '必须')
            ],
            'pharmaceutical': [
                ('IM001', '进口药品注册证', '必须'),
                ('IM002', '药品生产企业许可证', '必须'),
                ('IM003', '质量标准', '必须'),
                ('IM004', '检验报告', '必须'),
                ('IM005', '说明书和标签', '必须'),
                ('IM006', '原产地证明', '必须'),
                ('IM007', '自由销售证明', '必须'),
                ('IM008', 'GMP证书', '必须'),
                ('IM009', '稳定性研究资料', '必须'),
                ('IM010', '临床试验资料（如适用）', '可选')
            ],
            'ivd': [
                ('IM001', '体外诊断试剂注册证/备案凭证', '必须'),
                ('IM002', '产品技术要求', '必须'),
                ('IM003', '注册检验报告', '必须'),
                ('IM004', '说明书和标签', '必须'),
                ('IM005', '原产地证明', '必须'),
                ('IM006', '自由销售证明', '必须'),
                ('IM007', 'GMP证书', '必须'),
                ('IM008', '临床评价资料', '必须')
            ]
        }
        
        self.customs_documents = [
            '报关单',
            '发票',
            '装箱单',
            '提单/运单',
            '原产地证明',
            '检验检疫证明',
            '进口许可证',
            '自动进口许可证（如适用）'
        ]
    
    def check_import_compliance(self, product_info: Dict) -> Dict:
        """检查进口合规性"""
        product_type = product_info.get('product_type', 'medical_device')
        requirements = self.import_requirements.get(product_type, [])
        
        compliance_check = {
            'product_name': product_info.get('product_name', '未指定'),
            'product_type': product_type,
            'origin_country': product_info.get('origin_country', '未指定'),
            'compliance_status': 'pending',
            'required_documents': [],
            'missing_documents': [],
            'optional_documents': [],
            'customs_clearance_checklist': [],
            'estimated_timeline': '',
            'cost_estimate': {},
            'recommendations': []
        }
        
        # 检查必需文件
        for doc_id, doc_name, requirement_type in requirements:
            document_status = product_info.get('documents', {}).get(doc_id, 'missing')
            
            if requirement_type == '必须':
                compliance_check['required_documents'].append({
                    'id': doc_id,
                    'name': doc_name,
                    'status': document_status,
                    'requirement': '必须'
                })
                
                if document_status != 'available':
                    compliance_check['missing_documents'].append(doc_name)
            else:
                compliance_check['optional_documents'].append({
                    'id': doc_id,
                    'name': doc_name,
                    'status': document_status,
                    'requirement': '可选'
                })
        
        # 检查海关清关文件
        for doc in self.customs_documents:
            status = product_info.get('customs_documents', {}).get(doc, 'missing')
            compliance_check['customs_clearance_checklist'].append({
                'document': doc,
                'status': status
            })
        
        # 评估合规状态
        if not compliance_check['missing_documents']:
            compliance_check['compliance_status'] = 'compliant'
            compliance_check['recommendations'].append('所有必需文件齐全，可以开始进口流程')
        else:
            compliance_check['compliance_status'] = 'non-compliant'
            compliance_check['recommendations'].append(f'缺少{len(compliance_check["missing_documents"])}项必需文件，请补充')
        
        # 估算时间线
        compliance_check['estimated_timeline'] = self._estimate_timeline(product_type)
        
        # 估算费用
        compliance_check['cost_estimate'] = self._estimate_costs(product_type)
        
        return compliance_check
    
    def _estimate_timeline(self, product_type: str) -> str:
        """估算进口时间线"""
        timelines = {
            'medical_device': {
                'Class I': '30-45天',
                'Class II': '60-90天',
                'Class III': '90-180天'
            },
            'pharmaceutical': '90-180天',
            'ivd': {
                'Class I': '30-45天',
                'Class II': '60-90天',
                'Class III': '90-180天'
            }
        }
        
        return str(timelines.get(product_type, '60-90天'))
    
    def _estimate_costs(self, product_type: str) -> Dict:
        """估算费用"""
        costs = {
            'medical_device': {
                'registration_fee': '5000-20000 RMB',
                'testing_fee': '10000-50000 RMB',
                'agent_fee': '10000-30000 RMB',
                'customs_duty': '0-10% CIF',
                'VAT': '13% CIF'
            },
            'pharmaceutical': {
                'registration_fee': '5000-30000 RMB',
                'testing_fee': '20000-100000 RMB',
                'agent_fee': '20000-50000 RMB',
                'customs_duty': '0-6% CIF',
                'VAT': '13% CIF'
            },
            'ivd': {
                'registration_fee': '5000-15000 RMB',
                'testing_fee': '10000-30000 RMB',
                'agent_fee': '10000-25000 RMB',
                'customs_duty': '0-10% CIF',
                'VAT': '13% CIF'
            }
        }
        
        return costs.get(product_type, {})
    
    def generate_import_plan(self, product_info: Dict) -> str:
        """生成进口计划"""
        compliance = self.check_import_compliance(product_info)
        
        plan = {
            'plan_title': 'NMPA进口合规计划',
            'product_info': {
                'name': compliance['product_name'],
                'type': compliance['product_type'],
                'origin': compliance['origin_country']
            },
            'compliance_status': compliance['compliance_status'],
            'missing_documents': compliance['missing_documents'],
            'required_documents': compliance['required_documents'],
            'customs_documents': compliance['customs_clearance_checklist'],
            'timeline': compliance['estimated_timeline'],
            'cost_estimate': compliance['cost_estimate'],
            'implementation_steps': self._generate_implementation_steps(compliance),
            'recommendations': compliance['recommendations']
        }
        
        return json.dumps(plan, ensure_ascii=False, indent=2)
    
    def _generate_implementation_steps(self, compliance: Dict) -> List[Dict]:
        """生成实施步骤"""
        steps = []
        
        if compliance['missing_documents']:
            steps.append({
                'step': 1,
                'title': '文件准备',
                'description': f'补充缺少的文件：{", ".join(compliance["missing_documents"])}',
                'duration': '30-60天'
            })
        
        steps.extend([
            {
                'step': len(steps) + 1,
                'title': '注册申请',
                'description': '向NMPA提交注册申请',
                'duration': '60-90天'
            },
            {
                'step': len(steps) + 1,
                'title': '注册检验',
                'description': '提交样品进行注册检验',
                'duration': '30-60天'
            },
            {
                'step': len(steps) + 1,
                'title': '技术审评',
                'description': 'NMPA技术审评',
                'duration': '30-60天'
            },
            {
                'step': len(steps) + 1,
                'title': '证书领取',
                'description': '领取进口注册证',
                'duration': '7-15天'
            },
            {
                'step': len(steps) + 1,
                'title': '海关清关',
                'description': '准备海关文件并完成清关',
                'duration': '7-15天'
            }
        ])
        
        return steps
    
    def check_export_compliance(self, product_info: Dict) -> Dict:
        """检查出口合规性"""
        destination = product_info.get('destination_country', '未指定')
        
        export_check = {
            'product_name': product_info.get('product_name', '未指定'),
            'destination_country': destination,
            'export_requirements': self._get_export_requirements(destination),
            'china_export_documents': [
                {'document': '商业发票', 'status': 'required'},
                {'document': '装箱单', 'status': 'required'},
                {'document': '提单', 'status': 'required'},
                {'document': '原产地证明', 'status': 'required'},
                {'document': '出口许可证（如适用）', 'status': 'conditional'},
                {'document': '医疗器械出口销售证明', 'status': 'recommended'}
            ],
            'destination_requirements': self._get_destination_requirements(destination),
            'compliance_status': 'compliant' if product_info.get('has_license', False) else 'pending',
            'recommendations': []
        }
        
        return export_check
    
    def _get_export_requirements(self, country: str) -> List[str]:
        """获取出口要求"""
        # 简化的出口要求映射
        requirements_map = {
            '美国': ['FDA注册', '510(k)或PMA', '出口商注册'],
            '欧盟': ['CE认证', '欧盟授权代表', 'UDI'],
            '日本': ['PMDA注册', '日语标签'],
            '澳大利亚': ['TGA注册'],
            '韩国': ['KFDA注册'],
            '其他': ['当地注册要求', '进口许可证']
        }
        
        return requirements_map.get(country, requirements_map['其他'])
    
    def _get_destination_requirements(self, country: str) -> Dict:
        """获取目的地要求"""
        return {
            'import_license_required': True,
            'local_language_label': True if country in ['日本', '韩国'] else False,
            'local_agent_required': True if country in ['欧盟', '澳大利亚'] else False,
            'additional_certifications': self._get_export_requirements(country)
        }

def main():
    """示例用法"""
    tool = ImportExportCompliance()
    
    # 示例进口产品信息
    import_info = {
        'product_name': '进口心脏起搏器',
        'product_type': 'medical_device',
        'origin_country': '美国',
        'classification': 'Class III',
        'documents': {
            'IM001': 'available',  # 进口医疗器械注册证
            'IM002': 'available',  # 生产企业许可证
            'IM003': 'available',  # 产品技术要求
            'IM004': 'available',  # 注册检验报告
            'IM005': 'available',  # 说明书和标签
            'IM006': 'available',  # 原产地证明
            'IM007': 'available',  # 自由销售证明
            'IM008': 'available',  # CE证书
            'IM009': 'available',  # FDA 510(k)
            'IM010': 'available'   # GMP证书
        },
        'customs_documents': {
            '报关单': 'available',
            '发票': 'available',
            '装箱单': 'available',
            '提单/运单': 'available',
            '原产地证明': 'available',
            '检验检疫证明': 'pending',
            '进口许可证': 'available'
        }
    }
    
    plan = tool.generate_import_plan(import_info)
    print("进口合规计划:")
    print(plan)
    print("\n" + "="*50 + "\n")
    
    # 示例出口检查
    export_info = {
        'product_name': '国产一次性口罩',
        'destination_country': '欧盟',
        'has_license': True
    }
    
    export_check = tool.check_export_compliance(export_info)
    print("出口合规检查:")
    print(json.dumps(export_check, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
