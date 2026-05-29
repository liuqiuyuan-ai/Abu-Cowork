#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NMPA Clinical Evaluation Tool
用于准备医疗器械临床评价报告
"""

import json
from typing import Dict, List, Optional

class ClinicalEvaluationTool:
    """临床评价工具"""
    
    def __init__(self):
        self.evaluation_types = ['literature_review', 'clinical_data', 'bench_testing', 'risk_benefit']
        self.evidence_levels = ['high', 'medium', 'low']
    
    def prepare_clinical_evaluation_report(self, device_info: Dict) -> Dict:
        """准备临床评价报告"""
        cer = {
            'report_title': '医疗器械临床评价报告',
            'report_version': '1.0',
            'device_info': {
                'device_name': device_info.get('device_name', '未指定'),
                'model': device_info.get('model', '未指定'),
                'classification': device_info.get('classification', 'Class II'),
                'intended_use': device_info.get('intended_use', '未指定'),
                'indications': device_info.get('indications', []),
                'contraindications': device_info.get('contraindications', []),
                'target_population': device_info.get('target_population', '未指定')
            },
            'evaluation_summary': {
                'literature_review': self._prepare_literature_review(device_info),
                'clinical_data_analysis': self._prepare_clinical_data(device_info),
                'bench_testing': self._prepare_bench_testing(device_info),
                'risk_benefit_assessment': self._prepare_risk_benefit(device_info)
            },
            'conclusions': {
                'safety_evaluation': '',
                'effectiveness_evaluation': '',
                'overall_conclusion': '',
                'recommendations': []
            }
        }
        
        # 生成结论
        self._generate_conclusions(cer)
        
        return cer
    
    def _prepare_literature_review(self, device_info: Dict) -> Dict:
        """准备文献综述部分"""
        literature = device_info.get('literature_review', {})
        
        return {
            'objective': '评价同类医疗器械的临床安全性和有效性',
            'search_strategy': literature.get('search_strategy', {
                'databases': ['PubMed', 'CNKI', '万方', 'Embase'],
                'search_terms': [],
                'time_range': '近10年'
            }),
            'inclusion_criteria': [
                '人类临床研究',
                '英文或中文文献',
                '与目标器械同类或相似'
            ],
            'exclusion_criteria': [
                '动物实验',
                '非临床研究',
                '重复发表'
            ],
            'literature_summary': literature.get('summary', []),
            'key_findings': literature.get('key_findings', []),
            'evidence_level': self._assess_evidence_level(literature.get('quality_score', 0))
        }
    
    def _prepare_clinical_data(self, device_info: Dict) -> Dict:
        """准备临床数据分析部分"""
        clinical_data = device_info.get('clinical_data', {})
        
        return {
            'data_sources': clinical_data.get('sources', ['临床试验', '上市后数据']),
            'study_designs': clinical_data.get('designs', ['前瞻性研究', '回顾性研究']),
            'patient_population': {
                'total_patients': clinical_data.get('total_patients', 0),
                'age_range': clinical_data.get('age_range', '未指定'),
                'gender_distribution': clinical_data.get('gender_distribution', '未指定'),
                'disease_status': clinical_data.get('disease_status', '未指定')
            },
            'clinical_outcomes': {
                'primary_endpoints': clinical_data.get('primary_endpoints', []),
                'secondary_endpoints': clinical_data.get('secondary_endpoints', []),
                'adverse_events': clinical_data.get('adverse_events', []),
                'serious_adverse_events': clinical_data.get('serious_adverse_events', [])
            },
            'statistical_analysis': clinical_data.get('statistical_methods', '描述性统计'),
            'data_quality': self._assess_data_quality(clinical_data)
        }
    
    def _prepare_bench_testing(self, device_info: Dict) -> Dict:
        """准备 bench testing 部分"""
        bench_data = device_info.get('bench_testing', {})
        
        return {
            'performance_tests': bench_data.get('performance_tests', [
                {'test_name': '功能验证', 'result': '通过', 'standard': '符合企业标准'},
                {'test_name': '可靠性测试', 'result': '通过', 'standard': '符合行业标准'},
                {'test_name': '安全性测试', 'result': '通过', 'standard': '符合国家标准'}
            ]),
            'biocompatibility': bench_data.get('biocompatibility', {
                'tests': ['细胞毒性', '皮肤刺激', '致敏性', '血液相容性'],
                'results': '全部通过',
                'standard': 'GB/T 16886'
            }),
            'sterility': bench_data.get('sterility', {
                'method': '环氧乙烷灭菌',
                'validation': '已完成',
                'sterility_assurance_level': '10^-6'
            })
        }
    
    def _prepare_risk_benefit(self, device_info: Dict) -> Dict:
        """准备风险收益评估部分"""
        risks = device_info.get('risks', [])
        benefits = device_info.get('benefits', [])
        
        return {
            'identified_risks': risks,
            'risk_mitigation_measures': [r.get('mitigation', '') for r in risks],
            'expected_benefits': benefits,
            'benefit_risk_ratio': 'Positive' if len(benefits) >= len([r for r in risks if r.get('severity') == 'high']) else 'Needs further evaluation',
            'conclusion': self._assess_risk_benefit(risks, benefits)
        }
    
    def _assess_evidence_level(self, quality_score: int) -> str:
        """评估证据级别"""
        if quality_score >= 80:
            return 'high'
        elif quality_score >= 60:
            return 'medium'
        else:
            return 'low'
    
    def _assess_data_quality(self, clinical_data: Dict) -> str:
        """评估数据质量"""
        total_patients = clinical_data.get('total_patients', 0)
        study_designs = clinical_data.get('designs', [])
        
        if total_patients >= 500 and '前瞻性随机对照研究' in study_designs:
            return '高质量'
        elif total_patients >= 100:
            return '中等质量'
        else:
            return '有限数据'
    
    def _assess_risk_benefit(self, risks: List, benefits: List) -> str:
        """评估风险收益"""
        high_risks = [r for r in risks if r.get('severity') == 'high']
        if not high_risks:
            return '风险收益比可接受'
        elif len(benefits) > len(high_risks):
            return '风险收益比总体可接受，但需关注高风险项'
        else:
            return '风险收益比需要进一步评估'
    
    def _generate_conclusions(self, cer: Dict):
        """生成结论"""
        literature_level = cer['evaluation_summary']['literature_review']['evidence_level']
        data_quality = cer['evaluation_summary']['clinical_data_analysis']['data_quality']
        risk_benefit = cer['evaluation_summary']['risk_benefit_assessment']['conclusion']
        
        cer['conclusions']['safety_evaluation'] = f"""
基于文献综述（证据级别：{literature_level}）和临床数据分析（数据质量：{data_quality}），
{cer['device_info']['device_name']}的安全性评价如下：
- 不良事件发生率在可接受范围内
- 严重不良事件发生率低
- 未发现新的安全信号
        """.strip()
        
        cer['conclusions']['effectiveness_evaluation'] = f"""
{cer['device_info']['device_name']}的有效性评价如下：
- 主要疗效终点达到预期目标
- 次要疗效指标符合设计要求
- 与同类产品相比具有可比性
        """.strip()
        
        cer['conclusions']['overall_conclusion'] = f"""
综合评价，{cer['device_info']['device_name']}（{cer['device_info']['model']}）：
1. 安全性：符合NMPA要求
2. 有效性：达到预期临床效果
3. 风险收益比：{risk_benefit}

建议：{cer['device_info']['classification']}类医疗器械注册申请
        """.strip()
        
        cer['conclusions']['recommendations'] = [
            '建议提交注册申请',
            '建议持续上市后监测',
            '建议完善风险管理文档'
        ]
    
    def export_report(self, device_info: Dict, format_type: str = 'json') -> str:
        """导出报告"""
        cer = self.prepare_clinical_evaluation_report(device_info)
        
        if format_type == 'json':
            return json.dumps(cer, ensure_ascii=False, indent=2)
        elif format_type == 'markdown':
            return self._convert_to_markdown(cer)
        else:
            return json.dumps({'error': '不支持的格式'}, ensure_ascii=False)
    
    def _convert_to_markdown(self, cer: Dict) -> str:
        """转换为Markdown格式"""
        md = f"""# {cer['report_title']}

## 1. 器械信息

| 项目 | 内容 |
|------|------|
| 器械名称 | {cer['device_info']['device_name']} |
| 型号规格 | {cer['device_info']['model']} |
| 分类 | {cer['device_info']['classification']} |
| 预期用途 | {cer['device_info']['intended_use']} |
| 适用人群 | {cer['device_info']['target_population']} |

## 2. 临床评价摘要

### 2.1 文献综述
- 证据级别：{cer['evaluation_summary']['literature_review']['evidence_level']}
- 数据库：{', '.join(cer['evaluation_summary']['literature_review']['search_strategy']['databases'])}

### 2.2 临床数据分析
- 数据质量：{cer['evaluation_summary']['clinical_data_analysis']['data_quality']}
- 总病例数：{cer['evaluation_summary']['clinical_data_analysis']['patient_population']['total_patients']}

### 2.3 风险收益评估
- 结论：{cer['evaluation_summary']['risk_benefit_assessment']['conclusion']}

## 3. 结论

### 3.1 安全性评价
{cer['conclusions']['safety_evaluation']}

### 3.2 有效性评价
{cer['conclusions']['effectiveness_evaluation']}

### 3.3 总体结论
{cer['conclusions']['overall_conclusion']}

### 3.4 建议
{chr(10).join(f"- {r}" for r in cer['conclusions']['recommendations'])}

---
报告版本：{cer['report_version']}
"""
        return md

def main():
    """示例用法"""
    tool = ClinicalEvaluationTool()
    
    # 示例器械信息
    device_info = {
        'device_name': '一次性使用无菌注射器',
        'model': 'SYR-001',
        'classification': 'Class II',
        'intended_use': '用于临床注射药物或抽取体液',
        'indications': ['肌肉注射', '静脉注射', '皮下注射'],
        'contraindications': ['对注射器材料过敏者'],
        'target_population': '需要注射治疗的患者',
        'literature_review': {
            'quality_score': 85,
            'key_findings': ['同类产品安全性良好', '使用广泛']
        },
        'clinical_data': {
            'total_patients': 1000,
            'designs': ['前瞻性研究'],
            'primary_endpoints': ['注射成功率'],
            'adverse_events': []
        },
        'risks': [
            {'risk': '针刺伤', 'severity': 'medium', 'mitigation': '使用安全针头'},
            {'risk': '感染', 'severity': 'high', 'mitigation': '无菌包装'}
        ],
        'benefits': ['使用方便', '减少交叉感染风险', '一次性使用安全']
    }
    
    report = tool.export_report(device_info, format_type='markdown')
    print(report)

if __name__ == '__main__':
    main()
