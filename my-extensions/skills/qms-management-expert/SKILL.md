---
name: qms-management-expert
description: Senior QMS Management Expert for comprehensive quality management system design, implementation, documentation control, and continuous improvement. Provides ISO 13485 QMS implementation, document control system design, management review facilitation, design controls, risk management integration, and supplier quality management. Use for QMS establishment, documentation creation, process optimization, quality manual development, procedure standardization, and ISO 13485 certification preparation. Collaborates with QMS audit expert for independent assessment, and regulatory experts (FDA/MDR/NMPA) for market-specific compliance.
license: Proprietary. LICENSE.txt has complete terms
trigger: |
  - 用户要求建立、设计或实施ISO 13485质量管理体系（QMS）
  - 用户提到质量手册编写、程序文件创建或SOP标准化
  - 用户需要建立或优化文件控制系统（DMS）或文档生命周期管理
  - 用户要求准备或开展管理评审会议（management review）
  - 用户提到设计控制（design control）、设计转移或设计变更管理
  - 用户需要风险管理流程整合（ISO 14971）或风险评审
  - 用户要求建立供应商质量管理体系、供应商评估或供应商审核计划
  - 用户提到CAPA流程设计、持续改进或PDCA循环
  - 用户要求建立医疗器械技术文件（MDF）或设计开发档案
  - 用户提到关键质量指标（KQI）监控或QMS绩效仪表板
  - 用户要求创建质量目标或质量方针
do-not-trigger: |
  - 用户要求执行QMS内审、外审、认证审核或编写审计报告（应使用qms-audit-expert）
  - 用户要求处理FDA具体法规合规事务如510(k)、PMA提交或FDA检查准备（应使用fda-regulatory-expert）
  - 用户要求处理欧盟MDR法规合规事务如CE认证、技术文件、公告机构审核（应使用mdr-regulatory-expert）
  - 用户要求处理NMPA具体法规合规事务如医疗器械注册、药品注册、NMPA检查准备（应使用nmpa-regulatory-expert）
  - 用户要求处理非医疗器械行业的质量管理系统
  - 用户要求执行纯编码或软件开发任务
  - 用户要求生成设计开发历史文档DHF（应使用dhf-document-generator）
user-invocable: true
context: inline
tags:
  - QMS管理
  - ISO 13485
  - 质量管理体系
  - 文件控制
  - 设计控制
  - 风险管理
  - 供应商管理
  - 管理评审
  - 医疗器械
  - 持续改进
---

# Senior QMS Management Expert

Expert-level quality management system implementation and maintenance for medical device organizations with comprehensive capabilities in QMS design, documentation control, process optimization, and continuous improvement.

## Core QMS Management Competencies

### 1. ISO 13485 QMS Design and Implementation

Design and implement comprehensive quality management systems aligned with ISO 13485:2016 and regulatory requirements.

**QMS Implementation Workflow:**
```
QMS IMPLEMENTATION FRAMEWORK
├── Phase 1: Assessment and Planning
│   ├── Current state gap analysis
│   ├── ISO 13485 requirement mapping
│   ├── Implementation roadmap development
│   └── Resource allocation and timeline planning
├── Phase 2: QMS Design and Documentation
│   ├── Quality Manual development (Clause 4.2.2)
│   ├── Process documentation and mapping
│   ├── Procedure development (31+ required procedures)
│   └── Work instruction standardization
├── Phase 3: Process Implementation
│   ├── Cross-functional training and competency development
│   ├── Process deployment and monitoring
│   ├── Performance metrics establishment
│   └── Feedback loop integration
└── Phase 4: Verification and Optimization
    ├── Internal audit preparation
    ├── Process effectiveness verification
    ├── Management review execution
    └── Continuous improvement integration
```

**Implementation Planning:**
1. **Current State Assessment**
   - Obtain gap analysis results from QMS Audit Expert
   - Evaluate existing processes against ISO 13485 requirements
   - Identify missing procedures and documentation
   - Assess organizational readiness and capability
   - **Decision Point**: Determine implementation approach (full implementation vs. phased approach)

2. **Implementation Roadmap Development**
   - Prioritize critical QMS elements (quality manual, CAPA, complaints, document control)
   - Establish realistic timeline with milestones
   - Allocate resources and responsibilities
   - Define success criteria and KPIs

### 2. Document Control System (ISO 13485 Clause 4.2.3)

Establish and maintain robust document control processes ensuring compliance and traceability.

**Document Control Framework:**
```
DOCUMENT LIFECYCLE MANAGEMENT
├── Document Creation and Approval
│   ├── Template standardization (use templates/quality-manual-template.md)
│   ├── Review and approval workflow
│   ├── Version control system
│   └── Release authorization
├── Document Distribution and Access
│   ├── Controlled distribution matrix
│   ├── Access permission management
│   ├── Electronic system integration
│   └── External document control
├── Document Maintenance and Updates
│   ├── Periodic review scheduling
│   ├── Change control procedures
│   ├── Impact assessment process
│   └── Superseded document management
└── Document Retention and Disposal
    ├── Retention period definition (minimum device lifetime)
    ├── Archive management system
    ├── Disposal authorization
    └── Legal/regulatory compliance
```

**Document Control Implementation:**
1. **Document Classification System**
   - Establish document type taxonomy (Tier 1-4)
   - Define document numbering scheme
   - Create document hierarchy and relationships
   - Implement version control standards

2. **Electronic Document Management System (DMS)**
   - System requirements definition and vendor selection
   - System configuration and workflow automation
   - User training and competency verification
   - System validation and deployment

3. **Change Control Process**
   - Change request initiation and justification
   - Impact assessment and stakeholder consultation
   - Change review and approval workflow
   - Implementation verification and closure

### 3. Management Review Process (ISO 13485 Clause 5.6)

Facilitate effective management review meetings ensuring systematic QMS evaluation and improvement.

**Management Review Structure:**
- **Review Frequency**: Quarterly meetings with senior leadership (minimum annual per ISO 13485)
- **Input Preparation**: Comprehensive input package covering all ISO 13485 clause 5.6.2 requirements
- **Decision Tracking**: Action item management and follow-up verification
- **Effectiveness Monitoring**: Continuous improvement measurement

**Key Review Inputs:**
- Audit results (internal and external)
- Customer feedback and complaint trends
- Process performance and product conformity data
- Corrective and preventive actions status and effectiveness
- Changes affecting the QMS (organizational, regulatory, product)
- Improvement recommendations and opportunities
- Resource needs and allocation
- Applicable new or revised regulatory requirements

**Management Review Outputs:**
- Decisions and actions for QMS effectiveness improvement
- Product improvements related to customer requirements
- Resource needs and allocation decisions
- Changes necessary to maintain QMS effectiveness
- Quality objectives revision and establishment

### 4. Design Controls (ISO 13485 Clause 7.3)

Implement robust design controls ensuring systematic product development and risk management integration.

**Design Control Stages:**
```
DESIGN CONTROL PROCESS
├── 7.3.1 General
│   ├── Design and development plan
│   ├── Design and development file establishment
│   └── Procedure documentation
├── 7.3.2 Design Planning
│   ├── Design stages definition
│   ├── Review, verification, validation planning
│   ├── Responsibility and authority assignment
│   └── Resource and interface identification
├── 7.3.3 Design Inputs
│   ├── Functional and performance requirements
│   ├── Regulatory requirements and standards
│   ├── Risk management outputs integration
│   └── Input adequacy review and records
├── 7.3.4 Design Outputs
│   ├── Input requirement verification
│   ├── Procurement, production, service information
│   ├── Product acceptance criteria
│   └── Essential characteristics for safe use
├── 7.3.5 Design Review
│   ├── Systematic reviews at suitable stages
│   ├── Requirement evaluation and problem identification
│   ├── Multi-functional representative participation
│   └── Review records and follow-up actions
├── 7.3.6 Design Verification
│   ├── Output meets input requirements verification
│   └── Verification records and follow-up
├── 7.3.7 Design Validation
│   ├── Product meets intended use validation
│   ├── Pre-delivery validation under operating conditions
│   └── Validation records and follow-up
├── 7.3.8 Design Transfer
│   ├── Manufacturing transfer procedures
│   ├── Manufacturing output verification
│   └── Specification appropriateness verification
├── 7.3.9 Design Changes
│   ├── Change identification and documentation
│   ├── Review, verification, validation, approval
│   ├── Effect evaluation on products
│   └── Change records and follow-up
└── 7.3.10 Design Files
    ├── Design and development plan
    ├── Design inputs and outputs
    ├── Design review, verification, validation records
    └── Design change records
```

### 5. Risk Management Integration (ISO 14971)

Ensure seamless integration of risk management processes throughout the QMS and product lifecycle.

**Risk Management Workflow:**
- Risk management planning and file establishment
- Risk analysis (hazard identification, risk estimation)
- Risk evaluation (risk acceptability assessment)
- Risk control implementation and verification
- Production and post-production information analysis
- Risk management file maintenance and review

**Risk Management Integration Points:**
- Design and development (Clause 7.3)
- Purchasing and supplier management (Clause 7.4)
- Production and process control (Clause 7.5)
- Post-market surveillance and feedback (Clause 8.2.1)
- Corrective and preventive action (Clause 8.5)

### 6. Supplier Quality Management (ISO 13485 Clause 7.4)

Establish comprehensive supplier evaluation, selection, and monitoring processes.

**Supplier Management Process:**
```
SUPPLIER QUALITY MANAGEMENT
├── Supplier Qualification
│   ├── Supplier selection criteria
│   ├── Initial evaluation and approval
│   ├── Quality agreement establishment
│   └── Supplier registration and classification
├── Supplier Performance Monitoring
│   ├── Quality performance metrics
│   ├── Delivery performance tracking
│   ├── Corrective action management
│   └── Periodic re-evaluation schedule
├── Supplier Audit Program
│   ├── Risk-based audit scheduling
│   ├── On-site audit execution
│   ├── Audit report and findings
│   └── Corrective action verification
└── Supply Chain Risk Management
    ├── Supplier risk assessment
    ├── Alternate supplier identification
    ├── Contingency planning
    └── Supply chain continuity
```

## QMS Performance Monitoring and Continuous Improvement

### Key Quality Indicators (KQIs)

Monitor these critical quality metrics for QMS effectiveness:

- **QMS Process Performance**: Process cycle times, efficiency metrics, process capability
- **Customer Satisfaction**: Complaint trends, satisfaction surveys, feedback analysis
- **Internal Audit Effectiveness**: Finding trends, closure rates, recurrence prevention
- **CAPA Performance**: Closure timelines, effectiveness measures, root cause analysis quality
- **Training Effectiveness**: Competency assessments, compliance rates, training completion
- **Document Control Performance**: Document cycle times, approval efficiency, revision accuracy
- **Supplier Performance**: Quality ratings, on-time delivery, corrective action responsiveness

### Continuous Improvement Methodology

**PDCA Cycle Integration:**
1. **Plan (P)**
   - Data collection and analysis
   - Root cause analysis using `references/root-cause-analysis-tools.md`
   - Improvement planning and resource allocation
   - Objective setting and measurement criteria

2. **Do (D)**
   - Implementation of improvement actions
   - Pilot testing and validation
   - Training and communication
   - Process modification and optimization

3. **Check (C)**
   - Effectiveness verification and measurement
   - Data analysis and trend evaluation
   - Stakeholder feedback collection
   - Success criteria assessment

4. **Act (A)**
   - Standardization of successful improvements
   - Documentation of process changes
   - Training and communication
   - Identification of new improvement opportunities

## Medical Device File Management (ISO 13485 Clause 4.2.3)

Establish and maintain comprehensive Medical Device Files (MDF) for each device type or family.

**MDF Content Requirements:**
- General description of device and intended use/purpose
- Label and instructions for use specifications
- Product specifications
- Manufacturing specifications
- Procedures for purchasing, manufacturing, and servicing
- Procedures for measuring and monitoring
- Installation requirements (if applicable)
- Risk management file(s)
- Verification and validation information
- Design and development file(s) (if applicable)

**MDF Management Process:**
1. **MDF Establishment**
   - Device type or family identification
   - MDF structure and organization
   - Document collection and compilation
   - Cross-reference and traceability verification

2. **MDF Maintenance**
   - Change control integration
   - Document update synchronization
   - Version control management
   - Periodic review and verification

## Cross-Functional Coordination

### Collaboration with QMS Audit Expert

**Interface Points:**
- QMS establishment provides audit scope and documentation
- Audit findings inform QMS improvement initiatives
- CAPA integration between management and audit functions
- Management review includes audit results and effectiveness

**Collaboration Workflow:**
1. QMS Management Expert establishes QMS framework
2. QMS Audit Expert conducts independent assessment
3. Findings and recommendations shared with QMS Management Expert
4. QMS Management Expert implements corrective actions
5. QMS Audit Expert verifies effectiveness

### Collaboration with Regulatory Experts

**FDA Regulatory Expert Interface:**
- QMS foundation provided for FDA QSR compliance
- FDA-specific requirements integrated into QMS
- FDA submission documentation support
- FDA inspection readiness coordination

**MDR Regulatory Expert Interface:**
- QMS foundation provided for MDR Article 10 compliance
- MDR-specific technical documentation support
- Notified Body audit preparation coordination
- EUDAMED registration support

**NMPA Regulatory Expert Interface:**
- QMS foundation provided for NMPA GMP compliance
- NMPA-specific requirements integrated into QMS
- NMPA registration documentation support
- NMPA inspection readiness coordination

## Resources

### scripts/
- `qms-performance-dashboard.py`: Automated QMS metrics tracking and reporting
- `document-control-audit.py`: Document control compliance verification
- `management-review-prep.py`: Management review input compilation automation
- `capa-tracker.py`: CAPA lifecycle management and effectiveness tracking
- `supplier-performance-monitor.py`: Supplier quality performance tracking and evaluation

### references/
- `iso-13485-requirements.md`: Complete ISO 13485:2016 requirements breakdown (integrated from iso-13485-certification)
- `mandatory-documents.md`: All 31+ required procedures and mandatory documentation (integrated from iso-13485-certification)
- `quality-manual-guide.md`: Quality manual creation guide (integrated from iso-13485-certification)
- `iso13485-procedures.md`: Standard operating procedures templates (integrated from quality-manager-qms-iso13485)
- `design-control-templates.md`: Design control documentation templates (integrated from quality-manager-qms-iso13485)
- `risk-management-integration.md`: ISO 14971 integration guidelines (integrated from quality-manager-qms-iso13485)
- `supplier-qualification-criteria.md`: Supplier assessment frameworks (integrated from quality-manager-qms-iso13485)
- `root-cause-analysis-tools.md`: Problem-solving methodologies (integrated from quality-manager-qms-iso13485)
- `document-control-procedures.md`: Comprehensive document control implementation guide (integrated from quality-documentation-manager)
- `regulatory-documentation-standards.md`: Multi-jurisdictional documentation requirements (integrated from quality-documentation-manager)
- `dms-storage-design.md`: Document management system architecture and design (integrated from quality-documentation-manager)
- `workflow-automation.md`: Document workflow optimization and automation (integrated from quality-documentation-manager)
- `21cfr11-compliance-guide.md`: Electronic signature and record compliance framework (integrated from quality-documentation-manager)

### assets/templates/
- `quality-manual-template.md`: Complete quality manual template (integrated from iso-13485-certification)
- `procedures/CAPA-procedure-template.md`: CAPA procedure template (integrated from iso-13485-certification)
- `procedures/document-control-procedure-template.md`: Document control procedure template (integrated from iso-13485-certification)
- `procedures/complaint-handling-procedure-template.md`: Complaint handling procedure template
- `procedures/internal-audit-procedure-template.md`: Internal audit procedure template
- `procedures/management-review-procedure-template.md`: Management review procedure template
- `procedures/risk-management-procedure-template.md`: Risk management procedure template
- `procedures/supplier-qualification-procedure-template.md`: Supplier qualification procedure template
- `work-instructions/`: Work instruction templates for various QMS processes
- `forms/`: QMS forms and checklists (CAPA forms, audit checklists, etc.)

### assets/
- `qms-templates/`: Quality manual, procedure, and work instruction templates (integrated from quality-manager-qms-iso13485)
- `audit-forms/`: Internal audit report and checklist templates (integrated from quality-manager-qms-iso13485)
- `training-materials/`: ISO 13485 training presentations and materials (integrated from quality-manager-qms-iso13485)
- `process-flowcharts/`: Visual process documentation templates (integrated from quality-manager-qms-iso13485)
- `document-templates/`: Standardized document templates and formats (integrated from quality-documentation-manager)
- `change-control-forms/`: Change request and approval documentation templates (integrated from quality-documentation-manager)
- `training-materials/`: Document management training and competency programs (integrated from quality-documentation-manager)
- `audit-checklists/`: Document control compliance verification checklists (integrated from quality-documentation-manager)

## Typical Use Cases

### Use Case 1: QMS Implementation from Scratch

**User Request:** "We are a medical device startup. Help us implement ISO 13485 QMS."

**Workflow:**
1. Obtain gap analysis results from QMS Audit Expert
2. Develop implementation roadmap and timeline
4. Create quality manual using `assets/templates/quality-manual-template.md`
5. Develop required procedures using procedure templates
6. Establish document control system
7. Implement processes and train personnel
8. Conduct internal audits and management reviews
9. Prepare for certification audit

### Use Case 2: QMS Documentation Creation

**User Request:** "Help me create a CAPA procedure."

**Workflow:**
1. Review ISO 13485 Clause 8.5.2 and 8.5.3 requirements from `references/iso-13485-requirements.md`
2. Use `assets/templates/procedures/CAPA-procedure-template.md` as starting point
3. Customize based on organizational processes
4. Integrate with complaint handling and internal audit processes
5. Establish CAPA effectiveness verification criteria

### Use Case 3: Document Control System Implementation

**User Request:** "We need to implement an electronic document management system."

**Workflow:**
1. Assess current document control processes using `references/document-control-procedures.md`
2. Define DMS requirements using `references/dms-storage-design.md`
3. Evaluate DMS vendors and select appropriate solution
4. Configure system workflows using `references/workflow-automation.md`
5. Ensure 21 CFR Part 11 compliance using `references/21cfr11-compliance-guide.md`
6. Implement user training and validation
7. Monitor system performance using `scripts/document-control-audit.py`

### Use Case 4: Management Review Preparation

**User Request:** "Prepare for our quarterly management review meeting."

**Workflow:**
1. Use `scripts/management-review-prep.py` to compile required inputs
2. Gather audit results and findings
3. Compile customer feedback and complaint data
4. Analyze process performance and product conformity
5. Review CAPA status and effectiveness
6. Identify changes affecting QMS
7. Prepare improvement recommendations
8. Generate management review input package

### Use Case 5: Continuous Improvement Initiative

**User Request:** "Our CAPA closure rate is low. Help us improve."

**Workflow:**
1. Analyze CAPA performance data using `scripts/qms-performance-dashboard.py`
2. Identify root causes of delays using `references/root-cause-analysis-tools.md`
3. Review CAPA procedure effectiveness
4. Implement process improvements
5. Train personnel on improved processes
6. Monitor effectiveness and adjust as needed
7. Document improvements in management review

## Integration with Other Skills

### QMS Audit Expert Collaboration

**When to Collaborate:**
- After QMS implementation for independent assessment
- For internal audit planning and execution
- For audit finding resolution and CAPA verification
- For certification audit preparation

**Collaboration Example:**
```
User: "We've implemented our QMS. Now we need to prepare for ISO 13485 certification."

QMS Management Expert:
1. Verify QMS completeness using gap analysis
2. Ensure all required procedures are documented
3. Verify document control system effectiveness
4. Prepare management review records

QMS Audit Expert:
1. Conduct comprehensive internal audit
2. Identify nonconformities and improvement opportunities
3. Verify CAPA system effectiveness
4. Provide audit findings to QMS Management Expert

QMS Management Expert:
1. Implement corrective actions
2. Close nonconformities
3. Prepare for certification audit
```

### FDA Regulatory Expert Collaboration

**When to Collaborate:**
- For FDA QSR compliance assessment
- For FDA submission preparation
- For FDA inspection readiness
- For FDA QMSR transition planning

**Collaboration Example:**
```
User: "We need to prepare for FDA 510(k) submission."

QMS Management Expert:
1. Provide QMS documentation foundation
2. Ensure document control system meets requirements
3. Verify CAPA and complaint handling processes
4. Prepare quality system records

FDA Regulatory Expert:
1. Identify FDA-specific requirements
3. Prepare 510(k) submission documentation
4. Coordinate with QMS Management Expert for QMS alignment
```

### MDR Regulatory Expert Collaboration

**When to Collaborate:**
- For MDR Article 10 compliance verification
- For technical documentation preparation
- For Notified Body audit preparation
- For EUDAMED registration support

**Collaboration Example:**
```
User: "We need CE marking for our medical device."

QMS Management Expert:
1. Ensure QMS meets ISO 13485 requirements
2. Establish document control for technical documentation
3. Implement post-market surveillance processes
4. Prepare management review records

MDR Regulatory Expert:
1. Conduct MDR classification
2. Prepare Annex II technical documentation
3. Coordinate clinical evidence requirements
4. Prepare for Notified Body audit
```

### NMPA Regulatory Expert Collaboration

**When to Collaborate:**
- For NMPA GMP compliance verification
- For NMPA registration documentation preparation
- For NMPA inspection readiness
- For Chinese market access support

**Collaboration Example:**
```
User: "We need NMPA registration for our medical device."

QMS Management Expert:
1. Ensure QMS meets NMPA GMP requirements
2. Establish document control for NMPA registration documentation
3. Implement post-market surveillance processes
4. Prepare management review records

NMPA Regulatory Expert:
1. Conduct NMPA classification
2. Prepare NMPA registration documentation
3. Coordinate clinical evidence requirements
4. Prepare for NMPA inspection
```

## Best Practices

### QMS Implementation Best Practices

1. **Start with Quality Policy and Objectives**
   - Establish clear quality policy signed by top management
   - Define measurable quality objectives
   - Communicate throughout organization

2. **Use Risk-Based Approach**
   - Prioritize critical processes and documentation
   - Focus resources on high-risk areas
   - Integrate risk management throughout QMS

3. **Engage Stakeholders Early**
   - Involve cross-functional teams in QMS design
   - Ensure buy-in from all levels
   - Provide comprehensive training

4. **Document What You Do, Do What You Document**
   - Ensure procedures reflect actual processes
   - Avoid over-documentation
   - Maintain practical and usable documentation

5. **Focus on Process Effectiveness**
   - Monitor process performance metrics
   - Conduct regular management reviews
   - Implement continuous improvement

### Document Control Best Practices

1. **Establish Clear Document Hierarchy**
   - Tier 1: Quality Manual
   - Tier 2: Procedures
   - Tier 3: Work Instructions
   - Tier 4: Records and Forms

2. **Implement Robust Version Control**
   - Use consistent version numbering
   - Maintain revision history
   - Control distribution of current versions

3. **Ensure Document Accessibility**
   - Make current documents available at point of use
   - Implement electronic document management
   - Train personnel on document access

4. **Maintain Document Integrity**
   - Control document changes through formal process
   - Prevent unauthorized modifications
   - Ensure document accuracy and completeness

### Management Review Best Practices

1. **Prepare Comprehensive Input Package**
   - Include all ISO 13485 required inputs
   - Provide data-driven analysis
   - Include trend analysis and metrics

2. **Focus on Decision Making**
   - Make clear decisions on QMS effectiveness
   - Assign action items with responsibilities
   - Establish timelines and follow-up

3. **Document Review Outputs**
   - Maintain records of decisions and actions
   - Track action item completion
   - Verify effectiveness of actions

4. **Review Frequency**
   - Conduct management reviews at least annually
   - Consider quarterly reviews for better oversight
   - Schedule additional reviews for significant changes

## Common Pitfalls and How to Avoid Them

### Pitfall 1: Over-Documentation

**Problem:** Creating excessive documentation that is not practical or usable.

**Solution:**
- Focus on required procedures and essential documentation
- Use templates to ensure completeness without overkill
- Regularly review and streamline documentation
- Ensure documentation reflects actual processes

### Pitfall 2: Lack of Management Commitment

**Problem:** QMS implementation fails due to insufficient top management support.

**Solution:**
- Ensure top management signs quality policy
- Include management in QMS design and implementation
- Provide regular management review updates
- Demonstrate QMS value through metrics and improvements

### Pitfall 3: Ineffective Training

**Problem:** Personnel not adequately trained on QMS processes.

**Solution:**
- Develop comprehensive training programs
- Assess training effectiveness
- Provide ongoing training and refresher courses
- Document training records

### Pitfall 4: Ignoring Process Effectiveness

**Problem:** Focus on documentation rather than process performance.

**Solution:**
- Establish process performance metrics
- Monitor and analyze process data
- Conduct regular process reviews
- Implement continuous improvement initiatives

### Pitfall 5: Poor Document Control

**Problem:** Document control system ineffective, leading to nonconformities.

**Solution:**
- Implement robust document control procedures
- Use electronic document management system
- Train personnel on document control requirements
- Conduct regular document control audits

## Resources for Further Learning

### Standards and Regulations

- ISO 13485:2016 - Medical devices — Quality management systems
- ISO 14971 - Medical devices — Application of risk management
- FDA 21 CFR Part 820 - Quality System Regulation (QMSR)
- EU MDR 2017/745 - Medical Devices Regulation

### Industry Guidance

- MDCG guidance documents (EU)
- FDA guidance documents (US)
- IMDRF documents (International)
- Industry best practices and case studies

### Training and Certification

- ISO 13485 lead auditor training
- Quality management training programs
- Regulatory affairs certification
- Professional development courses

---

**Note:** This skill provides comprehensive QMS management expertise and collaborates with QMS audit expert, FDA regulatory expert, MDR regulatory expert, and NMPA regulatory expert for complete quality and regulatory compliance support.