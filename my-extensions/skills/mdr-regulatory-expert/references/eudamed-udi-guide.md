# EUDAMED and UDI Guide

This guide provides comprehensive guidance on the Unique Device Identification system and EUDAMED database under EU MDR 2017/745.

## Table of Contents

1. [UDI System Overview](#udi-system-overview)
2. [UDI Structure](#udi-structure)
3. [UDI Assignment](#udi-assignment)
4. [UDI Labeling Requirements](#udi-labeling-requirements)
5. [EUDAMED Overview](#eudamed-overview)
6. [EUDAMED Registration](#eudamed-registration)

## UDI System Overview

### Purpose
The UDI system aims to:
- Enable identification of medical devices
- Facilitate traceability
- Improve adverse event reporting
- Support post-market surveillance
- Combat counterfeiting

### Legal Basis
- Article 27: UDI system
- Article 29: UDI database
- Article 123(3)(d): Registration
- Commission Delegated Regulation 2017/1430

### Implementation Timeline
- Class III and IIb: May 2023 (extended)
- Class IIa and Is/Im/Ir: May 2025 (extended)
- Class I: May 2027 (extended)

## UDI Structure

### UDI Components

#### UDI-DI (Device Identifier)
- Unique to device model/variant
- Links to device information in EUDAMED
- Static information
- Required for all devices

#### UDI-PI (Production Identifier)
- Identifies production unit
- May include:
  - Lot or batch number (L)
  - Serial number (S)
  - Manufacturing date (M)
  - Expiration date (E)
  - Date of application (D)

### UDI Format
- Based on international standards
- AIDC format (barcode, RFID)
- HRI format (human-readable)

### Issuing Entities
- GS1
- HIBCC
- ICCBBA

## UDI Assignment

### Step 1: Determine Basic UDI-DI
- Groups devices with same:
  - Intended purpose
  - Design and manufacturing
  - Risk class
  - Basic UDI-DI structure

### Step 2: Assign UDI-DIs
- Unique DI for each:
  - Device model
  - Device size
  - Device variant
  - Packaging configuration

### Step 3: Assign UDI-PIs
- Per production batch/serial
- Based on device class
- Required PI types per risk class

### Basic UDI-DI vs. UDI-DI

| Aspect | Basic UDI-DI | UDI-DI |
|--------|---------------|--------|
| Level | Device model | Specific device variant |
| Uniqueness | Groups similar devices | Unique to variant |
| EUDAMED | Links to device data | Registered separately |
| Use | Technical documentation | Traceability |

### UDI Assignment Workflow

```
1. Identify device family
   ↓
2. Determine Basic UDI-DI structure
   ↓
3. Assign Basic UDI-DI
   ↓
4. Identify device variants
   ↓
5. Assign UDI-DIs for variants
   ↓
6. Assign UDI-PIs for production
   ↓
7. Update technical documentation
   ↓
8. Implement labeling
```

## UDI Labeling Requirements

### Where UDI Must Appear
- Device label
- All higher-level packaging
- In case of Class III/IIb: every sales unit

### Labeling Format
- AIDC format: Required
- HRI format: Required on device label
- Placement: Readable at point of use

### UDI Carrier
- Barcode (1D or 2D)
- RFID (for higher risk devices)
- Must be scannable

### Information Requirements
- UDI-DI readable
- UDI-PI readable
- Production information

### Language Requirements
- HRI in official EU language(s)
- Translations required

## EUDAMED Overview

### Purpose
European Database on Medical Devices:
- Central repository for device information
- Enhanced transparency
- Improved coordination
- Facilitated market surveillance

### Modules
1. **Actor Registration**: Manufacturers, ARs, importers, distributors
2. **Device Registration**: UDI-DI and device information
3. **Certificate Management**: NB certificates
4. **Vigilance and Surveillance**: Serious incidents, FSCAs
5. **Clinical Investigation**: Clinical study registration

### Registration Timeline
- Actor registration: Mandatory when EUDAMED available
- Device registration: Per device class timeline
- Certificate registration: Upon certificate issuance
- Vigilance reporting: Upon system availability

### Current Status
- Module by module implementation
- Actor registration active
- Other modules being deployed

## EUDAMED Registration

### Actor Registration

#### Who Must Register
- Manufacturers
- Authorized Representatives
- Importers
- Distributors (in some cases)

#### Information Required
- Organization name and address
- Contact details
- Legal representative
- Economic operator type
- SRN (Single Registration Number)

### Device Registration

#### Information Required
- Basic UDI-DI
- UDI-DI
- Device classification
- Device description
- GMDN code
- Manufacturer details
- Authorized Representative details
- Manufacturing information

### Certificate Registration

#### Information Required
- Certificate number
- Certificate type
- Scope
- Holder
- Issuing Notified Body
- Validity dates

### Vigilance Reporting

#### What to Report
- Serious incidents
- FSCAs
- Trend reports

#### How to Report
- Via EUDAMED system
- Standardized forms
- Within timelines

## UDI/EUDAMED Implementation Checklist

### Phase 1: Planning
- [ ] Understand UDI requirements
- [ ] Determine issuing entity
- [ ] Plan Basic UDI-DI structure
- [ ] Assess labeling systems

### Phase 2: Implementation
- [ ] Obtain UDI codes
- [ ] Update labeling systems
- [ ] Implement UDI database
- [ ] Train personnel

### Phase 3: Integration
- [ ] Integrate UDI into QMS
- [ ] Update traceability procedures
- [ ] Connect to EUDAMED
- [ ] Validate processes

### Phase 4: Maintenance
- [ ] Monitor compliance
- [ ] Update as devices change
- [ ] Keep EUDAMED current
- [ ] Respond to queries

## Common Challenges

### Top Implementation Issues

1. **System Integration**
   - ERP/MES integration
   - Labeling system updates
   - Database connections

2. **Labeling Changes**
   - Label redesign
   - Printing capabilities
   - Packaging updates

3. **Process Changes**
   - Traceability procedures
   - Quality records
   - Training requirements

4. **EUDAMED Preparation**
   - Understanding requirements
   - Data quality
   - Registration timing

### Best Practices

1. **Start Early**
   - Plan ahead of timelines
   - Allow time for changes

2. **Engage Stakeholders**
   - Quality, Regulatory, IT, Operations
   - External partners

3. **Test Thoroughly**
   - Validate UDI assignment
   - Test labeling
   - Verify EUDAMED registration

4. **Maintain Data Quality**
   - Accurate device information
   - Current registrations
   - Complete documentation