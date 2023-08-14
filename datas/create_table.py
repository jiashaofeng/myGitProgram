import aiqdata as tb


# adj_factor.py--1
def create_table_mktadjfaf():
    schema = {'secID': 'varchar(33)', 'ticker': 'varchar(18)', 'exchangeCD': 'varchar(12)',
              'secShortName': 'varchar(15)', 'secShortNameEn': 'varchar(33)', 'exDivDate': 'long',
              'perCashDiv': 'float', 'perShareDivRatio': 'float', 'perShareTransRatio': 'float',
              'allotmentRatio': 'float', 'allotmentPrice': 'float', 'splitsRatio': 'float', 'adjFactor': 'float',
              'accumAdjFactor': 'float', 'endDate': 'varchar(30)'}

    tb.create_table('mktadjfaf', schema, 'exDivDate', 'time_colunm', 'security_column', 0)


# adj_factor.py--1
def create_table_mktadjf():
    schema = {'secID': 'varchar(33)', 'ticker': 'varchar(18)', 'exchangeCD': 'varchar(12)',
              'secShortName': 'varchar(15)', 'secShortNameEn': 'varchar(33)', 'exDivDate': 'long',
              'perCashDiv': 'float', 'perShareDivRatio': 'float', 'perShareTransRatio': 'float',
              'allotmentRatio': 'float', 'allotmentPrice': 'float', 'adjFactor': 'float',
              'accumAdjFactor': 'float', 'endDate': 'varchar(30)', 'updateTime': 'varchar(57)'}

    tb.create_table('mktadjf', schema, 'exDivDate', 'time_colunm', 'security_column', 0)


# equ.py--1
def create_table_equ():
    schema = {'date': 'long', 'secID': 'varchar(32)', 'ticker': 'varchar(16)', 'exchangeCD': 'varchar(16)',
              'ListSectorCD': 'long', 'ListSector': 'varchar(16)', 'transCurrCD': 'varchar(16)',
              'secShortName': 'varchar(16)', 'secFullName': 'varchar(64)', 'listStatusCD': 'varchar(16)',
              'listDate': 'varchar(32)', 'delistDate': 'varchar(32)', 'equTypeCD': 'varchar(32)',
              'equType': 'varchar(16)', 'exCountryCD': 'varchar(16)', 'partyID': 'long', 'totalShares': 'float',
              'nonrestFloatShares': 'float', 'nonrestfloatA': 'float', 'officeAddr': 'varchar(256)',
              'primeOperating': 'varchar(2048)', 'endDate': 'varchar(32)', 'TShEquity': 'float'}

    tb.create_table('equ', schema, 'date', 'time_colunm', 'security_column', 0)


# balance_bank.py--
# (新)银行业资产负债表——已定义字段长度
def create_table_fdmtbsbank2018():
    schema = {'secID': 'varchar(32)', 'secShortName': 'varchar(16)', 'ticker': 'varchar(16)', 'partyID': 'long',
              'exchangeCD': 'varchar(16)', 'actPubtime': 'varchar(64)', 'publishDate': 'long',
              'endDateRep': 'varchar(32)', 'endDate': 'varchar(32)', 'reportType': 'varchar(16)',
              'fiscalPeriod': 'long',
              'mergedFlag': 'varchar(16)', 'accoutingStandards': 'varchar(32)', 'currencyCD': 'varchar(16)',
              'industryCategory': 'varchar(16)', 'cReserCb': 'float', 'deposInOthBfi': 'float', 'preciMetals': 'float',
              'loanToOthBankFi': 'float', 'tradingFa': 'float', 'tradingOthCompreIncomevFa': 'float',
              'tradingAmortizeFa': 'float', 'debtInvest': 'float', 'othDebtInvest': 'float',
              'othEquityInstrInvest': 'float', 'derivAssets': 'float', 'purResaleFa': 'float',
              'intReceiv': 'float', 'disburLa': 'float', 'finanLeaseReceiv': 'float',
              'availForSaleFa': 'float', 'htmInvest': 'float', 'investAsReceiv': 'float',
              'ltEquityInvest': 'float', 'investRealEstate': 'float', 'fixedAssets': 'float', 'cip': 'float',
              'intanAssets': 'float', 'goodwill': 'float', 'deferTaxAssets': 'float', 'othAssets': 'float',
              'ae': 'float', 'aa': 'float', 'tAssets': 'float', 'cbBorr': 'float', 'deposFrOthBfi': 'float',
              'loanFrOthBankFi': 'float', 'tradingFl': 'float', 'derivLiab': 'float',
              'soldForRepurFa': 'float', 'depos': 'float', 'payrollPayable': 'float',
              'taxesPayable': 'float', 'intPayable': 'float', 'estimatedLiab': 'float',
              'bondPayable': 'float', 'preferredStockL': 'float', 'perpetualBondL': 'float',
              'deferTaxLiab': 'float', 'othLiab': 'float', 'le': 'float', 'la': 'float', 'tLiab': 'float',
              'paidInCapital': 'float', 'othEquityInstr': 'float', 'preferredStockE': 'float',
              'perpetualBondE': 'float', 'capitalReser': 'float', 'treasuryShare': 'float',
              'othCompreIncome': 'float', 'surplusReser': 'float', 'ordinRiskReser': 'float',
              'retainedEarnings': 'float', 'forexDiffer': 'float', 'see': 'float', 'sea': 'float',
              'tEquityAttrP': 'float', 'minorityInt': 'float', 'othEffectSe': 'float', 'othEffectSa': 'float',
              'tShEquity': 'float', 'lee': 'float', 'lea': 'float', 'tLiabEquity': 'float',
              'updateTime': 'varchar(64)'}
    tb.create_table('fdmtbsbank2018', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# balance_indu.py-------------建表已验证
# (新)一般工商业资产负债表
def create_table_fdmtbsindu2018():
    schema = {'secID': 'varchar(32)', 'secShortName': 'varchar(16)', 'ticker': 'varchar(16)', 'partyID': 'long',
              'exchangeCD': 'varchar(16)', 'actPubtime': 'varchar(64)', 'publishDate': 'long',
              'endDateRep': 'varchar(32)', 'endDate': 'varchar(32)', 'reportType': 'varchar(16)',
              'fiscalPeriod': 'long', 'mergedFlag': 'varchar(16)', 'accoutingStandards': 'varchar(32)',
              'currencyCD': 'varchar(16)', 'industryCategory': 'varchar(16)', 'cashCEquiv': 'float',
              'settProv': 'float', 'loanToOthBankFi': 'float', 'tradingFa': 'float', 'derivAssets': 'float',
              'nrAr': 'float', 'notesReceiv': 'float', 'ar': 'float', 'finanReceiv': 'float', 'prepayment': 'float',
              'premiumReceiv': 'float', 'reinsurReceiv': 'float', 'reinsurReserReceiv': 'float',
              'othReceivTotal': 'float', 'intReceiv': 'float', 'divReceiv': 'float', 'othReceiv': 'float',
              'purResaleFa': 'float', 'inventories': 'float', 'contAssets': 'float', 'assetsHeldForSale': 'float',
              'ncaWithin1y': 'float', 'othCa': 'float', 'cae': 'float',
              'caa': 'float', 'tCa': 'float', 'disburLa': 'float', 'tradingOthCompreIncomevFa': 'float',
              'tradingAmortizeFa': 'float', 'availForSaleFa': 'float', 'htmInvest': 'float', 'debtInvest': 'float',
              'othDebtInvest': 'float', 'ltReceiv': 'float', 'ltEquityInvest': 'float', 'othEquityInstrInvest': 'float',
              'assetsNc': 'float', 'investRealEstate': 'float', 'fixedAssetsTotal': 'float', 'fixedAssets': 'float',
              'fixedAssetsDisp': 'float', 'cipTotal': 'float', 'cip': 'float', 'constMaterials': 'float',
              'producBiolAssets': 'float', 'commonwealBiolAssets': 'float', 'oilAndGasAssets': 'float',
              'usageAssets': 'float', 'intanAssets': 'float', 'rD': 'float', 'goodwill': 'float', 'ltAmorExp': 'float',
              'deferTaxAssets': 'float', 'othNca': 'float', 'ncae': 'float', 'ncaa': 'float', 'tNca': 'float',
              'ae': 'float',
              'aa': 'float', 'tAssets': 'float', 'stBorr': 'float', 'cbBorr': 'float', 'depos': 'float',
              'loanFrOthBankFi': 'float', 'tradingFl': 'float', 'derivLiab': 'float', 'npAp': 'float',
              'notesPayable': 'float',
              'ap': 'float', 'advanceReceipts': 'float', 'soldForRepurFa': 'float', 'commisPayable': 'float',
              'contLiab': 'float', 'payrollPayable': 'float', 'taxesPayable': 'float', 'othPayableTotal': 'float',
              'intPayable': 'float', 'divPayable': 'float', 'othPayable': 'float', 'reinsurPayable': 'float',
              'fundsSecTradAgen': 'float', 'fundsSecUndwAgen': 'float', 'liabHeldForSale': 'float',
              'nclWithin1y': 'float',
              'accruedExp': 'float', 'othCl': 'float', 'cle': 'float', 'cla': 'float', 'tCl': 'float',
              'insurReser': 'float',
              'ltBorr': 'float', 'bondPayable': 'float', 'preferredStockL': 'float', 'perpetualBondL': 'float',
              'leaseLiab': 'float', 'ltPayableTotal': 'float', 'ltPayable': 'float', 'specificPayables': 'float',
              'ltPayrollPayable': 'float', 'estimatedLiab': 'float', 'deferRevenue': 'float', 'deferTaxLiab': 'float',
              'othNcl': 'float', 'ncle': 'float', 'ncla': 'float', 'tNcl': 'float', 'le': 'float', 'la': 'float',
              'tLiab': 'float', 'paidInCapital': 'float', 'othEquityInstr': 'float', 'preferredStockE': 'float',
              'perpetualBondE': 'float', 'updateTime': 'varchar(64)', 'capitalReser': 'float', 'treasuryShare': 'float',
              'othCompreIncome': 'float', 'specialReser': 'float', 'surplusReser': 'float', 'ordinRiskReser': 'float',
              'transacRiskReser': 'float', 'retainedEarnings': 'float', 'forexDiffer': 'float', 'see': 'float',
              'sea': 'float',
              'tEquityAttrP': 'float', 'minorityInt': 'float', 'othEffectSe': 'float', 'othEffectSa': 'float',
              'tShEquity': 'float', 'lee': 'float', 'lea': 'float', 'tLiabEquity': 'float'}
    tb.create_table('fdmtbsindu2018', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# balance_secu.py-------------建表已验证
# (新)证券业资产负债表
def create_table_fdmtbssecu2018():
    schema = {'secID': 'varchar(32)', 'secShortName': 'varchar(16)', 'ticker': 'varchar(16)', 'partyID': 'long',
              'exchangeCD': 'varchar(16)', 'actPubtime': 'varchar(64)', 'publishDate': 'long',
              'endDateRep': 'varchar(32)', 'endDate': 'varchar(32)', 'reportType': 'varchar(16)',
              'fiscalPeriod': 'long',
              'mergedFlag': 'varchar(16)', 'accoutingStandards': 'varchar(32)', 'currencyCD': 'varchar(16)',
              'industryCategory': 'varchar(16)', 'cashCEquiv': 'float', 'clientDepos': 'float', 'settProv': 'float',
              'clientProv': 'float', 'loanToOthBankFi': 'float', 'tradingFa': 'float', 'derivAssets': 'float',
              'purResaleFa': 'float', 'tradingOthCompreIncomevFa': 'float', 'tradingAmortizeFa': 'float',
              'debtInvest': 'float', 'othDebtInvest': 'float', 'othEquityInstrInvest': 'float', 'intReceiv': 'float',
              'refundDepos': 'float', 'availForSaleFa': 'float', 'htmInvest': 'float',
              'ltEquityInvest': 'float', 'investRealEstate': 'float', 'fixedAssets': 'float',
              'intanAssets': 'float', 'transacSeatFee': 'float', 'deferTaxAssets': 'float',
              'othAssets': 'float', 'ae': 'float', 'aa': 'float', 'tAssets': 'float', 'stBorr': 'float',
              'pledgeBorr': 'float', 'loanFrOthBankFi': 'float', 'tradingFl': 'float', 'derivLiab': 'float',
              'soldForRepurFa': 'float', 'fundsSecTradAgen': 'float', 'fundsSecUndwAgen': 'float',
              'payrollPayable': 'float', 'taxesPayable': 'float', 'intPayable': 'float',
              'estimatedLiab': 'float', 'ltBorr': 'float', 'bondPayable': 'float', 'preferredStockL': 'float',
              'perpetualBondL': 'float', 'deferTaxLiab': 'float', 'othLiab': 'float', 'le': 'float',
              'la': 'float', 'tLiab': 'float', 'paidInCapital': 'float', 'othEquityInstr': 'float',
              'preferredStockE': 'float', 'perpetualBondE': 'float', 'capitalReser': 'float',
              'treasuryShare': 'float', 'othCompreIncome': 'float', 'surplusReser': 'float',
              'ordinRiskReser': 'float', 'transacRiskReser': 'float', 'retainedEarnings': 'float',
              'forexDiffer': 'float', 'see': 'float', 'sea': 'float', 'updateTime': 'varchar(64)',
              'tEquityAttrP': 'float', 'minorityInt': 'float', 'othEffectSe': 'float', 'othEffectSa': 'float',
              'tShEquity': 'float', 'lee': 'float', 'lea': 'float', 'tLiabEquity': 'float'}
    tb.create_table('fdmtbssecu2018', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# balance_insu.py-------------建表已验证
# (新)保险业资产负债表
def create_table_fdmtbsinsu2018():
    schema = {'secID': 'varchar(32)', 'secShortName': 'varchar(16)', 'partyID': 'long', 'ticker': 'varchar(16)',
              'exchangeCD': 'varchar(16)', 'actPubtime': 'varchar(64)', 'publishDate': 'long',
              'endDateRep': 'varchar(32)', 'endDate': 'varchar(32)', 'reportType': 'varchar(16)',
              'fiscalPeriod': 'long',
              'mergedFlag': 'varchar(16)', 'accoutingStandards': 'varchar(32)', 'currencyCD': 'varchar(16)',
              'industryCategory': 'varchar(16)', 'cashCEquiv': 'float', 'loanToOthBankFi': 'float', 'tradingFa': 'float',
              'derivAssets': 'float', 'purResaleFa': 'float', 'tradingOthCompreIncomevFa': 'float',
              'tradingAmortizeFa': 'float', 'debtInvest': 'float', 'othDebtInvest': 'float',
              'othEquityInstrInvest': 'float',
              'intReceiv': 'float', 'premiumReceiv': 'float', 'subrogRecoReceiv': 'float',
              'reinsurReceiv': 'float', 'rrReinsUnePrem': 'float', 'rrReinsOutstdCla': 'float',
              'rrReinsLinsLiab': 'float', 'rrReinsLthinsLiab': 'float', 'phPledgeLoans': 'float',
              'fixedTermDepos': 'float', 'availForSaleFa': 'float', 'htmInvest': 'float',
              'ltEquityInvest': 'float', 'refundCapDepos': 'float', 'investRealEstate': 'float',
              'fixedAssets': 'float', 'intanAssets': 'float', 'indepAccAssets': 'float',
              'deferTaxAssets': 'float', 'othAssets': 'float', 'ae': 'float', 'aa': 'float',
              'tAssets': 'float', 'stBorr': 'float', 'loanFrOthBankFi': 'float', 'tradingFl': 'float',
              'derivLiab': 'float', 'soldForRepurFa': 'float', 'premReceivAdva': 'float',
              'commisPayable': 'float', 'reinsurPayable': 'float', 'payrollPayable': 'float',
              'taxesPayable': 'float', 'indemAccPayable': 'float', 'policyDivPayable': 'float',
              'phInvest': 'float', 'reserUnePrem': 'float', 'reserOutstdClaims': 'float',
              'reserLinsLiab': 'float', 'reserLthinsLiab': 'float', 'ltBorr': 'float', 'bondPayable': 'float',
              'preferredStockL': 'float', 'perpetualBondL': 'float', 'indeptAccLiab': 'float',
              'deferTaxLiab': 'float', 'othLiab': 'float', 'le': 'float', 'la': 'float', 'tLiab': 'float',
              'paidInCapital': 'float', 'othEquityInstr': 'float', 'preferredStockE': 'float',
              'perpetualBondE': 'float', 'capitalReser': 'float', 'treasuryShare': 'float',
              'othCompreIncome': 'float', 'surplusReser': 'float', 'ordinRiskReser': 'float',
              'retainedEarnings': 'float', 'forexDiffer': 'float', 'see': 'float', 'sea': 'float',
              'tEquityAttrP': 'float', 'minorityInt': 'float', 'othEffectSe': 'float', 'othEffectSa': 'float',
              'tShEquity': 'float', 'lee': 'float', 'lea': 'float', 'tLiabEquity': 'float',
              'updateTime': 'varchar(64)', 'reinsurReserReceiv': 'float', 'insurReser': 'float'}

    tb.create_table('fdmtbsinsu2018', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# balance_all.py-------------建表已验证
# (新)合并资产负债表
def create_table_fdmtbs2018():
    schema = {'secID': 'varchar(32)', 'secShortName': 'varchar(16)', 'ticker': 'varchar(16)', 'partyID': 'long',
              'exchangeCD': 'varchar(16)', 'actPubtime': 'varchar(64)', 'publishDate': 'long',
              'endDateRep': 'varchar(32)', 'endDate': 'varchar(32)', 'reportType': 'varchar(16)',
              'fiscalPeriod': 'long',
              'mergedFlag': 'varchar(16)', 'accoutingStandards': 'varchar(32)', 'currencyCD': 'varchar(16)',
              'industryCategory': 'varchar(16)', 'cashCEquiv': 'float', 'settProv': 'float', 'loanToOthBankFi': 'float',
              'tradingFa': 'float', 'derivAssets': 'float', 'nrAr': 'float', 'notesReceiv': 'float', 'ar': 'float',
              'finanReceiv': 'float', 'prepayment': 'float', 'premiumReceiv': 'float', 'reinsurReceiv': 'float',
              'reinsurReserReceiv': 'float', 'othReceivTotal': 'float', 'intReceiv': 'float', 'divReceiv': 'float',
              'othReceiv': 'float', 'purResaleFa': 'float', 'inventories': 'float', 'contAssets': 'float',
              'assetsHeldForSale': 'float', 'ncaWithin1y': 'float', 'othCa': 'float', 'cae': 'float', 'caa': 'float',
              'tCa': 'float', 'disburLa': 'float', 'tradingOthCompreIncomevFa': 'float', 'tradingAmortizeFa': 'float',
              'availForSaleFa': 'float', 'htmInvest': 'float', 'debtInvest': 'float', 'othDebtInvest': 'float',
              'ltReceiv': 'float', 'ltEquityInvest': 'float', 'othEquityInstrInvest': 'float', 'assetsNc': 'float',
              'investRealEstate': 'float', 'fixedAssetsTotal': 'float', 'fixedAssets': 'float',
              'fixedAssetsDisp': 'float',
              'cipTotal': 'float', 'cip': 'float', 'constMaterials': 'float', 'producBiolAssets': 'float',
              'commonwealBiolAssets': 'float', 'oilAndGasAssets': 'float', 'usageAssets': 'float',
              'intanAssets': 'float',
              'rD': 'float', 'goodwill': 'float', 'ltAmorExp': 'float', 'deferTaxAssets': 'float', 'othNca': 'float',
              'ncae': 'float', 'ncaa': 'float', 'tNca': 'float', 'cReserCb': 'float', 'deposInOthBfi': 'float',
              'preciMetals': 'float', 'finanLeaseReceiv': 'float', 'investAsReceiv': 'float',
              'subrogRecoReceiv': 'float',
              'rrReinsUnePrem': 'float', 'rrReinsOutstdCla': 'float', 'rrReinsLinsLiab': 'float',
              'rrReinsLthinsLiab': 'float', 'phPledgeLoans': 'float', 'fixedTermDepos': 'float',
              'refundCapDepos': 'float',
              'indepAccAssets': 'float', 'refundDepos': 'float', 'othAssets': 'float', 'ae': 'float', 'aa': 'float',
              'tAssets': 'float', 'stBorr': 'float', 'cbBorr': 'float', 'depos': 'float', 'loanFrOthBankFi': 'float',
              'tradingFl': 'float', 'derivLiab': 'float', 'npAp': 'float', 'notesPayable': 'float', 'ap': 'float',
              'advanceReceipts': 'float', 'updateTime': 'varchar(64)', 'soldForRepurFa': 'float',
              'commisPayable': 'float',
              'contLiab': 'float', 'payrollPayable': 'float', 'taxesPayable': 'float', 'othPayableTotal': 'float',
              'intPayable': 'float', 'divPayable': 'float', 'othPayable': 'float', 'reinsurPayable': 'float',
              'fundsSecTradAgen': 'float', 'fundsSecUndwAgen': 'float', 'liabHeldForSale': 'float',
              'nclWithin1y': 'float',
              'accruedExp': 'float', 'othCl': 'float', 'cle': 'float', 'cla': 'float', 'tCl': 'float',
              'insurReser': 'float',
              'ltBorr': 'float', 'bondPayable': 'float', 'preferredStockL': 'float', 'perpetualBondL': 'float',
              'leaseLiab': 'float', 'ltPayableTotal': 'float', 'ltPayable': 'float', 'specificPayables': 'float',
              'ltPayrollPayable': 'float', 'estimatedLiab': 'float', 'deferRevenue': 'float', 'deferTaxLiab': 'float',
              'othNcl': 'float', 'ncle': 'float', 'ncla': 'float', 'tNcl': 'float', 'deposFrOthBfi': 'float',
              'premReceivAdva': 'float', 'indemAccPayable': 'float', 'policyDivPayable': 'float', 'phInvest': 'float',
              'reserUnePrem': 'float', 'reserOutstdClaims': 'float', 'reserLinsLiab': 'float',
              'reserLthinsLiab': 'float',
              'indeptAccLiab': 'float', 'othLiab': 'float', 'le': 'float', 'la': 'float', 'tLiab': 'float',
              'paidInCapital': 'float', 'othEquityInstr': 'float', 'preferredStockE': 'float',
              'perpetualBondE': 'float',
              'capitalReser': 'float', 'treasuryShare': 'float', 'othCompreIncome': 'float', 'specialReser': 'float',
              'surplusReser': 'float', 'ordinRiskReser': 'float', 'transacRiskReser': 'float',
              'retainedEarnings': 'float',
              'forexDiffer': 'float', 'see': 'float', 'sea': 'float', 'tEquityAttrP': 'float', 'minorityInt': 'float',
              'othEffectSe': 'float', 'othEffectSa': 'float', 'tShEquity': 'float', 'lee': 'float', 'lea': 'float',
              'tLiabEquity': 'float'}

    tb.create_table('fdmtbs2018', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# balance_2007.py--
# 银行业资产负债表
def create_table_fdmtbsbank():
    schema = {'secID': 'varchar(32)', 'publishDate': 'long', 'endDate': 'varchar(32)', 'endDateRep': 'varchar(32)',
              'partyID': 'long', 'ticker': 'varchar(16)', 'secShortName': 'varchar(16)', 'exchangeCD': 'varchar(16)',
              'actPubtime': 'varchar(64)', 'mergedFlag': 'varchar(16)', 'reportType': 'varchar(16)',
              'fiscalPeriod': 'varchar(16)', 'accoutingStandards': 'varchar(32)', 'currencyCD': 'varchar(16)',
              'loanToOthBankFi': 'float', 'tradingFA': 'float', 'intReceiv': 'float', 'purResaleFa': 'float',
              'disburLA': 'float', 'availForSaleFA': 'float', 'htmInvest': 'float', 'LTEquityInvest': 'float',
              'investRealEstate': 'float', 'fixedAssets': 'float', 'CIP': 'float', 'intanAssets': 'float',
              'goodwill': 'float', 'deferTaxAssets': 'float', 'CReserCB': 'float', 'deposInOthBfi': 'float',
              'preciMetals': 'float', 'derivAssets': 'float', 'finanLeaseReceiv': 'float',
              'investAsReceiv': 'float', 'othAssets': 'float', 'AE': 'float', 'AA': 'float', 'TAssets': 'float',
              'CBBorr': 'float', 'depos': 'float', 'loanFrOthBankFi': 'float', 'tradingFL': 'float',
              'soldForRepurFa': 'float', 'payrollPayable': 'float', 'taxesPayable': 'float', 'intPayable': 'float',
              'bondPayable': 'float', 'preferredStockL': 'float', 'perpetualBondL': 'float',
              'estimatedLiab': 'float', 'deferTaxLiab': 'float', 'deposFrOthBfi': 'float', 'derivLiab': 'float',
              'othLiab': 'float', 'LE': 'float', 'LA': 'float', 'TLiab': 'float', 'paidInCapital': 'float',
              'othEquityInstr': 'float', 'preferredStockE': 'float', 'perpetualBondE': 'float',
              'capitalReser': 'float', 'treasuryShare': 'float', 'othCompreIncome': 'float',
              'surplusReser': 'float', 'ordinRiskReser': 'float', 'retainedEarnings': 'float',
              'forexDiffer': 'float', 'SEE': 'float', 'SEA': 'float', 'TEquityAttrP': 'float',
              'minorityInt': 'float', 'othEffectSE': 'float', 'othEffectSA': 'float', 'TShEquity': 'float',
              'LEE': 'float', 'LEA': 'float', 'TLiabEquity': 'float', 'updateTime': 'varchar(64)'}

    tb.create_table('fdmtbsbank', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# balance_2007.py-------------建表已验证
# 银行业资产负债表
def create_table_fdmtbsindu():
    schema = {'secID': 'varchar(32)', 'publishDate': 'long', 'endDate': 'varchar(32)',
              'endDateRep': 'varchar(32)', 'partyID': 'long', 'ticker': 'varchar(16)', 'secShortName': 'varchar(16)',
              'exchangeCD': 'varchar(16)', 'actPubtime': 'varchar(64)', 'mergedFlag': 'varchar(16)',
              'reportType': 'varchar(16)', 'fiscalPeriod': 'varchar(16)', 'accoutingStandards': 'varchar(32)',
              'currencyCD': 'varchar(16)', 'cashCEquiv': 'float', 'settProv': 'float', 'loanToOthBankFi': 'float',
              'tradingFA': 'float', 'derivAssets': 'float', 'NotesReceiv': 'float', 'AR': 'float',
              'prepayment': 'float', 'premiumReceiv': 'float', 'reinsurReceiv': 'float',
              'reinsurReserReceiv': 'float', 'intReceiv': 'float', 'divReceiv': 'float', 'othReceiv': 'float',
              'purResaleFa': 'float', 'inventories': 'float', 'assetsHeldForSale': 'float', 'NCAWithin1Y': 'float',
              'othCA': 'float', 'CAE': 'float', 'CAA': 'float', 'TCA': 'float', 'disburLA': 'float',
              'availForSaleFa': 'float', 'htmInvest': 'float', 'LTReceive': 'float', 'LTEquityInvest': 'float',
              'investRealEstate': 'float', 'fixedAssets': 'float', 'CIP': 'float', 'constMaterials': 'float',
              'fixedAssetsDisp': 'float', 'producBiolAssets': 'float', 'oilAndGasAssets': 'float',
              'intanAssets': 'float', 'RD': 'float', 'goodwill': 'float', 'LTAmorExp': 'float',
              'deferTaxAssets': 'float', 'othNCA': 'float', 'NCAE': 'float', 'NCAA': 'float', 'TNCA': 'float',
              'AE': 'float', 'AA': 'float', 'TAssets': 'float', 'STBorr': 'float', 'CBBorr': 'float',
              'depos': 'float', 'loanFrOthBankFi': 'float', 'tradingFL': 'float', 'derivLiab': 'float',
              'NotesPayable': 'float', 'AP': 'float', 'advanceReceipts': 'float', 'soldForRepurFa': 'float',
              'commisPayable': 'float', 'payrollPayable': 'float', 'taxesPayable': 'float', 'intPayable': 'float',
              'divPayable': 'float', 'othPayable': 'float', 'reinsurPayable': 'float', 'insurReser': 'float',
              'fundsSecTradAgen': 'float', 'fundsSecUndwAgen': 'float', 'liabHeldForSale': 'float',
              'NCLWithin1Y': 'float', 'accruedExp': 'float', 'othCL': 'float', 'CLE': 'float', 'CLA': 'float',
              'TCL': 'float', 'LTBorr': 'float', 'bondPayable': 'float', 'preferredStockL': 'float',
              'perpetualBondL': 'float', 'LTPayable': 'float', 'LTPayrollPayable': 'float',
              'specificPayables': 'float', 'estimatedLiab': 'float', 'deferRevenue': 'float',
              'deferTaxLiab': 'float', 'othNCL': 'float', 'NCLE': 'float', 'NCLA': 'float', 'TNCL': 'float',
              'LE': 'float', 'LA': 'float', 'TLiab': 'float', 'paidInCapital': 'float', 'othEquityInstr': 'float',
              'preferredStockE': 'float', 'perpetualBondE': 'float', 'capitalReser': 'float',
              'treasuryShare': 'float', 'othCompreIncome': 'float', 'specialReser': 'float',
              'surplusReser': 'float', 'ordinRiskReser': 'float', 'retainedEarnings': 'float',
              'forexDiffer': 'float', 'SEE': 'float', 'SEA': 'float', 'TEquityAttrP': 'float',
              'minorityInt': 'float', 'othEffectSE': 'float', 'othEffectSA': 'float', 'TShEquity': 'float',
              'LEE': 'float', 'LEA': 'float', 'TLiabEquity': 'float', 'updateTime': 'varchar(64)'}

    tb.create_table('fdmtbsindu', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# balance_2007.py-------------建表已验证
# 银行业资产负债表
def create_table_fdmtbsinsu():
    schema = {'secID': 'varchar(32)', 'publishDate': 'long', 'endDate': 'varchar(32)',
              'endDateRep': 'varchar(32)', 'partyID': 'long', 'ticker': 'varchar(16)', 'secShortName': 'varchar(16)',
              'exchangeCD': 'varchar(16)', 'actPubtime': 'varchar(64)', 'mergedFlag': 'varchar(16)',
              'reportType': 'varchar(16)', 'fiscalPeriod': 'varchar(16)', 'accoutingStandards': 'varchar(32)',
              'currencyCD': 'varchar(16)', 'cashCEquiv': 'float', 'loanToOthBankFi': 'float', 'tradingFA': 'float',
              'premiumReceiv': 'float', 'reinsurReceiv': 'float', 'intReceiv': 'float', 'purResaleFa': 'float',
              'availForSaleFa': 'float', 'htmInvest': 'float', 'LTEquityInvest': 'float',
              'investRealEstate': 'float', 'fixedAssets': 'float', 'intanAssets': 'float',
              'deferTaxAssets': 'float', 'derivAssets': 'float', 'subrogRecoReceiv': 'float',
              'RRReinsUnePrem': 'float', 'RRReinsOutstdCla': 'float', 'RRReinsLinsLiab': 'float',
              'RRReinsLThinsLiab': 'float', 'PHPledgeLoans': 'float', 'fixedTermDepos': 'float',
              'refundCapDepos': 'float', 'indepAccAssets': 'float', 'othAssets': 'float', 'AE': 'float',
              'AA': 'float', 'TAssets': 'float', 'STBorr': 'float', 'loanFrOthBankFi': 'float',
              'tradingFL': 'float', 'soldForRepurFa': 'float', 'commisPayable': 'float', 'payrollPayable': 'float',
              'taxesPayable': 'float', 'reinsurPayable': 'float', 'LTBorr': 'float', 'bondPayable': 'float',
              'preferredStockL': 'float', 'perpetualBondL': 'float', 'deferTaxLiab': 'float', 'derivLiab': 'float',
              'premReceivAdva': 'float', 'indemAccPayable': 'float', 'policyDivPayable': 'float',
              'PHInvest': 'float', 'reserUnePrem': 'float', 'reserOutstdClaims': 'float', 'reserLinsLiab': 'float',
              'reserLthinsLiab': 'float', 'indeptAccLiab': 'float', 'othLiab': 'float', 'LE': 'float',
              'LA': 'float', 'TLiab': 'float', 'paidInCapital': 'float', 'othEquityInstr': 'float',
              'preferredStockE': 'float', 'perpetualBondE': 'float', 'capitalReser': 'float',
              'treasuryShare': 'float', 'othCompreIncome': 'float', 'surplusReser': 'float',
              'ordinRiskReser': 'float', 'retainedEarnings': 'float', 'forexDiffer': 'float', 'SEE': 'float',
              'SEA': 'float', 'TEquityAttrP': 'float', 'minorityInt': 'float', 'othEffectSE': 'float',
              'othEffectSA': 'float', 'TShEquity': 'float', 'LEE': 'float', 'LEA': 'float',
              'TLiabEquity': 'float', 'updateTime': 'varchar(64)'}

    tb.create_table('fdmtbsinsu', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# balance_2007.py-------------建表已验证
# 银行业资产负债表
def create_table_fdmtbssecu():
    schema = {'secID': 'varchar(32)', 'publishDate': 'long', 'endDate': 'varchar(32)', 'endDateRep': 'varchar(32)',
              'partyID': 'long', 'ticker': 'varchar(16)', 'secShortName': 'varchar(16)', 'exchangeCD': 'varchar(16)',
              'actPubtime': 'varchar(64)', 'mergedFlag': 'varchar(16)', 'reportType': 'varchar(16)',
              'fiscalPeriod': 'varchar(16)', 'accoutingStandards': 'varchar(32)', 'currencyCD': 'varchar(16)',
              'cashCEquiv': 'float', 'clientDepos': 'float', 'settProv': 'float', 'clientProv': 'float',
              'loanToOthBankFi': 'float', 'tradingFA': 'float', 'intReceiv': 'float', 'purResaleFa': 'float',
              'availForSaleFa': 'float', 'htmInvest': 'float', 'LTEquityInvest': 'float',
              'investRealEstate': 'float', 'fixedAssets': 'float', 'intanAssets': 'float',
              'transacSeatFee': 'float', 'deferTaxAssets': 'float', 'derivAssets': 'float', 'refundDepos': 'float',
              'othAssets': 'float', 'AE': 'float', 'AA': 'float', 'TAssets': 'float', 'STBorr': 'float',
              'pledgeBorr': 'float', 'loanFrOthBankFi': 'float', 'tradingFL': 'float', 'soldForRepurFa': 'float',
              'payrollPayable': 'float', 'taxesPayable': 'float', 'intPayable': 'float',
              'fundsSecTradAgen': 'float', 'fundsSecUndwAgen': 'float', 'LTBorr': 'float', 'bondPayable': 'float',
              'preferredStockL': 'float', 'perpetualBondL': 'float', 'estimatedLiab': 'float',
              'deferTaxLiab': 'float', 'derivLiab': 'float', 'othLiab': 'float', 'LE': 'float', 'LA': 'float',
              'TLiab': 'float', 'paidInCapital': 'float', 'othEquityInstr': 'float', 'preferredStockE': 'float',
              'perpetualBondE': 'float', 'capitalReser': 'float', 'treasuryShare': 'float',
              'othCompreIncome': 'float', 'surplusReser': 'float', 'ordinRiskReser': 'float',
              'transacRiskReser': 'float', 'retainedEarnings': 'float', 'forexDiffer': 'float', 'SEE': 'float',
              'SEA': 'float', 'TEquityAttrP': 'float', 'minorityInt': 'float', 'othEffectSE': 'float',
              'othEffectSA': 'float', 'TShEquity': 'float', 'TLiabEquity': 'float', 'updateTime': 'varchar(64)'}

    tb.create_table('fdmtbssecu', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# cashflow.py-------------建表已验证
# 银行业资产负债表
def create_table_fdmtcfbank2018():
    schema = {'partyID': 'long', 'ticker': 'varchar(16)', 'exchangeCD': 'varchar(16)', 'secID': 'varchar(32)',
              'actPubtime': 'varchar(64)', 'publishDate': 'long', 'endDateRep': 'varchar(32)',
              'endDate': 'varchar(32)', 'reportType': 'varchar(16)', 'fiscalPeriod': 'long',
              'mergedFlag': 'varchar(16)', 'accoutingStandards': 'varchar(32)', 'currencyCD': 'varchar(16)',
              'industryCategory': 'varchar(16)', 'nDeposIncrCFI': 'float', 'nIncrBorrFRCB': 'float',
              'nIncBorrOthFI': 'float', 'nDecrInDisburOFLA': 'float', 'netDecrInDeposINFI': 'float',
              'nDecrLoanToOthFI': 'float', 'ifcCashIncr': 'float', 'cFROthOperateA': 'float', 'specOCIF': 'float',
              'AOCIF': 'float', 'cInfFrOperateA': 'float', 'nDeposDecrFRFI': 'float', 'nDecrBorrFRCB': 'float',
              'nDecrBorrFROthFI': 'float', 'nIncDisburOFLA': 'float', 'netIncrDeposINFI': 'float',
              'nIncrLoansToOthFI': 'float', 'cPaidIFC': 'float', 'cPaidToForEmpl': 'float',
              'cPaidForTaxes': 'float', 'cPaidForOthOpA': 'float', 'specOcof': 'float', 'AOCOF': 'float',
              'cOutfOperateA': 'float', 'ANOCF': 'float', 'nCfOperateA': 'float', 'procSellInvest': 'float',
              'gainInvest': 'float', 'dispFixAssetsOth': 'float', 'nDispSubsOthBizC': 'float',
              'cFrOthInvestA': 'float', 'specCIF': 'float', 'ACIF': 'float', 'cInfFrInvestA': 'float',
              'cPaidInvest': 'float', 'purFixAssetsOth': 'float', 'nCPaidAcquis': 'float',
              'cPaidOthInvestA': 'float', 'specCOF': 'float', 'ACOF': 'float', 'cOutfFrInvestA': 'float',
              'ANICF': 'float', 'nCFFRInvestA': 'float', 'cFRCapContr': 'float', 'cFRMinoSSubs': 'float',
              'cFRIssueBond': 'float', 'cFROthFinanA': 'float', 'specFCIF': 'float', 'AFCIF': 'float',
              'cInfFRFinanA': 'float', 'cPaidForDebts': 'float', 'cPaidDivProfInt': 'float',
              'divProfSubsMinoS': 'float', 'cPaidOthFinanA': 'float', 'specFCOF': 'float', 'AFCOF': 'float',
              'cOutFRFinanA': 'float', 'ANFCF': 'float', 'nCFFRFinanA': 'float', 'forexEffects': 'float',
              'othEffectCE': 'float', 'ACE': 'float', 'nChangeInCash': 'float', 'nCEBegBal': 'float',
              'othEffectCEI': 'float', 'ACEI': 'float', 'nCeEndBAL': 'float'}

    tb.create_table('fdmtcfbank2018', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# cashflow.py-------------建表已验证
# 银行业资产负债表
def create_table_fdmtcfindu2018():
    schema = {'partyID': 'long', 'ticker': 'varchar(16)', 'echangeCD': 'varchar(16)', 'secID': 'varchar(32)',
              'secShortName': 'varchar(16)', 'actPubtime': 'varchar(64)', 'publishDate': 'long',
              'endDateRep': 'varchar(32)', 'endDate': 'varchar(32)', 'reportType': 'varchar(16)',
              'fiscalPeriod': 'long', 'mergedFlag': 'varchar(16)', 'accountingStand': 'varchar(32)',
              'currencyCD': 'varchar(16)', 'industryCategory': 'varchar(16)', 'cFRSaleGS': 'float',
              'nDeposIncrCFI': 'float', 'nIncrBorrFRCB': 'float', 'nIncBorrOthFI': 'float',
              'premFROrigContr': 'float', 'nReinsurPrem': 'float', 'nIncPHDeposInv': 'float',
              'nIncDispTradFA': 'float', 'ifcCashIncr': 'float', 'nIncFRBorr': 'float', 'nCapIncrRepur': 'float',
              'refundOFTax': 'float', 'cFROthOperA': 'float', 'specOCIF': 'float', 'AOCIF': 'float',
              'cInfFROperA': 'float', 'cPaidFROperA': 'float', 'nIncDisburOFLA': 'float',
              'netIncrDeposINFI': 'float', 'origContrCIndem': 'float', 'cPaidIFC': 'float', 'cPaidPOLDiv': 'float',
              'cPaidToForEmpl': 'float', 'cPaidForTaxex': 'float', 'cPaidForOthOPA': 'float', 'specOCOF': 'float',
              'AOCOF': 'float', 'cOutfOperA': 'float', 'ANOCF': 'float', 'nCFOperA': 'float',
              'procSellInvest': 'float', 'gainInvest': 'float', 'dispFixAssetsOth': 'float',
              'nDispSubsOthBIZC': 'float', 'cFROthInvestA': 'float', 'specCIF': 'float', 'ACIF': 'float',
              'cInfFRInvestA': 'float', 'purFixAssetsOth': 'float', 'cPaidInvest': 'float',
              'nIncrPledgeLoan': 'float', 'nCPaidAcquis': 'float', 'cPaidPOthInvestA': 'float', 'specCOF': 'float',
              'ACOF': 'float', 'cOutfFRInvestA': 'float', 'ANICF': 'float', 'nCFFRInvestA': 'float',
              'cFRCapContr': 'float', 'cFRMinoSSubs': 'float', 'cFRBorr': 'float', 'cFRIssueBond': 'float',
              'cFROthFinanA': 'float', 'specFCIF': 'float', 'AFCIF': 'float', 'cInfFRFinanA': 'float',
              'cPaidForDebts': 'float', 'cPaidDivProfInt': 'float', 'divProfSubsMinoS': 'float',
              'cPaidOthFinanA': 'float', 'specFCOF': 'float', 'AFCOF': 'float', 'cOutfFRFinanA': 'float',
              'ANFCF': 'float', 'nCFFRFinanA': 'float', 'forexEffects': 'float', 'othEffectCE': 'float',
              'ACE': 'float', 'nChangeInCash': 'float', 'nCEBegBAL': 'float', 'othEffectCEI': 'float',
              'ACEI': 'float', 'nCEEndBal': 'float'}

    tb.create_table('fdmtcfindu2018', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# cashflow.py-------------建表已验证
# 银行业资产负债表
def create_table_fdmtcfinsu2018():
    schema = {'partyID': 'long', 'ticker': 'varchar(16)', 'echangeCD': 'varchar(16)', 'secID': 'varchar(32)',
              'secShortName': 'varchar(16)', 'actPubtime': 'varchar(64)', 'publishDate': 'long',
              'endDateRep': 'varchar(32)', 'endDate': 'varchar(32)', 'reportType': 'varchar(16)',
              'fiscalPeriod': 'long', 'mergedFlag': 'varchar(16)', 'accountingStand': 'varchar(32)',
              'currencyCD': 'varchar(16)', 'industryCategory': 'varchar(16)', 'nDeposIncrCFI': 'float',
              'nIncrBorrFRCB': 'float', 'premFROrigContr': 'float', 'nReinsurPrem': 'float',
              'nIncPHDeposInv': 'float', 'ifcCashIncr': 'float', 'refundOFTax': 'float', 'cFROthOperateA': 'float',
              'specOCIF': 'float', 'AOCIF': 'float', 'cInfFROperateA': 'float', 'nIncDisburOFLA': 'float',
              'netIncrDeposINFI': 'float', 'origContrCIndem': 'float', 'cPaidIFC': 'float', 'cPaidPolDiv': 'float',
              'cPaidToForEmpl': 'float', 'cPaidForTaxes': 'float', 'cPaidForOthOpA': 'float', 'specOCOF': 'float',
              'AOCOF': 'float', 'cOutfOperateA': 'float', 'ANOCF': 'float', 'nCFOperateA': 'float',
              'procSellInvest': 'float', 'gainInvest': 'float', 'dispFixAssetsOth': 'float',
              'nDispSubsOthBIZC': 'float', 'cFROthInvestA': 'float', 'specCIF': 'float', 'ACIF': 'float',
              'cInfFRInvestA': 'float', 'purFixAssetsOth': 'float', 'cPaidInvest': 'float',
              'nIncrPledgeLoan': 'float', 'nCPaidAcquis': 'float', 'cPaidOthInvestA': 'float', 'specCOF': 'float',
              'ACOF': 'float', 'cOutfFRInvestA': 'float', 'ANICF': 'float', 'nCFFRInvestA': 'float',
              'cFRCapContr': 'float', 'cFRMinoSSubs': 'float', 'cFRBorr': 'float', 'cFRIssueBond': 'float',
              'cFROthFinanA': 'float', 'specFCIF': 'float', 'AFCIF': 'float', 'cInfFRFinanA': 'float',
              'cPaidForDebts': 'float', 'cPaidDivProfInt': 'float', 'divProfSubsMinoS': 'float',
              'cPaidOthFinanA': 'float', 'specFCOF': 'float', 'AFCOF': 'float', 'cOutfFRFinanA': 'float',
              'ANFCF': 'float', 'nCFFRFinanA': 'float', 'forexEffects': 'float', 'othEffectCE': 'float',
              'ACE': 'float', 'nChangeInCash': 'float', 'nCEBegBal': 'float', 'othEffectCEI': 'float',
              'ACEI': 'float', 'nCeEndBal': 'float'}

    tb.create_table('fdmtcfinsu2018', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# cashflow.py-------------建表已验证
# 银行业资产负债表
def create_table_fdmtcfsecu2018():
    schema = {'partyID': 'long', 'ticker': 'varchar(16)', 'exchangeCD': 'varchar(16)', 'secID': 'varchar(32)',
              'secShortName': 'varchar(16)', 'actPubtime': 'varchar(64)', 'publishDate': 'long',
              'endDateRep': 'varchar(32)', 'endDate': 'varchar(32)', 'reportType': 'varchar(16)',
              'fiscalPeriod': 'long', 'mergedFlag': 'varchar(16)', 'accountingStand': 'varchar(32)',
              'currencyCD': 'varchar(16)', 'industryCategory': 'varchar(16)', 'nIncBorrOthFI': 'float',
              'nIncDispTradFA': 'float', 'nIncDispFAFS': 'float', 'ifcCashIncr': 'float', 'nIncFRBorr': 'float',
              'nCAPIncrRepur': 'float', 'reFundOfTax': 'float', 'cFROthOperateA': 'float', 'specOCIF': 'float',
              'AOCIF': 'float', 'cInfFROperateA': 'float', 'cPaidIFC': 'float', 'cPaidToForEmpl': 'float',
              'cPaidForTaxes': 'float', 'cPaidForOthOpA': 'float', 'specOCOF': 'float', 'AOCOF': 'float',
              'cOutfOperateA': 'float', 'ANOCF': 'float', 'nCFOperateA': 'float', 'procSellInvest': 'float',
              'gainInvest': 'float', 'dispFixAssetsOth': 'float', 'nDispSubsOthBIZC': 'float',
              'cFROthInvestA': 'float', 'specCIF': 'float', 'ACIF': 'float', 'cInfFRInvestA': 'float',
              'purFixAssetsOth': 'float', 'cPaidInvest': 'float', 'nCPaidAcquis': 'float',
              'cPaidOthInvestA': 'float', 'specCOF': 'float', 'ACOF': 'float', 'cOutfFRInvestA': 'float',
              'ANICF': 'float', 'nCFFRInvestA': 'float', 'cFRCapContr': 'float', 'cFRMinoSSubs': 'float',
              'cFRBorr': 'float', 'cFRIssueBond': 'float', 'cFROthFinanA': 'float', 'specFCIF': 'float',
              'AFCIF': 'float', 'cINFFRFinanA': 'float', 'cPaidForDebts': 'float', 'cPaidDivProfInt': 'float',
              'divProfSubsMinoS': 'float', 'cPaidOthFinanA': 'float', 'specFCOF': 'float', 'AFCOF': 'float',
              'cOutfFRFinanA': 'float', 'ANFCF': 'float', 'nCFFRFinanA': 'float', 'forexEffects': 'float',
              'othEffectCE': 'float', 'ACE': 'float', 'nChangeInCash': 'float', 'nCEBegBal': 'float',
              'othEffectCEI': 'float', 'ACEI': 'float', 'nCEEndBal': 'float'}

    tb.create_table('fdmtcfsecu2018', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# cashflow_2007.py-------------建表已验证
# 银行业资产负债表
def create_table_fdmtcfbank():
    schema = {'secID': 'varchar(32)', 'publishDate': 'long', 'endDate': 'varchar(32)', 'endDateRep': 'varchar(32)',
              'partyID': 'long', 'ticker': 'varchar(16)', 'secShortName': 'varchar(16)', 'exchangeCD': 'varchar(16)',
              'actPubtime': 'varchar(64)', 'mergedFlag': 'varchar(16)', 'reportType': 'varchar(16)',
              'fiscalPeriod': 'varchar(16)', 'accoutingStandards': 'varchar(32)', 'currencyCD': 'varchar(16)',
              'NDeposIncrCFI': 'float', 'NIncrBorrFrCB': 'float', 'NIncBorrOthFI': 'float',
              'NDecrInDisburOfLa': 'float', 'NDecrInDeposInFI': 'float', 'NDecrLoanToOthFI': 'float',
              'IFCCashIncr': 'float', 'CFrOthOperateA': 'float', 'specOCIF': 'float', 'AOCIF': 'float',
              'CInfFrOperateA': 'float', 'NDeposDecrFrFI': 'float', 'NDecrBorrFrCB': 'float',
              'NDecrBorrFrOthFI': 'float', 'NIncDisburOfLA': 'float', 'NIncrDeposInFI': 'float',
              'NIncrLoansToOthFi': 'float', 'CPaidIFC': 'float', 'CPaidToForEmpl': 'float',
              'CPaidForTaxes': 'float', 'CPaidForOthOpA': 'float', 'specOCOF': 'float', 'AOCOF': 'float',
              'COutfOperateA': 'float', 'ANOCF': 'float', 'NCFOperateA': 'float', 'procSellInvest': 'float',
              'gainInvest': 'float', 'dispFixAssetsOth': 'float', 'NDispSubsOthBizC': 'float',
              'CFrOthInvestA': 'float', 'specICIF': 'float', 'AICIF': 'float', 'CInfFrInvestA': 'float',
              'purFixAssetsOth': 'float', 'CPaidInvest': 'float', 'NCPaidAcquis': 'float',
              'CPaidOthInvestA': 'float', 'specICOF': 'float', 'AICOF': 'float', 'COutfFrInvestA': 'float',
              'ANICF': 'float', 'NCFFrInvestA': 'float', 'CFrCapContr': 'float', 'CFrMinoSSubs': 'float',
              'CFrIssueBond': 'float', 'CFrOthFinanA': 'float', 'specFCIF': 'float', 'AFCIF': 'float',
              'CInfFrFinanA': 'float', 'CPaidForDebts': 'float', 'CPaidDivProfInt': 'float',
              'divProfSubsMinoS': 'float', 'CPaidOthFinanA': 'float', 'specFCOF': 'float', 'AFCOF': 'float',
              'COutfFrFinanA': 'float', 'ANFCF': 'float', 'NCFFrFinanA': 'float', 'forexEffects': 'float',
              'othEffectCE': 'float', 'ACE': 'float', 'NChangeInCash': 'float', 'NCEBegBal': 'float',
              'othEffectCEI': 'float', 'ACEI': 'float', 'NCEEndBal': 'float', 'updateTime': 'varchar(64)'}

    tb.create_table('fdmtcfbank', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# cashflow_2007.py-------------建表已验证
# 银行业资产负债表
def create_table_fdmtcfindu():
    schema = {'secID': 'varchar(32)', 'publishDate': 'long', 'endDate': 'varchar(32)', 'endDateRep': 'varchar(32)',
              'partyID': 'long', 'ticker': 'varchar(16)', 'secShortName': 'varchar(16)', 'exchangeCD': 'varchar(16)',
              'actPubtime': 'varchar(64)', 'mergedFlag': 'varchar(16)', 'reportType': 'varchar(16)',
              'fiscalPeriod': 'varchar(16)', 'accoutingStandards': 'varchar(32)', 'currencyCD': 'varchar(16)',
              'CFrSaleGS': 'float', 'NDeposIncrCFI': 'float', 'NIncrBorrFrCB': 'float', 'NIncBorrOthFI': 'float',
              'premFrOrigContr': 'float', 'NReinsurPrem': 'float', 'NIncPhDeposInv': 'float',
              'NIncDispTradFA': 'float', 'IFCCashIncr': 'float', 'NIncFrBorr': 'float', 'NCApIncrRepur': 'float',
              'refundOfTax': 'float', 'CFrOthOperateA': 'float', 'specOCIF': 'float', 'AOCIF': 'float',
              'CInfFrOperateA': 'float', 'CPaidGS': 'float', 'NIncDisburOfLA': 'float', 'NIncrDeposInFI': 'float',
              'origContrCIndem': 'float', 'CPaidIFC': 'float', 'CPaidPolDiv': 'float', 'CPaidToForEmpl': 'float',
              'CPaidForTaxes': 'float', 'CPaidForOthOpA': 'float', 'specOCOF': 'float', 'AOCOF': 'float',
              'COutfOperateA': 'float', 'ANOCF': 'float', 'NCFOperateA': 'float', 'procSellInvest': 'float',
              'gainInvest': 'float', 'dispFixAssetsOth': 'float', 'NDispSubsOthBizC': 'float',
              'CFrOthInvestA': 'float', 'specICIF': 'float', 'AICIF': 'float', 'CInfFrInvestA': 'float',
              'purFixAssetsOth': 'float', 'CPaidInvest': 'float', 'NIncrPledgeLoan': 'float',
              'NCPaidAcquis': 'float', 'CPaidOthInvestA': 'float', 'specICOF': 'float', 'AICOF': 'float',
              'COutfFrInvestA': 'float', 'ANICF': 'float', 'NCFFrInvestA': 'float', 'CFrCapContr': 'float',
              'CFrMinoSSubs': 'float', 'CFrBorr': 'float', 'CFrIssueBond': 'float', 'CFrOthFinanA': 'float',
              'specFCIF': 'float', 'AFCIF': 'float', 'CInfFrFinanA': 'float', 'CPaidForDebts': 'float',
              'CPaidDivProfInt': 'float', 'divProfSubsMinoS': 'float', 'CPaidOthFinanA': 'float',
              'specFCOF': 'float', 'AFCOF': 'float', 'COutfFrFinanA': 'float', 'ANFCF': 'float',
              'NCFFrFinanA': 'float', 'forexEffects': 'float', 'othEffectCE': 'float', 'ACE': 'float',
              'NChangeInCash': 'float', 'NCEBegBal': 'float', 'othEffectCEI': 'float', 'ACEI': 'float',
              'NCEEndBal': 'float', 'updateTime': 'varchar(64)'}

    tb.create_table('fdmtcfindu', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# cashflow_2007.py-------------建表已验证
# 银行业资产负债表
def create_table_fdmtcfsecu():
    schema = {'secID': 'varchar(32)', 'publishDate': 'long', 'endDate': 'varchar(32)', 'endDateRep': 'varchar(32)',
              'partyID': 'long', 'ticker': 'varchar(16)', 'secShortName': 'varchar(16)', 'exchangeCD': 'varchar(16)',
              'actPubtime': 'varchar(64)', 'mergedFlag': 'varchar(16)', 'reportType': 'varchar(16)',
              'fiscalPeriod': 'varchar(16)', 'accoutingStandards': 'varchar(32)', 'currencyCD': 'varchar(16)',
              'NIncBorrOthFI': 'float', 'NIncDispTradFA': 'float', 'NIncDispFaFS': 'float', 'IFCCashIncr': 'float',
              'NIncFrBorr': 'float', 'NCApIncrRepur': 'float', 'refundOfTax': 'float', 'CFrOthOperateA': 'float',
              'specOCIF': 'float', 'AOCIF': 'float', 'CInfFrOperateA': 'float', 'CPaidIFC': 'float',
              'CPaidToForEmpl': 'float', 'CPaidForTaxes': 'float', 'CPaidForOthOpA': 'float', 'specOCOF': 'float',
              'AOCOF': 'float', 'COutfOperateA': 'float', 'ANOCF': 'float', 'NCFOperateA': 'float',
              'procSellInvest': 'float', 'gainInvest': 'float', 'dispFixAssetsOth': 'float',
              'NDispSubsOthBizC': 'float', 'CFrOthInvestA': 'float', 'specICIF': 'float', 'AICIF': 'float',
              'CInfFrInvestA': 'float', 'purFixAssetsOth': 'float', 'CPaidInvest': 'float', 'NCPaidAcquis': 'float',
              'CPaidOthInvestA': 'float', 'specICOF': 'float', 'AICOF': 'float', 'COutfFrInvestA': 'float',
              'ANICF': 'float', 'NCFFrInvestA': 'float', 'CFrCapContr': 'float', 'CFrMinoSSubs': 'float',
              'CFrBorr': 'float', 'CFrIssueBond': 'float', 'CFrOthFinanA': 'float', 'specFCIF': 'float',
              'AFCIF': 'float', 'CInfFrFinanA': 'float', 'CPaidForDebts': 'float', 'CPaidDivProfInt': 'float',
              'divProfSubsMinoS': 'float', 'CPaidOthFinanA': 'float', 'specFCOF': 'float', 'AFCOF': 'float',
              'COutfFrFinanA': 'float', 'ANFCF': 'float', 'NCFFrFinanA': 'float', 'forexEffects': 'float',
              'othEffectCE': 'float', 'ACE': 'float', 'NChangeInCash': 'float', 'NCEBegBal': 'float',
              'othEffectCEI': 'float', 'ACEI': 'float', 'NCEEndBal': 'float', 'updateTime': 'varchar(64)'}

    tb.create_table('fdmtcfsecu', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# cashflow_2007.py-------------建表已验证
# 银行业资产负债表
def create_table_fdmtcfinsu():
    schema = {'secID': 'varchar(32)', 'publishDate': 'long', 'endDate': 'varchar(32)', 'endDateRep': 'varchar(32)',
              'partyID': 'long', 'ticker': 'varchar(16)', 'secShortName': 'varchar(16)', 'exchangeCD': 'varchar(16)',
              'actPubtime': 'varchar(64)', 'mergedFlag': 'varchar(16)', 'reportType': 'varchar(16)',
              'fiscalPeriod': 'varchar(16)', 'accoutingStandards': 'varchar(32)', 'currencyCD': 'varchar(16)',
              'NDeposIncrCFI': 'float', 'NIncrBorrFrCB': 'float', 'premFrOrigContr': 'float',
              'NReinsurPrem': 'float', 'NIncPhDeposInv': 'float', 'IFCCashIncr': 'float', 'refundOfTax': 'float',
              'CFrOthOperateA': 'float', 'specOCIF': 'float', 'AOCIF': 'float', 'CInfFrOperateA': 'float',
              'NIncDisburOfLA': 'float', 'NIncrDeposInFI': 'float', 'origContrCIndem': 'float',
              'CPaidIFC': 'float', 'CPaidPolDiv': 'float', 'CPaidToForEmpl': 'float', 'CPaidForTaxes': 'float',
              'CPaidForOthOpA': 'float', 'specOCOF': 'float', 'AOCOF': 'float', 'COutfOperateA': 'float',
              'ANOCF': 'float', 'NCFOperateA': 'float', 'procSellInvest': 'float', 'gainInvest': 'float',
              'dispFixAssetsOth': 'float', 'NDispSubsOthBizC': 'float', 'CFrOthInvestA': 'float',
              'specICIF': 'float', 'AICIF': 'float', 'CInfFrInvestA': 'float', 'PurFixAssetsOth': 'float',
              'CPaidInvest': 'float', 'NIncrPledgeLoan': 'float', 'NCPaidAcquis': 'float',
              'CPaidOthInvestA': 'float', 'specICOF': 'float', 'AICOF': 'float', 'COutfFrInvestA': 'float',
              'ANICF': 'float', 'NCFFrInvestA': 'float', 'CFrCapContr': 'float', 'CFrMinoSSubs': 'float',
              'CFrBorr': 'float', 'CFrIssueBond': 'float', 'CFrOthFinanA': 'float', 'specFCIF': 'float',
              'AFCIF': 'float', 'CInfFrFinanA': 'float', 'CPaidForDebts': 'float', 'CPaidDivProfInt': 'float',
              'divProfSubsMinoS': 'float', 'CPaidOthFinanA': 'float', 'specFCOF': 'float', 'AFCOF': 'float',
              'COutfFrFinanA': 'float', 'ANFCF': 'float', 'NCFFrFinanA': 'float', 'forexEffects': 'float',
              'othEffectCE': 'float', 'ACE': 'float', 'NChangeInCash': 'float', 'NCEBegBal': 'float',
              'othEffectCEI': 'float', 'ACEI': 'float', 'NCEEndBal': 'float', 'updateTime': 'varchar(64)'}

    tb.create_table('fdmtcfinsu', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# classify.py--sectyperel---api核对到这里了
# (新)合并资产负债表
def create_table_sectyperel():
    schema = {"date":"long", 'typeID':'varchar(64)', 'typeName':'varchar(32)', 'secID':'varchar(64)',
              'ticker':'varchar(64)', 'exchangeCD':'varchar(16)','secShortName':'varchar(128)'}

    tb.create_table('sectyperel', schema, 'date', 'time_colunm', 'security_column', 0)


# classify.py--industrystd---已完成验证
# (新)合并资产负债表
def create_table_industrystd():
    schema = {"date":"long", 'industryVersionCD':'varchar(16)', 'industryVersion':'varchar(16)', 'industry':'varchar(32)',
              'industryID':'varchar(16)', 'industrySymbol':'varchar(16)','industryName':'varchar(64)',
              'industryLevel':'float', 'isNew':'long', 'indexSymbol':'varchar(16)', 'prntIndustryID':'varchar(16)',
              'beginDate':'varchar(16)', 'endDate':'float', 'updateTime':'varchar(32)'}

    tb.create_table('industrystd', schema, 'date', 'time_colunm', 'security_column', 0)


# classify.py--equindustry---已完成验证
# (新)合并资产负债表
def create_table_equindustry():
    schema = {"date":"long",'secID':'varchar(32)', 'ticker':'varchar(16)', 'exchangeCD':'varchar(16)',
              'secShortName':'varchar(16)', 'secFullName':'varchar(64)','partyID':'long',
              'industryVersionCD':'varchar(16)', 'industry':'varchar(32)', 'industryID':'varchar(32)',
              'industrySymbol':'varchar(16)', 'intoDate':'varchar(32)', 'outDate':'varchar(16)', 'isNew':'long',
              'industryID1':'varchar(16)', 'industryName1':'varchar(32)', 'industryID2':'varchar(32)',
              'industryName2':'varchar(64)', 'industryID3':'varchar(32)', 'industryName3':'varchar(64)',
              'IndustryID4':'varchar(32)', 'IndustryName4':'varchar(32)', 'equType':'varchar(16)'}

    tb.create_table('equindustry', schema, 'date', 'time_colunm', 'security_column', 0)


# companyInfo.py
def create_table_partyid():
    schema = {'date': 'long', 'partyID': 'long', 'partyFullName': 'varchar(64)', 'partyFullNameEn': 'varchar(256)',
              'partyShortName': 'varchar(64)', 'partyShortNameEn': 'varchar(128)', 'officeAddr': 'varchar(256)',
              'primeOperating': 'varchar(2048)', 'partyNatureCD': 'varchar(16)', 'instStatus': 'float',
              'isIssBond': 'varchar(16)', 'regDate': 'varchar(32)', 'legalRep': 'varchar(64)',
              'regCountryCD': 'varchar(16)', 'regProvince': 'varchar(16)', 'regCity': 'varchar(16)',
              'regAddr': 'varchar(256)', 'regCap': 'float', 'regCapCurrCD': 'varchar(16)', 'email': 'varchar(256)',
              'website': 'varchar(128)', 'tel': 'varchar(128)', 'fax': 'varchar(128)', 'boardSecry': 'varchar(64)',
              'genMana': 'varchar(64)', 'opaScope': 'varchar(4096)', 'legalEntityID': 'varchar(64)',
              'isIssMf': 'float', 'closeDate': 'varchar(30)', 'profile': 'varchar(8574)'}

    tb.create_table('partyid', schema, 'date', 'time_colunm', 'security_column', 0)


# div.py
def create_table_equdiv():
    schema = {'secID': 'varchar(33)', 'ticker': 'varchar(18)', 'exchangeCD': 'varchar(12)',
              'secShortName': 'varchar(15)', 'endDate': 'varchar(30)', 'publishDate': 'long', 'eventProcessCD': 'long',
              'perShareDivRatio': 'float', 'perShareTransRatio': 'float', 'perCashDiv': 'float',
              'perCashDivAfTax': 'float', 'currencyCD': 'varchar(9)', 'frPerCashDiv': 'float',
              'frPerCashDivAfTax': 'float', 'frCurrencyCD': 'varchar(9)', 'recordDate': 'varchar(30)',
              'exDivDate': 'varchar(30)', 'bLastTradeDate': 'float', 'payCashDate': 'varchar(30)',
              'bonusShareListDate': 'varchar(30)', 'ftdAfExdiv': 'varchar(30)', 'sharesBfDiv': 'float',
              'sharesAfDiv': 'float'}

    tb.create_table('equdiv', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# div_eval.py
def create_table_mktequdeval():
    schema = {'secID': 'varchar(32)', 'ticker': 'varchar(16)', 'secShortName': 'varchar(16)',
              'exchangeCD': 'varchar(16)', 'tradeDate': 'long', 'marketValue': 'float',
              'negMarketValue': 'float', 'PE': 'float', 'PE1': 'float', 'PE2': 'float', 'PB': 'float',
              'PS': 'float', 'PS1': 'float', 'PCF': 'float', 'PCF1': 'float', 'PCF2': 'float', 'PCF3': 'float',
              'EV': 'float', 'EVEBITDA': 'float', 'EVSales': 'float', 'updateTime': 'varchar(64)'}

    tb.create_table('mktequdeval', schema, 'tradeDate', 'time_colunm', 'security_column', 0)


# equ_limit.py
def create_table_mktlimit():
    schema = {'secID': 'varchar(32)', 'ticker': 'varchar(16)', 'secShortName': 'varchar(64)',
              'secShortNameEn': 'varchar(256)', 'exchangeCD': 'varchar(16)', 'tradeDate': 'long',
              'limitUpPrice': 'float', 'limitDownPrice': 'float', 'upLimitReachedTimes': 'long',
              'downLimitReachedTimes': 'long'}

    tb.create_table('mktlimit', schema, 'tradeDate', 'time_colunm', 'security_column', 0)


# equ_min.py  ---- 未搞----- 分钟级
def create_table_mktlimit():
    schema = {'secID': 'varchar(32)', 'ticker': 'varchar(16)', 'secShortName': 'varchar(64)',
              'secShortNameEn': 'varchar(256)', 'exchangeCD': 'varchar(16)', 'tradeDate': 'long',
              'limitUpPrice': 'float', 'limitDownPrice': 'float', 'upLimitReachedTimes': 'long',
              'downLimitReachedTimes': 'long'}

    tb.create_table('mktlimit', schema, 'tradeDate', 'time_colunm', 'security_column', 0)


# equdind.py
def create_table_mktequdind():
    schema = {'secID': 'varchar(32)', 'ticker': 'varchar(16)', 'tradeDate': 'long', 'secShortName': 'varchar(16)',
              'exchangeCD': 'varchar(16)', 'chgStatus': 'long', 'conChg': 'long', 'conLimit': 'long', 'days1': 'long',
              'days2': 'long', 'days3': 'long', 'days4': 'long', 'chgPct3': 'float', 'turnRate3': 'float',
              'dealValue': 'float', 'dealValue20': 'float', 'updateTime': 'varchar(64)'}

    tb.create_table('mktequdind', schema, 'tradeDate', 'time_colunm', 'security_column', 0)


# equPledge.py
def create_table_equpledge():
    schema = {'partyID': 'long', 'secID': 'varchar(33)', 'ticker': 'varchar(18)', 'secShortName': 'varchar(18)',
              'exchangeCD': 'varchar(12)', 'publishDate': 'long', 'shName': 'varchar(108)',
              'shNameType': 'varchar(15)', 'orgName': 'varchar(135)', 'involvesum': 'float', 'pledgeShare': 'float',
              'shareType': 'float', 'isCollateralRepo': 'long', 'holdVol': 'float', 'holdPct': 'float',
              'accPledge': 'float', 'accPledgeShare': 'float', 'accPledgeTotal': 'float', 'beginDate': 'varchar(30)',
              'endDate': 'varchar(30)', 'thawDate': 'varchar(30)', 'isThaw': 'long', 'statement': 'varchar(2397)',
              'eventNum': 'varchar(39)', 'updateTime': 'varchar(57)'}

    tb.create_table('equpledge', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# equStockPledge.py
def create_table_equstockpledg():
    schema = {'secID': 'varchar(64)', 'ticker': 'varchar(32)', 'secShortName': 'varchar(16)',
              'exchangeCD': 'varchar(16)', 'publishDate': 'long', 'nPledgedShares': 'float',
              'yPledgedShares': 'float', 'aTotalShares': 'float', 'pledgeNumber': 'float', 'pledgeRatio': 'float',
              'updateTime': 'varchar(64)'}

    tb.create_table('equstockpledg', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# factor.py
def create_table_factorinfo():
    schema = {'secID': 'varchar(33)', 'ticker': 'varchar(18)', 'tradeDate': 'long', 'AccountsPayablesTDays': 'float',
              'AccountsPayablesTRate': 'float', 'AdminiExpenseRate': 'float', 'ARTDays': 'float',
              'ARTRate': 'float', 'ASSI': 'float', 'BLEV': 'float', 'BondsPayableToAsset': 'float',
              'CashRateOfSales': 'float', 'CashToCurrentLiability': 'float', 'CMRA': 'float', 'CTOP': 'float',
              'CTP5': 'float', 'CurrentAssetsRatio': 'float', 'CurrentAssetsTRate': 'float',
              'CurrentRatio': 'float', 'DAVOL10': 'float', 'DAVOL20': 'float', 'DAVOL5': 'float', 'DDNBT': 'float',
              'DDNCR': 'float', 'DDNSR': 'float', 'DebtEquityRatio': 'float', 'DebtsAssetRatio': 'float',
              'DHILO': 'float', 'DilutedEPS': 'float', 'DVRAT': 'float', 'EBITToTOR': 'float', 'EGRO': 'float',
              'EMA10': 'float', 'EMA120': 'float', 'EMA20': 'float', 'EMA5': 'float', 'EMA60': 'float',
              'EPS': 'float', 'EquityFixedAssetRatio': 'float', 'EquityToAsset': 'float', 'EquityTRate': 'float',
              'ETOP': 'float', 'ETP5': 'float', 'FinancialExpenseRate': 'float', 'FinancingCashGrowRate': 'float',
              'FixAssetRatio': 'float', 'FixedAssetsTRate': 'float', 'GrossIncomeRatio': 'float', 'HBETA': 'float',
              'HSIGMA': 'float', 'IntangibleAssetRatio': 'float', 'InventoryTDays': 'float',
              'InventoryTRate': 'float', 'InvestCashGrowRate': 'float', 'LCAP': 'float', 'LFLO': 'float',
              'LongDebtToAsset': 'float', 'LongDebtToWorkingCapital': 'float', 'LongTermDebtToAsset': 'float',
              'MA10': 'float', 'MA120': 'float', 'MA20': 'float', 'MA5': 'float', 'MA60': 'float',
              'MAWVAD': 'float', 'MFI': 'float', 'MLEV': 'float', 'NetAssetGrowRate': 'float',
              'NetProfitGrowRate': 'float', 'NetProfitRatio': 'float', 'NOCFToOperatingNI': 'float',
              'NonCurrentAssetsRatio': 'float', 'NPParentCompanyGrowRate': 'float', 'NPToTOR': 'float',
              'OperatingExpenseRate': 'float', 'OperatingProfitGrowRate': 'float', 'OperatingProfitRatio': 'float',
              'OperatingProfitToTOR': 'float', 'OperatingRevenueGrowRate': 'float', 'OperCashGrowRate': 'float',
              'OperCashInToCurrentLiability': 'float', 'PB': 'float', 'PCF': 'float', 'PE': 'float', 'PS': 'float',
              'PSY': 'float', 'QuickRatio': 'float', 'REVS10': 'float', 'REVS20': 'float', 'REVS5': 'float',
              'ROA': 'float', 'ROA5': 'float', 'ROE': 'float', 'ROE5': 'float', 'RSI': 'float', 'RSTR12': 'float',
              'RSTR24': 'float', 'SalesCostRatio': 'float', 'SaleServiceCashToOR': 'float', 'SUE': 'float',
              'TaxRatio': 'float', 'TOBT': 'float', 'TotalAssetGrowRate': 'float', 'TotalAssetsTRate': 'float',
              'TotalProfitCostRatio': 'float', 'TotalProfitGrowRate': 'float', 'VOL10': 'float', 'VOL120': 'float',
              'VOL20': 'float', 'VOL240': 'float', 'VOL5': 'float', 'VOL60': 'float', 'WVAD': 'float',
              'REC': 'float', 'DAREC': 'float', 'GREC': 'float', 'FY12P': 'float', 'DAREV': 'float',
              'GREV': 'float', 'SFY12P': 'float', 'DASREV': 'float', 'GSREV': 'float', 'FEARNG': 'float',
              'FSALESG': 'float', 'TA2EV': 'float', 'CFO2EV': 'float', 'ACCA': 'float', 'DEGM': 'float',
              'SUOI': 'float', 'EARNMOM': 'float', 'FiftyTwoWeekHigh': 'float', 'Volatility': 'float',
              'Skewness': 'float', 'ILLIQUIDITY': 'float', 'BackwardADJ': 'float', 'MACD': 'float',
              'ADTM': 'float', 'ATR14': 'float', 'ATR6': 'float', 'BIAS10': 'float', 'BIAS20': 'float',
              'BIAS5': 'float', 'BIAS60': 'float', 'BollDown': 'float', 'BollUp': 'float', 'CCI10': 'float',
              'CCI20': 'float', 'CCI5': 'float', 'CCI88': 'float', 'KDJ_K': 'float', 'KDJ_D': 'float',
              'KDJ_J': 'float', 'ROC6': 'float', 'ROC20': 'float', 'SBM': 'float', 'STM': 'float',
              'UpRVI': 'float', 'DownRVI': 'float', 'RVI': 'float', 'SRMI': 'float', 'ChandeSD': 'float',
              'ChandeSU': 'float', 'CMO': 'float', 'DBCD': 'float', 'ARC': 'float', 'OBV': 'float',
              'OBV6': 'float', 'OBV20': 'float', 'TVMA20': 'float', 'TVMA6': 'float', 'TVSTD20': 'float',
              'TVSTD6': 'float', 'VDEA': 'float', 'VDIFF': 'float', 'VEMA10': 'float', 'VEMA12': 'float',
              'VEMA26': 'float', 'VEMA5': 'float', 'VMACD': 'float', 'VOSC': 'float', 'VR': 'float',
              'VROC12': 'float', 'VROC6': 'float', 'VSTD10': 'float', 'VSTD20': 'float',
              'KlingerOscillator': 'float', 'MoneyFlow20': 'float', 'AD': 'float', 'AD20': 'float', 'AD6': 'float',
              'CoppockCurve': 'float', 'ASI': 'float', 'ChaikinOscillator': 'float', 'ChaikinVolatility': 'float',
              'EMV14': 'float', 'EMV6': 'float', 'plusDI': 'float', 'minusDI': 'float', 'ADX': 'float',
              'ADXR': 'float', 'Aroon': 'float', 'AroonDown': 'float', 'AroonUp': 'float', 'DEA': 'float',
              'DIFF': 'float', 'DDI': 'float', 'DIZ': 'float', 'DIF': 'float', 'MTM': 'float', 'MTMMA': 'float',
              'PVT': 'float', 'PVT6': 'float', 'PVT12': 'float', 'TRIX5': 'float', 'TRIX10': 'float',
              'UOS': 'float', 'MA10RegressCoeff12': 'float', 'MA10RegressCoeff6': 'float', 'PLRC6': 'float',
              'PLRC12': 'float', 'SwingIndex': 'float', 'Ulcer10': 'float', 'Ulcer5': 'float', 'Hurst': 'float',
              'ACD6': 'float', 'ACD20': 'float', 'EMA12': 'float', 'EMA26': 'float', 'APBMA': 'float',
              'BBI': 'float', 'BBIC': 'float', 'TEMA10': 'float', 'TEMA5': 'float', 'MA10Close': 'float',
              'AR': 'float', 'BR': 'float', 'ARBR': 'float', 'CR20': 'float', 'MassIndex': 'float',
              'BearPower': 'float', 'BullPower': 'float', 'Elder': 'float', 'NVI': 'float', 'PVI': 'float',
              'RC12': 'float', 'RC24': 'float', 'JDQS20': 'float', 'Variance20': 'float', 'Variance60': 'float',
              'Variance120': 'float', 'Kurtosis20': 'float', 'Kurtosis60': 'float', 'Kurtosis120': 'float',
              'Alpha20': 'float', 'Alpha60': 'float', 'Alpha120': 'float', 'Beta20': 'float', 'Beta60': 'float',
              'Beta120': 'float', 'SharpeRatio20': 'float', 'SharpeRatio60': 'float', 'SharpeRatio120': 'float',
              'TreynorRatio20': 'float', 'TreynorRatio60': 'float', 'TreynorRatio120': 'float',
              'InformationRatio20': 'float', 'InformationRatio60': 'float', 'InformationRatio120': 'float',
              'GainVariance20': 'float', 'GainVariance60': 'float', 'GainVariance120': 'float',
              'LossVariance20': 'float', 'LossVariance60': 'float', 'LossVariance120': 'float',
              'GainLossVarianceRatio20': 'float', 'GainLossVarianceRatio60': 'float',
              'GainLossVarianceRatio120': 'float', 'RealizedVolatility': 'float', 'REVS60': 'float',
              'REVS120': 'float', 'REVS250': 'float', 'REVS750': 'float', 'REVS5m20': 'float', 'REVS5m60': 'float',
              'REVS5Indu1': 'float', 'REVS20Indu1': 'float', 'Volumn1M': 'float', 'Volumn3M': 'float',
              'Price1M': 'float', 'Price3M': 'float', 'Price1Y': 'float', 'Rank1M': 'float',
              'CashDividendCover': 'float', 'DividendCover': 'float', 'DividendPaidRatio': 'float',
              'RetainedEarningRatio': 'float', 'CashEquivalentPS': 'float', 'DividendPS': 'float',
              'EPSTTM': 'float', 'NetAssetPS': 'float', 'TORPS': 'float', 'TORPSLatest': 'float',
              'OperatingRevenuePS': 'float', 'OperatingRevenuePSLatest': 'float', 'OperatingProfitPS': 'float',
              'OperatingProfitPSLatest': 'float', 'CapitalSurplusFundPS': 'float', 'SurplusReserveFundPS': 'float',
              'UndividedProfitPS': 'float', 'RetainedEarningsPS': 'float', 'OperCashFlowPS': 'float',
              'CashFlowPS': 'float', 'NetNonOIToTP': 'float', 'NetNonOIToTPLatest': 'float',
              'PeriodCostsRate': 'float', 'InterestCover': 'float', 'NetProfitGrowRate3Y': 'float',
              'NetProfitGrowRate5Y': 'float', 'OperatingRevenueGrowRate3Y': 'float',
              'OperatingRevenueGrowRate5Y': 'float', 'NetCashFlowGrowRate': 'float', 'NetProfitCashCover': 'float',
              'OperCashInToAsset': 'float', 'CashConversionCycle': 'float', 'OperatingCycle': 'float',
              'PEG3Y': 'float', 'PEG5Y': 'float', 'PEIndu': 'float', 'PBIndu': 'float', 'PSIndu': 'float',
              'PCFIndu': 'float', 'PEHist20': 'float', 'PEHist60': 'float', 'PEHist120': 'float',
              'PEHist250': 'float', 'StaticPE': 'float', 'ForwardPE': 'float', 'EnterpriseFCFPS': 'float',
              'ShareholderFCFPS': 'float', 'ROEDiluted': 'float', 'ROEAvg': 'float', 'ROEWeighted': 'float',
              'ROECut': 'float', 'ROECutWeighted': 'float', 'ROIC': 'float', 'ROAEBIT': 'float',
              'ROAEBITTTM': 'float', 'OperatingNIToTP': 'float', 'OperatingNIToTPLatest': 'float',
              'InvestRAssociatesToTP': 'float', 'InvestRAssociatesToTPLatest': 'float', 'NPCutToNP': 'float',
              'SuperQuickRatio': 'float', 'TSEPToInterestBearDebt': 'float', 'DebtTangibleEquityRatio': 'float',
              'TangibleAToInteBearDebt': 'float', 'TangibleAToNetDebt': 'float', 'NOCFToTLiability': 'float',
              'NOCFToInterestBearDebt': 'float', 'NOCFToNetDebt': 'float', 'TSEPToTotalCapital': 'float',
              'InteBearDebtToTotalCapital': 'float', 'NPParentCompanyCutYOY': 'float',
              'SalesServiceCashToORLatest': 'float', 'CashRateOfSalesLatest': 'float',
              'NOCFToOperatingNILatest': 'float', 'TotalAssets': 'float', 'MktValue': 'float',
              'NegMktValue': 'float', 'TEAP': 'float', 'NIAP': 'float', 'TotalFixedAssets': 'float',
              'IntFreeCL': 'float', 'IntFreeNCL': 'float', 'IntCL': 'float', 'IntDebt': 'float',
              'NetDebt': 'float', 'NetTangibleAssets': 'float', 'WorkingCapital': 'float',
              'NetWorkingCapital': 'float', 'TotalPaidinCapital': 'float', 'RetainedEarnings': 'float',
              'OperateNetIncome': 'float', 'ValueChgProfit': 'float', 'NetIntExpense': 'float', 'EBIT': 'float',
              'EBITDA': 'float', 'EBIAT': 'float', 'NRProfitLoss': 'float', 'NIAPCut': 'float', 'FCFF': 'float',
              'FCFE': 'float', 'DA': 'float', 'TRevenueTTM': 'float', 'TCostTTM': 'float', 'RevenueTTM': 'float',
              'CostTTM': 'float', 'GrossProfitTTM': 'float', 'SalesExpenseTTM': 'float', 'AdminExpenseTTM': 'float',
              'FinanExpenseTTM': 'float', 'AssetImpairLossTTM': 'float', 'NPFromOperatingTTM': 'float',
              'NPFromValueChgTTM': 'float', 'OperateProfitTTM': 'float', 'NonOperatingNPTTM': 'float',
              'TProfitTTM': 'float', 'NetProfitTTM': 'float', 'NetProfitAPTTM': 'float',
              'SaleServiceRenderCashTTM': 'float', 'NetOperateCFTTM': 'float', 'NetInvestCFTTM': 'float',
              'NetFinanceCFTTM': 'float', 'GrossProfit': 'float', 'Beta252': 'float', 'RSTR504': 'float',
              'EPIBS': 'float', 'CETOP': 'float', 'DASTD': 'float', 'CmraCNE5': 'float', 'HsigmaCNE5': 'float',
              'SGRO': 'float', 'EgibsLong': 'float', 'STOM': 'float', 'STOQ': 'float', 'STOA': 'float',
              'NLSIZE': 'float'}

    tb.create_table('factorinfo', schema, 'tradeDate', 'time_colunm', 'security_column', 0)


# fdmt_mainPIT.py
def create_table_fdmtmaindatapit():
    schema = {'secID': 'varchar(64)', 'secShortName': 'varchar(16)', 'exchangeCD': 'varchar(16)',
              'ticker': 'varchar(32)', 'partyID': 'long', 'publishDate': 'long',
              'endDateRep': 'varchar(32)', 'endDate': 'varchar(32)', 'isNew': 'long', 'reportType': 'varchar(16)',
              'mergedFlag': 'varchar(16)', 'fiscalPeriod': 'long', 'tFixedAssets': 'float',
              'intFreeCl': 'float', 'intFreeNcl': 'float', 'intCl': 'float', 'intDebt': 'float',
              'nDebt': 'float', 'nTanAssets': 'float', 'workCapital': 'float',
              'nWorkCapital': 'float', 'ic': 'float', 'tRe': 'float', 'grossProfit': 'float',
              'opaProfit': 'float', 'valChgProfit': 'float', 'nIntExp': 'float',
              'ebit': 'float', 'ebitda': 'float', 'ebiat': 'float', 'nrProfitLoss': 'float',
              'niAttrPCut': 'float', 'fcff': 'float', 'fcfe': 'float', 'da': 'float',
              'rd': 'float', 'rdENiAttrPCut': 'float', 'eps': 'float', 'epsCut': 'float',
              'basicEps': 'float', 'dilutedEps': 'float', 'basicEpsCut': 'float',
              'dilutedEpsCut': 'float', 'nAssetPs': 'float', 'tRevPs': 'float',
              'revPs': 'float', 'opPs': 'float', 'ebitPs': 'float', 'ebitdaPs': 'float',
              'cReserPs': 'float', 'sReserPs': 'float', 'reserPs': 'float', 'rePs': 'float',
              'tRePs': 'float', 'nCFOperAPs': 'float', 'nCInCashPs': 'float', 'fcffPs': 'float',
              'fcfePs': 'float', 'grossMargin': 'float', 'npMargin': 'float',
              'scRatio': 'float', 'periodExpTr': 'float', 'pCostExp': 'float', 'roe': 'float',
              'roeA': 'float', 'roeW': 'float', 'roeCut': 'float', 'roeCutA': 'float',
              'roeCutW': 'float', 'roa': 'float', 'roaEbit': 'float', 'roic': 'float',
              'rop': 'float', 'faTurnover': 'float', 'dayFa': 'float', 'tfaTurnover': 'float',
              'dayTfa': 'float', 'caTurnover': 'float', 'ncaTurnover': 'float',
              'taTurnover': 'float', 'invenTurnover': 'float', 'daysInven': 'float',
              'nrArTurnover': 'float', 'daysNrAr': 'float', 'arTurnover': 'float',
              'daysAr': 'float', 'npApTurnover': 'float', 'daysNpAp': 'float',
              'apTurnover': 'float', 'daysAp': 'float', 'workCapitalTurnover': 'float',
              'daysWorkCapital': 'float', 'nWorkCapitalTurnover': 'float',
              'daysWorkCapital2018': 'float', 'operCycle': 'float', 'nOperCycle': 'float',
              'currentRatio': 'float', 'quickRatio': 'float', 'squickRatio': 'float',
              'opCl': 'float', 'opTl': 'float', 'assetLiabRatio': 'float',
              'equityRatio': 'float', 'tlTeap': 'float', 'teapTl': 'float', 'teapID': 'float',
              'nTanATl': 'float', 'nTanAID': 'float', 'nTanANd': 'float', 'ebitdaTl': 'float',
              'ebitdaID': 'float', 'cashIcl': 'float', 'cashCl': 'float', 'nCFOpaCl': 'float',
              'nCFOpaLiab': 'float', 'nCFOpaID': 'float', 'nCFOpaNd': 'float',
              'nCFOpaNcl': 'float', 'nCFNfaCl': 'float', 'nCFNfaLiab': 'float',
              'nclWc': 'float', 'timesInteEbit': 'float', 'timesInteEbitda': 'float',
              'timesInteCF': 'float', 'cashRatio': 'float', 'nCFOpaDebtDue': 'float',
              'ltLiabRatio': 'float', 'nrArRecR': 'float', 'nrArR': 'float', 'arRecR': 'float',
              'arR': 'float', 'advRR': 'float', 'cfsgsR': 'float', 'nCFOpaTr': 'float',
              'nCFOpaR': 'float', 'nCFOpaOpap': 'float', 'nCFOpaOp': 'float',
              'nCFOpaNia': 'float', 'pFixaODa': 'float', 'cRcvryA': 'float',
              'nCFOpaPropt': 'float', 'nCFIaPropt': 'float', 'nCFFaPropt': 'float',

              'cashMInvRatio': 'float', 'cashOperRatio': 'float', 'cashDivCover': 'float',
              'tRevenueYoy': 'float', 'revenueYoy': 'float', 'operProfitYoy': 'float',
              'tProfitYoy': 'float', 'niYoy': 'float', 'niAttrPYoy': 'float',
              'rDExpYoy': 'float', 'niAttrPCutYoy': 'float', 'tFaYtd': 'float',
              'roeYoy': 'float', 'nCFOpaYoy': 'float', 'basicEpsYoy': 'float',
              'dilutedEpsYoy': 'float', 'nCFOpaPsYoy': 'float', 'naPsYtd': 'float',
              'taYtd': 'float', 'naYtd': 'float', 'teAttrPYtd': 'float', 'tlYtd': 'float',
              'cashCeYtd': 'float', 'epsYoy': 'float', 'epsCutYoy': 'float', 'cogsYoy': 'float',
              'grossProfitYoy': 'float', 'npMarginYoy': 'float', 'cFrSaleGSYoy': 'float',
              'cPaidGSYoy': 'float', 'cPToForEmplYoy': 'float', 'nCFOpaNiaYoy': 'float',
              'cTa': 'float', 'nrArTa': 'float', 'arTa': 'float', 'repayTa': 'float',
              'invenTa': 'float', 'caTa': 'float', 'fixedATTa': 'float', 'tFixedATa': 'float',
              'intanATa': 'float', 'ltAmorExpTa': 'float', 'ncaTa': 'float', 'npApTa': 'float',
              'apTa': 'float', 'advRTa': 'float', 'stBorrTa': 'float', 'ltBorrTa': 'float',
              'bpTa': 'float', 'nTanATa': 'float', 'treTa': 'float', 'teapTa': 'float',
              'tseTa': 'float', 'idIc': 'float', 'teapIc': 'float', 'clTa': 'float',
              'nclTa': 'float', 'equMultiplier': 'float', 'capFixRatio': 'float',
              'ltDebtCapRatio': 'float', 'ltAssetSuitRatio': 'float', 'nclTeap': 'float',
              'clTeap': 'float', 'rTr': 'float', 'tcogsTr': 'float', 'cogsTr': 'float',
              'btaxSurchgTr': 'float', 'sellExpTr': 'float', 'adminExpTr': 'float',
              'rDExpTr': 'vfloat', 'finanExpTr': 'float', 'ailTr': 'float', 'cilTr': 'float',
              'opaPTr': 'float', 'valChgPTr': 'float', 'fvChgGTr': 'float', 'invIncTr': 'float',
              'opTr': 'float', 'nopgTr': 'float', 'noplTr': 'float', 'tpTr': 'float',
              'itTr': 'float', 'niTr': 'float', 'ebitdaTr': 'float', 'ebitTr': 'float',
              'opaPTp': 'float', 'valChgPTp': 'float', 'opTp': 'float', 'nNopiTp': 'float',
              'itTp': 'float', 'niCutNi': 'float'}

    tb.create_table('fdmtmaindatapit', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# fdmt_mainPIT.py
def create_table_fdmtmaindataqpit():
    schema = {'secID': 'varchar(33)', 'secShortName': 'varchar(15)', 'exchangeCD': 'varchar(12)',
              'ticker': 'varchar(18)', 'partyID': 'long', 'publishDate': 'long',
              'endDateRep': 'varchar(30)', 'endDate': 'varchar(30)', 'isNew': 'long', 'reportType': 'varchar(9)',
              'mergedFlag': 'varchar(3)', 'fiscalPeriod': 'long', 'grossProfit': 'float',
              'opaProfit': 'float', 'valChgProfit': 'float', 'nIntExp': 'float',
              'ebit': 'float', 'ebitda': 'float', 'ebiat': 'float', 'nrProfitLoss': 'float',
              'niAttrPCut': 'float', 'fcff': 'float', 'fcfe': 'float', 'da': 'float',
              'rd': 'float', 'rdENiAttrPCut': 'float', 'eps': 'float', 'epsCut': 'float',
              'basicEps': 'float', 'dilutedEps': 'float', 'basicEpsCut': 'float',
              'dilutedEpsCut': 'float', 'nAssetPs': 'float', 'tRevPs': 'float',
              'revPs': 'float', 'opPs': 'float', 'ebitPs': 'float', 'ebitdaPs': 'float',
              'cReserPs': 'float', 'sReserPs': 'float', 'reserPs': 'float', 'rePs': 'float',
              'tRePs': 'float', 'nCFOperAPs': 'float', 'nCInCashPs': 'float', 'fcffPs': 'float',
              'fcfePs': 'float', 'grossMargin': 'float', 'npMargin': 'float',
              'scRatio': 'float', 'periodExpTr': 'float', 'pCostExp': 'float', 'roe': 'float',
              'roeA': 'float', 'roeW': 'float', 'roeCut': 'float', 'roeCutA': 'float',
              'roeCutW': 'float', 'roa': 'float', 'roaEbit': 'float', 'roic': 'float',
              'rop': 'float', 'faTurnover': 'float', 'dayFa': 'float', 'tfaTurnover': 'float',
              'dayTfa': 'float', 'caTurnover': 'float', 'ncaTurnover': 'float',
              'taTurnover': 'float', 'invenTurnover': 'float', 'daysInven': 'float',
              'nrArTurnover': 'float', 'daysNrAr': 'float', 'arTurnover': 'float',
              'daysAr': 'float', 'npApTurnover': 'float', 'daysNpAp': 'float',
              'apTurnover': 'float', 'daysAp': 'float', 'workCapitalTurnover': 'float',
              'daysWorkCapital': 'float', 'nWorkCapitalTurnover': 'float',
              'daysWorkCapital2018': 'float', 'operCycle': 'float', 'nOperCycle': 'float',
              'currentRatio': 'float', 'quickRatio': 'float', 'squickRatio': 'float',
              'opCl': 'varchar(21)', 'opTl': 'varchar(57)', 'assetLiabRatio': 'float',
              'equityRatio': 'float', 'tlTeap': 'float', 'teapTl': 'float', 'teapID': 'float',
              'nTanATl': 'float', 'nTanAID': 'float', 'nTanANd': 'float', 'ebitdaTl': 'float',
              'ebitdaID': 'float', 'cashIcl': 'float', 'cashCl': 'float', 'nCFOpaCl': 'float',
              'nCFOpaLiab': 'float', 'nCFOpaID': 'float', 'nCFOpaNd': 'float',
              'nCFOpaNcl': 'float', 'nCFNfaCl': 'float', 'nCFNfaLiab': 'float',
              'nclWc': 'float', 'timesInteEbit': 'float', 'timesInteEbitda': 'float',
              'timesInteCF': 'float', 'cashRatio': 'float', 'nCFOpaDebtDue': 'float',
              'ltLiabRatio': 'float', 'nrArRecR': 'float', 'nrArR': 'float',
              'arRecR': 'float', 'arR': 'float', 'advRR': 'float', 'cfsgsR': 'float',
              'nCFOpaTr': 'float', 'nCFOpaR': 'float', 'nCFOpaOpap': 'float',
              'nCFOpaOp': 'float', 'nCFOpaNia': 'float', 'pFixaODa': 'float',
              'cRcvryA': 'float', 'nCFOpaPropt': 'float', 'nCFIaPropt': 'float',
              'nCFFaPropt': 'float', 'cashMInvRatio': 'float', 'cashOperRatio': 'float',
              'cashDivCover': 'float', 'tRevenueYoy': 'float', 'revenueYoy': 'float',
              'operProfitYoy': 'float', 'tProfitYoy': 'float', 'niYoy': 'float',
              'niAttrPYoy': 'float', 'rDExpYoy': 'float', 'niAttrPCutYoy': 'float',
              'tFaYtd': 'float', 'roeYoy': 'float', 'nCFOpaYoy': 'float',
              'basicEpsYoy': 'float', 'dilutedEpsYoy': 'float', 'nCFOpaPsYoy': 'float',
              'naPsYtd': 'float', 'taYtd': 'float', 'naYtd': 'float', 'teAttrPYtd': 'float',
              'tlYtd': 'float', 'cashCeYtd': 'float', 'epsYoy': 'float', 'epsCutYoy': 'float',
              'cogsYoy': 'float', 'grossProfitYoy': 'float', 'npMarginYoy': 'float',
              'cFrSaleGSYoy': 'float', 'cPaidGSYoy': 'float', 'cPToForEmplYoy': 'float',
              'nCFOpaNiaYoy': 'float', 'cTa': 'float', 'nrArTa': 'float', 'arTa': 'float',
              'repayTa': 'float', 'invenTa': 'float', 'caTa': 'float', 'fixedATTa': 'float',
              'tFixedATa': 'float', 'intanATa': 'float', 'ltAmorExpTa': 'float',
              'ncaTa': 'float', 'npApTa': 'float', 'apTa': 'float', 'advRTa': 'float',
              'stBorrTa': 'float', 'ltBorrTa': 'float', 'bpTa': 'float', 'nTanATa': 'float',
              'treTa': 'float', 'teapTa': 'float', 'tseTa': 'float', 'idIc': 'float',
              'teapIc': 'float', 'clTa': 'float', 'nclTa': 'float', 'equMultiplier': 'float',
              'capFixRatio': 'float', 'ltDebtCapRatio': 'float', 'ltAssetSuitRatio': 'float',
              'nclTeap': 'float', 'clTeap': 'float', 'rTr': 'float', 'tcogsTr': 'float',
              'cogsTr': 'float', 'btaxSurchgTr': 'float', 'sellExpTr': 'float',
              'adminExpTr': 'float', 'rDExpTr': 'float', 'finanExpTr': 'float',
              'ailTr': 'float', 'cilTr': 'float', 'opaPTr': 'float', 'valChgPTr': 'float',
              'fvChgGTr': 'float', 'invIncTr': 'float', 'opTr': 'float', 'nopgTr': 'float',
              'noplTr': 'float', 'tpTr': 'float', 'itTr': 'float', 'niTr': 'float',
              'ebitdaTr': 'float', 'ebitTr': 'float', 'opaPTp': 'float', 'valChgPTp': 'float',
              'opTp': 'float', 'nNopiTp': 'float', 'itTp': 'float', 'niCutNi': 'float'}

    tb.create_table('fdmtmaindataqpit', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# fdmtCfs.py
def create_table_fdmtcfs():
    schema = {'secID': 'varchar(64)', 'ticker': 'varchar(32)', 'secShortName': 'varchar(32)',
              'exchangeCD': 'varchar(16)', 'publishDate': 'varchar(64)', 'endDate': 'long',
              'endDateRep': 'varchar(30)', 'reportType': 'varchar(9)', 'fiscalPeriod': 'long',
              'mergedFlag': 'varchar(3)', 'accoutingStandARds': 'varchar(27)', 'currencyCD': 'varchar(9)',
              'NIncome': 'float', 'assetsImpairLoss': 'float', 'FAOGPBDepr': 'float', 'intanAssetsAmor': 'float',
              'LTAmorExpAmor': 'float', 'amorExpDecr': 'float', 'accrExpIncr': 'float', 'dispFaOthLoss': 'float',
              'FAWritOff': 'float', 'FValueChgLoss': 'float', 'finanExp': 'float', 'invLoss': 'float',
              'deferTaDecr': 'float', 'deferTlIncr': 'float', 'invenDecr': 'float', 'operReceiDecr': 'float',
              'operPayaIncr': 'float', 'other': 'float', 'specNOCF1': 'float', 'ANOCF1': 'float',
              'NCFOperateANotes': 'float', 'contrANOCF': 'float', 'convDebtCAPi': 'float', 'convBonds1Y': 'float',
              'finanLeaFA': 'float', 'CEndBal': 'float', 'CBegBal': 'float', 'CEEndBal': 'float',
              'CEBegBal': 'float', 'specC': 'float', 'AC': 'float', 'NChangeInCash': 'float', 'contrANC': 'float'}

    tb.create_table('fdmtcfs', schema, 'endDate', 'time_colunm', 'security_column', 0)

# fdmtEe.py
def create_table_fdmte():
    schema = {'secID': 'varchar(33)', 'publishDate': 'long', 'endDate': 'varchar(30)', 'partyID': 'long',
              'ticker': 'varchar(18)', 'secShortName': 'varchar(12)', 'exchangeCD': 'varchar(12)',
              'actPubtime': 'varchar(57)', 'mergedFlag': 'varchar(3)', 'reportType': 'varchar(3)',
              'fiscalPeriod': 'varchar(6)', 'accoutingStandards': 'varchar(27)', 'currencyCD': 'varchar(9)',
              'revenue': 'float', 'primeOperRev': 'float', 'grossProfit': 'float', 'operateProfit': 'float',
              'TProfit': 'float', 'NIncomeAttrP': 'float', 'NIncomeCut': 'float', 'NCfOperA': 'float',
              'basicEPS': 'float', 'EPSW': 'float', 'EPSCut': 'float', 'EPSCutW': 'float', 'ROE': 'float',
              'ROEW': 'float', 'ROECut': 'float', 'ROECutW': 'float', 'NCfOperAPs': 'float', 'TAssets': 'float',
              'TEquityAttrP': 'float', 'paidInCapital': 'float', 'NAssetPS': 'float', 'revenueLY': 'float',
              'primeOperRevLY': 'float', 'grossProfitLY': 'float', 'operProfitLY': 'float', 'TProfitLY': 'float',
              'NIncomeAttrPLY': 'float', 'NIncomeCutLY': 'float', 'NCfOperALY': 'float', 'basicEPSLY': 'float',
              'EPSWLY': 'float', 'EPSCutLY': 'float', 'EPSCutWLY': 'float', 'ROELY': 'float', 'ROEWLY': 'float',
              'ROECutLY': 'float', 'ROECutWLY': 'float', 'NCfOperAPsLY': 'float', 'TAssetsLY': 'float',
              'TEquityAttrPLY': 'float', 'NAssetPsLY': 'float', 'revenueYOY': 'float', 'primeOperRevYOY': 'float',
              'grossProfitYOY': 'float', 'operProfitYOY': 'float', 'TProfitYOY': 'float',
              'NIncomeAttrPYOY': 'float', 'NIncomeCutYOY': 'float', 'NCFOperAYOY': 'float', 'basicEPSYOY': 'float',
              'EPSWYOY': 'float', 'EPSCutYOY': 'float', 'EPSCutWYOY': 'float', 'ROEYOY': 'float',
              'ROEWYOY': 'float', 'ROECutYOY': 'float', 'ROECutWYOY': 'float', 'NCfOperAPsYOY': 'float',
              'TAssetsYOY': 'float', 'TEquityAttrPYOY': 'float', 'NAssetPsYOY': 'float', 'updateTime': 'varchar(57)'}

    tb.create_table('fdmte', schema, 'publishDate', 'time_colunm', 'security_column', 0)

# fdmtfinanceQPIT.py
def create_table_fdmtisqpit2018():
    schema ={'secID': 'varchar(33)', 'ticker': 'varchar(18)', 'secShortName': 'varchar(15)',
             'exchangeCD': 'varchar(12)', 'partyID': 'long', 'publishDate': 'long', 'endDateRep': 'varchar(30)',
             'endDate': 'varchar(30)', 'fiscalPeriod': 'long', 'mergedFlag': 'varchar(3)', 'isCalc': 'varchar(3)',
             'isNew': 'varchar(3)', 'industryCategory': 'varchar(15)', 'tRevenue': 'float', 'revenue': 'float',
             'intIncome': 'float', 'premEarned': 'float', 'grossPremWrit': 'float', 'reinsur': 'float',
             'unePremReser': 'float', 'commisIncome': 'float', 'nSecTaIncome': 'float', 'nUndwrtSecIncome': 'float',
             'nTrustIncome': 'float', 'othOperRev': 'float', 'specOr': 'float', 'aor': 'float', 'tCogs': 'float',
             'cogs': 'float', 'intExp': 'float', 'commisExp': 'float', 'premRefund': 'float',
             'nCompensPayout': 'float', 'compensPayout': 'float', 'compensPayoutRefu': 'float',
             'reserInsurContr': 'float', 'reserInsurLiab': 'float', 'insurLiabReserRefu': 'float',
             'reinsCostRefund': 'float', 'policyDivPayt': 'float', 'reinsurExp': 'float', 'bizTaxSurchg': 'float',
             'sellExp': 'float', 'adminExp': 'float', 'genlAdminExp': 'float', 'rDExp': 'float',
             'finanExp': 'float', 'intExpFinanExp': 'float', 'intIncomeFinanExp': 'float', 'othOperCosts': 'float',
             'specToc': 'float', 'atoc': 'float', 'othGain': 'float', 'investIncome': 'float',
             'aJInvestIncome': 'float', 'tafQuitGain': 'float', 'netExpHIncome': 'float', 'fValueChgGain': 'float',
             'assetsImpairLoss': 'float', 'creditImpairLoss': 'float', 'assetsDispGain': 'float',
             'forexGain': 'float', 'othEffectOp': 'float', 'aeEffectOp': 'float', 'operateProfit': 'float',
             'noperateIncome': 'float', 'noperateExp': 'float', 'ncaDisploss': 'float', 'othEffectTp': 'float',
             'aeEffectTp': 'float', 'tProfit': 'float', 'incomeTax': 'float', 'othEffectNp': 'float',
             'aeEffectNp': 'float', 'nIncome': 'float', 'goingConcernNi': 'float', 'quitConcernNi': 'float',
             'nIncomeAttrP': 'float', 'minorityGain': 'float', 'aeEffectNpp': 'float', 'othComprIncome': 'float',
             'othEffectNpp': 'float', 'othEffectCi': 'float', 'aeEffectCi': 'float', 'tComprIncome': 'float',
             'comprIncAttrP': 'float', 'comprIncAttrMS': 'float', 'othEffectPci': 'float', 'aeEffectPci': 'float'}

    tb.create_table('fdmtisqpit2018', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# fdmtfinanceQPIT.py
def create_table_fdmtcfqpit2018():
    schema = {'secID': 'varchar(33)', 'ticker': 'varchar(18)', 'secShortName': 'varchar(15)',
              'exchangeCD': 'varchar(12)', 'fiscalPeriod': 'long', 'mergedFlag': 'varchar(3)', 'isCalc': 'varchar(3)',
              'isNew': 'long', 'industryCategory': 'varchar(15)', 'cFrSaleGS': 'float', 'nDeposIncrCFi': 'float',
              'nIncrBorrFrCb': 'float', 'nIncBorrOthFi': 'float', 'premFrOrigContr': 'float',
              'nReinsurPrem': 'float', 'nIncPhDeposInv': 'float', 'nIncDispTradFa': 'float',
              'nDecrInDisburOfLa': 'float', 'netDecrInDeposInFi': 'float', 'nIncDispFaFs': 'float',
              'nDecrLoanToOthFi': 'float', 'ifcCashIncr': 'float', 'nIncFrBorr': 'float', 'nCapIncrRepur': 'float',
              'refundOfTax': 'float', 'cFrOthOperateA': 'float', 'specOcif': 'float', 'aocif': 'float',
              'cInfFrOperateA': 'float', 'cPaidGS': 'float', 'nDeposDecrFrFi': 'float', 'nDecrBorrFrCb': 'float',
              'nIncDisburOfLa': 'float', 'netIncrDeposInFi': 'float', 'origContrCIndem': 'float',
              'nIncrLoansToOthFi': 'float', 'cPaidIfc': 'float', 'cPaidPolDiv': 'float', 'cPaidToForEmpl': 'float',
              'cPaidForTaxes': 'float', 'cPaidForOthOpA': 'float', 'specOcof': 'float', 'aocof': 'float',
              'cOutfOperateA': 'float', 'anocf': 'float', 'nCfOperateA': 'float', 'procSellInvest': 'float',
              'gainInvest': 'float', 'dispFixAssetsOth': 'float', 'nDispSubsOthBizC': 'float',
              'cFrOthInvestA': 'float', 'specCif': 'float', 'acif': 'float', 'cInfFrInvestA': 'float',
              'purFixAssetsOth': 'float', 'cPaidInvest': 'float', 'nIncrPledgeLoan': 'float',
              'nCPaidAcquis': 'float', 'cPaidOthInvestA': 'float', 'specCof': 'float', 'acof': 'float',
              'cOutfFrInvestA': 'float', 'anicf': 'float', 'nCfFrInvestA': 'float', 'cFrCapContr': 'float',
              'cFrMinoSSubs': 'float', 'cFrBorr': 'float', 'cFrIssueBond': 'float', 'cFrOthFinanA': 'float',
              'specFcif': 'float', 'afcif': 'float', 'cInfFrFinanA': 'float', 'cPaidForDebts': 'float',
              'cPaidDivProfInt': 'float', 'divProfSubsMinoS': 'float', 'cPaidOthFinanA': 'float',
              'specFcof': 'float', 'afcof': 'float', 'cOutfFrFinanA': 'float', 'anfcf': 'float',
              'nCfFrFinanA': 'float', 'forexEffects': 'float', 'othEffectCe': 'float', 'ace': 'float',
              'nChangeInCash': 'float', 'nCeBegBal': 'float', 'othEffectCei': 'float', 'acei': 'float',
              'nCeEndBal': 'float', 'partyID': 'long', 'publishDate': 'long', 'endDateRep': 'varchar(30)',
              'endDate': 'varchar(30)'}

    tb.create_table('fdmtcfqpit2018', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# fdmtMain.py
def create_table_fdmtmainopern():
    schema = {'partyID': 'long', 'secID': 'varchar(36)', 'ticker': 'varchar(18)', 'secShortName': 'varchar(18)',
              'exchangeCD': 'varchar(12)', 'actPubtime': 'varchar(57)', 'publishDate': 'varchar(30)',
              'endDate': 'long', 'fiscalPeriod': 'long', 'mergeFlag': 'long', 'classifCD': 'long',
              'isLatest': 'long', 'industry': 'varchar(15)', 'itemParentNo': 'float', 'itemNo': 'long',
              'itemName': 'varchar(186)', 'revenue': 'float', 'revPctge': 'float', 'revIsPctge': 'float',
              'tRevIsPctge': 'float', 'cogs': 'float', 'costPctge': 'float', 'cogsIsPctge': 'float',
              'tCogsIsPctge': 'float', 'grossProfit': 'float', 'grossMargin': 'float', 'updateTime': 'varchar(57)'}

    tb.create_table('fdmtmainopern', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# fdmtMain.py
def create_table_fdmtmostditem():
    schema = {'secID': 'varchar(36)', 'ticker': 'varchar(18)', 'secShortName': 'varchar(18)',
              'exchangeCD': 'varchar(12)', 'partyID': 'long', 'endDate': 'long', 'classifCD': 'long',
              'itemID': 'long', 'itemName': 'varchar(126)', 'itemIDSuperior': 'long',
              'itemNameSuperior': 'varchar(126)', 'revenue': 'float', 'revIsPctge': 'float', 'tRevIsPctge': 'float',
              'revYOY': 'float', 'cogs': 'float', 'cogsIsPctge': 'float', 'tCogsIsPctge': 'float',
              'cogsYOY': 'float', 'grossProfit': 'float', 'grossProfitYOY': 'float', 'grossMargin': 'float',
              'grossMarginYOY': 'float', 'isCalc': 'long'}

    tb.create_table('fdmtmostditem', schema, 'endDate', 'time_colunm', 'security_column', 0)


# finance_der.py
def create_table_fdmtderpit():
    schema = {'secID': 'varchar(33)', 'partyID': 'long', 'ticker': 'varchar(18)', 'exchangeCD': 'varchar(12)',
              'secShortName': 'varchar(12)', 'publishDate': 'long', 'actPubtime': 'varchar(57)',
              'endDate': 'varchar(30)', 'tFixedAssets': 'float', 'intFreeCl': 'float',
              'intFreeNcl': 'float', 'intCl': 'float', 'intDebt': 'float', 'nDebt': 'float',
              'nTanAssets': 'float', 'workCapital': 'float', 'nWorkCapital': 'float',
              'IC': 'float', 'tRe': 'float', 'grossProfit': 'float', 'opaProfit': 'float',
              'valChgProfit': 'float', 'nIntExp': 'float', 'EBIT': 'float', 'EBITDA': 'float',
              'EBIAT': 'float', 'nrProfitLoss': 'float', 'niAttrPCut': 'float', 'FCFF': 'float',
              'FCFE': 'float', 'DA': 'float'}

    tb.create_table('fdmtderpit', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# finance_der.py
def create_table_fdmtderttmpi():
    schema = {'secID': 'varchar(33)', 'partyID': 'varchar(21)', 'ticker': 'varchar(18)', 'exchangeCD': 'varchar(12)',
              'secShortName': 'varchar(12)', 'publishDate': 'long', 'endDate': 'varchar(30)', 'mergedFlag': 'float',
              'tFixedAssets': 'float', 'intFreeCl': 'float', 'intFreeNcl': 'float',
              'intCl': 'float', 'intDebt': 'float', 'nDebt': 'float', 'nTanAssets': 'float',
              'workCapital': 'float', 'nWorkCapital': 'float', 'IC': 'float', 'tRe': 'float',
              'grossProfit': 'float', 'opaProfit': 'float', 'valChgProfit': 'float',
              'nIntExp': 'float', 'EBIT': 'float', 'EBITDA': 'float', 'EBIAT': 'float',
              'nrProfitLoss': 'float', 'niAttrPCut': 'float', 'FCFF': 'float',
              'FCFE': 'float', 'DA': 'float'}

    tb.create_table('fdmtderttmpi', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# flow_order.py
def create_table_mktequfloworder():
    schema = {'secID': 'varchar(33)', 'ticker': 'varchar(18)', 'secShortName': 'varchar(18)', 'tradeDate': 'long',
              'inflowS': 'float', 'inflowM': 'float', 'inflowL': 'float', 'inflowXl': 'float', 'outflowS': 'float',
              'outflowM': 'float', 'outflowL': 'float', 'outflowXl': 'float', 'netInflowS': 'float',
              'netInflowM': 'float', 'netInflowL': 'float', 'netInflowXl': 'float', 'netRateS': 'float',
              'netRateM': 'float', 'netRateL': 'float', 'netRateXL': 'float', 'mainInflow': 'float',
              'mainRate': 'float'}

    tb.create_table('mktequfloworder', schema, 'tradeDate', 'time_colunm', 'security_column', 0)


# flow_order.py
def create_table_mktequflow():
    schema = {'secID': 'varchar(33)', 'ticker': 'varchar(18)', 'secShortName': 'varchar(18)',
              'secShortNameEn': 'varchar(231)', 'exchangeCD': 'varchar(12)', 'tradeDate': 'long',
              'moneyInflow': 'float', 'moneyOutflow': 'float', 'netMoneyInflow': 'float', 'netInflowRate': 'float',
              'netInflowOpen': 'float', 'netInflowClose': 'float', 'updateTime': 'varchar(57)'}

    tb.create_table('mktequflow', schema, 'tradeDate', 'time_colunm', 'security_column', 0)


# flow_order.py
def create_table_mktindustryflow():
    schema = {'industryID': 'varchar(36)', 'industryName': 'varchar(60)', 'tradeDate': 'long', 'moneyInflow': 'float',
              'moneyOutflow': 'float', 'netMoneyInflow': 'float', 'netInflowRate': 'float',
              'netInflowOpen': 'float', 'netInflowClose': 'float', 'updateTime': 'varchar(57)'}

    tb.create_table('mktindustryflow', schema, 'tradeDate', 'time_colunm', 'security_column', 0)


# flow_order.py
def create_table_mktindustryfloworder():
    schema = {'industryID': 'varchar(36)', 'industryName': 'varchar(60)', 'tradeDate': 'long', 'inflowS': 'float',
              'inflowM': 'float', 'inflowL': 'float', 'inflowXl': 'float', 'outflowS': 'float',
              'outflowM': 'float', 'outflowL': 'float', 'outflowXl': 'float', 'netInflowS': 'float',
              'netInflowM': 'float', 'netInflowL': 'float', 'netInflowXl': 'float', 'netRateS': 'float',
              'netRateM': 'float', 'netRateL': 'float', 'netRateXL': 'float', 'mainInflow': 'float',
              'mainRate': 'float'}

    tb.create_table('mktindustryfloworder', schema, 'tradeDate', 'time_colunm', 'security_column', 0)


# flow_order.py
def create_table_mktequmf():
    schema = {'secID': 'varchar(33)', 'ticker': 'varchar(18)', 'secShortName': 'varchar(18)',
              'exchangeCD': 'varchar(12)', 'tradeDate': 'long', 'turnoverValue': 'float', 'turnoverVol': 'long',
              'dealAmount': 'long', 'netFlow': 'float', 'inflow': 'float', 'outflow': 'float', 'mainFlow': 'float',
              'smainFlow': 'float', 'mainInflow': 'float', 'mainOutflow': 'float', 'netFlowS': 'float',
              'netFlowM': 'float', 'netFlowL': 'float', 'netFlowXL': 'float', 'inflowS': 'float',
              'inflowM': 'float', 'inflowL': 'float', 'inflowXL': 'float', 'outflowS': 'float',
              'outflowM': 'float', 'outflowL': 'float', 'outflowXL': 'float', 'netVol': 'long', 'buyVol': 'long',
              'sellVol': 'long', 'mainBuyVol': 'long', 'mainSellVol': 'long', 'buyVolS': 'long', 'buyVolM': 'long',
              'buyVolL': 'long', 'buyVolXL': 'long', 'sellVolS': 'long', 'sellVolM': 'long', 'sellVolL': 'long',
              'sellVolXL': 'long', 'netOrd': 'long', 'buyOrd': 'long', 'sellOrd': 'long', 'mainBuyOrd': 'long',
              'mainSellOrd': 'long', 'buyOrdS': 'long', 'buyOrdM': 'long', 'buyOrdL': 'long', 'buyOrdXL': 'long',
              'sellOrdS': 'long', 'sellOrdM': 'long', 'sellOrdL': 'long', 'sellOrdXL': 'long', 'netFlowRate': 'float',
              'inflowRate': 'float', 'outflowRate': 'float', 'mainFlowRate': 'float', 'smainFlowRate': 'float',
              'mainInflowRate': 'float', 'mainOutflowRate': 'float', 'netFlowSRate': 'float',
              'netFlowMRate': 'float', 'netFlowLRate': 'float', 'netFlowXLRate': 'float', 'inflowSRate': 'float',
              'inflowMRate': 'float', 'inflowLRate': 'float', 'inflowXLRate': 'float', 'outflowSRate': 'float',
              'outflowMRate': 'float', 'outflowLRate': 'float', 'outflowXLRate': 'float', 'netVolRate': 'float',
              'buyVolRate': 'float', 'sellVolRate': 'float', 'mainBuyVolRate': 'float', 'mainSellVolRate': 'float',
              'netOrdRate': 'float', 'buyOrdRate': 'float', 'sellOrdRate': 'float', 'mainBuyOrdRate': 'float',
              'mainSellOrdRate': 'float', 'updateTime': 'varchar(57)'}

    tb.create_table('mktequmf', schema, 'tradeDate', 'time_colunm', 'security_column', 0)


# forecast.py
def create_table_fdmtefnew():
    schema = {'secID': 'varchar(33)', 'publishDate': 'long', 'endDate': 'varchar(30)', 'partyID': 'long',
              'ticker': 'varchar(18)', 'secShortName': 'varchar(18)', 'exchangeCD': 'varchar(12)',
              'actPubtime': 'varchar(57)', 'mergedFlag': 'varchar(3)', 'reportType': 'varchar(6)',
              'fiscalPeriod': 'varchar(6)', 'accoutingStandards': 'varchar(27)', 'currencyCD': 'varchar(9)',
              'forecastType': 'long', 'revChgrLL': 'float', 'revChgrUPL': 'float', 'expRevLL': 'float',
              'expRevUPL': 'float', 'NIncomeChgrLL': 'float', 'NIncomeChgrUPL': 'float', 'expnIncomeLL': 'float',
              'expnIncomeUPL': 'float', 'NIncAPChgrLL': 'float', 'NIncAPChgrUPL': 'float', 'expnIncAPLL': 'float',
              'expnIncAPUPL': 'float', 'expEPSLL': 'float', 'expEPSUPL': 'float', 'updateTime': 'varchar(57)'}

    tb.create_table('fdmtefnew', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# holderChgcf.py
def create_table_equholderchgcsf():
    schema = {'secID': 'varchar(33)', 'ticker': 'varchar(18)', 'secShortName': 'varchar(12)', 'partyID': 'long',
              'shareholderName': 'varchar(78)', 'endDateL': 'varchar(30)', 'shareNumL': 'float',
              'endDate': 'long', 'shareNum': 'float', 'holdType': 'varchar(6)'}

    tb.create_table('equholderchgcsf', schema, 'endDate', 'time_colunm', 'security_column', 0)


# hybk_daily.py
def create_table_mktinstequd():
    schema = {'industrySymbol': 'varchar(18)', 'industryName': 'varchar(24)', 'secID': 'varchar(33)',
              'indexSymbol': 'varchar(18)', 'tradeDate': 'long', 'preClosePrice': 'float', 'openPrice': 'float',
              'highestPrice': 'float', 'lowestPrice': 'float', 'closePrice': 'float', 'turnoverVol': 'long',
              'turnoverValue': 'float', 'chgPct': 'float', 'ticker': 'varchar(18)', 'upNum': 'long',
              'downNum': 'long', 'equalNum': 'long', 'upLimitNum': 'long', 'downLimitNum': 'long',
              'turnoverRate': 'float', 'netInflow': 'float', 'netMainInflow': 'float', 'industryID': 'varchar(36)',
              'chgPct5': 'float', 'chgPct10': 'float', 'chgPct20': 'float', 'chgPctFY': 'float',
              'updateTime': 'varchar(57)'}

    tb.create_table('mktinstequd', schema, 'tradeDate', 'time_colunm', 'security_column', 0)


# incom.py
def create_table_fdmtisbank2018():
    schema = {'partyID': 'long', 'ticker': 'varchar(18)', 'exchangeCD': 'varchar(12)', 'actPubtime': 'varchar(57)',
              'secID': 'varchar(33)', 'publishDate': 'long', 'secShortName': 'varchar(12)', 'endDateRep': 'varchar(30)',
              'endDate': 'varchar(30)', 'reportType': 'varchar(6)', 'fiscalPeriod': 'long', 'mergedFlag': 'varchar(3)',
              'accoutingStandards': 'varchar(27)', 'currencyCD': 'varchar(9)', 'industryCategory': 'varchar(9)',
              'revenue': 'float', 'nIntIncome': 'float', 'intIncome': 'float', 'intExp': 'float',
              'nCommisIncome': 'float', 'commisIncome': 'float', 'commisExp': 'float', 'othGain': 'float',
              'investIncome': 'float', 'aJInvestIncome': 'float', 'tafQuitGain': 'float', 'netExpHIncome': 'float',
              'fValueChgGain': 'float', 'assetsImpairLoss': 'float', 'creditImpairLoss': 'float',
              'assetsDispGain': 'float', 'forexGain': 'float', 'othOperRev': 'float', 'specOr': 'float',
              'aor': 'float', 'cogs': 'float', 'bizTaxSurchg': 'float', 'genlAdminExp': 'float',
              'othOperCosts': 'float', 'specOp': 'float', 'aop': 'float', 'othEffectOp': 'float',
              'aeEffectOp': 'float', 'operateProfit': 'float', 'noperateIncome': 'float', 'noperateExp': 'float',
              'othEffectTp': 'float', 'aeEffectTp': 'float', 'tProfit': 'float', 'incomeTax': 'float',
              'othEffectNp': 'float', 'aeEffectNp': 'float', 'nIncome': 'float', 'nIncomeAttrP': 'float',
              'minorityGain': 'float', 'goingConcernNi': 'float', 'quitConcernNi': 'float', 'othEffectNpp': 'float',
              'aeEffectNpp': 'float', 'basicEps': 'float', 'dilutedEps': 'float', 'othComprIncome': 'float',
              'othEffectCi': 'float', 'aeEffectCi': 'float', 'tComprIncome': 'float', 'comprIncAttrP': 'float',
              'comprIncAttrMS': 'float', 'othEffectPci': 'float', 'aeEffectPci': 'float'}

    tb.create_table('fdmtisbank2018', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# incom.py
def create_table_fdmtisindu2018():
    schema = {'partyID': 'long', 'ticker': 'varchar(18)', 'exchangeCD': 'varchar(12)', 'secID': 'varchar(33)',
              'secShortName': 'varchar(18)', 'endDateRep': 'varchar(30)', 'endDate': 'varchar(30)',
              'reportType': 'varchar(6)', 'fiscalPeriod': 'long', 'mergedFlag': 'varchar(3)',
              'accoutingStandards': 'varchar(27)', 'currencyCD': 'varchar(9)', 'industryCategory': 'varchar(15)',
              'tRevenue': 'float', 'revenue': 'float', 'intIncome': 'float', 'premEarned': 'float',
              'commisIncome': 'float', 'specOr': 'float', 'aor': 'float', 'tCogs': 'float', 'cogs': 'float',
              'intExp': 'float', 'commisExp': 'float', 'premRefund': 'float', 'nCompensPayout': 'float',
              'reserInsurContr': 'float', 'policyDivPayt': 'float', 'reinsurExp': 'float', 'bizTaxSurchg': 'float',
              'sellExp': 'float', 'adminExp': 'float', 'rDExp': 'float', 'finanExp': 'float',
              'intExpFinanExp': 'float', 'intIncomeFinanExp': 'float', 'specToc': 'float', 'atoc': 'float',
              'othGain': 'float', 'investIncome': 'float', 'aJInvestIncome': 'float', 'tafQuitGain': 'float',
              'netExpHIncome': 'float', 'fValueChgGain': 'float', 'assetsImpairLoss': 'float',
              'creditImpairLoss': 'float', 'assetsDispGain': 'float', 'forexGain': 'float', 'othEffectOp': 'float',
              'aeEffectOp': 'float', 'operateProfit': 'float', 'noperateIncome': 'float', 'noperateExp': 'float',
              'ncaDisploss': 'float', 'othEffectTp': 'float', 'aeEffectTp': 'float', 'tProfit': 'float',
              'incomeTax': 'float', 'othEffectNp': 'float', 'aeEffectNp': 'float', 'nIncome': 'float',
              'nIncomeBma': 'float', 'nIncomeAttrP': 'float', 'minorityGain': 'float', 'goingConcernNi': 'float',
              'quitConcernNi': 'float', 'othEffectNpp': 'float', 'aeEffectNpp': 'float', 'basicEps': 'float',
              'dilutedEps': 'float', 'othComprIncome': 'float', 'othEffectCi': 'float', 'aeEffectCi': 'float',
              'tComprIncome': 'float', 'comprIncAttrP': 'float', 'comprIncAttrMS': 'float', 'othEffectPci': 'float',
              'aeEffectPci': 'float', 'actPubtime': 'varchar(57)', 'publishDate': 'long'}

    tb.create_table('fdmtisindu2018', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# incom.py
def create_table_fdmtissecu2018():
    schema = {'partyID': 'long', 'ticker': 'varchar(18)', 'exchangeCD': 'varchar(12)', 'actPubtime': 'varchar(57)',
              'secID': 'varchar(33)', 'publishDate': 'long', 'secShortName': 'varchar(12)', 'endDateRep': 'varchar(30)',
              'endDate': 'varchar(30)', 'reportType': 'varchar(6)', 'fiscalPeriod': 'long', 'mergedFlag': 'varchar(3)',
              'accoutingStandards': 'varchar(27)', 'currencyCD': 'varchar(9)', 'industryCategory': 'varchar(9)',
              'revenue': 'float', 'nCommisIncome': 'float', 'nSecTaIncome': 'float', 'nUndwrtSecIncome': 'float',
              'nTrustIncome': 'float', 'nIntIncome': 'float', 'othGain': 'float', 'investIncome': 'float',
              'aJInvestIncome': 'float', 'tafQuitGain': 'float', 'netExpHIncome': 'float', 'fValueChgGain': 'float',
              'assetsImpairLoss': 'float', 'creditImpairLoss': 'float', 'assetsDispGain': 'float',
              'forexGain': 'float', 'othOperRev': 'float', 'specOr': 'float', 'aor': 'float', 'cogs': 'float',
              'bizTaxSurchg': 'float', 'genlAdminExp': 'float', 'othOperCosts': 'float', 'specOp': 'float',
              'aop': 'float', 'othEffectOp': 'float', 'aeEffectOp': 'float', 'operateProfit': 'float',
              'noperateIncome': 'float', 'noperateExp': 'float', 'othEffectTp': 'float', 'aeEffectTp': 'float',
              'tProfit': 'float', 'incomeTax': 'float', 'othEffectNp': 'float', 'aeEffectNp': 'float',
              'nIncome': 'float', 'nIncomeAttrP': 'float', 'minorityGain': 'float', 'goingConcernNi': 'float',
              'quitConcernNi': 'float', 'othEffectNpp': 'float', 'aeEffectNpp': 'float', 'basicEps': 'float',
              'dilutedEps': 'float', 'othComprIncome': 'float', 'othEffectCi': 'float', 'aeEffectCi': 'float',
              'tComprIncome': 'float', 'comprIncAttrP': 'float', 'comprIncAttrMS': 'float', 'othEffectPci': 'float',
              'aeEffectPci': 'float'}

    tb.create_table('fdmtissecu2018', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# incom.py
def create_table_fdmtisinsu2018():
    schema = {'partyID': 'long', 'ticker': 'varchar(18)', 'exchangeCD': 'varchar(12)', 'actPubtime': 'varchar(57)',
              'secID': 'varchar(33)', 'publishDate': 'long', 'secShortName': 'varchar(15)', 'endDateRep': 'varchar(30)',
              'endDate': 'varchar(30)', 'reportType': 'varchar(6)', 'fiscalPeriod': 'long', 'mergedFlag': 'varchar(3)',
              'accoutingStandards': 'varchar(27)', 'currencyCD': 'varchar(9)', 'industryCategory': 'varchar(9)',
              'revenue': 'float', 'premEarned': 'float', 'grossPremWrit': 'float', 'reinsIncome': 'float',
              'reinsur': 'float', 'unePremReser': 'float', 'othGain': 'float', 'investIncome': 'float',
              'aJInvestIncome': 'float', 'tafQuitGain': 'float', 'netExpHIncome': 'float', 'fValueChgGain': 'float',
              'assetsImpairLoss': 'float', 'creditImpairLoss': 'float', 'assetsDispGain': 'float',
              'forexGain': 'float', 'othOperRev': 'float', 'specOr': 'float', 'aor': 'float', 'cogs': 'float',
              'premRefund': 'float', 'compensPayout': 'float', 'compensPayoutRefu': 'float',
              'reserInsurLiab': 'float', 'insurLiabReserRefu': 'float', 'policyDivPayt': 'float',
              'reinsurExp': 'float', 'bizTaxSurchg': 'float', 'commisExp': 'float', 'genlAdminExp': 'float',
              'reinsCostRefund': 'float', 'othOperCosts': 'float', 'specOp': 'float', 'aop': 'float',
              'othEffectOp': 'float', 'aeEffectOp': 'float', 'operateProfit': 'float', 'noperateIncome': 'float',
              'noperateExp': 'float', 'othEffectTp': 'float', 'aeEffectTp': 'float', 'tProfit': 'float',
              'incomeTax': 'float', 'othEffectNp': 'float', 'aeEffectNp': 'float', 'nIncome': 'float',
              'goingConcernNi': 'float', 'quitConcernNi': 'float', 'nIncomeAttrP': 'float', 'minorityGain': 'float',
              'othEffectNpp': 'float', 'aeEffectNpp': 'float', 'basicEps': 'float', 'dilutedEps': 'float',
              'othComprIncome': 'float', 'othEffectCi': 'float', 'aeEffectCi': 'float', 'tComprIncome': 'float',
              'comprIncAttrP': 'float', 'comprIncAttrMS': 'float', 'othEffectPci': 'float', 'aeEffectPci': 'float'}

    tb.create_table('fdmtisinsu2018', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# incom_2007.py
def create_table_fdmtisbank():
    schema = {'secID': 'varchar(33)', 'publishDate': 'long', 'endDate': 'varchar(30)', 'endDateRep': 'varchar(30)',
              'partyID': 'long', 'ticker': 'varchar(18)', 'secShortName': 'varchar(12)', 'exchangeCD': 'varchar(12)',
              'actPubtime': 'varchar(57)', 'mergedFlag': 'varchar(3)', 'reportType': 'varchar(9)',
              'fiscalPeriod': 'varchar(6)', 'accoutingStandards': 'varchar(27)', 'currencyCD': 'varchar(9)',
              'revenue': 'float', 'NIntIncome': 'float', 'intIncome': 'float', 'intExp': 'float',
              'NCommisIncome': 'float', 'commisIncome': 'float', 'commisExp': 'float', 'othOperRev': 'float',
              'specOR': 'float', 'AOR': 'float', 'COGS': 'float', 'bizTaxSurchg': 'float', 'genlAdminExp': 'float',
              'assetsImpairLoss': 'float', 'othOperCosts': 'float', 'specOC': 'float', 'AOC': 'float',
              'fValueChgGain': 'float', 'investIncome': 'float', 'AJInvestIncome': 'float', 'forexGain': 'float',
              'assetsDispGain': 'float', 'othGain': 'float', 'othEffectOP': 'float', 'aeEffectOp': 'float',
              'operateProfit': 'float', 'NoperateIncome': 'float', 'NoperateExp': 'float', 'othEffectTP': 'float',
              'AEEffectTP': 'float', 'TProfit': 'float', 'incomeTax': 'float', 'othEffectNP': 'float',
              'AEEffectNP': 'float', 'NIncome': 'float', 'goingConcernNI': 'float', 'quitConcernNI': 'float',
              'NIncomeAttrP': 'float', 'minorityGain': 'float', 'othEffectNPP': 'float', 'AEEffectNPP': 'float',
              'basicEPS': 'float', 'dilutedEPS': 'float', 'othComprIncome': 'float', 'othEffectCI': 'float',
              'AEEffectCI': 'float', 'TComprIncome': 'float', 'comprIncAttrP': 'float', 'comprIncAttrMS': 'float',
              'othEffectPCI': 'float', 'AEEffectPCI': 'float', 'updateTime': 'varchar(57)'}

    tb.create_table('fdmtisbank', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# incom_2007.py
def create_table_fdmtisindu():
    schema = {'secID': 'varchar(36)', 'publishDate': 'long', 'endDate': 'varchar(30)', 'endDateRep': 'varchar(30)',
              'partyID': 'long', 'ticker': 'varchar(18)', 'secShortName': 'varchar(18)', 'exchangeCD': 'varchar(12)',
              'actPubtime': 'varchar(57)', 'mergedFlag': 'varchar(3)', 'reportType': 'varchar(9)',
              'fiscalPeriod': 'varchar(6)', 'accoutingStandards': 'varchar(27)', 'currencyCD': 'varchar(9)',
              'tRevenue': 'float', 'revenue': 'float', 'intIncome': 'float', 'intExp': 'float',
              'premEarned': 'float', 'commisIncome': 'float', 'commisExp': 'float', 'specTOR': 'float',
              'ATOR': 'float', 'TCogs': 'float', 'COGS': 'float', 'premRefund': 'float', 'NCompensPayout': 'float',
              'reserInsurContr': 'float', 'policyDivPayt': 'float', 'reinsurExp': 'float', 'bizTaxSurchg': 'float',
              'sellExp': 'float', 'adminExp': 'float', 'finanExp': 'float', 'assetsImpairLoss': 'float',
              'specTOC': 'float', 'ATOC': 'float', 'fValueChgGain': 'float', 'investIncome': 'float',
              'AJInvestIncome': 'float', 'forexGain': 'float', 'assetsDispGain': 'float', 'othGain': 'float',
              'othEffectOP': 'float', 'aeEffectOp': 'float', 'operateProfit': 'float', 'NoperateIncome': 'float',
              'NoperateExp': 'float', 'NCADisploss': 'float', 'othEffectTP': 'float', 'AEEffectTP': 'float',
              'TProfit': 'float', 'incomeTax': 'float', 'othEffectNP': 'float', 'AEEffectNP': 'float',
              'NIncome': 'float', 'goingConcernNI': 'float', 'quitConcernNI': 'float', 'NIncomeAttrP': 'float',
              'NIncomeBMA': 'float', 'minorityGain': 'float', 'othEffectNPP': 'float', 'AEEffectNPP': 'float',
              'basicEPS': 'float', 'dilutedEPS': 'float', 'othComprIncome': 'float', 'othEffectCI': 'float',
              'AEEffectCI': 'float', 'TComprIncome': 'float', 'comprIncAttrP': 'float', 'comprIncAttrMS': 'float',
              'othEffectPCI': 'float', 'AEEffectPCI': 'float', 'updateTime': 'varchar(57)'}

    tb.create_table('fdmtisindu', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# incom_2007.py
def create_table_fdmtissecu():
    schema = {'secID': 'varchar(33)', 'publishDate': 'long', 'endDate': 'varchar(30)', 'endDateRep': 'varchar(30)',
              'partyID': 'long', 'ticker': 'varchar(18)', 'secShortName': 'varchar(12)', 'exchangeCD': 'varchar(12)',
              'actPubtime': 'varchar(57)', 'mergedFlag': 'varchar(3)', 'reportType': 'varchar(9)',
              'fiscalPeriod': 'varchar(6)', 'accoutingStandards': 'varchar(27)', 'currencyCD': 'varchar(9)',
              'revenue': 'float', 'NIntIncome': 'float', 'NCommisIncome': 'float', 'NSecTaIncome': 'float',
              'NUndwrtSecIncome': 'float', 'NTrustIncome': 'float', 'othOperRev': 'float', 'specOR': 'float',
              'AOR': 'float', 'COGS': 'float', 'bizTaxSurchg': 'float', 'genlAdminExp': 'float',
              'assetsImpairLoss': 'float', 'othOperCosts': 'float', 'specOC': 'float', 'AOC': 'float',
              'fValueChgGain': 'float', 'investIncome': 'float', 'AJInvestIncome': 'float', 'forexGain': 'float',
              'assetsDispGain': 'float', 'othGain': 'float', 'othEffectOP': 'float', 'aeEffectOp': 'float',
              'operateProfit': 'float', 'NoperateIncome': 'float', 'NoperateExp': 'float', 'othEffectTP': 'float',
              'AEEffectTP': 'float', 'TProfit': 'float', 'incomeTax': 'float', 'othEffectNP': 'float',
              'AEEffectNP': 'float', 'NIncome': 'float', 'goingConcernNI': 'float', 'quitConcernNI': 'float',
              'NIncomeAttrP': 'float', 'minorityGain': 'float', 'othEffectNPP': 'float', 'AEEffectNPP': 'float',
              'basicEPS': 'float', 'dilutedEPS': 'float', 'othComprIncome': 'float', 'othEffectCI': 'float',
              'AEEffectCI': 'float', 'TComprIncome': 'float', 'comprIncAttrP': 'float', 'comprIncAttrMS': 'float',
              'othEffectPCI': 'float', 'AEEffectPCI': 'float', 'updateTime': 'varchar(57)'}

    tb.create_table('fdmtissecu', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# incom_2007.py
def create_table_fdmtisinsu():
    schema = {'secID': 'varchar(33)', 'publishDate': 'long', 'endDate': 'varchar(30)', 'endDateRep': 'varchar(30)',
              'partyID': 'long', 'ticker': 'varchar(18)', 'secShortName': 'varchar(15)', 'exchangeCD': 'varchar(12)',
              'actPubtime': 'varchar(57)', 'mergedFlag': 'varchar(3)', 'reportType': 'varchar(9)',
              'fiscalPeriod': 'varchar(3)', 'accoutingStandards': 'varchar(27)', 'currencyCD': 'varchar(9)',
              'revenue': 'float', 'premEarned': 'float', 'grossPremWrit': 'float', 'reinsIncome': 'float',
              'reinsur': 'float', 'unePremReser': 'float', 'commisExp': 'float', 'othOperRev': 'float',
              'specOR': 'float', 'AOR': 'float', 'COGS': 'float', 'premRefund': 'float', 'compensPayout': 'float',
              'compensPayoutRefu': 'float', 'reserInsurLiab': 'float', 'insurLiabReserRefu': 'float',
              'policyDivPayt': 'float', 'reinsurExp': 'float', 'bizTaxSurchg': 'float', 'genlAdminExp': 'float',
              'reinsCostRefund': 'float', 'assetsImpairLoss': 'float', 'othOperCosts': 'float', 'specOC': 'float',
              'AOC': 'float', 'fValueChgGain': 'float', 'investIncome': 'float', 'AJInvestIncome': 'float',
              'forexGain': 'float', 'assetsDispGain': 'float', 'othGain': 'float', 'othEffectOP': 'float',
              'aeEffectOp': 'float', 'operateProfit': 'float', 'NoperateIncome': 'float', 'NoperateExp': 'float',
              'othEffectTP': 'float', 'AEEffectTP': 'float', 'TProfit': 'float', 'incomeTax': 'float',
              'othEffectNP': 'float', 'AEEffectNP': 'float', 'NIncome': 'float', 'goingConcernNI': 'float',
              'quitConcernNI': 'float', 'NIncomeAttrP': 'float', 'minorityGain': 'float', 'othEffectNPP': 'float',
              'AEEffectNPP': 'float', 'basicEPS': 'float', 'dilutedEPS': 'float', 'othComprIncome': 'float',
              'othEffectCI': 'float', 'AEEffectCI': 'float', 'TComprIncome': 'float', 'comprIncAttrP': 'float',
              'comprIncAttrMS': 'float', 'othEffectPCI': 'float', 'AEEffectPCI': 'float',
              'updateTime': 'varchar(57)'}

    tb.create_table('fdmtisinsu', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# InstSstate.py
def create_table_equinstssta():
    schema = {'secID': 'varchar(33)', 'ticker': 'varchar(18)', 'secShortName': 'varchar(12)',
              'exchangeCD': 'varchar(12)', 'partyState': 'long', 'effDate': 'long', 'reason': 'float',
              'updateTime': 'varchar(57)'}

    tb.create_table('equinstssta', schema, 'effDate', 'time_colunm', 'security_column', 0)


# mktblockD.py
def create_table_mktblockd():
    schema = {'tradeDate': 'long', 'secID': 'varchar(33)', 'ticker': 'varchar(18)', 'assetClass': 'varchar(3)',
              'exchangeCD': 'varchar(12)', 'secFullName': 'varchar(69)', 'currencyCD': 'varchar(9)',
              'tradePrice': 'float', 'tradeVal': 'float', 'tradeVol': 'float', 'buyerBD': 'varchar(81)',
              'sellerBD': 'varchar(81)'}

    tb.create_table('mktblockd', schema, 'tradeDate', 'time_colunm', 'security_column', 0)


# mktequd.py
def create_table_mktequd():
    schema = {'secID': 'varchar(33)', 'ticker': 'varchar(18)', 'secShortName': 'varchar(18)',
              'exchangeCD': 'varchar(12)', 'tradeDate': 'long', 'preClosePrice': 'float', 'actPreClosePrice': 'float',
              'openPrice': 'float', 'highestPrice': 'float', 'lowestPrice': 'float', 'closePrice': 'float',
              'turnoverVol': 'float', 'turnoverValue': 'float', 'dealAmount': 'float', 'turnoverRate': 'float',
              'accumAdjFactor': 'float', 'negMarketValue': 'float', 'marketValue': 'float', 'chgPct': 'float',
              'PE': 'float', 'PE1': 'float', 'PB': 'float', 'isOpen': 'long', 'vwap': 'float'}

    tb.create_table('mktequd', schema, 'tradeDate', 'time_colunm', 'security_column', 0)


# mktequd.py
def create_table_mktequdadjadj():
    schema = {'secID': 'varchar(33)', 'ticker': 'varchar(18)', 'secShortName': 'varchar(18)',
              'exchangeCD': 'varchar(12)', 'tradeDate': 'long', 'preClosePrice': 'float', 'actPreClosePrice': 'float',
              'openPrice': 'float', 'highestPrice': 'float', 'lowestPrice': 'float', 'closePrice': 'float',
              'turnoverVol': 'float', 'negMarketValue': 'float', 'dealAmount': 'float', 'turnoverRate': 'float',
              'accumAdjFactor': 'float', 'turnoverValue': 'float', 'marketValue': 'float', 'isOpen': 'long',
              'vwap': 'float'}

    tb.create_table('mktequdadjadj', schema, 'tradeDate', 'time_colunm', 'security_column', 0)


# mktequd.py
def create_table_mktequdadjaf():
    schema = {'secID': 'varchar(33)', 'ticker': 'varchar(18)', 'secShortName': 'varchar(18)',
              'exchangeCD': 'varchar(12)', 'tradeDate': 'long', 'preClosePrice': 'float', 'actPreClosePrice': 'float',
              'openPrice': 'float', 'highestPrice': 'float', 'lowestPrice': 'float', 'closePrice': 'float',
              'turnoverVol': 'float', 'turnoverValue': 'float', 'dealAmount': 'float', 'turnoverRate': 'float',
              'accumAdjFactor': 'float', 'negMarketValue': 'float', 'marketValue': 'float', 'isOpen': 'long',
              'vwap': 'float'}

    tb.create_table('mktequdadjaf', schema, 'tradeDate', 'time_colunm', 'security_column', 0)


# production.py
def create_table_equcompproduction():
    schema = {'item': 'varchar(15)', 'ticker': 'varchar(18)', 'secShortName': 'varchar(15)', 'prodName': 'varchar(51)',
              'prodPct': 'float', 'periodDate': 'long', 'updateTime': 'varchar(57)'}

    tb.create_table('equcompproduction', schema, 'periodDate', 'time_colunm', 'security_column', 0)


# ranklist.py
def create_table_mktrankliststocks():
    schema = {'secID': 'varchar(33)', 'ticker': 'varchar(18)', 'secShortName': 'varchar(15)',
              'exchangeCD': 'varchar(12)', 'tradeDate': 'long', 'abnormalTypeCD': 'long',
              'abnormalType': 'varchar(123)', 'deviation': 'float', 'turnoverVol': 'float', 'turnoverValue': 'float',
              'abnormalBeginDate': 'varchar(30)', 'abnormalEndDate': 'varchar(30)'}

    tb.create_table('mktrankliststocks', schema, 'tradeDate', 'time_colunm', 'security_column', 0)


# ranklist.py
def create_table_mktranklistsales():
    schema = {'secID': 'varchar(33)', 'ticker': 'varchar(18)', 'secShortName': 'varchar(15)',
              'exchangeCD': 'varchar(12)', 'tradeDate': 'long', 'side': 'varchar(3)', 'rank': 'long',
              'sales': 'varchar(81)', 'buyValue': 'float', 'sellValue': 'float', 'totalValue': 'float',
              'abnormalTypeCD': 'long', 'updateTime': 'varchar(57)'}

    tb.create_table('mktranklistsales', schema, 'tradeDate', 'time_colunm', 'security_column', 0)


# reportPre.py
def create_table_equreportpredisclo():
    schema = {'secID': 'varchar(33)', 'ticker': 'varchar(18)', 'secShortName': 'varchar(15)',
              'exchangeCD': 'varchar(12)', 'preDate': 'long', 'endDate': 'varchar(30)',
              'actDate': 'varchar(30)', 'updateDate1': 'varchar(30)', 'updateDate2': 'varchar(30)',
              'updateDate3': 'varchar(30)'}

    tb.create_table('equreportpredisclo', schema, 'preDate', 'time_colunm', 'security_column', 0)


# SecChgHistoryGet.py
def create_table_secchghistory():
    schema = {'date':'long', 'secID': 'varchar(33)', 'ticker': 'varchar(18)', 'changType': 'varchar(12)',
              'value': 'varchar(18)', 'beginDate': 'varchar(30)', 'endDate': 'varchar(30)',
              'secShortName': 'varchar(18)', 'assetClass': 'varchar(3)', 'exchangeCD': 'varchar(12)'}

    tb.create_table('secchghistory', schema, 'date', 'time_colunm', 'security_column', 0)


# sechalt.py
def create_table_sechalt():
    schema = {'tradeDate':'long', 'secID': 'varchar(33)', 'haltBeginTime': 'varchar(57)', 'haltEndTime': 'varchar(57)',
              'ticker': 'varchar(18)', 'secShortName': 'varchar(15)', 'exchangeCD': 'varchar(12)',
              'listStatusCD': 'varchar(3)', 'delistDate': 'varchar(9)', 'assetClass': 'varchar(3)'}

    tb.create_table('sechalt', schema, 'tradeDate', 'time_colunm', 'security_column', 0)


# sharefloat.py
def create_table_equsharesfloat():
    schema = {'secID': 'varchar(33)', 'ticker': 'varchar(18)', 'secShortName': 'varchar(12)',
              'exchangeCD': 'varchar(12)', 'publishDate': 'long', 'floatDate': 'varchar(30)',
              'floatNum': 'float', 'shareProperty': 'varchar(6)'}

    tb.create_table('equsharesfloat', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# shares.py
def create_table_equshareschg():
    schema = {'partyID': 'long', 'secID': 'varchar(36)', 'ticker': 'varchar(18)', 'secShortName': 'varchar(12)',
              'exchangeCD': 'varchar(12)', 'publishDate': 'long', 'changeDate': 'varchar(30)',
              'changeType': 'varchar(15)', 'totalShares': 'float', 'floatShares': 'float',
              'floatA': 'float', 'floatB': 'float', 'floatH': 'float', 'floatOverseas': 'float',
              'restShares': 'float', 'restA': 'float', 'restState': 'float',
              'restStateLegal': 'float', 'restOtherDome': 'float', 'restLegalPer': 'float',
              'restPer': 'float', 'restManager': 'float', 'restFr': 'float',
              'restFrLegalPer': 'float', 'restFrPer': 'float', 'restB': 'float',
              'restH': 'float', 'nonfShares': 'float', 'nonfStateShares': 'float',
              'nonfStateLegal': 'float', 'nonfDomeCap': 'float', 'nonfFr': 'float',
              'nonfFrLegalPer': 'float', 'nonfOtherFr': 'float', 'nonfOthSpoShares': 'float',
              'nonfCorpRa': 'float', 'nonfStateLegalRa': 'float', 'nonfPerson': 'float',
              'nonfEmployee': 'float', 'nonfTransfer': 'float', 'nonfPreOther': 'float',
              'nonfPre': 'float', 'updateTime': 'varchar(57)'}

    tb.create_table('equshareschg', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# shares.py
def create_table_equfreeshares():
    schema = {'ticker': 'varchar(18)', 'partyID': 'long', 'partyShortName': 'varchar(12)',
              'partyFullName': 'varchar(48)', 'publishDate': 'varchar(30)', 'changeDate': 'long',
              'freeShares': 'float'}

    tb.create_table('equfreeshares', schema, 'changeDate', 'time_colunm', 'security_column', 0)


# shares.py
def create_table_equallot():
    schema = {'date':'long', 'secID': 'varchar(33)', 'ticker': 'varchar(18)', 'exchangeCD': 'varchar(12)',
              'secShortName': 'varchar(18)', 'publishDate': 'varchar(30)', 'isAllotment': 'long',
              'equType': 'varchar(6)', 'allotmentRatio': 'float', 'allotmentPrice': 'float',
              'currencyCD': 'varchar(9)', 'allotFrPrice': 'float', 'frCurrencyCD': 'varchar(12)',
              'recordDate': 'varchar(30)', 'exRightsDate': 'varchar(30)', 'payBeginDate': 'varchar(30)',
              'payEndDate': 'varchar(30)', 'listDate': 'varchar(30)', 'allotShares': 'float',
              'sharesBfAllot': 'varchar(42)', 'sharesAfAllot': 'varchar(42)'}

    tb.create_table('equallot', schema, 'date', 'time_colunm', 'security_column', 0)


# shTen.py
def create_table_equshten():
    schema = {'secID': 'varchar(36)', 'ticker': 'varchar(18)', 'secShortName': 'varchar(15)',
              'exchangeCD': 'varchar(12)', 'endDate': 'long', 'shNum': 'long', 'shName': 'varchar(189)',
              'holdVol': 'float', 'holdPct': 'float', 'shareType': 'varchar(33)', 'updateTime': 'varchar(57)',
              'publishDate': 'varchar(30)'}

    tb.create_table('equshten', schema, 'endDate', 'time_colunm', 'security_column', 0)


# stock_FctIndic.py
def create_table_stockfctindiconeday():
    schema = {'secID': 'varchar(36)', 'ticker': 'varchar(18)', 'tradeDate': 'long', 'EBITPS': 'float',
              'RESERPS': 'float', 'dividendPS': 'float', 'invCFNetInc': 'float', 'finCFNetInc': 'float',
              'finCFps': 'float', 'invCFps': 'float', 'revenueC3': 'float', 'revenueC5': 'float',
              'netProfitC3': 'float', 'netProfitC5': 'float', 'roe5': 'float', 'CEps': 'float', 'TAps': 'float',
              'chgPct': 'float', 'totalShares': 'float', 'nonrestFloat': 'float', 'dealAmount': 'float',
              'priceAmp': 'float', 'daysOnMkt': 'float', 'tradeDays': 'float', 'inflowT': 'float',
              'outflowT': 'float', 'netInflowT': 'float', 'inflowS': 'float', 'inflowM': 'float',
              'inflowL': 'float', 'inflowXl': 'float', 'outflowS': 'float', 'outflowM': 'float',
              'outflowL': 'float', 'outflowXl': 'float', 'netInflowS': 'float', 'netInflowS5': 'float',
              'netInflowS20': 'float', 'netInflowM': 'float', 'netInflowM5': 'float', 'netInflowM20': 'float',
              'netInflowL': 'float', 'netInflowL5': 'float', 'netInflowL20': 'float', 'netInflowXl': 'float',
              'netInflowXl5': 'float', 'netInflowXl20': 'float', 'upLimitTimes': 'float', 'upLimitOpen': 'float',
              'upLimitDay': 'float', 'udLimitTimes': 'float', 'dnLimitTimes': 'float', 'dnLimitOpen': 'float',
              'dnLimitDay': 'float', 'top5NetIn': 'float', 'top5NetOut': 'float', 'tWorth': 'float',
              'tROE': 'float', 'tProfit': 'float', 'tPrice': 'float', 'tPE': 'float', 'tMobility': 'float',
              'tMVStyle': 'float', 'tLeverage': 'float', 'tHbeta': 'float', 'tGrowth': 'float',
              'bulkFundNum': 'float', 'bulkFundPct': 'float', 'bollUpBreak': 'float', 'bollDnBreak': 'float',
              'rsiGoldCross': 'float', 'rsiDeathCross': 'float', 'rsiTopDiver': 'float', 'rsiBtmDiver': 'float',
              'rsiShort': 'float', 'rsiLong': 'float', 'volGoldCross': 'float', 'volDeathCross': 'float',
              'volLong': 'float', 'volShort': 'float', 'maLong': 'float', 'maShort': 'float',
              'maDeathCross': 'float', 'maGoldCross': 'float', 'emaLong': 'float', 'emaShort': 'float',
              'emaGoldCross': 'float', 'emaDeathCross': 'float', 'macdLong': 'float', 'macdShort': 'float',
              'macdTopDiver': 'float', 'macdBtmDiver': 'float', 'macdGoldCross': 'float', 'macdDeathCross': 'float',
              'macdTopDiverW': 'float', 'macdBtmDiverW': 'float', 'macdGoldCrossW': 'float',
              'macdDeathCrossW': 'float', 'mfiOB': 'float', 'mfiOS': 'float', 'crOB': 'float', 'crOS': 'float',
              'cciOB': 'float', 'cciOS': 'float', 'kdjLong': 'float', 'kdjShort': 'float',
              'kdjLGoldCross': 'float', 'kdjHDeathCross': 'float', 'kdjBtmDiver': 'float', 'kdjTopDiver': 'float',
              'volatility20': 'float', 'volatility60': 'float', 'volatility120': 'float', 'boldHead': 'float',
              'boldBottom': 'float', 'longUpShadow': 'float', 'midUpShadow': 'float', 'longLowShadow': 'float',
              'midLowShadow': 'float', 'openLow': 'float', 'jumpOpenLow': 'float', 'sunK': 'float',
              'microSun': 'float', 'shortSun': 'float', 'midSun': 'float', 'longSun': 'float', 'lunarK': 'float',
              'microLunar': 'float', 'shortLunar': 'float', 'midLunar': 'float', 'longLunar': 'float',
              'longT': 'float', 'revLongT': 'float', 'oneFlag': 'float', 'cross': 'float', 'shootStar': 'float',
              'crossDying': 'float', 'longCross': 'float', 'bearishEngulf': 'float', 'shrinkVol': 'float',
              'enlargeVol': 'float', 'above20High': 'float', 'above60High': 'float', 'below20Low': 'float',
              'below60Low': 'float', 'openHigh': 'float', 'multiLongMark': 'float', 'jumpOpenHigh': 'float',
              'mgrHIncNum': 'float', 'mgrHIncAmt': 'float', 'mgrHIncTimes': 'float', 'mgrHIncPct': 'float',
              'mgrHIncNum5': 'float', 'mgrHIncAmt5': 'float', 'mgrHIncTimes5': 'float', 'mgrHIncPct5': 'float',
              'mgrHIncNum20': 'float', 'mgrHIncAmt20': 'float', 'mgrHIncTimes20': 'float', 'mgrHIncPct20': 'float',
              'rFloatNum': 'float', 'rFloatPct': 'float', 'rFloatNum20': 'float', 'rFloatPct20': 'float',
              'rFloatNum60': 'float', 'rFloatPct60': 'float', 'accuPFloor': 'float', 'accuPCeil': 'float',
              'preAccuPFloor': 'float', 'preAccuPCeil': 'float', 'preDays': 'float', 'preSTIn': 'float',
              'preSTSpd': 'float', 'punishMark': 'float', 'holderNum': 'float', 'avgHoldings': 'float',
              'holderChgPct60': 'float', 'instHoldPct': 'float', 'instHoldLrr': 'float', 'stateHoldPct': 'float',
              'stateHoldLrr': 'float', 'socialHoldPct': 'float', 'socialHoldLrr': 'float', 'top10HoldPct': 'float',
              'top10HoldLrr': 'float'}

    tb.create_table('stockfctindiconeday', schema, 'tradeDate', 'time_colunm', 'security_column', 0)


# tips.py
def create_table_sectips():
    schema = {'secID': 'varchar(33)', 'ticker': 'varchar(18)', 'exchangeCD': 'varchar(12)',
              'secShortName': 'varchar(15)', 'tipsDesc': 'varchar(126)', 'tipsTypeCD': 'varchar(3)',
              'tipsType': 'varchar(6)', 'tradeDate': 'long'}

    tb.create_table('sectips', schema, 'tradeDate', 'time_colunm', 'security_column', 0)


# tradeCal_trade.py
def create_table_tradecal():
    schema = {'exchangeCD': 'varchar(12)', 'calendarDate': 'long', 'isOpen': 'long',
              'prevTradeDate': 'varchar(30)', 'isWeekEnd': 'long', 'isMonthEnd': 'long', 'isQuarterEnd': 'long',
              'isYearEnd': 'long'}

    tb.create_table('tradecal', schema, 'calendarDate', 'time_colunm', 'security_column', 0)


# tradeCal_work.py
def create_table_workingcal():
    schema = {'calendarDate': 'long', 'isWork': 'long', 'prevWorkDate': 'varchar(30)', 'weekStartDate': 'varchar(30)',
              'weekEndDate': 'varchar(30)', 'monthStartDate': 'varchar(30)', 'monthEndDate': 'varchar(30)',
              'quarterStartDate': 'varchar(30)', 'quarterEndDate': 'varchar(30)', 'yearStartDate': 'varchar(30)',
              'yearEndDate': 'varchar(30)', 'updateTime': 'varchar(57)'}

    tb.create_table('workingcal', schema, 'calendarDate', 'time_colunm', 'security_column', 0)


# TTM_PIT.py
def create_table_fdmtcfinduttmpit():
    schema = {'secID': 'varchar(36)', 'partyID': 'long', 'ticker': 'varchar(18)', 'secShortName': 'varchar(12)',
              'exchangeCD': 'varchar(12)', 'endDate': 'varchar(30)', 'publishDate': 'long', 'isNew': 'long',
              'isCalc': 'long', 'CFrSaleGS': 'float', 'NDeposIncrCFI': 'float', 'NIncrBorrFrCB': 'float',
              'NIncBorrOthFI': 'float', 'premFrOrigContr': 'float', 'NReinsurPrem': 'float',
              'NIncPhDeposInv': 'float', 'NIncDispTradFA': 'float', 'IFCCashIncr': 'float', 'NIncFrBorr': 'float',
              'NCApIncrRepur': 'float', 'refundOfTax': 'float', 'CFrOthOperateA': 'float',
              'CInfFrOperateA': 'float', 'CPaidGS': 'float', 'NIncDisburOfLA': 'float', 'NIncrDeposInFI': 'float',
              'origContrCIndem': 'float', 'CPaidIFC': 'float', 'CPaidPolDiv': 'float', 'CPaidToForEmpl': 'float',
              'CPaidForTaxes': 'float', 'CPaidForOthOpA': 'float', 'COutfOperateA': 'float', 'NCFOperateA': 'float',
              'procSellInvest': 'float', 'gainInvest': 'float', 'dispFixAssetsOth': 'float',
              'NDispSubsOthBizC': 'float', 'CFrOthInvestA': 'float', 'CInfFrInvestA': 'float',
              'purFixAssetsOth': 'float', 'CPaidInvest': 'float', 'NIncrPledgeLoan': 'float',
              'NCPaidAcquis': 'float', 'CPaidOthInvestA': 'float', 'COutfFrInvestA': 'float',
              'NCFFrInvestA': 'float', 'CFrCapContr': 'float', 'CFrMinoSSubs': 'float', 'CFrBorr': 'float',
              'CFrIssueBond': 'float', 'CFrOthFinanA': 'float', 'CInfFrFinanA': 'float', 'CPaidForDebts': 'float',
              'CPaidDivProfInt': 'float', 'divProfSubsMinoS': 'float', 'CPaidOthFinanA': 'float',
              'COutfFrFinanA': 'float', 'NCFFrFinanA': 'float', 'forexEffects': 'float', 'NChangeInCash': 'float',
              'NCEBegBal': 'float', 'NCEEndBal': 'float'}

    tb.create_table('fdmtcfinduttmpit', schema, 'publishDate', 'time_colunm', 'security_column', 0)


# TTM_PIT.py
def create_table_fdmtisinduttmpit():
    schema = {'secID': 'varchar(33)', 'partyID': 'long', 'ticker': 'varchar(18)', 'secShortName': 'varchar(12)',
              'exchangeCD': 'varchar(12)', 'endDate': 'varchar(30)', 'publishDate': 'long', 'isNew': 'long',
              'isCalc': 'long', 'tRevenue': 'float', 'revenue': 'float', 'intIncome': 'float',
              'premEarned': 'float', 'commisIncome': 'float', 'TCogs': 'float', 'COGS': 'float',
              'intExp': 'float', 'commisExp': 'float', 'premRefund': 'float', 'NCompensPayout': 'float',
              'reserInsurContr': 'float', 'policyDivPayt': 'float', 'reinsurExp': 'float', 'bizTaxSurchg': 'float',
              'sellExp': 'float', 'adminExp': 'float', 'finanExp': 'float', 'assetsImpairLoss': 'float',
              'fValueChgGain': 'float', 'investIncome': 'float', 'AJInvestIncome': 'float', 'forexGain': 'float',
              'assetsDispGain': 'float', 'othGain': 'float', 'operateProfit': 'float', 'NoperateIncome': 'float',
              'NoperateExp': 'float', 'NCADisploss': 'float', 'TProfit': 'float', 'incomeTax': 'float',
              'NIncome': 'float', 'goingConcernNI': 'float', 'quitConcernNI': 'float', 'NIncomeAttrP': 'float',
              'minorityGain': 'float', 'othComprIncome': 'float', 'TComprIncome': 'float', 'comprIncAttrP': 'float',
              'comprIncAttrMS': 'float'}

    tb.create_table('fdmtisinduttmpit', schema, 'publishDate', 'time_colunm', 'security_column', 0)



# WMQY.py
def create_table_mktequwadjaf():
    schema = {'secID': 'varchar(33)', 'ticker': 'varchar(18)', 'secShortName': 'varchar(18)',
              'exchangeCD': 'varchar(12)', 'weekBeginDate': 'varchar(30)', 'endDate': 'long', 'tradeDays': 'long',
              'preClosePrice': 'float', 'openPrice': 'float', 'highestPrice': 'float', 'lowestPrice': 'float',
              'closePrice': 'float', 'turnoverVol': 'float', 'turnoverValue': 'float', 'chg': 'float',
              'chgPct': 'float', 'return': 'float', 'turnoverRate': 'float', 'avgTurnoverRate': 'float',
              'varReturn100': 'float', 'sdReturn100': 'float', 'avgReturn100': 'float'}

    tb.create_table('mktequwadjaf', schema, 'endDate', 'time_colunm', 'security_column', 0)


# WMQY.py
def create_table_mktequmadjaf():
    schema = {'secID': 'varchar(33)', 'ticker': 'varchar(18)', 'secShortName': 'varchar(18)',
              'exchangeCD': 'varchar(12)', 'monthBeginDate': 'varchar(30)', 'endDate': 'long', 'tradeDays': 'long',
              'preClosePrice': 'float', 'openPrice': 'float', 'highestPrice': 'float', 'lowestPrice': 'float',
              'closePrice': 'float', 'turnoverVol': 'float', 'turnoverValue': 'float', 'chg': 'float',
              'chgPct': 'float', 'return': 'float', 'turnoverRate': 'float', 'avgTurnoverRate': 'float',
              'varReturn24': 'float', 'sdReturn24': 'float', 'avgReturn24': 'float', 'varReturn60': 'float',
              'sdReturn60': 'float', 'avgReturn60': 'float'}

    tb.create_table('mktequmadjaf', schema, 'endDate', 'time_colunm', 'security_column', 0)


# WMQY.py
def create_table_mktequqadjaf():
    schema = {'secID': 'varchar(33)', 'ticker': 'varchar(18)', 'secShortName': 'varchar(18)',
              'exchangeCD': 'varchar(12)', 'endDate': 'long', 'tradeDays': 'long', 'preClosePrice': 'float',
              'openPrice': 'float', 'highestPrice': 'float', 'lowestPrice': 'float', 'closePrice': 'float',
              'turnoverVol': 'float', 'turnoverValue': 'float', 'chg': 'float', 'chgPct': 'float'}

    tb.create_table('mktequqadjaf', schema, 'endDate', 'time_colunm', 'security_column', 0)


# WMQY.py---年
def create_table_mktequaadjaf():
    schema = {'secID': 'varchar(33)', 'ticker': 'varchar(18)', 'secShortName': 'varchar(18)',
              'exchangeCD': 'varchar(12)', 'endDate': 'long', 'tradeDays': 'long', 'preClosePrice': 'float',
              'openPrice': 'float', 'highestPrice': 'float', 'lowestPrice': 'float', 'closePrice': 'float',
              'turnoverVol': 'float', 'turnoverValue': 'float', 'chg': 'float', 'chgPct': 'float'}

    tb.create_table('mktequaadjaf', schema, 'endDate', 'time_colunm', 'security_column', 0)


# WMQY.py----半年
def create_table_mktequsadjaf():
    schema = {'secID': 'varchar(33)', 'ticker': 'varchar(18)', 'secShortName': 'varchar(18)',
              'exchangeCD': 'varchar(12)', 'endDate': 'long', 'tradeDays': 'long', 'preClosePrice': 'float',
              'openPrice': 'float', 'highestPrice': 'float', 'lowestPrice': 'float', 'closePrice': 'float',
              'turnoverVol': 'float', 'turnoverValue': 'float', 'chg': 'float', 'chgPct': 'float'}

    tb.create_table('mktequsadjaf', schema, 'endDate', 'time_colunm', 'security_column', 0)



if __name__ == "__main__":

    create_table_mktlimit()