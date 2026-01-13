# Copyright 2025-present Coinbase Global, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dataclasses import dataclass
from typing import List
from prime_sdk.enums import NetworkType


@dataclass
class OnchainAddress:
    name: str
    address: str
    chain_ids: List[str]


@dataclass
class AddressGroup:
    id: str
    name: str
    network_type: NetworkType
    addresses: List[OnchainAddress]
    added_at: str


@dataclass
class Portfolio:
    id: str
    name: str
    entity_id: str
    organization_id: str
    entity_name: str


@dataclass
class PortfolioUser:
    id: str
    name: str
    email: str
    portfolio_id: str
    entity_id: str
    role: str


@dataclass
class User:
    id: str
    name: str
    email: str
    entity_id: str
    role: str


@dataclass
class Network:
    id: str
    type: str


@dataclass
class Blockchain:
    address: str
    account_identifier: str
    network: Network


@dataclass
class AssetNetwork:
    network: Network
    name: str
    max_decimals: str
    default: bool
    trading_supported: bool
    vault_supported: bool
    prime_custody_supported: bool
    destination_tag_required: bool
    network_link: str


@dataclass
class Asset:
    name: str
    symbol: str
    decimal_precision: str
    trading_supported: bool
    explorer_url: str
    networks: List[AssetNetwork]
  

@dataclass
class ConsensusMetadata:
    approval_deadline: str
    has_passed_consensus: bool


@dataclass
class TransactionsMetadata:
    consensus: ConsensusMetadata


@dataclass
class AccountMetadata:
    consensus: ConsensusMetadata


@dataclass
class UserAction:
    action: str
    user_id: str
    timestamp: str


@dataclass
class Activity:
    id: str
    reference_id: str
    category: str
    type: str
    secondary_type: str
    status: str
    created_by: str
    title: str
    description: str
    user_actions: List[UserAction]
    transactions_metadata: TransactionsMetadata = None
    account_metadata: AccountMetadata = None
    symbols: List[str] = None
    created_at: str = None
    updated_at: str = None
    hierarchy_type: str = None


@dataclass
class ActivityResponse:
    activity: Activity


@dataclass
class Add:
    id: str
    name: str
    avatar_url: str


@dataclass
class Address:
    id: str
    currency_symbol: str
    name: str
    address: str
    account_identifier: str
    account_identifier_name: str
    state: str
    explorer_link: str
    last_used_at: str
    added_at: str
    added_by: Add
    type: str
    counterparty_id: str


@dataclass
class Destination:
    leg_id: str
    portfolio_id: str
    allocation_base: str
    allocation_quote: str
    fees_allocated_leg: str


@dataclass
class Allocation:
    root_id: str
    reversal_id: str
    allocation_completed_at: str
    user_id: str
    product_id: str
    side: str
    avg_price: str
    base_quantity: str
    quote_value: str
    fees_allocated: str
    status: str
    source: str
    order_ids: List[str]
    destinations: List[Destination]
    netting_id: str


@dataclass
class Details:
    id: str
    symbol: str
    payment_method_type: str
    bank_name: str = None
    account_number: str = None
    bank_name_2: str = None
    name: str = None
    bank_code: str = None


@dataclass
class FuturesPosition:
    product_id: str = None
    side: str = None
    number_of_contracts: str = None
    daily_realized_pnl: str = None
    unrealized_pnl: str = None
    current_price: str = None
    avg_entry_price: str = None
    expiration_time: str = None
    symbol: str = None
    long: str = None
    short: str = None
    position_reference: str = None



@dataclass
class FcmMarginCall:
    type: str = None
    state: str = None
    initial_amount: str = None
    remaining_amount: str = None
    business_date: str = None
    cure_deadline: str = None


@dataclass
class FcmRiskLimits:
    cfm_risk_limit: str = None
    cfm_risk_limit_utilization: str = None
    cfm_total_margin: str = None
    cfm_delta_ote: str = None
    cfm_unsettled_realized_pnl: str = None
    cfm_unsettled_accrued_funding_pnl: str = None


@dataclass
class OrderEditHistory:
    price: str
    size: str
    display_size: str
    stop_price: str
    stop_limit_price: str
    end_time: str
    accept_time: str


@dataclass
class EditHistory:
    price: str
    base_quantity: str
    quote_value: str
    display_quote_size: str
    display_base_size: str
    stop_price: str
    expiry_time: str
    accept_time: str
    client_order_id: str


@dataclass
class Order:
    id: str
    user_id: str
    portfolio_id: str
    product_id: str
    side: str
    client_order_id: str
    type: str
    base_quantity: str
    quote_value: str
    limit_price: str
    start_time: str
    expiry_time: str
    status: str
    time_in_force: str
    created_at: str
    filled_quantity: str
    filled_value: str
    average_filled_price: str
    commission: str
    exchange_fee: str
    historical_pov: str
    stop_price: str
    net_average_filled_price: str
    user_context: str
    client_product_id: str
    post_only: bool = None
    order_edit_history: List[OrderEditHistory] = None
    is_raise_exact: bool = None
    display_size: str = None
    display_quote_size: str = None
    display_base_size: str = None
    edit_history: List[EditHistory] = None
    peg_offset_type: str = None
    offset: str = None
    wig_level: str = None


@dataclass
class Commission:
    type: str
    rate: str
    trading_volume: str


@dataclass
class AmountDue:
    currency: str
    amount: str
    due_date: str

@dataclass
class PostTradeCredit:
    portfolio_id: str
    currency: str
    limit: str
    utilized: str
    available: str
    frozen: str
    frozen_reason: str
    amounts_due: List[AmountDue]
    enabled: str
    adjusted_credit_utilized: str
    adjusted_portfolio_equity: str


@dataclass
class TransferLocation:
    type: str
    value: str


@dataclass
class EstimatedNetworkFees:
    lower_bound: str
    upper_bound: str


@dataclass
class Collection:
    name: str = None


@dataclass
class Item:
    name: str = None


@dataclass
class AssetChange:
    type: str = None
    symbol: str = None
    amount: str = None
    collection: Collection = None
    item: Item = None


@dataclass
class MatchMetadata:
    reference_id: str = None
    settlement_date: str = None


@dataclass
class Web3TransactionMetadata:
    label: str = None
    confirmed_asset_changes: List[AssetChange] = None


@dataclass
class RewardMetadata:
    subtype: str = None


@dataclass
class TransactionMetadata:
    match_metadata: MatchMetadata = None
    web3_transaction_metadata: Web3TransactionMetadata = None
    reward_metadata: RewardMetadata = None


@dataclass
class RiskAssessment:
    compliance_risk_detected: bool
    security_risk_detected: bool


@dataclass
class OnchainDetails:
    signed_transaction: str = None
    risk_assessment: RiskAssessment = None
    chain_id: str = None
    nonce: str = None
    replaced_transaction_id: str = None
    destination_address: str = None
    skip_broadcast: bool = None
    failure_reason: str = None
    signing_status: str = None


@dataclass
class ProcessRequirements:
    travel_rule_status: str = None


@dataclass
class Transaction:
    id: str = None
    wallet_id: str = None
    portfolio_id: str = None
    type: str = None
    status: str = None
    symbol: str = None
    created_at: str = None
    completed_at: str = None
    amount: str = None
    transfer_from: TransferLocation = None
    transfer_to: TransferLocation = None
    network_fees: str = None
    fees: str = None
    fee_symbol: str = None
    blockchain_ids: List[str] = None
    transaction_id: str = None
    destination_symbol: str = None
    estimated_network_fees: EstimatedNetworkFees = None
    network: str = None
    estimated_asset_changes: List[AssetChange] = None
    metadata: TransactionMetadata = None
    idempotency_key: str = None
    onchain_details: OnchainDetails = None
    network_info: Network = None
    process_requirements: ProcessRequirements = None


@dataclass
class TransactionValidator:
    transaction_id: str = None
    validator_address: str = None
    validator_status: str = None


@dataclass
class Balance:
    symbol: str
    amount: str
    holds: str
    bonded_amount: str
    reserved_amount: str
    unbonding_amount: str
    unvested_amount: str
    pending_rewards_amount: str
    past_rewards_amount: str
    bondable_amount: str
    withdrawable_amount: str
    fiat_amount: str
    unbondable_amount: str
    claimable_rewards_amount: str


@dataclass
class CryptoInstructions:
    id: str
    name: str
    type: str
    address: str
    account_identifier: str
    account_identifier_name: str
    network: Network


@dataclass
class FiatInstructions:
    id: str
    name: str
    type: str
    account_number: str
    routing_number: str
    reference_code: str


@dataclass
class Instructions:
    crypto_instructions: CryptoInstructions
    fiat_instructions: FiatInstructions


@dataclass
class Wallet:
    id: str
    name: str
    symbol: str
    type: str
    created_at: str
    address: str
    visibility: str
    network: Network


@dataclass
class RequestedAmount:
    currency: str
    amount: str


@dataclass
class Sweep:
    id: str
    requested_amount: RequestedAmount
    should_sweep_all: bool
    status: str
    scheduled_time: str


@dataclass
class InvoiceItem:
    description: str
    currency_symbol: str
    invoice_type: str
    rate: float
    quantity: float
    price: float
    average_auc: float
    total: float


@dataclass
class Invoice:
    id: str
    billing_month: int
    billing_year: int
    due_date: str
    invoice_number: str
    state: str
    usd_amount_paid: float
    usd_amount_owed: float
    invoice_items: List[InvoiceItem]


@dataclass
class Fill:
    id: str
    order_id: str
    product_id: str
    client_product_id: str
    side: str
    filled_quantity: str
    filled_value: str
    price: str
    time: str
    commission: str
    venue: str
    venue_fees: str = None
    ces_commission: str = None


@dataclass
class BalanceWithHolds:
    total: str
    holds: str


@dataclass
class RfqProductDetails:
    tradable: bool
    min_notional_size: str
    max_notional_size: str
    min_base_size: str
    max_base_size: str
    min_quote_size: str
    max_quote_size: str


@dataclass
class Product:
    id: str
    base_increment: str
    quote_increment: str
    base_min_size: str
    quote_min_size: str
    base_max_size: str
    quote_max_size: str
    permissions: List[str]
    price_increment: str
    rfq_product_details: RfqProductDetails


@dataclass
class DefiBalance:
    network: str
    protocol: str
    net_usd_value: str


@dataclass
class OnchainBalance:
    asset: Asset
    amount: str
    visibility_status: str


@dataclass
class MarketRate:
    symbol: str
    rate: str


@dataclass
class AssetBalance:
    portfolio_id: str
    symbol: str
    amount: str
    notional_amount: str
    conversion_rate: str


@dataclass
class TfLoan:
    portfolio_id: str
    symbol: str
    amount: str
    notional_amount: str
    due_date: str


@dataclass
class PmLoan:
    portfolio_id: str
    symbol: str
    amount: str
    notional_amount: str
    due_date: str


@dataclass
class ShortCollateral:
    portfolio_id: str
    symbol: str
    amount: str
    notional_amount: str
    due_date: str


@dataclass
class PortfolioStressTriggered:
    amount: str
    add_on_type: str


@dataclass
class PmAssetInfo:
    symbol: str
    amount: str
    price: str
    notional_amount: str
    asset_tier: str
    margin_eligible: bool
    base_margin_requirement: str
    base_margin_requirement_notional: str
    adv_30d: str
    hist_5d_vol: str
    hist_30d_vol: str
    hist_90d_vol: str
    volatility_addon: str
    liquidity_addon: str
    total_position_margin: str
    short_nominal: str
    long_nominal: str


@dataclass
class MarginSummary:
    entity_id: str
    margin_equity: str
    margin_requirement: str
    excess_deficit: str
    pm_credit_consumed: str
    tf_credit_limit: str
    tf_credit_consumed: str
    tf_adjusted_asset_value: str
    tf_adjusted_liability_value: str
    tf_adjusted_credit_consumed: str
    tf_adjusted_equity: str
    frozen: bool
    frozen_reason: str
    tf_enabled: bool
    pm_enabled: bool
    market_rates: List[MarketRate]
    asset_balances: List[AssetBalance]
    tf_loans: List[TfLoan]
    pm_loans: List[PmLoan]
    short_collateral: List[ShortCollateral]
    gross_market_value: str
    net_market_value: str
    long_market_value: str
    non_marginable_long_market_value: str
    short_market_value: str
    gross_leverage: str
    net_exposure: str
    portfolio_stress_triggered: PortfolioStressTriggered
    pm_asset_info: List[PmAssetInfo]
    pm_credit_limit: str
    pm_margin_limit: str
    pm_margin_consumed: str


@dataclass
class MarginCall:
    id: str
    initial_notional_amount: str
    outstanding_notional_amount: str
    created_at: str
    due_at: str


@dataclass
class WithdrawalPower:
    symbol: str
    amount: str


@dataclass
class BuyingPower:
    portfolio_id: str
    base_currency: str
    quote_currency: str
    base_buying_power: str
    quote_buying_power: str


@dataclass
class ConversionDetail:
    symbol: str
    tf_balance: str
    notional_tf_balance: str
    converted_balance: str
    notional_converted_balance: str
    interest_rate: str
    conversion_rate: str


@dataclass
class ShortCollateral:
    old_balance: str
    new_balance: str
    loan_interest_rate: str
    collateral_interest_rate: str


@dataclass
class Conversion:
    conversion_details: List[ConversionDetail]
    short_collateral: ShortCollateral
    conversion_datetime: str
    portfolio_id: str


@dataclass
class Accrual:
    accrual_id: str
    date: str
    portfolio_id: str
    symbol: str
    loan_type: str
    interest_rate: str
    nominal_accrual: str
    notional_accrual: str
    conversion_rate: str
    loan_amount: str
    benchmark: str
    benchmark_rate: str
    spread: str
    rate_type: str
    loan_amount_notional: str
    nominal_open_borrow_sod: str
    notional_open_borrow_sod: str


@dataclass
class Reference:
    id: str
    type: str


@dataclass
class Position:
    symbol: str
    long: str
    short: str
    position_reference: Reference


@dataclass
class MarginSummaryRecord:
    conversion_datetime: str
    conversion_date: str
    margin_summary: MarginSummary


@dataclass
class EntityBalance:
    symbol: str
    long_amount: str
    long_notional: str
    short_amount: str
    short_notional: str


@dataclass
class LocateAvailability:
    symbol: str
    quantity: str
    rate: str


@dataclass
class Locate:
    locate_id: str
    entity_id: str
    portfolio_id: str
    symbol: str
    requested_amount: str
    interest_rate: str
    status: str
    approved_amount: str
    conversion_date: str
    created_at: str
    locate_date: str


@dataclass
class MarginCallRecord:
    margin_call_id: str
    initial_notional_amount: str
    outstanding_notional_amount: str
    created_at: str
    due_at: str


@dataclass
class MarginInformation:
    margin_call_records: List[MarginCallRecord]
    margin_summary: MarginSummary


@dataclass
class ScenarioAddon:
    amount: str = None
    add_on_type: str = None


@dataclass
class XmPosition:
    currency: str = None
    market_price: str = None
    margin_eligible: str = None
    market_cap: str = None
    adv30_days: str = None
    hist5d_vol: str = None
    hist30d_vol: str = None
    hist90d_vol: str = None
    margin_requirement: str = None
    spot_balance: str = None
    spot_balance_notional: str = None
    spot_total_position_margin: str = None
    futures_balance: str = None
    futures_balance_notional: str = None
    futures_total_position_margin: str = None
    gmv_basis: str = None
    base_requirement: str = None
    liq_shorts_add_on: str = None
    liq_longs_add_on: str = None
    vol_shorts_add_on: str = None
    vol_longs_add_on: str = None
    vol5days_add_on: str = None
    vol30days_add_on: str = None
    vol90days_add_on: str = None
    total_position_margin: str = None


@dataclass
class RiskNettingInfo:
    nodal_margin_requirement: str = None
    portfolio_margin_requirement: str = None
    integrated_portfolio_margin_requirement: str = None
    ineligible_futures_margin_requirement: str = None
    position_margin_requirement: str = None
    portfolio_margin_addon: str = None
    integrated_position_margin_requirement: str = None
    integrated_portfolio_margin_addon: str = None
    netted_futures_notional: str = None
    total_gmv_basis: str = None
    ipm_cash_balance: str = None
    integrated_scenario_addon: ScenarioAddon = None
    all_integrated_scenario_addons: List[ScenarioAddon] = None
    xm_positions: List[XmPosition] = None


@dataclass
class CrossMarginSummary:
    margin_requirement: str = None
    account_equity: str = None
    margin_excess_shortfall: str = None
    consumed_credit: str = None
    xm_credit_limit: str = None
    xm_margin_limit: str = None
    spot_equity: str = None
    futures_equity: str = None
    risk_netting_info: RiskNettingInfo = None


@dataclass
class CrossMarginLoan:
    loan_id: str = None
    loan_party: str = None
    principal_currency: str = None
    principal_currency_market_price: str = None
    initial_principal_amount: str = None
    outstanding_principal_amount: str = None
    created_at: str = None
    updated_at: str = None


@dataclass
class CrossMarginCall:
    margin_call_id: str = None
    currency: str = None
    initial_notional_amount: str = None
    outstanding_notional_amount: str = None
    margin_call_type: str = None
    margin_call_status: str = None
    called_with_margin_level: str = None
    called_with_margin_summary: CrossMarginSummary = None
    due_at: str = None
    created_at: str = None
    updated_at: str = None


@dataclass
class CrossMarginOverview:
    control_status: str = None
    call_status: str = None
    margin_level: str = None
    margin_summary: CrossMarginSummary = None
    active_margin_calls: List[CrossMarginCall] = None
    active_loans: List[CrossMarginLoan] = None


@dataclass
class AmountDue:
    currency: str
    amount: str
    due_date: str


@dataclass
class PostTradeCredit:
    portfolio_id: str
    currency: str
    limit: str
    utilized: str
    available: str
    frozen: bool
    frozen_reason: str
    amounts_due: List[AmountDue]
    enabled: bool
    adjusted_credit_utilized: str
    adjusted_portfolio_equity: str


@dataclass
class Fee:
    symbol: str
    fee: str


@dataclass
class BlockchainAddress:
    address: str
    account_identifier: str
    network: Network


@dataclass
class Candle:
    timestamp: str
    open: str
    high: str
    low: str
    close: str
    volume: str


@dataclass
class Counterparty:
    counterparty_id: str


@dataclass
class TFAsset:
    symbol: str
    asset_adjustment: str
    liability_adjustment: str


@dataclass
class TFObligation:
    portfolio_id: str
    symbol: str
    amount_due: str
    notional_amount: str
    due_date: str
