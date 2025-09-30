# Table Name: CAMPAIGN_VISA

## Table Description
Campaign-level advertising performance data showing impressions, clicks, CTR/VTR metrics and completed video views broken down by market, channel, site, media buy, format and targeting attributes. The table contains campaign identifiers and descriptive metadata (market, channel, site_name, media_buy_name, primary_target, target_type) plus engagement and performance measures (impressions, clicks, ctr_tm_version, completed_video_views, vtr_tm_version) and is used to monitor and optimize media delivery, creative formats, and audience targeting — suitable for audience generation and segmentation. | :ui-name:Campaign Visa Performance: :short-name:camp_visa: |<

## Data Dictionary

### Fields:

- `market` (STRING): Two-letter market or country code indicating the geographic market for the campaign (e.g., FR). Business purpose: used to group, filter and roll up performance and targeting by geography. | :upper: :all-unique-vals: |<
- `channel` (STRING): High-level advertising channel used to deliver the campaign (e.g., Programmatic, Digital Display). Business purpose: categorizes spend and performance by channel type for planning and analysis. | :lower: |<
- `site_name` (STRING): Publisher or platform name where ads ran (e.g., The Trade Desk, Adara). Business purpose: identifies the inventory/source for performance attribution and vendor analysis.
- `primary_target` (STRING): Primary audience or targeting strategy label for the line item (e.g., Demographic). Business purpose: indicates the main targeting segment used for campaign delivery to analyze audience performance. | :lower: |<
- `media_buy_name` (STRING): Descriptive media buy or line-item name for the campaign insertion order. Business purpose: uniquely identifies the specific buy/configuration for tracking, reconciliation and optimization. | :upper: |<
- `target_type` (STRING): Secondary or detailed targeting attribute describing how the audience was targeted (e.g., behavioral, lookalike). Business purpose: provides additional targeting metadata for segmentation and performance comparison. | :lower: |<
- `site_name_2` (STRING): Alternate or normalized publisher/platform name (likely standardized version of site_name). Business purpose: provides a consistent publisher label for reporting and joins when site_name contains variations.
- `impressions` (INTEGER): Total number of ad impressions delivered for the row's buy/line item. Business purpose: core exposure metric used for reach, frequency and CPM calculations.
- `clicks` (INTEGER): Total number of clicks recorded for the buy/line item. Business purpose: primary engagement metric used to compute CTR and evaluate creative/placement effectiveness.
- `ctr_tm_version` (FLOAT): Click-through rate calculated for this row (ratio of clicks to impressions, likely in decimal form). Business purpose: measures engagement efficiency of impressions to clicks for optimization and benchmarking.
- `completed_video_views` (INTEGER): Count of completed video views for video placements (users who watched to completion). Business purpose: video engagement metric used to evaluate creative and VTR-based billing or optimization.
- `vtr_tm_version` (FLOAT): Video completion or view-through rate for this row (ratio of completed views to served video impressions). Business purpose: assesses video creative effectiveness and is used for video performance optimization.

## (OPTIONAL) Table Relationships

## (Optional) Business Context

## (Optional) Notes

