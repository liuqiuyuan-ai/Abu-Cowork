#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NMPA Regulatory Pathway Analyzer
用于分析医疗器械和药品的NMPA注册路径
"""

import json
from typing import Dict, List, Optional

class NMPAPathwayAnalyzer:
    """NMPA监管路径分析器"""
    
    def __init__(self):
        self.classification_rules = {
            'medical_device': {
                'class_i': ['低风险', '非侵入性', '简单结构'],
                'class_ii': ['中等风险', '侵入性短期', '诊断功能'],
                'class_iii': ['高风险', '植入式', '生命支持']
            },
            'pharmaceutical': {
                'new_drug': ['未在中国上市', '新化学实体', '新适应症'],
                'generic': ['已上市仿制药', '生物等效性'],
                'import': ['境外生产', '首次进口']
            },
            'ivd': {
                'class_i': ['低风险', '目视检查', '简单试剂'],
                'class_ii': ['中等风险', '核酸检测', '自动化分析'],
                'class_iii': ['高风险', '基因检测', '伴随诊断']
            }
        }
    
    def analyze_device_classification(self, product_info: Dict) -> Dict:
        """分析医疗器械分类"""
        analysis = {
            'product_type': 'medical_device',
            'classification': None,
            'reasoning': [],
            'registration_path': None,
            'estimated_timeline': None,
            'requirements': []
        }
        
        risk_level = product_info.get('risk_level', 'medium')
        is_invasive = product_info.get('is_invasive', False)
        is_implantable = product_info.get('is_implantable', False)
        
        if is_implantable or risk_level == 'high':
            analysis['classification'] = 'Class III'
            analysis['registration_path'] = '国家药品监督管理局审查'
            analysis['estimated_timeline'] = '180-365天'
            analysis['reasoning'].append('高风险或植入式设备需国家层面审查')
            analysis['requirements'] = [
                '完整技术文档',
                '临床评价报告',
                'GMP认证',
                '注册检验报告'
            ]
        elif is_invasive or risk_level == 'medium':
            analysis['classification'] = 'Class II'
            analysis['registration_path'] = '省级药品监督管理局审查'
            analysis['estimated_timeline'] = '90-180天'
            analysis['reasoning'].append('中等风险或侵入性设备需省级审查')
            analysis['requirements'] = [
                '技术文档',
                '临床评价报告',
                '注册检验报告'
            ]
        else:
            analysis['classification'] = 'Class I'
            analysis['registration_path'] = '备案'
            analysis['estimated_timeline'] = '30-60天'
            analysis['reasoning'].append('低风险非侵入性设备只需备案')
            analysis['requirements'] = [
                '产品备案表',
                '产品技术要求',
                '符合性声明'
            ]
        
        return analysis
    
    def analyze_pharmaceutical_pathway(self, product_info: Dict) -> Dict:
        """分析药品注册路径"""
        analysis = {
            'product_type': 'pharmaceutical',
            'pathway': None,
            'reasoning': [],
            'estimated_timeline': None,
            'requirements': []
        }
        
        is_new_drug = product_info.get('is_new_drug', False)
        is_import = product_info.get('is_import', False)
        is_generic = product_info.get('is_generic', False)
        
        if is_new_drug:
            analysis['pathway'] = '新药申请 (NDA)'
            analysis['estimated_timeline'] = '365-730天'
            analysis['reasoning'].append('新化学实体或新适应症需完整临床试验')
            analysis['requirements'] = [
                '临床前研究数据',
                'Phase I/II/III临床试验',
                '药学研究资料',
                'GMP符合性证明'
            ]
        elif is_generic:
            analysis['pathway'] = '仿制药申请 (ANDA)'
            analysis['estimated_timeline'] = '180-365天'
            analysis['reasoning'].append('仿制药需证明生物等效性')
            analysis['requirements'] = [
                '生物等效性研究',
                '药学等效性资料',
                'GMP符合性证明',
                '参比制剂信息'
            ]
        elif is_import:
            analysis['pathway'] = '进口药品申请'
            analysis['estimated_timeline'] = '180-365天'
            analysis['reasoning'].append('进口药品需额外的境外生产现场检查')
            analysis['requirements'] = [
                '原产地证明',
                '境外生产企业GMP证明',
                '进口药品注册检验',
                '中文说明书'
            ]
        
        return analysis
    
    def analyze_ivd_classification(self, product_info: Dict) -> Dict:
        """分析IVD分类"""
        analysis = {
            'product_type': 'ivd',
            'classification': None,
            'reasoning': [],
            'registration_path': None,
            'estimated_timeline': None,
            'requirements': []
        }
        
        risk_level = product_info.get('risk_level', 'medium')
        test_complexity = product_info.get('test_complexity', 'simple')
        
        if risk_level == 'high' or test_complexity == 'high':
            analysis['classification'] = 'Class III'
            analysis['registration_path'] = '国家药品监督管理局审查'
            analysis['estimated_timeline'] = '180-365天'
            analysis['reasoning'].append('高风险或复杂检测需国家审查')
            analysis['requirements'] = [
                '临床性能评价',
                '注册检验',
                'GMP认证',
                '风险管理文档'
            ]
        elif risk_level == 'medium' or test_complexity == 'medium':
            analysis['classification'] = 'Class II'
            analysis['registration_path'] = '技术审查'
            analysis['estimated_timeline'] = '90-180天'
            analysis['reasoning'].append('中等风险检测需技术审查')
            analysis['requirements'] = [
                '性能验证数据',
                '注册检验',
                '临床评价'
            ]
        else:
            analysis['classification'] = 'Class I'
            analysis['registration_path'] = '备案'
            analysis['estimated_timeline'] = '30-60天'
            analysis['reasoning'].append('低风险简单检测只需备案')
            analysis['requirements'] = [
                '产品备案表',
                '性能指标',
                '符合性声明'
            ]
        
        return analysis
    
    def generate_pathway_report(self, product_info: Dict) -> str:
        """生成完整的路径分析报告"""
        product_type = product_info.get('product_type', 'medical_device')
        
        if product_type == 'medical_device':
            result = self.analyze_device_classification(product_info)
        elif product_type == 'pharmaceutical':
            result = self.analyze_pharmaceutical_pathway(product_info)
        elif product_type == 'ivd':
            result = self.analyze_ivd_classification(product_info)
        else:
            return json.dumps({'error': '未知产品类型'}, ensure_ascii=False, indent=2)
        
        report = {
            'product_name': product_info.get('product_name', '未指定'),
            'analysis_date': '2026-05-28',
            'pathway_analysis': result
        }
        
        return json.dumps(report, ensure_ascii=False, indent=2)

def main():
    """示例用法"""
    analyzer = NMPAPathwayAnalyzer()
    
    # 示例：分析医疗器械
    device_info = {
        'product_name': '植入式心脏起搏器',
        'product_type': 'medical_device',
        'risk_level': 'high',
        'is_invasive': True,
        'is_implantable': True
    }
    
    report = analyzer.generate_pathway_report(device_info)
    print("医疗器械路径分析报告:")
    print(report)
    print("\n" + "="*50 + "\n")
    
    # 示例：分析药品
    drug_info = {
        'product_name': '新型抗生素',
        'product_type': 'pharmaceutical',
        'is_new_drug': True,
        'is_import': False
    }
    
    report = analyzer.generate_pathway_report(drug_info)
    print("药品路径分析报告:")
    print(report)

if __name__ == '__main__':
    main()
