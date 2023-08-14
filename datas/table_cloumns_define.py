import json
import aiqdata as tb

def mktadjfaf_define(table_name):

    mktadjfaf_str = {
            "table_name": "mktadjfaf",
            "table_show_name": "沪深股票后复权因子",
            "table_comment": "沪深股票用来调整历史行情的后复权因子数据",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {
                        "col_name": "secID",
                        "col_show_name": "通联编制的证券编码",
                        "col_comment": "通联编制的证券编码-描述"
                },
                {
                        "col_name": "ticker",
                        "col_show_name": "通用交易代码",
                        "col_comment": "通用交易代码-描述"
                },
                {
                        "col_name": "exchangeCD",
                        "col_show_name": "通联编制的交易市场编码",
                        "col_comment": "通联编制的交易市场编码-描述"
                },
                {
                        "col_name": "secShortName",
                        "col_show_name": "证券简称",
                        "col_comment": "证券简称-描述"
                },
                {
                        "col_name": "secShortNameEn",
                        "col_show_name": "证券英文简称",
                        "col_comment": "证券英文简称-描述"
                },
                {
                        "col_name": "exDivDate",
                        "col_show_name": "除权除息日",
                        "col_comment": "除权除息日-描述"
                },
                {
                        "col_name": "perCashDiv",
                        "col_show_name": "每股派现（税前）",
                        "col_comment": "每股派现（税前）-描述"
                },
                {
                        "col_name": "perShareDivRatio",
                        "col_show_name": "每股送股比例",
                        "col_comment": "每股送股比例-描述"
                }
                ,
                {
                        "col_name": "perShareTransRatio",
                        "col_show_name": "每股转增股比例",
                        "col_comment": "每股转增股比例-描述"
                }
                ,
                {
                        "col_name": "allotmentRatio",
                        "col_show_name": "每股配股比例",
                        "col_comment": "每股配股比例-描述"
                }
                ,
                {
                        "col_name": "allotmentPrice",
                        "col_show_name": "配股价",
                        "col_comment": "配股价-描述"
                }
                ,
                {
                        "col_name": "splitsRatio",
                        "col_show_name": "拆股比例",
                        "col_comment": "拆股比例-描述"
                }
                ,
                {
                        "col_name": "adjFactor",
                        "col_show_name": "单次后复权因子，对应一个除权除息日的权息修复比例",
                        "col_comment": "单次后复权因子，对应一个除权除息日的权息修复比例-描述"
                }
                ,
                {
                        "col_name": "accumAdjFactor",
                        "col_show_name": "累积后复权因子，发生在本次除权除息日（含）之前的单次后复权因子累乘",
                        "col_comment": "累积后复权因子，发生在本次除权除息日（含）之前的单次后复权因子累乘-描述"
                }
                ,
                {
                        "col_name": "endDate",
                        "col_show_name": "累积后复权因子截止生效日期，后复权价=对应交易日期在[exDivDate,endDate]区间的未复权价*累积后复权因子",
                        "col_comment": "累积后复权因子截止生效日期，后复权价=对应交易日期在[exDivDate,endDate]区间的未复权价*累积后复权因子-描述"
                }
            ]
        }
    define_json = json.dumps(mktadjfaf_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def mktadjf_define(table_name):

    mktadjf_str = {
            "table_name": "mktadjf",
            "table_show_name": "沪深股票后复权因子",
            "table_comment": "沪深股票用来调整历史行情的后复权因子数据",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {
                        "col_name": "secID",
                        "col_show_name": "通联编制的证券编码",
                        "col_comment": "通联编制的证券编码-描述"
                },
                {
                        "col_name": "ticker",
                        "col_show_name": "通用交易代码",
                        "col_comment": "通用交易代码-描述"
                },
                {
                        "col_name": "exchangeCD",
                        "col_show_name": "通联编制的交易市场编码",
                        "col_comment": "通联编制的交易市场编码-描述"
                },
                {
                        "col_name": "secShortName",
                        "col_show_name": "证券简称",
                        "col_comment": "证券简称-描述"
                },
                {
                        "col_name": "secShortNameEn",
                        "col_show_name": "证券英文简称",
                        "col_comment": "证券英文简称-描述"
                },
                {
                        "col_name": "exDivDate",
                        "col_show_name": "除权除息日，股改对应股改后首个交易日",
                        "col_comment": "除权除息日，股改对应股改后首个交易日-描述"
                },
                {
                        "col_name": "perCashDiv",
                        "col_show_name": "每股派现（税前）",
                        "col_comment": "每股派现（税前）-描述"
                },
                {
                        "col_name": "perShareDivRatio",
                        "col_show_name": "每股送股比例",
                        "col_comment": "每股送股比例-描述"
                }
                ,
                {
                        "col_name": "perShareTransRatio",
                        "col_show_name": "每股转增股比例",
                        "col_comment": "每股转增股比例-描述"
                }
                ,
                {
                        "col_name": "allotmentRatio",
                        "col_show_name": "每股配股比例",
                        "col_comment": "每股配股比例-描述"
                }
                ,
                {
                        "col_name": "allotmentPrice",
                        "col_show_name": "配股价",
                        "col_comment": "配股价-描述"
                }
                ,
                {
                        "col_name": "adjFactor",
                        "col_show_name": "单次后复权因子，对应一个除权除息日的权息修复比例",
                        "col_comment": "单次后复权因子，对应一个除权除息日的权息修复比例-描述"
                }
                ,
                {
                        "col_name": "accumAdjFactor",
                        "col_show_name": "累积前复权因子，发生在本次除权除息日（含）之后的前复权因子累乘。每当有新的前复权因子产生，该股票的所有累积前复权因子均会刷新",
                        "col_comment": "累积前复权因子，发生在本次除权除息日（含）之后的前复权因子累乘。每当有新的前复权因子产生，该股票的所有累积前复权因子均会刷新-描述"
                }
                ,
                {
                        "col_name": "endDate",
                        "col_show_name": "累积前复权因子起始生效日期，前复权价=对应交易日期在[endDate,exDivDate)区间的未复权价*累积前复权因子",
                        "col_comment": "累积前复权因子起始生效日期，前复权价=对应交易日期在[endDate,exDivDate)区间的未复权价*累积前复权因子-描述"
                }
                ,
                {
                    "col_name": "updateTime",
                    "col_show_name": "最近一次更新时间",
                    "col_comment": "最近一次更新时间-描述"
                }
            ]
        }
    define_json = json.dumps(mktadjf_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def sectyperel_define(table_name):

    sectyperel_str = {
        "table_name": "sectyperel",
        "table_show_name": "证券板块成分",
        "table_comment": "证券板块成分-描述",
        "table_category1": "1",
        "table_category2": "2",
        "table_category3": "3",
        "columns": [
            {
                    "col_name": "date",
                    "col_show_name": "新增索引",
                    "col_comment": "新增索引-描述"
            },
            {
                    "col_name": "typeID",
                    "col_show_name": "通联编制的分类编码",
                    "col_comment": "通联编制的分类编码-描述"
            },
            {
                    "col_name": "typeName",
                    "col_show_name": "板块分类名称",
                    "col_comment": "板块分类名称-描述"
            },
            {
                    "col_name": "secID",
                    "col_show_name": "通联编制的证券编码",
                    "col_comment": "通联编制的证券编码-描述"
            },
            {
                    "col_name": "ticker",
                    "col_show_name": "通用交易代码",
                    "col_comment": "通用交易代码-描述"
            },
            {
                    "col_name": "exchangeCD",
                    "col_show_name": "通联编制的交易市场编码",
                    "col_comment": "通联编制的交易市场编码-描述"
            },
            {
                    "col_name": "secShortName",
                    "col_show_name": "证券简称",
                    "col_comment": "证券简称-描述"
            }
        ]
    }
    define_json = json.dumps(sectyperel_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def equ_define(table_name):

    equ_str = {
            "table_name": "equ",
            "table_show_name": "股票基本信息",
            "table_comment": "股票基本信息-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {
                        "col_name": "date",
                        "col_show_name": "新增索引",
                        "col_comment": "新增索引-描述"
                }
                ,
                {
                    "col_name": "secID",
                    "col_show_name": "证券ID",
                    "col_comment": "证券ID-描述"
                }
                ,
                {
                    "col_name": "ticker",
                    "col_show_name": "交易代码",
                    "col_comment": "交易代码-描述"
                }
                ,
                {
                    "col_name": "exchangeCD",
                    "col_show_name": "交易市场。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所。对应getSysCode.codeTypeID=10002。",
                    "col_comment": "交易市场。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所。对应getSysCode.codeTypeID=10002。-描述"
                }
                ,
                {
                    "col_name": "ListSectorCD",
                    "col_show_name": "上市板块编码。例如，1-主板；2-创业板；4-科创板。",
                    "col_comment": "上市板块编码。例如，1-主板；2-创业板；4-科创板。-描述"
                }
                ,
                {
                    "col_name": "ListSector",
                    "col_show_name": "上市板块。",
                    "col_comment": "上市板块。-描述"
                }
                ,
                {
                    "col_name": "transCurrCD",
                    "col_show_name": "交易货币。例如，CNY-人民币元；USD-美元。对应getSysCode.codeTypeID=10004。",
                    "col_comment": "交易货币。例如，CNY-人民币元；USD-美元。对应getSysCode.codeTypeID=10004。-描述"
                }
                ,
                {
                    "col_name": "secShortName",
                    "col_show_name": "证券简称",
                    "col_comment": "证券简称-描述"
                }
                ,
                {
                    "col_name": "secFullName",
                    "col_show_name": "证券全称",
                    "col_comment": "证券全称-描述"
                }
                ,
                {
                    "col_name": "listStatusCD",
                    "col_show_name": "上市状态。L-上市；S-暂停；DE-终止上市；UN-未上市。对应getSysCode.codeTypeID=10005。",
                    "col_comment": "上市状态。L-上市；S-暂停；DE-终止上市；UN-未上市。对应getSysCode.codeTypeID=10005。-描述"
                }
                ,
                {
                    "col_name": "listDate",
                    "col_show_name": "上市日期",
                    "col_comment": "上市日期-描述"
                }
                ,
                {
                    "col_name": "delistDate",
                    "col_show_name": "摘牌日期",
                    "col_comment": "摘牌日期-描述"
                }
                ,
                {
                    "col_name": "equTypeCD",
                    "col_show_name": "股票分类编码。例如，A-A股；B-B股。",
                    "col_comment": "股票分类编码。例如，A-A股；B-B股。-描述"
                }
                ,
                {
                    "col_name": "equType",
                    "col_show_name": "股票类别",
                    "col_comment": "股票类别-描述"
                }
                ,
                {
                    "col_name": "exCountryCD",
                    "col_show_name": "交易市场所属地区。例如，CHN-中国大陆；HKG-香港。对应getSysCode.codeTypeID=10002。",
                    "col_comment": "交易市场所属地区。例如，CHN-中国大陆；HKG-香港。对应getSysCode.codeTypeID=10002。-描述"
                }
                ,
                {
                    "col_name": "partyID",
                    "col_show_name": "机构内部ID",
                    "col_comment": "机构内部ID-描述"
                }
                ,
                {
                    "col_name": "totalShares",
                    "col_show_name": "总股本(最新)",
                    "col_comment": "总股本(最新)-描述"
                }
                ,
                {
                    "col_name": "nonrestFloatShares",
                    "col_show_name": "公司无限售流通股份合计(最新)",
                    "col_comment": "公司无限售流通股份合计(最新)-描述"
                }
                ,
                {
                    "col_name": "nonrestfloatA",
                    "col_show_name": "无限售流通股本(最新)。如果为A股，该列为最新无限售流通A股股本数量；如果为B股，该列为最新流通B股股本数量",
                    "col_comment": "无限售流通股本(最新)。如果为A股，该列为最新无限售流通A股股本数量；如果为B股，该列为最新流通B股股本数量-描述"
                }
                ,
                {
                    "col_name": "officeAddr",
                    "col_show_name": "办公地址",
                    "col_comment": "办公地址-描述"
                }
                ,
                {
                    "col_name": "primeOperating",
                    "col_show_name": "主营业务范围",
                    "col_comment": "主营业务范围-描述"
                }
                ,
                {
                    "col_name": "endDate",
                    "col_show_name": "财务报告日期",
                    "col_comment": "财务报告日期-描述"
                }
                ,
                {
                    "col_name": "TShEquity",
                    "col_show_name": "所有者权益合计",
                    "col_comment": "所有者权益合计-描述"
                }
            ]
        }
    define_json = json.dumps(equ_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def fdmtbsbank2018_define(table_name):

    fdmtbsbank2018_str = {
            "table_name": "fdmtbsbank2018",
            "table_show_name": "(新)银行业资产负债表(PIT)",
            "table_comment": "(新)银行业资产负债表(PIT)-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {
                        "col_name": "secID",
                        "col_show_name": "通联编制的证券编码，格式是“交易代码.证券市场代码”，如000002.XSHE。可传入证券交易代码使用DataAPI.SecIDGet接口获取到。",
                        "col_comment": "通联编制的证券编码，格式是“交易代码.证券市场代码”，如000002.XSHE。可传入证券交易代码使用DataAPI.SecIDGet接口获取到。-描述"
                }
                ,
                {
                    "col_name": "secShortName",
                    "col_show_name": "证券简称",
                    "col_comment": "证券简称-描述"
                }
                ,
                {
                    "col_name": "ticker",
                    "col_show_name": "证券在证券市场通用的交易代码",
                    "col_comment": "证券在证券市场通用的交易代码-描述"
                }
                ,
                {
                    "col_name": "partyID",
                    "col_show_name": "机构内部ID",
                    "col_comment": "机构内部ID-描述"
                }
                ,
                {
                    "col_name": "exchangeCD",
                    "col_show_name": "交易市场代码：XSHG-上海证券交易所,XSHE-深圳证券交易所",
                    "col_comment": "交易市场代码：XSHG-上海证券交易所,XSHE-深圳证券交易所-描述"
                }
                ,
                {
                    "col_name": "actPubtime",
                    "col_show_name": "实际披露时间",
                    "col_comment": "实际披露时间-描述"
                }
                ,
                {
                    "col_name": "publishDate",
                    "col_show_name": "发布日期",
                    "col_comment": "发布日期-描述"
                }
                ,
                {
                    "col_name": "endDateRep",
                    "col_show_name": "报告截止日期",
                    "col_comment": "报告截止日期-描述"
                }
                ,
                {
                    "col_name": "endDate",
                    "col_show_name": "截止日期",
                    "col_comment": "截止日期-描述"
                }
                ,
                {
                    "col_name": "reportType",
                    "col_show_name": "报告类型：Q1-一季度,S1-半年度,Q3-第三季度或前三季度,A-年度",
                    "col_comment": "报告类型：Q1-一季度,S1-半年度,Q3-第三季度或前三季度,A-年度-描述"
                }
                ,
                {
                    "col_name": "fiscalPeriod",
                    "col_show_name": "会计区间",
                    "col_comment": "会计区间-描述"
                }
                ,
                {
                    "col_name": "mergedFlag",
                    "col_show_name": "合并标志：1-合并；2-母公司",
                    "col_comment": "合并标志：1-合并；2-母公司-描述"
                }
                ,
                {
                    "col_name": "accoutingStandards",
                    "col_show_name": "会计准则：CHAS_2018-中国会计准则_2018",
                    "col_comment": "会计准则：CHAS_2018-中国会计准则_2018-描述"
                }
                ,
                {
                    "col_name": "currencyCD",
                    "col_show_name": "货币代码：CNY-人民币",
                    "col_comment": "货币代码：CNY-人民币-描述"
                }
                ,
                {
                    "col_name": "industryCategory",
                    "col_show_name": "按照财务报表内容分类：银行业",
                    "col_comment": "按照财务报表内容分类：银行业-描述"
                }
                ,
                {
                    "col_name": "cReserCb",
                    "col_show_name": "现金及存放中央银行款项",
                    "col_comment": "现金及存放中央银行款项-描述"
                }
                ,
                {
                    "col_name": "deposInOthBfi",
                    "col_show_name": "存放同业款项",
                    "col_comment": "存放同业款项-描述"
                }
                ,
                {
                    "col_name": "preciMetals",
                    "col_show_name": "贵金属",
                    "col_comment": "贵金属-描述"
                }
                ,
                {
                    "col_name": "loanToOthBankFi",
                    "col_show_name": "拆出资金",
                    "col_comment": "拆出资金-描述"
                }
                ,
                {
                    "col_name": "tradingFa",
                    "col_show_name": "交易性金融资产",
                    "col_comment": "交易性金融资产-描述"
                }
                ,
                {
                    "col_name": "tradingOthCompreIncomevFa",
                    "col_show_name": "以公允价值计量且其变动计入其他综合收益的金融资产",
                    "col_comment": "以公允价值计量且其变动计入其他综合收益的金融资产-描述"
                }
                ,
                {
                    "col_name": "tradingAmortizeFa",
                    "col_show_name": "以摊余成本计量的金融资产",
                    "col_comment": "以摊余成本计量的金融资产-描述"
                }
                ,
                {
                    "col_name": "debtInvest",
                    "col_show_name": "债权投资",
                    "col_comment": "债权投资-描述"
                }
                ,
                {
                    "col_name": "othDebtInvest",
                    "col_show_name": "其他债权投资",
                    "col_comment": "其他债权投资-描述"
                }
                ,
                {
                    "col_name": "othEquityInstrInvest",
                    "col_show_name": "其他权益工具投资",
                    "col_comment": "其他权益工具投资-描述"
                }
                ,
                {
                    "col_name": "derivAssets",
                    "col_show_name": "衍生金融资产",
                    "col_comment": "衍生金融资产-描述"
                }
                ,
                {
                    "col_name": "purResaleFa",
                    "col_show_name": "买入返售金融资产",
                    "col_comment": "买入返售金融资产-描述"
                }
                ,
                {
                    "col_name": "intReceiv",
                    "col_show_name": "应收利息",
                    "col_comment": "应收利息-描述"
                }
                ,
                {
                    "col_name": "disburLa",
                    "col_show_name": "发放委托贷款及垫款",
                    "col_comment": "发放委托贷款及垫款-描述"
                }
                ,
                {
                    "col_name": "finanLeaseReceiv",
                    "col_show_name": "应收融资租赁款",
                    "col_comment": "应收融资租赁款-描述"
                }
                ,
                {
                    "col_name": "availForSaleFa",
                    "col_show_name": "可供出售金融资产",
                    "col_comment": "可供出售金融资产-描述"
                }
                ,
                {
                    "col_name": "htmInvest",
                    "col_show_name": "持有至到期投资",
                    "col_comment": "持有至到期投资-描述"
                }
                ,
                {
                    "col_name": "investAsReceiv",
                    "col_show_name": "应收款项类投资",
                    "col_comment": "应收款项类投资-描述"
                }
                ,
                {
                    "col_name": "ltEquityInvest",
                    "col_show_name": "长期股权投资",
                    "col_comment": "长期股权投资-描述"
                }
                ,
                {
                    "col_name": "investRealEstate",
                    "col_show_name": "投资性房地产",
                    "col_comment": "投资性房地产-描述"
                }
                ,
                {
                    "col_name": "fixedAssets",
                    "col_show_name": "固定资产",
                    "col_comment": "固定资产-描述"
                }
                ,
                {
                    "col_name": "cip",
                    "col_show_name": "在建工程",
                    "col_comment": "在建工程-描述"
                }
                ,
                {
                    "col_name": "intanAssets",
                    "col_show_name": "无形资产",
                    "col_comment": "无形资产-描述"
                }
                ,
                {
                    "col_name": "goodwill",
                    "col_show_name": "商誉",
                    "col_comment": "商誉-描述"
                }
                ,
                {
                    "col_name": "deferTaxAssets",
                    "col_show_name": "递延所得税资产",
                    "col_comment": "递延所得税资产-描述"
                }
                ,
                {
                    "col_name": "othAssets",
                    "col_show_name": "其他资产",
                    "col_comment": "其他资产-描述"
                }
                ,
                {
                    "col_name": "ae",
                    "col_show_name": "资产的调整项目",
                    "col_comment": "资产的调整项目-描述"
                }
                ,
                {
                    "col_name": "aa",
                    "col_show_name": "资产的差错金额",
                    "col_comment": "资产的差错金额-描述"
                }
                ,
                {
                    "col_name": "tAssets",
                    "col_show_name": "资产总计",
                    "col_comment": "资产总计-描述"
                }
                ,
                {
                    "col_name": "cbBorr",
                    "col_show_name": "向中央银行借款",
                    "col_comment": "向中央银行借款-描述"
                }
                ,
                {
                    "col_name": "deposFrOthBfi",
                    "col_show_name": "同业及其他金融机构存放款项",
                    "col_comment": "同业及其他金融机构存放款项-描述"
                }
                ,
                {
                    "col_name": "loanFrOthBankFi",
                    "col_show_name": "拆入资金",
                    "col_comment": "-描述"
                }
                ,
                {
                    "col_name": "tradingFl",
                    "col_show_name": "交易性金融负债",
                    "col_comment": "交易性金融负债-描述"
                }
                ,
                {
                    "col_name": "derivLiab",
                    "col_show_name": "衍生金融负债",
                    "col_comment": "衍生金融负债-描述"
                }
                ,
                {
                    "col_name": "soldForRepurFa",
                    "col_show_name": "卖出回购金融资产款",
                    "col_comment": "卖出回购金融资产款-描述"
                }
                ,
                {
                    "col_name": "depos",
                    "col_show_name": "吸收存款",
                    "col_comment": "吸收存款-描述"
                }
                ,
                {
                    "col_name": "payrollPayable",
                    "col_show_name": "应付职工薪酬",
                    "col_comment": "应付职工薪酬-描述"
                }
                ,
                {
                    "col_name": "taxesPayable",
                    "col_show_name": "应交税费",
                    "col_comment": "应交税费-描述"
                }
                ,
                {
                    "col_name": "intPayable",
                    "col_show_name": "应付利息",
                    "col_comment": "应付利息-描述"
                }
                ,
                {
                    "col_name": "estimatedLiab",
                    "col_show_name": "预计负债",
                    "col_comment": "预计负债-描述"
                }
                ,
                {
                    "col_name": "bondPayable",
                    "col_show_name": "应付债券",
                    "col_comment": "应付债券-描述"
                }
                ,
                {
                    "col_name": "preferredStockL",
                    "col_show_name": "其中:优先股",
                    "col_comment": "其中:优先股-描述"
                }
                ,
                {
                    "col_name": "perpetualBondL",
                    "col_show_name": "永续债",
                    "col_comment": "永续债-描述"
                }
                ,
                {
                    "col_name": "deferTaxLiab",
                    "col_show_name": "递延所得税负债",
                    "col_comment": "递延所得税负债-描述"
                }
                ,
                {
                    "col_name": "othLiab",
                    "col_show_name": "其他负债",
                    "col_comment": "其他负债-描述"
                }
                ,
                {
                    "col_name": "le",
                    "col_show_name": "负债的调整项目",
                    "col_comment": "负债的调整项目-描述"
                }
                ,
                {
                    "col_name": "la",
                    "col_show_name": "负债的差错金额",
                    "col_comment": "负债的差错金额-描述"
                }
                ,
                {
                    "col_name": "tLiab",
                    "col_show_name": "负债合计",
                    "col_comment": "负债合计-描述"
                }
                ,
                {
                    "col_name": "paidInCapital",
                    "col_show_name": "实收资本(或股本)",
                    "col_comment": "实收资本(或股本)-描述"
                }
                ,
                {
                    "col_name": "othEquityInstr",
                    "col_show_name": "其他权益工具",
                    "col_comment": "其他权益工具-描述"
                }
                ,
                {
                    "col_name": "preferredStockE",
                    "col_show_name": "其中:优先股",
                    "col_comment": "其中:优先股-描述"
                }
                ,
                {
                    "col_name": "perpetualBondE",
                    "col_show_name": "永续债",
                    "col_comment": "永续债-描述"
                }
                ,
                {
                    "col_name": "capitalReser",
                    "col_show_name": "资本公积",
                    "col_comment": "资本公积-描述"
                }
                ,
                {
                    "col_name": "treasuryShare",
                    "col_show_name": "减:库存股",
                    "col_comment": "减:库存股-描述"
                }
                ,
                {
                    "col_name": "othCompreIncome",
                    "col_show_name": "其他综合收益",
                    "col_comment": "其他综合收益-描述"
                }
                ,
                {
                    "col_name": "surplusReser",
                    "col_show_name": "盈余公积",
                    "col_comment": "盈余公积-描述"
                }
                ,
                {
                    "col_name": "ordinRiskReser",
                    "col_show_name": "一般风险准备",
                    "col_comment": "一般风险准备-描述"
                }
                ,
                {
                    "col_name": "retainedEarnings",
                    "col_show_name": "未分配利润",
                    "col_comment": "未分配利润-描述"
                }
                ,
                {
                    "col_name": "forexDiffer",
                    "col_show_name": "外币报表折算差额",
                    "col_comment": "外币报表折算差额-描述"
                }
                ,
                {
                    "col_name": "see",
                    "col_show_name": "归属于母公司所有者权益的调整项目",
                    "col_comment": "归属于母公司所有者权益的调整项目-描述"
                }
                ,
                {
                    "col_name": "sea",
                    "col_show_name": "归属于母公司所有者权益的差错金额",
                    "col_comment": "归属于母公司所有者权益的差错金额-描述"
                }
                ,
                {
                    "col_name": "tEquityAttrP",
                    "col_show_name": "归属于母公司所有者权益合计",
                    "col_comment": "归属于母公司所有者权益合计-描述"
                }
                ,
                {
                    "col_name": "minorityInt",
                    "col_show_name": "少数股东权益",
                    "col_comment": "少数股东权益-描述"
                }
                ,
                {
                    "col_name": "othEffectSe",
                    "col_show_name": "所有者权益的调整项目",
                    "col_comment": "所有者权益的调整项目-描述"
                }
                ,
                {
                    "col_name": "othEffectSa",
                    "col_show_name": "所有者权益的差错金额",
                    "col_comment": "所有者权益的差错金额-描述"
                }
                ,
                {
                    "col_name": "tShEquity",
                    "col_show_name": "所有者权益(或股东权益)合计",
                    "col_comment": "所有者权益(或股东权益)合计-描述"
                }
                ,
                {
                    "col_name": "lee",
                    "col_show_name": "负债和权益的调整项目",
                    "col_comment": "负债和权益的调整项目-描述"
                }
                ,
                {
                    "col_name": "lea",
                    "col_show_name": "负债和权益的差错金额",
                    "col_comment": "负债和权益的差错金额-描述"
                }
                ,
                {
                    "col_name": "tLiabEquity",
                    "col_show_name": "负债和所有者权益(或股东权益)总计",
                    "col_comment": "负债和所有者权益(或股东权益)总计-描述"
                }
                ,
                {
                    "col_name": "updateTime",
                    "col_show_name": "更新时间",
                    "col_comment": "更新时间-描述"
                }
            ]
        }
    define_json = json.dumps(fdmtbsbank2018_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def fdmtbsindu2018_define(table_name):

    fdmtbsindu2018_str = {
            "table_name": "fdmtbsindu2018",
            "table_show_name": "(新)一般工商业资产负债表(PIT)",
            "table_comment": "(新)一般工商业资产负债表(PIT)-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID",
                 "col_show_name": "通联编制的证券编码，格式是“交易代码.证券市场代码”，如000002.XSHE。可传入证券交易代码使用DataAPI.SecIDGet接口获取到。",
                 "col_comment": "通联编制的证券编码，格式是“交易代码.证券市场代码”，如000002.XSHE。可传入证券交易代码使用DataAPI.SecIDGet接口获取到。-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "ticker", "col_show_name": "证券在证券市场通用的交易代码。", "col_comment": "证券在证券市场通用的交易代码。-描述"},
                {"col_name": "partyID", "col_show_name": "机构内部ID", "col_comment": "机构内部ID-描述"},
                {"col_name": "exchangeCD", "col_show_name": "交易市场代码：XSHG-上海证券交易所,XSHE-深圳证券交易所",
                 "col_comment": "交易市场代码：XSHG-上海证券交易所,XSHE-深圳证券交易所-描述"},
                {"col_name": "actPubtime", "col_show_name": "实际披露时间", "col_comment": "实际披露时间-描述"},
                {"col_name": "publishDate", "col_show_name": "发布日期", "col_comment": "发布日期-描述"},
                {"col_name": "endDateRep", "col_show_name": "报告截止日期", "col_comment": "报告截止日期-描述"},
                {"col_name": "endDate", "col_show_name": "截止日期", "col_comment": "截止日期-描述"},
                {"col_name": "reportType", "col_show_name": "报告类型：Q1-一季度,S1-半年度,Q3-第三季度或前三季度,A-年度",
                 "col_comment": "报告类型：Q1-一季度,S1-半年度,Q3-第三季度或前三季度,A-年度-描述"},
                {"col_name": "fiscalPeriod", "col_show_name": "会计区间", "col_comment": "会计区间-描述"},
                {"col_name": "mergedFlag", "col_show_name": "合并标志：1-合并；2-母公司", "col_comment": "合并标志：1-合并；2-母公司-描述"},
                {"col_name": "accoutingStandards", "col_show_name": "会计准则：CHAS_2018-中国会计准则_2018",
                 "col_comment": "会计准则：CHAS_2018-中国会计准则_2018-描述"},
                {"col_name": "currencyCD", "col_show_name": "货币代码：CNY-人民币", "col_comment": "货币代码：CNY-人民币-描述"},
                {"col_name": "industryCategory", "col_show_name": "按照财务报表内容分类：一般工商业",
                 "col_comment": "按照财务报表内容分类：一般工商业-描述"},
                {"col_name": "cashCEquiv", "col_show_name": "货币资金", "col_comment": "货币资金-描述"},
                {"col_name": "settProv", "col_show_name": "结算备付金", "col_comment": "结算备付金-描述"},
                {"col_name": "loanToOthBankFi", "col_show_name": "拆出资金", "col_comment": "拆出资金-描述"},
                {"col_name": "tradingFa", "col_show_name": "交易性金融资产", "col_comment": "交易性金融资产-描述"},
                {"col_name": "derivAssets", "col_show_name": "衍生金融资产", "col_comment": "衍生金融资产-描述"},
                {"col_name": "nrAr", "col_show_name": "应收票据及应收账款", "col_comment": "应收票据及应收账款-描述"},
                {"col_name": "notesReceiv", "col_show_name": "应收票据及应收账款：应收票据", "col_comment": "应收票据及应收账款：应收票据-描述"},
                {"col_name": "ar", "col_show_name": "应收票据及应收账款：应收账款", "col_comment": "应收票据及应收账款：应收账款-描述"},
                {"col_name": "finanReceiv", "col_show_name": "应收票据及应收账款：应收款项融资", "col_comment": "应收票据及应收账款：应收款项融资-描述"},
                {"col_name": "prepayment", "col_show_name": "预付款项", "col_comment": "预付款项-描述"},
                {"col_name": "premiumReceiv", "col_show_name": "应收保费", "col_comment": "应收保费-描述"},
                {"col_name": "reinsurReceiv", "col_show_name": "应收分保账款", "col_comment": "应收分保账款-描述"},
                {"col_name": "reinsurReserReceiv", "col_show_name": "应收分保合同准备金", "col_comment": "应收分保合同准备金-描述"},
                {"col_name": "othReceivTotal", "col_show_name": "其他应收款(合计)", "col_comment": "其他应收款(合计)-描述"},
                {"col_name": "intReceiv", "col_show_name": "其他应收款(合计)：应收利息", "col_comment": "其他应收款(合计)：应收利息-描述"},
                {"col_name": "divReceiv", "col_show_name": "其他应收款(合计)：应收股利", "col_comment": "其他应收款(合计)：应收股利-描述"},
                {"col_name": "othReceiv", "col_show_name": "其他应收款(合计)：其他应收款", "col_comment": "其他应收款(合计)：其他应收款-描述"},
                {"col_name": "purResaleFa", "col_show_name": "买入返售金融资产", "col_comment": "买入返售金融资产-描述"},
                {"col_name": "inventories", "col_show_name": "存货", "col_comment": "存货-描述"},
                {"col_name": "contAssets", "col_show_name": "合同资产", "col_comment": "合同资产-描述"},
                {"col_name": "assetsHeldForSale", "col_show_name": "持有待售资产", "col_comment": "持有待售资产-描述"},
                {"col_name": "ncaWithin1y", "col_show_name": "一年内到期的非流动资产", "col_comment": "一年内到期的非流动资产-描述"},
                {"col_name": "othCa", "col_show_name": "其他流动资产", "col_comment": "其他流动资产-描述"},
                {"col_name": "cae", "col_show_name": "流动资产的调整项目", "col_comment": "流动资产的调整项目-描述"},
                {"col_name": "caa", "col_show_name": "流动资产的差错金额", "col_comment": "流动资产的差错金额-描述"},
                {"col_name": "tCa", "col_show_name": "流动资产合计", "col_comment": "流动资产合计-描述"},
                {"col_name": "disburLa", "col_show_name": "发放委托贷款及垫款", "col_comment": "发放委托贷款及垫款-描述"},
                {"col_name": "tradingOthCompreIncomevFa", "col_show_name": "以公允价值计量且其变动计入其他综合收益的金融资产",
                 "col_comment": "以公允价值计量且其变动计入其他综合收益的金融资产-描述"},
                {"col_name": "tradingAmortizeFa", "col_show_name": "以摊余成本计量的金融资产", "col_comment": "以摊余成本计量的金融资产-描述"},
                {"col_name": "availForSaleFa", "col_show_name": "可供出售金融资产", "col_comment": "可供出售金融资产-描述"},
                {"col_name": "htmInvest", "col_show_name": "持有至到期投资", "col_comment": "持有至到期投资-描述"},
                {"col_name": "debtInvest", "col_show_name": "债权投资", "col_comment": "债权投资-描述"},
                {"col_name": "othDebtInvest", "col_show_name": "其他债权投资", "col_comment": "其他债权投资-描述"},
                {"col_name": "ltReceiv", "col_show_name": "长期应收款", "col_comment": "长期应收款-描述"},
                {"col_name": "ltEquityInvest", "col_show_name": "长期股权投资", "col_comment": "长期股权投资-描述"},
                {"col_name": "othEquityInstrInvest", "col_show_name": "其他权益工具投资", "col_comment": "其他权益工具投资-描述"},
                {"col_name": "assetsNc", "col_show_name": "其他非流动金融资产", "col_comment": "其他非流动金融资产-描述"},
                {"col_name": "investRealEstate", "col_show_name": "投资性房地产", "col_comment": "投资性房地产-描述"},
                {"col_name": "fixedAssetsTotal", "col_show_name": "固定资产(合计)", "col_comment": "固定资产(合计)-描述"},
                {"col_name": "fixedAssets", "col_show_name": "固定资产(合计)：固定资产", "col_comment": "固定资产(合计)：固定资产-描述"},
                {"col_name": "fixedAssetsDisp", "col_show_name": "固定资产(合计)：固定资产清理",
                 "col_comment": "固定资产(合计)：固定资产清理-描述"},
                {"col_name": "cipTotal", "col_show_name": "在建工程(合计)", "col_comment": "在建工程(合计)-描述"},
                {"col_name": "cip", "col_show_name": "在建工程(合计)：在建工程", "col_comment": "在建工程(合计)：在建工程-描述"},
                {"col_name": "constMaterials", "col_show_name": "在建工程(合计)：工程物资", "col_comment": "在建工程(合计)：工程物资-描述"},
                {"col_name": "producBiolAssets", "col_show_name": "生产性生物资产", "col_comment": "生产性生物资产-描述"},
                {"col_name": "commonwealBiolAssets", "col_show_name": "公益性生物资产", "col_comment": "公益性生物资产-描述"},
                {"col_name": "oilAndGasAssets", "col_show_name": "油气资产", "col_comment": "油气资产-描述"},
                {"col_name": "usageAssets", "col_show_name": "使用权资产", "col_comment": "使用权资产-描述"},
                {"col_name": "intanAssets", "col_show_name": "无形资产", "col_comment": "无形资产-描述"},
                {"col_name": "rD", "col_show_name": "研发支出", "col_comment": "研发支出-描述"},
                {"col_name": "goodwill", "col_show_name": "商誉", "col_comment": "商誉-描述"},
                {"col_name": "ltAmorExp", "col_show_name": "长期待摊费用", "col_comment": "长期待摊费用-描述"},
                {"col_name": "deferTaxAssets", "col_show_name": "递延所得税资产", "col_comment": "递延所得税资产-描述"},
                {"col_name": "othNca", "col_show_name": "其他非流动资产", "col_comment": "其他非流动资产-描述"},
                {"col_name": "ncae", "col_show_name": "非流动资产的调整项目", "col_comment": "非流动资产的调整项目-描述"},
                {"col_name": "ncaa", "col_show_name": "非流动资产的差错金额", "col_comment": "非流动资产的差错金额-描述"},
                {"col_name": "tNca", "col_show_name": "非流动资产合计", "col_comment": "非流动资产合计-描述"},
                {"col_name": "ae", "col_show_name": "资产的调整项目", "col_comment": "资产的调整项目-描述"},
                {"col_name": "aa", "col_show_name": "资产的差错金额", "col_comment": "资产的差错金额-描述"},
                {"col_name": "tAssets", "col_show_name": "资产总计", "col_comment": "资产总计-描述"},
                {"col_name": "stBorr", "col_show_name": "短期借款", "col_comment": "短期借款-描述"},
                {"col_name": "cbBorr", "col_show_name": "向中央银行借款", "col_comment": "向中央银行借款-描述"},
                {"col_name": "depos", "col_show_name": "吸收存款", "col_comment": "吸收存款-描述"},
                {"col_name": "loanFrOthBankFi", "col_show_name": "拆入资金", "col_comment": "拆入资金-描述"},
                {"col_name": "tradingFl", "col_show_name": "交易性金融负债", "col_comment": "交易性金融负债-描述"},
                {"col_name": "derivLiab", "col_show_name": "衍生金融负债", "col_comment": "衍生金融负债-描述"},
                {"col_name": "npAp", "col_show_name": "应付票据及应付账款", "col_comment": "应付票据及应付账款-描述"},
                {"col_name": "notesPayable", "col_show_name": "应付票据及应付账款：应付票据", "col_comment": "应付票据及应付账款：应付票据-描述"},
                {"col_name": "ap", "col_show_name": "应付票据及应付账款：应付账款", "col_comment": "应付票据及应付账款：应付账款-描述"},
                {"col_name": "advanceReceipts", "col_show_name": "预收款项", "col_comment": "预收款项-描述"},
                {"col_name": "soldForRepurFa", "col_show_name": "卖出回购金融资产款", "col_comment": "卖出回购金融资产款-描述"},
                {"col_name": "commisPayable", "col_show_name": "应付手续费及佣金", "col_comment": "应付手续费及佣金-描述"},
                {"col_name": "contLiab", "col_show_name": "合同负债", "col_comment": "合同负债-描述"},
                {"col_name": "payrollPayable", "col_show_name": "应付职工薪酬", "col_comment": "应付职工薪酬-描述"},
                {"col_name": "taxesPayable", "col_show_name": "应交税费", "col_comment": "应交税费-描述"},
                {"col_name": "othPayableTotal", "col_show_name": "其他应付款(合计)", "col_comment": "其他应付款(合计)-描述"},
                {"col_name": "intPayable", "col_show_name": "其他应付款(合计)：应付利息", "col_comment": "其他应付款(合计)：应付利息-描述"},
                {"col_name": "divPayable", "col_show_name": "其他应付款(合计)：应付股利", "col_comment": "其他应付款(合计)：应付股利-描述"},
                {"col_name": "othPayable", "col_show_name": "其他应付款(合计)：其他应付款", "col_comment": "其他应付款(合计)：其他应付款-描述"},
                {"col_name": "reinsurPayable", "col_show_name": "应付分保账款", "col_comment": "应付分保账款-描述"},
                {"col_name": "fundsSecTradAgen", "col_show_name": "代理买卖证券款", "col_comment": "代理买卖证券款-描述"},
                {"col_name": "fundsSecUndwAgen", "col_show_name": "代理承销证券款", "col_comment": "代理承销证券款-描述"},
                {"col_name": "liabHeldForSale", "col_show_name": "持有待售负债", "col_comment": "持有待售负债-描述"},
                {"col_name": "nclWithin1y", "col_show_name": "一年内到期的非流动负债", "col_comment": "一年内到期的非流动负债-描述"},
                {"col_name": "accruedExp", "col_show_name": "预提费用", "col_comment": "预提费用-描述"},
                {"col_name": "othCl", "col_show_name": "其他流动负债", "col_comment": "其他流动负债-描述"},
                {"col_name": "cle", "col_show_name": "流动负债的调整项目", "col_comment": "流动负债的调整项目-描述"},
                {"col_name": "cla", "col_show_name": "流动负债的差错金额", "col_comment": "流动负债的差错金额-描述"},
                {"col_name": "tCl", "col_show_name": "流动负债合计", "col_comment": "流动负债合计-描述"},
                {"col_name": "insurReser", "col_show_name": "保险合同准备金", "col_comment": "保险合同准备金-描述"},
                {"col_name": "ltBorr", "col_show_name": "长期借款", "col_comment": "长期借款-描述"},
                {"col_name": "bondPayable", "col_show_name": "应付债券", "col_comment": "应付债券-描述"},
                {"col_name": "preferredStockL", "col_show_name": "应付债券：优先股", "col_comment": "应付债券：优先股-描述"},
                {"col_name": "perpetualBondL", "col_show_name": "应付债券：永续债", "col_comment": "应付债券：永续债-描述"},
                {"col_name": "leaseLiab", "col_show_name": "租赁负债", "col_comment": "租赁负债-描述"},
                {"col_name": "ltPayableTotal", "col_show_name": "长期应付款(合计)", "col_comment": "长期应付款(合计)-描述"},
                {"col_name": "ltPayable", "col_show_name": "长期应付款(合计)：长期应付款", "col_comment": "长期应付款(合计)：长期应付款-描述"},
                {"col_name": "specificPayables", "col_show_name": "长期应付款(合计)：专项应付款",
                 "col_comment": "长期应付款(合计)：专项应付款-描述"},
                {"col_name": "ltPayrollPayable", "col_show_name": "长期应付职工薪酬", "col_comment": "长期应付职工薪酬-描述"},
                {"col_name": "estimatedLiab", "col_show_name": "预计负债", "col_comment": "预计负债-描述"},
                {"col_name": "deferRevenue", "col_show_name": "递延收益", "col_comment": "递延收益-描述"},
                {"col_name": "deferTaxLiab", "col_show_name": "递延所得税负债", "col_comment": "递延所得税负债-描述"},
                {"col_name": "othNcl", "col_show_name": "其他非流动负债", "col_comment": "其他非流动负债-描述"},
                {"col_name": "ncle", "col_show_name": "非流动负债的调整项目", "col_comment": "非流动负债的调整项目-描述"},
                {"col_name": "ncla", "col_show_name": "非流动负债的差错金额", "col_comment": "非流动负债的差错金额-描述"},
                {"col_name": "tNcl", "col_show_name": "非流动负债合计", "col_comment": "非流动负债合计-描述"},
                {"col_name": "le", "col_show_name": "负债的调整项目", "col_comment": "负债的调整项目-描述"},
                {"col_name": "la", "col_show_name": "负债的差错金额", "col_comment": "负债的差错金额-描述"},
                {"col_name": "tLiab", "col_show_name": "负债合计", "col_comment": "负债合计-描述"},
                {"col_name": "paidInCapital", "col_show_name": "实收资本(或股本)", "col_comment": "实收资本(或股本)-描述"},
                {"col_name": "othEquityInstr", "col_show_name": "其他权益工具", "col_comment": "其他权益工具-描述"},
                {"col_name": "preferredStockE", "col_show_name": "其他权益工具：优先股", "col_comment": "其他权益工具：优先股-描述"},
                {"col_name": "perpetualBondE", "col_show_name": "其他权益工具：永续债", "col_comment": "其他权益工具：永续债-描述"},
                {"col_name": "updateTime", "col_show_name": "更新时间", "col_comment": "更新时间-描述"},
                {"col_name": "capitalReser", "col_show_name": "资本公积", "col_comment": "资本公积-描述"},
                {"col_name": "treasuryShare", "col_show_name": "减:库存股", "col_comment": "减:库存股-描述"},
                {"col_name": "othCompreIncome", "col_show_name": "其他综合收益", "col_comment": "其他综合收益-描述"},
                {"col_name": "specialReser", "col_show_name": "专项储备", "col_comment": "专项储备-描述"},
                {"col_name": "surplusReser", "col_show_name": "盈余公积", "col_comment": "盈余公积-描述"},
                {"col_name": "ordinRiskReser", "col_show_name": "一般风险准备", "col_comment": "一般风险准备-描述"},
                {"col_name": "transacRiskReser", "col_show_name": "交易风险准备", "col_comment": "交易风险准备-描述"},
                {"col_name": "retainedEarnings", "col_show_name": "未分配利润", "col_comment": "未分配利润-描述"},
                {"col_name": "forexDiffer", "col_show_name": "外币报表折算差额", "col_comment": "外币报表折算差额-描述"},
                {"col_name": "see", "col_show_name": "归属于母公司所有者权益的调整项目", "col_comment": "归属于母公司所有者权益的调整项目-描述"},
                {"col_name": "sea", "col_show_name": "归属于母公司所有者权益的差错金额", "col_comment": "归属于母公司所有者权益的差错金额-描述"},
                {"col_name": "tEquityAttrP", "col_show_name": "归属于母公司所有者权益合计", "col_comment": "归属于母公司所有者权益合计-描述"},
                {"col_name": "minorityInt", "col_show_name": "少数股东权益", "col_comment": "少数股东权益-描述"},
                {"col_name": "othEffectSe", "col_show_name": "所有者权益的调整项目", "col_comment": "所有者权益的调整项目-描述"},
                {"col_name": "othEffectSa", "col_show_name": "所有者权益的差错金额", "col_comment": "所有者权益的差错金额-描述"},
                {"col_name": "tShEquity", "col_show_name": "所有者权益(或股东权益)合计", "col_comment": "所有者权益(或股东权益)合计-描述"},
                {"col_name": "lee", "col_show_name": "负债和权益的调整项目", "col_comment": "负债和权益的调整项目-描述"},
                {"col_name": "lea", "col_show_name": "负债和权益的差错金额", "col_comment": "负债和权益的差错金额-描述"},
                {"col_name": "tLiabEquity", "col_show_name": "负债和所有者权益(或股东权益)总计",
                 "col_comment": "负债和所有者权益(或股东权益)总计-描述"}
        ]
    }
    define_json = json.dumps(fdmtbsindu2018_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def fdmtbssecu2018_define(table_name):

    fdmtbssecu2018_str = {
            "table_name": "fdmtbssecu2018",
            "table_show_name": "(新)证券业资产负债表(PIT)",
            "table_comment": "(新)证券业资产负债表(PIT)-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID",
                 "col_show_name": "通联编制的证券编码，格式是“交易代码.证券市场代码”，如000002.XSHE。可传入证券交易代码使用DataAPI.SecIDGet接口获取到。",
                 "col_comment": "通联编制的证券编码，格式是“交易代码.证券市场代码”，如000002.XSHE。可传入证券交易代码使用DataAPI.SecIDGet接口获取到。-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "ticker", "col_show_name": "证券在证券市场通用的交易代码。", "col_comment": "证券在证券市场通用的交易代码。-描述"},
                {"col_name": "partyID", "col_show_name": "机构内部ID", "col_comment": "机构内部ID-描述"},
                {"col_name": "exchangeCD", "col_show_name": "交易市场代码：XSHG-上海证券交易所,XSHE-深圳证券交易所",
                 "col_comment": "交易市场代码：XSHG-上海证券交易所,XSHE-深圳证券交易所-描述"},
                {"col_name": "actPubtime", "col_show_name": "实际披露时间", "col_comment": "实际披露时间-描述"},
                {"col_name": "publishDate", "col_show_name": "发布日期", "col_comment": "发布日期-描述"},
                {"col_name": "endDateRep", "col_show_name": "报告截止日期", "col_comment": "报告截止日期-描述"},
                {"col_name": "endDate", "col_show_name": "截止日期", "col_comment": "截止日期-描述"},
                {"col_name": "reportType", "col_show_name": "报告类型：Q1-一季度,S1-半年度,Q3-第三季度或前三季度,A-年度",
                 "col_comment": "报告类型：Q1-一季度,S1-半年度,Q3-第三季度或前三季度,A-年度-描述"},
                {"col_name": "fiscalPeriod", "col_show_name": "会计区间", "col_comment": "会计区间-描述"},
                {"col_name": "mergedFlag", "col_show_name": "合并标志：1-合并；2-母公司", "col_comment": "合并标志：1-合并；2-母公司-描述"},
                {"col_name": "accoutingStandards", "col_show_name": "会计准则：CHAS_2018-中国会计准则_2018",
                 "col_comment": "会计准则：CHAS_2018-中国会计准则_2018-描述"},
                {"col_name": "currencyCD", "col_show_name": "货币代码：CNY-人民币", "col_comment": "货币代码：CNY-人民币-描述"},
                {"col_name": "industryCategory", "col_show_name": "按照财务报表内容分类：证券业", "col_comment": "按照财务报表内容分类：证券业-描述"},
                {"col_name": "cashCEquiv", "col_show_name": "货币资金", "col_comment": "货币资金-描述"},
                {"col_name": "clientDepos", "col_show_name": "其中:客户资金存款", "col_comment": "其中:客户资金存款-描述"},
                {"col_name": "settProv", "col_show_name": "结算备付金", "col_comment": "结算备付金-描述"},
                {"col_name": "clientProv", "col_show_name": "其中:客户备付金", "col_comment": "其中:客户备付金-描述"},
                {"col_name": "loanToOthBankFi", "col_show_name": "拆出资金", "col_comment": "拆出资金-描述"},
                {"col_name": "tradingFa", "col_show_name": "交易性金融资产", "col_comment": "交易性金融资产-描述"},
                {"col_name": "derivAssets", "col_show_name": "衍生金融资产", "col_comment": "衍生金融资产-描述"},
                {"col_name": "purResaleFa", "col_show_name": "买入返售金融资产", "col_comment": "买入返售金融资产-描述"},
                {"col_name": "tradingOthCompreIncomevFa", "col_show_name": "以公允价值计量且其变动计入其他综合收益的金融资产",
                 "col_comment": "以公允价值计量且其变动计入其他综合收益的金融资产-描述"},
                {"col_name": "tradingAmortizeFa", "col_show_name": "以摊余成本计量的金融资产", "col_comment": "以摊余成本计量的金融资产-描述"},
                {"col_name": "debtInvest", "col_show_name": "债权投资", "col_comment": "债权投资-描述"},
                {"col_name": "othDebtInvest", "col_show_name": "其他债权投资", "col_comment": "其他债权投资-描述"},
                {"col_name": "othEquityInstrInvest", "col_show_name": "其他权益工具投资", "col_comment": "其他权益工具投资-描述"},
                {"col_name": "intReceiv", "col_show_name": "应收利息", "col_comment": "应收利息-描述"},
                {"col_name": "refundDepos", "col_show_name": "存出保证金", "col_comment": "存出保证金-描述"},
                {"col_name": "availForSaleFa", "col_show_name": "可供出售金融资产", "col_comment": "可供出售金融资产-描述"},
                {"col_name": "htmInvest", "col_show_name": "持有至到期投资", "col_comment": "持有至到期投资-描述"},
                {"col_name": "ltEquityInvest", "col_show_name": "长期股权投资", "col_comment": "长期股权投资-描述"},
                {"col_name": "investRealEstate", "col_show_name": "投资性房地产", "col_comment": "投资性房地产-描述"},
                {"col_name": "fixedAssets", "col_show_name": "固定资产", "col_comment": "固定资产-描述"},
                {"col_name": "intanAssets", "col_show_name": "无形资产", "col_comment": "无形资产-描述"},
                {"col_name": "transacSeatFee", "col_show_name": "其中:交易席位费", "col_comment": "其中:交易席位费-描述"},
                {"col_name": "deferTaxAssets", "col_show_name": "递延所得税资产", "col_comment": "递延所得税资产-描述"},
                {"col_name": "othAssets", "col_show_name": "其他资产", "col_comment": "其他资产-描述"},
                {"col_name": "ae", "col_show_name": "资产的调整项目", "col_comment": "资产的调整项目-描述"},
                {"col_name": "aa", "col_show_name": "资产的差错金额", "col_comment": "资产的差错金额-描述"},
                {"col_name": "tAssets", "col_show_name": "资产总计", "col_comment": "资产总计-描述"},
                {"col_name": "stBorr", "col_show_name": "短期借款", "col_comment": "短期借款-描述"},
                {"col_name": "pledgeBorr", "col_show_name": "其中:质押借款", "col_comment": "其中:质押借款-描述"},
                {"col_name": "loanFrOthBankFi", "col_show_name": "拆入资金", "col_comment": "拆入资金-描述"},
                {"col_name": "tradingFl", "col_show_name": "交易性金融负债", "col_comment": "交易性金融负债-描述"},
                {"col_name": "derivLiab", "col_show_name": "衍生金融负债", "col_comment": "衍生金融负债-描述"},
                {"col_name": "soldForRepurFa", "col_show_name": "卖出回购金融资产款", "col_comment": "卖出回购金融资产款-描述"},
                {"col_name": "fundsSecTradAgen", "col_show_name": "代理买卖证券款", "col_comment": "代理买卖证券款-描述"},
                {"col_name": "fundsSecUndwAgen", "col_show_name": "代理承销证券款", "col_comment": "代理承销证券款-描述"},
                {"col_name": "payrollPayable", "col_show_name": "应付职工薪酬", "col_comment": "应付职工薪酬-描述"},
                {"col_name": "taxesPayable", "col_show_name": "应交税费", "col_comment": "应交税费-描述"},
                {"col_name": "intPayable", "col_show_name": "应付利息", "col_comment": "应付利息-描述"},
                {"col_name": "estimatedLiab", "col_show_name": "预计负债", "col_comment": "预计负债-描述"},
                {"col_name": "ltBorr", "col_show_name": "长期借款", "col_comment": "长期借款-描述"},
                {"col_name": "bondPayable", "col_show_name": "应付债券", "col_comment": "应付债券-描述"},
                {"col_name": "preferredStockL", "col_show_name": "其中:优先股", "col_comment": "其中:优先股-描述"},
                {"col_name": "perpetualBondL", "col_show_name": "永续债", "col_comment": "永续债-描述"},
                {"col_name": "deferTaxLiab", "col_show_name": "递延所得税负债", "col_comment": "递延所得税负债-描述"},
                {"col_name": "othLiab", "col_show_name": "其他负债", "col_comment": "其他负债-描述"},
                {"col_name": "le", "col_show_name": "负债的调整项目", "col_comment": "负债的调整项目-描述"},
                {"col_name": "la", "col_show_name": "负债的差错金额", "col_comment": "负债的差错金额-描述"},
                {"col_name": "tLiab", "col_show_name": "负债合计", "col_comment": "负债合计-描述"},
                {"col_name": "paidInCapital", "col_show_name": "实收资本(或股本)", "col_comment": "实收资本(或股本)-描述"},
                {"col_name": "othEquityInstr", "col_show_name": "其他权益工具", "col_comment": "其他权益工具-描述"},
                {"col_name": "preferredStockE", "col_show_name": "其中:优先股", "col_comment": "其中:优先股-描述"},
                {"col_name": "perpetualBondE", "col_show_name": "永续债", "col_comment": "永续债-描述"},
                {"col_name": "capitalReser", "col_show_name": "资本公积", "col_comment": "资本公积-描述"},
                {"col_name": "treasuryShare", "col_show_name": "减:库存股", "col_comment": "减:库存股-描述"},
                {"col_name": "othCompreIncome", "col_show_name": "其他综合收益", "col_comment": "其他综合收益-描述"},
                {"col_name": "surplusReser", "col_show_name": "盈余公积", "col_comment": "盈余公积-描述"},
                {"col_name": "ordinRiskReser", "col_show_name": "一般风险准备", "col_comment": "一般风险准备-描述"},
                {"col_name": "transacRiskReser", "col_show_name": "交易风险准备", "col_comment": "交易风险准备-描述"},
                {"col_name": "retainedEarnings", "col_show_name": "未分配利润", "col_comment": "未分配利润-描述"},
                {"col_name": "forexDiffer", "col_show_name": "外币报表折算差额", "col_comment": "外币报表折算差额-描述"},
                {"col_name": "see", "col_show_name": "归属于母公司所有者权益的调整项目", "col_comment": "归属于母公司所有者权益的调整项目-描述"},
                {"col_name": "sea", "col_show_name": "归属于母公司所有者权益的差错金额", "col_comment": "归属于母公司所有者权益的差错金额-描述"},
                {"col_name": "updateTime", "col_show_name": "更新时间", "col_comment": "更新时间-描述"},
                {"col_name": "tEquityAttrP", "col_show_name": "归属于母公司所有者权益合计", "col_comment": "归属于母公司所有者权益合计-描述"},
                {"col_name": "minorityInt", "col_show_name": "少数股东权益", "col_comment": "少数股东权益-描述"},
                {"col_name": "othEffectSe", "col_show_name": "所有者权益的调整项目", "col_comment": "所有者权益的调整项目-描述"},
                {"col_name": "othEffectSa", "col_show_name": "所有者权益的差错金额", "col_comment": "所有者权益的差错金额-描述"},
                {"col_name": "tShEquity", "col_show_name": "所有者权益(或股东权益)合计", "col_comment": "所有者权益(或股东权益)合计-描述"},
                {"col_name": "lee", "col_show_name": "负债和权益的调整项目", "col_comment": "负债和权益的调整项目-描述"},
                {"col_name": "lea", "col_show_name": "负债和权益的差错金额", "col_comment": "负债和权益的差错金额-描述"},
                {"col_name": "tLiabEquity", "col_show_name": "负债和所有者权益(或股东权益)总计",
                 "col_comment": "负债和所有者权益(或股东权益)总计-描述"}
            ]
        }
    define_json = json.dumps(fdmtbssecu2018_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def fdmtbsinsu2018_define(table_name):

    fdmtbsinsu2018_str = {
        "table_name": "fdmtbsinsu2018",
        "table_show_name": "(新)保险业资产负债表(PIT)",
        "table_comment": "(新)保险业资产负债表(PIT)-描述",
        "table_category1": "1",
        "table_category2": "2",
        "table_category3": "3",
        "columns": [
            {"col_name": "secID",
             "col_show_name": "通联编制的证券编码，格式是“交易代码.证券市场代码”，如000002.XSHE。可传入证券交易代码使用DataAPI.SecIDGet接口获取到。",
             "col_comment": "通联编制的证券编码，格式是“交易代码.证券市场代码”，如000002.XSHE。可传入证券交易代码使用DataAPI.SecIDGet接口获取到。-描述"},
            {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
            {"col_name": "partyID", "col_show_name": "机构内部ID", "col_comment": "机构内部ID-描述"},
            {"col_name": "ticker", "col_show_name": "股票代码", "col_comment": "股票代码-描述"},
            {"col_name": "exchangeCD", "col_show_name": "交易市场代码：XSHG-上海证券交易所,XSHE-深圳证券交易所",
             "col_comment": "交易市场代码：XSHG-上海证券交易所,XSHE-深圳证券交易所-描述"},
            {"col_name": "actPubtime", "col_show_name": "实际披露时间", "col_comment": "实际披露时间-描述"},
            {"col_name": "publishDate", "col_show_name": "发布日期", "col_comment": "发布日期-描述"},
            {"col_name": "endDateRep", "col_show_name": "报告截止日期", "col_comment": "报告截止日期-描述"},
            {"col_name": "endDate", "col_show_name": "截止日期", "col_comment": "截止日期-描述"},
            {"col_name": "reportType", "col_show_name": "报告类型：Q1-一季度,S1-半年度,Q3-第三季度或前三季度,A-年度",
             "col_comment": "报告类型：Q1-一季度,S1-半年度,Q3-第三季度或前三季度,A-年度-描述"},
            {"col_name": "fiscalPeriod", "col_show_name": "会计区间", "col_comment": "会计区间-描述"},
            {"col_name": "mergedFlag", "col_show_name": "合并标志:1-合并；2-母公司", "col_comment": "合并标志:1-合并；2-母公司-描述"},
            {"col_name": "accoutingStandards", "col_show_name": "会计准则：CHAS_2018-中国会计准则_2018",
             "col_comment": "会计准则：CHAS_2018-中国会计准则_2018-描述"},
            {"col_name": "currencyCD", "col_show_name": "货币代码:CNY-人民币", "col_comment": "货币代码:CNY-人民币-描述"},
            {"col_name": "industryCategory", "col_show_name": "按照财务报表内容分类：保险业", "col_comment": "按照财务报表内容分类：保险业-描述"},
            {"col_name": "cashCEquiv", "col_show_name": "货币资金", "col_comment": "货币资金-描述"},
            {"col_name": "loanToOthBankFi", "col_show_name": "拆出资金", "col_comment": "拆出资金-描述"},
            {"col_name": "tradingFa", "col_show_name": "交易性金融资产", "col_comment": "交易性金融资产-描述"},
            {"col_name": "derivAssets", "col_show_name": "衍生金融资产", "col_comment": "衍生金融资产-描述"},
            {"col_name": "purResaleFa", "col_show_name": "买入返售金融资产", "col_comment": "买入返售金融资产-描述"},
            {"col_name": "tradingOthCompreIncomevFa", "col_show_name": "以公允价值计量且其变动计入其他综合收益的金融资产",
             "col_comment": "以公允价值计量且其变动计入其他综合收益的金融资产-描述"},
            {"col_name": "tradingAmortizeFa", "col_show_name": "以摊余成本计量的金融资产", "col_comment": "以摊余成本计量的金融资产-描述"},
            {"col_name": "debtInvest", "col_show_name": "债权投资", "col_comment": "债权投资-描述"},
            {"col_name": "othDebtInvest", "col_show_name": "其他债权投资", "col_comment": "其他债权投资-描述"},
            {"col_name": "othEquityInstrInvest", "col_show_name": "其他权益工具投资", "col_comment": "其他权益工具投资-描述"},
            {"col_name": "intReceiv", "col_show_name": "应收利息", "col_comment": "应收利息-描述"},
            {"col_name": "premiumReceiv", "col_show_name": "应收保费", "col_comment": "应收保费-描述"},
            {"col_name": "subrogRecoReceiv", "col_show_name": "应收代位追偿款", "col_comment": "应收代位追偿款-描述"},
            {"col_name": "reinsurReceiv", "col_show_name": "应收分保账款", "col_comment": "应收分保账款-描述"},
            {"col_name": "rrReinsUnePrem", "col_show_name": "应收分保未到期责任准备金", "col_comment": "应收分保未到期责任准备金-描述"},
            {"col_name": "rrReinsOutstdCla", "col_show_name": "应收分保未决赔款准备金", "col_comment": "应收分保未决赔款准备金-描述"},
            {"col_name": "rrReinsLinsLiab", "col_show_name": "应收分保寿险责任准备金", "col_comment": "应收分保寿险责任准备金-描述"},
            {"col_name": "rrReinsLthinsLiab", "col_show_name": "应收分保长期健康险责任准备金", "col_comment": "应收分保长期健康险责任准备金-描述"},
            {"col_name": "phPledgeLoans", "col_show_name": "保户质押贷款", "col_comment": "保户质押贷款-描述"},
            {"col_name": "fixedTermDepos", "col_show_name": "定期存款", "col_comment": "定期存款-描述"},
            {"col_name": "availForSaleFa", "col_show_name": "可供出售金融资产", "col_comment": "可供出售金融资产-描述"},
            {"col_name": "htmInvest", "col_show_name": "持有至到期投资", "col_comment": "持有至到期投资-描述"},
            {"col_name": "ltEquityInvest", "col_show_name": "长期股权投资", "col_comment": "长期股权投资-描述"},
            {"col_name": "refundCapDepos", "col_show_name": "存出资本保证金", "col_comment": "存出资本保证金-描述"},
            {"col_name": "investRealEstate", "col_show_name": "投资性房地产", "col_comment": "投资性房地产-描述"},
            {"col_name": "fixedAssets", "col_show_name": "固定资产", "col_comment": "固定资产-描述"},
            {"col_name": "intanAssets", "col_show_name": "无形资产", "col_comment": "无形资产-描述"},
            {"col_name": "indepAccAssets", "col_show_name": "独立账户资产", "col_comment": "独立账户资产-描述"},
            {"col_name": "deferTaxAssets", "col_show_name": "递延所得税资产", "col_comment": "递延所得税资产-描述"},
            {"col_name": "othAssets", "col_show_name": "其他资产", "col_comment": "其他资产-描述"},
            {"col_name": "ae", "col_show_name": "资产的调整项目", "col_comment": "资产的调整项目-描述"},
            {"col_name": "aa", "col_show_name": "资产的差错金额", "col_comment": "资产的差错金额-描述"},
            {"col_name": "tAssets", "col_show_name": "资产总计", "col_comment": "资产总计-描述"},
            {"col_name": "stBorr", "col_show_name": "短期借款", "col_comment": "短期借款-描述"},
            {"col_name": "loanFrOthBankFi", "col_show_name": "拆入资金", "col_comment": "拆入资金-描述"},
            {"col_name": "tradingFl", "col_show_name": "交易性金融负债", "col_comment": "交易性金融负债-描述"},
            {"col_name": "derivLiab", "col_show_name": "衍生金融负债", "col_comment": "衍生金融负债-描述"},
            {"col_name": "soldForRepurFa", "col_show_name": "卖出回购金融资产款", "col_comment": "卖出回购金融资产款-描述"},
            {"col_name": "premReceivAdva", "col_show_name": "预收保费", "col_comment": "预收保费-描述"},
            {"col_name": "commisPayable", "col_show_name": "应付手续费及佣金", "col_comment": "应付手续费及佣金-描述"},
            {"col_name": "reinsurPayable", "col_show_name": "应付分保账款", "col_comment": "应付分保账款-描述"},
            {"col_name": "payrollPayable", "col_show_name": "应付职工薪酬", "col_comment": "应付职工薪酬-描述"},
            {"col_name": "taxesPayable", "col_show_name": "应交税费", "col_comment": "应交税费-描述"},
            {"col_name": "indemAccPayable", "col_show_name": "应付赔付款", "col_comment": "应付赔付款-描述"},
            {"col_name": "policyDivPayable", "col_show_name": "应付保单红利", "col_comment": "应付保单红利-描述"},
            {"col_name": "phInvest", "col_show_name": "保户储金及投资款", "col_comment": "保户储金及投资款-描述"},
            {"col_name": "reserUnePrem", "col_show_name": "未到期责任准备金", "col_comment": "未到期责任准备金-描述"},
            {"col_name": "reserOutstdClaims", "col_show_name": "未决赔款准备金", "col_comment": "未决赔款准备金-描述"},
            {"col_name": "reserLinsLiab", "col_show_name": "寿险责任准备金", "col_comment": "寿险责任准备金-描述"},
            {"col_name": "reserLthinsLiab", "col_show_name": "长期健康险责任准备金", "col_comment": "长期健康险责任准备金-描述"},
            {"col_name": "ltBorr", "col_show_name": "长期借款", "col_comment": "长期借款-描述"},
            {"col_name": "bondPayable", "col_show_name": "应付债券", "col_comment": "应付债券-描述"},
            {"col_name": "preferredStockL", "col_show_name": "其中:优先股", "col_comment": "其中:优先股-描述"},
            {"col_name": "perpetualBondL", "col_show_name": "永续债", "col_comment": "永续债-描述"},
            {"col_name": "indeptAccLiab", "col_show_name": "独立账户负债", "col_comment": "独立账户负债-描述"},
            {"col_name": "deferTaxLiab", "col_show_name": "递延所得税负债", "col_comment": "递延所得税负债-描述"},
            {"col_name": "othLiab", "col_show_name": "其他负债", "col_comment": "其他负债-描述"},
            {"col_name": "le", "col_show_name": "负债的调整项目", "col_comment": "负债的调整项目-描述"},
            {"col_name": "la", "col_show_name": "负债的差错金额", "col_comment": "负债的差错金额-描述"},
            {"col_name": "tLiab", "col_show_name": "负债合计", "col_comment": "负债合计-描述"},
            {"col_name": "paidInCapital", "col_show_name": "实收资本(或股本)", "col_comment": "实收资本(或股本)-描述"},
            {"col_name": "othEquityInstr", "col_show_name": "其他权益工具", "col_comment": "其他权益工具-描述"},
            {"col_name": "preferredStockE", "col_show_name": "其中:优先股", "col_comment": "其中:优先股-描述"},
            {"col_name": "perpetualBondE", "col_show_name": "永续债", "col_comment": "永续债-描述"},
            {"col_name": "capitalReser", "col_show_name": "资本公积", "col_comment": "资本公积-描述"},
            {"col_name": "treasuryShare", "col_show_name": "减:库存股", "col_comment": "减:库存股-描述"},
            {"col_name": "othCompreIncome", "col_show_name": "其他综合收益", "col_comment": "其他综合收益-描述"},
            {"col_name": "surplusReser", "col_show_name": "盈余公积", "col_comment": "盈余公积-描述"},
            {"col_name": "ordinRiskReser", "col_show_name": "一般风险准备", "col_comment": "一般风险准备-描述"},
            {"col_name": "retainedEarnings", "col_show_name": "未分配利润", "col_comment": "未分配利润-描述"},
            {"col_name": "forexDiffer", "col_show_name": "外币报表折算差额", "col_comment": "外币报表折算差额-描述"},
            {"col_name": "see", "col_show_name": "归属于母公司所有者权益的调整项目", "col_comment": "归属于母公司所有者权益的调整项目-描述"},
            {"col_name": "sea", "col_show_name": "归属于母公司所有者权益的差错金额", "col_comment": "归属于母公司所有者权益的差错金额-描述"},
            {"col_name": "tEquityAttrP", "col_show_name": "归属于母公司所有者权益合计", "col_comment": "归属于母公司所有者权益合计-描述"},
            {"col_name": "minorityInt", "col_show_name": "少数股东权益", "col_comment": "少数股东权益-描述"},
            {"col_name": "othEffectSe", "col_show_name": "所有者权益的调整项目", "col_comment": "所有者权益的调整项目-描述"},
            {"col_name": "othEffectSa", "col_show_name": "所有者权益的差错金额", "col_comment": "所有者权益的差错金额-描述"},
            {"col_name": "tShEquity", "col_show_name": "所有者权益(或股东权益)合计", "col_comment": "所有者权益(或股东权益)合计-描述"},
            {"col_name": "lee", "col_show_name": "负债和权益的调整项目", "col_comment": "负债和权益的调整项目-描述"},
            {"col_name": "lea", "col_show_name": "负债和权益的差错金额", "col_comment": "负债和权益的差错金额-描述"},
            {"col_name": "tLiabEquity", "col_show_name": "负债和所有者权益(或股东权益)总计", "col_comment": "负债和所有者权益(或股东权益)总计-描述"},
            {"col_name": "updateTime", "col_show_name": "更新时间", "col_comment": "更新时间-描述"},
            {"col_name": "reinsurReserReceiv", "col_show_name": "应收分保合同准备金", "col_comment": "应收分保合同准备金-描述"},
            {"col_name": "insurReser", "col_show_name": "保险合同准备金", "col_comment": "保险合同准备金-描述"}
        ]
    }

    define_json = json.dumps(fdmtbsinsu2018_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def fdmtbsbank_define(table_name):

    fdmtbsbank_str = {
        "table_name": "fdmtbsbank",
        "table_show_name": "银行业资产负债表(PIT)",
        "table_comment": "银行业资产负债表(PIT)-描述",
        "table_category1": "1",
        "table_category2": "2",
        "table_category3": "3",
        "columns": [
            {"col_name": "secID", "col_show_name": "证券内部ID", "col_comment": "证券内部ID-描述"},
            {"col_name": "publishDate", "col_show_name": "发布日期", "col_comment": "发布日期-描述"},
            {"col_name": "endDate", "col_show_name": "截止日期", "col_comment": "截止日期-描述"},
            {"col_name": "endDateRep", "col_show_name": "报表截止日期", "col_comment": "报表截止日期-描述"},
            {"col_name": "partyID", "col_show_name": "机构内部ID", "col_comment": "机构内部ID-描述"},
            {"col_name": "ticker", "col_show_name": "股票代码", "col_comment": "股票代码-描述"},
            {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
            {"col_name": "exchangeCD",
             "col_show_name": "通联编制的证券市场编码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所等。对应DataAPI.SysCodeGet.codeTypeID=10002。",
             "col_comment": "通联编制的证券市场编码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所等。对应DataAPI.SysCodeGet.codeTypeID=10002。-描述"},
            {"col_name": "actPubtime", "col_show_name": "实际披露时间", "col_comment": "实际披露时间-描述"},
            {"col_name": "mergedFlag", "col_show_name": "合并类型。1-合并,2-母公司。对应DataAPI.SysCodeGet.codeTypeID=70003。",
             "col_comment": "合并类型。1-合并,2-母公司。对应DataAPI.SysCodeGet.codeTypeID=70003。-描述"},
            {"col_name": "reportType",
             "col_show_name": "报告类型。Q1-一季度，S1-半年度，Q3-三季度，A-年度。对应DataAPI.SysCodeGet.codeTypeID=70001。",
             "col_comment": "报告类型。Q1-一季度，S1-半年度，Q3-三季度，A-年度。对应DataAPI.SysCodeGet.codeTypeID=70001。-描述"},
            {"col_name": "fiscalPeriod", "col_show_name": "会计期间", "col_comment": "会计期间-描述"},
            {"col_name": "accoutingStandards", "col_show_name": "会计准则", "col_comment": "会计准则-描述"},
            {"col_name": "currencyCD",
             "col_show_name": "货币代码。例如，USD-美元；CAD-加元等。对应DataAPI.SysCodeGet.codeTypeID=10004。",
             "col_comment": "货币代码。例如，USD-美元；CAD-加元等。对应DataAPI.SysCodeGet.codeTypeID=10004。-描述"},
            {"col_name": "loanToOthBankFi", "col_show_name": "拆出资金", "col_comment": "拆出资金-描述"},
            {"col_name": "tradingFA", "col_show_name": "交易性金融资产", "col_comment": "交易性金融资产-描述"},
            {"col_name": "intReceiv", "col_show_name": "应收利息", "col_comment": "应收利息-描述"},
            {"col_name": "purResaleFa", "col_show_name": "买入返售金融资产", "col_comment": "买入返售金融资产-描述"},
            {"col_name": "disburLA", "col_show_name": "发放委托贷款及垫款", "col_comment": "发放委托贷款及垫款-描述"},
            {"col_name": "availForSaleFA", "col_show_name": "可供出售金融资产", "col_comment": "可供出售金融资产-描述"},
            {"col_name": "htmInvest", "col_show_name": "持有至到期投资", "col_comment": "持有至到期投资-描述"},
            {"col_name": "LTEquityInvest", "col_show_name": "长期股权投资", "col_comment": "长期股权投资-描述"},
            {"col_name": "investRealEstate", "col_show_name": "投资性房地产", "col_comment": "投资性房地产-描述"},
            {"col_name": "fixedAssets", "col_show_name": "固定资产", "col_comment": "固定资产-描述"},
            {"col_name": "CIP", "col_show_name": "在建工程", "col_comment": "在建工程-描述"},
            {"col_name": "intanAssets", "col_show_name": "无形资产", "col_comment": "无形资产-描述"},
            {"col_name": "goodwill", "col_show_name": "商誉", "col_comment": "商誉-描述"},
            {"col_name": "deferTaxAssets", "col_show_name": "递延所得税资产", "col_comment": "递延所得税资产-描述"},
            {"col_name": "CReserCB", "col_show_name": "现金及存放中央银行款项", "col_comment": "现金及存放中央银行款项-描述"},
            {"col_name": "deposInOthBfi", "col_show_name": "存放同业款项", "col_comment": "存放同业款项-描述"},
            {"col_name": "preciMetals", "col_show_name": "贵金属", "col_comment": "贵金属-描述"},
            {"col_name": "derivAssets", "col_show_name": "衍生金融资产", "col_comment": "衍生金融资产-描述"},
            {"col_name": "finanLeaseReceiv", "col_show_name": "应收融资租赁款", "col_comment": "应收融资租赁款-描述"},
            {"col_name": "investAsReceiv", "col_show_name": "应收款项类投资", "col_comment": "应收款项类投资-描述"},
            {"col_name": "othAssets", "col_show_name": "其他资产", "col_comment": "其他资产-描述"},
            {"col_name": "AE", "col_show_name": "资产的特殊项目", "col_comment": "资产的特殊项目-描述"},
            {"col_name": "AA", "col_show_name": "资产的调整金额", "col_comment": "资产的调整金额-描述"},
            {"col_name": "TAssets", "col_show_name": "资产总计", "col_comment": "资产总计-描述"},
            {"col_name": "CBBorr", "col_show_name": "向中央银行借款", "col_comment": "向中央银行借款-描述"},
            {"col_name": "depos", "col_show_name": "吸收存款", "col_comment": "吸收存款-描述"},
            {"col_name": "loanFrOthBankFi", "col_show_name": "拆入资金", "col_comment": "拆入资金-描述"},
            {"col_name": "tradingFL", "col_show_name": "交易性金融负债", "col_comment": "交易性金融负债-描述"},
            {"col_name": "soldForRepurFa", "col_show_name": "卖出回购金融资产款", "col_comment": "卖出回购金融资产款-描述"},
            {"col_name": "payrollPayable", "col_show_name": "应付职工薪酬", "col_comment": "应付职工薪酬-描述"},
            {"col_name": "taxesPayable", "col_show_name": "应交税费", "col_comment": "应交税费-描述"},
            {"col_name": "intPayable", "col_show_name": "应付利息", "col_comment": "应付利息-描述"},
            {"col_name": "bondPayable", "col_show_name": "应付债券", "col_comment": "应付债券-描述"},
            {"col_name": "preferredStockL", "col_show_name": "其中：优先股", "col_comment": "其中：优先股-描述"},
            {"col_name": "perpetualBondL", "col_show_name": "其中：永续债", "col_comment": "其中：永续债-描述"},
            {"col_name": "estimatedLiab", "col_show_name": "预计负债", "col_comment": "预计负债-描述"},
            {"col_name": "deferTaxLiab", "col_show_name": "递延所得税负债", "col_comment": "递延所得税负债-描述"},
            {"col_name": "deposFrOthBfi", "col_show_name": "同业及其他金融机构存放款项", "col_comment": "同业及其他金融机构存放款项-描述"},
            {"col_name": "derivLiab", "col_show_name": "衍生金融负债", "col_comment": "衍生金融负债-描述"},
            {"col_name": "othLiab", "col_show_name": "其他负债", "col_comment": "其他负债-描述"},
            {"col_name": "LE", "col_show_name": "负债的特殊项目", "col_comment": "负债的特殊项目-描述"},
            {"col_name": "LA", "col_show_name": "负债的调整金额", "col_comment": "负债的调整金额-描述"},
            {"col_name": "TLiab", "col_show_name": "负债合计", "col_comment": "负债合计-描述"},
            {"col_name": "paidInCapital", "col_show_name": "实收资本(或股本)", "col_comment": "实收资本(或股本)-描述"},
            {"col_name": "othEquityInstr", "col_show_name": "其他权益工具", "col_comment": "其他权益工具-描述"},
            {"col_name": "preferredStockE", "col_show_name": "其中：优先股", "col_comment": "其中：优先股-描述"},
            {"col_name": "perpetualBondE", "col_show_name": "其中：永续债", "col_comment": "其中：永续债-描述"},
            {"col_name": "capitalReser", "col_show_name": "资本公积", "col_comment": "资本公积-描述"},
            {"col_name": "treasuryShare", "col_show_name": "减:库存股", "col_comment": "减:库存股-描述"},
            {"col_name": "othCompreIncome", "col_show_name": "其他综合收益", "col_comment": "其他综合收益-描述"},
            {"col_name": "surplusReser", "col_show_name": "盈余公积", "col_comment": "盈余公积-描述"},
            {"col_name": "ordinRiskReser", "col_show_name": "一般风险准备", "col_comment": "一般风险准备-描述"},
            {"col_name": "retainedEarnings", "col_show_name": "未分配利润", "col_comment": "未分配利润-描述"},
            {"col_name": "forexDiffer", "col_show_name": "外币报表折算差额", "col_comment": "外币报表折算差额-描述"},
            {"col_name": "SEE", "col_show_name": "归属于母公司所有者权益特殊项目", "col_comment": "归属于母公司所有者权益特殊项目-描述"},
            {"col_name": "SEA", "col_show_name": "归属于母公司所有者权益调整金额", "col_comment": "归属于母公司所有者权益调整金额-描述"},
            {"col_name": "TEquityAttrP", "col_show_name": "归属于母公司所有者权益合计", "col_comment": "归属于母公司所有者权益合计-描述"},
            {"col_name": "minorityInt", "col_show_name": "少数股东权益", "col_comment": "少数股东权益-描述"},
            {"col_name": "othEffectSE", "col_show_name": "所有者权益特殊项目", "col_comment": "所有者权益特殊项目-描述"},
            {"col_name": "othEffectSA", "col_show_name": "所有者权益调整金额", "col_comment": "所有者权益调整金额-描述"},
            {"col_name": "TShEquity", "col_show_name": "所有者权益合计", "col_comment": "所有者权益合计-描述"},
            {"col_name": "LEE", "col_show_name": "负债和所有者权益合计特殊项目", "col_comment": "负债和所有者权益合计特殊项目-描述"},
            {"col_name": "LEA", "col_show_name": "负债和所有者权益合计调整金额", "col_comment": "负债和所有者权益合计调整金额-描述"},
            {"col_name": "TLiabEquity", "col_show_name": "负债和所有者权益总计", "col_comment": "负债和所有者权益总计-描述"},
            {"col_name": "updateTime", "col_show_name": "更新时间", "col_comment": "更新时间-描述"}
            ]
        }
    define_json = json.dumps(fdmtbsbank_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def fdmtbsindu_define(table_name):

    fdmtbsindu_str = {
        "table_name": "fdmtbsindu",
        "table_show_name": "一般工商业资产负债表(PIT)",
        "table_comment": "一般工商业资产负债表(PIT)-描述",
        "table_category1": "1",
        "table_category2": "2",
        "table_category3": "3",
        "columns": [
            {"col_name": "secID", "col_show_name": "证券内部ID", "col_comment": "证券内部ID-描述"},
            {"col_name": "publishDate", "col_show_name": "发布日期", "col_comment": "发布日期-描述"},
            {"col_name": "endDate", "col_show_name": "截止日期", "col_comment": "截止日期-描述"},
            {"col_name": "endDateRep", "col_show_name": "报表截止日期", "col_comment": "报表截止日期-描述"},
            {"col_name": "partyID", "col_show_name": "机构内部ID", "col_comment": "机构内部ID-描述"},
            {"col_name": "ticker", "col_show_name": "股票代码", "col_comment": "股票代码-描述"},
            {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
            {"col_name": "exchangeCD",
             "col_show_name": "通联编制的证券市场编码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所等。对应DataAPI.SysCodeGet.codeTypeID=10002。",
             "col_comment": "通联编制的证券市场编码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所等。对应DataAPI.SysCodeGet.codeTypeID=10002。-描述"},
            {"col_name": "actPubtime", "col_show_name": "实际披露时间", "col_comment": "实际披露时间-描述"},
            {"col_name": "mergedFlag", "col_show_name": "合并类型。1-合并,2-母公司。对应DataAPI.SysCodeGet.codeTypeID=70003。",
             "col_comment": "合并类型。1-合并,2-母公司。对应DataAPI.SysCodeGet.codeTypeID=70003。-描述"},
            {"col_name": "reportType",
             "col_show_name": "报告类型。Q1-一季度，S1-半年度，Q3-三季度，A-年度。对应DataAPI.SysCodeGet.codeTypeID=70001。",
             "col_comment": "报告类型。Q1-一季度，S1-半年度，Q3-三季度，A-年度。对应DataAPI.SysCodeGet.codeTypeID=70001。-描述"},
            {"col_name": "fiscalPeriod", "col_show_name": "会计期间", "col_comment": "会计期间-描述"},
            {"col_name": "accoutingStandards", "col_show_name": "会计准则", "col_comment": "会计准则-描述"},
            {"col_name": "currencyCD", "col_show_name": "货币代码。例如，USD-美元；CAD-加元等。对应DataAPI.SysCodeGet.codeTypeID=10004。",
             "col_comment": "货币代码。例如，USD-美元；CAD-加元等。对应DataAPI.SysCodeGet.codeTypeID=10004。-描述"},
            {"col_name": "cashCEquiv", "col_show_name": "货币资金", "col_comment": "货币资金-描述"},
            {"col_name": "settProv", "col_show_name": "结算备付金", "col_comment": "结算备付金-描述"},
            {"col_name": "loanToOthBankFi", "col_show_name": "拆出资金", "col_comment": "拆出资金-描述"},
            {"col_name": "tradingFA", "col_show_name": "交易性金融资产", "col_comment": "交易性金融资产-描述"},
            {"col_name": "derivAssets", "col_show_name": "衍生金融资产", "col_comment": "衍生金融资产-描述"},
            {"col_name": "NotesReceiv", "col_show_name": "应收票据", "col_comment": "应收票据-描述"},
            {"col_name": "AR", "col_show_name": "应收账款", "col_comment": "应收账款-描述"},
            {"col_name": "prepayment", "col_show_name": "预付款项", "col_comment": "预付款项-描述"},
            {"col_name": "premiumReceiv", "col_show_name": "应收保费", "col_comment": "应收保费-描述"},
            {"col_name": "reinsurReceiv", "col_show_name": "应收分保账款", "col_comment": "应收分保账款-描述"},
            {"col_name": "reinsurReserReceiv", "col_show_name": "应收分保合同准备金", "col_comment": "应收分保合同准备金-描述"},
            {"col_name": "intReceiv", "col_show_name": "应收利息", "col_comment": "应收利息-描述"},
            {"col_name": "divReceiv", "col_show_name": "应收股利", "col_comment": "应收股利-描述"},
            {"col_name": "othReceiv", "col_show_name": "其他应收款", "col_comment": "其他应收款-描述"},
            {"col_name": "purResaleFa", "col_show_name": "买入返售金融资产", "col_comment": "买入返售金融资产-描述"},
            {"col_name": "inventories", "col_show_name": "存货", "col_comment": "存货-描述"},
            {"col_name": "assetsHeldForSale", "col_show_name": "划分为持有至待售资产", "col_comment": "划分为持有至待售资产-描述"},
            {"col_name": "NCAWithin1Y", "col_show_name": "一年内到期的非流动资产", "col_comment": "一年内到期的非流动资产-描述"},
            {"col_name": "othCA", "col_show_name": "其他流动资产", "col_comment": "其他流动资产-描述"},
            {"col_name": "CAE", "col_show_name": "流动资产的特殊项目", "col_comment": "流动资产的特殊项目-描述"},
            {"col_name": "CAA", "col_show_name": "流动资产的调整金额", "col_comment": "流动资产的调整金额-描述"},
            {"col_name": "TCA", "col_show_name": "流动资产合计", "col_comment": "流动资产合计-描述"},
            {"col_name": "disburLA", "col_show_name": "发放委托贷款及垫款", "col_comment": "发放委托贷款及垫款-描述"},
            {"col_name": "availForSaleFa", "col_show_name": "可供出售金融资产", "col_comment": "可供出售金融资产-描述"},
            {"col_name": "htmInvest", "col_show_name": "持有至到期投资", "col_comment": "持有至到期投资-描述"},
            {"col_name": "LTReceive", "col_show_name": "长期应收款", "col_comment": "长期应收款-描述"},
            {"col_name": "LTEquityInvest", "col_show_name": "长期股权投资", "col_comment": "长期股权投资-描述"},
            {"col_name": "investRealEstate", "col_show_name": "投资性房地产", "col_comment": "投资性房地产-描述"},
            {"col_name": "fixedAssets", "col_show_name": "固定资产", "col_comment": "固定资产-描述"},
            {"col_name": "CIP", "col_show_name": "在建工程", "col_comment": "在建工程-描述"},
            {"col_name": "constMaterials", "col_show_name": "工程物资", "col_comment": "工程物资-描述"},
            {"col_name": "fixedAssetsDisp", "col_show_name": "固定资产清理", "col_comment": "固定资产清理-描述"},
            {"col_name": "producBiolAssets", "col_show_name": "生产性生物资产", "col_comment": "生产性生物资产-描述"},
            {"col_name": "oilAndGasAssets", "col_show_name": "油气资产", "col_comment": "油气资产-描述"},
            {"col_name": "intanAssets", "col_show_name": "无形资产", "col_comment": "无形资产-描述"},
            {"col_name": "RD", "col_show_name": "开发支出", "col_comment": "开发支出-描述"},
            {"col_name": "goodwill", "col_show_name": "商誉", "col_comment": "商誉-描述"},
            {"col_name": "LTAmorExp", "col_show_name": "长期待摊费用", "col_comment": "长期待摊费用-描述"},
            {"col_name": "deferTaxAssets", "col_show_name": "递延所得税资产", "col_comment": "递延所得税资产-描述"},
            {"col_name": "othNCA", "col_show_name": "其他非流动资产", "col_comment": "其他非流动资产-描述"},
            {"col_name": "NCAE", "col_show_name": "非流动资产的特殊项目", "col_comment": "非流动资产的特殊项目-描述"},
            {"col_name": "NCAA", "col_show_name": "非流动资产的调整金额", "col_comment": "非流动资产的调整金额-描述"},
            {"col_name": "TNCA", "col_show_name": "非流动资产合计", "col_comment": "非流动资产合计-描述"},
            {"col_name": "AE", "col_show_name": "资产的特殊项目", "col_comment": "资产的特殊项目-描述"},
            {"col_name": "AA", "col_show_name": "资产的调整金额", "col_comment": "资产的调整金额-描述"},
            {"col_name": "TAssets", "col_show_name": "资产总计", "col_comment": "资产总计-描述"},
            {"col_name": "STBorr", "col_show_name": "短期借款", "col_comment": "短期借款-描述"},
            {"col_name": "CBBorr", "col_show_name": "向中央银行借款", "col_comment": "向中央银行借款-描述"},
            {"col_name": "depos", "col_show_name": "吸收存款及同业存放", "col_comment": "吸收存款及同业存放-描述"},
            {"col_name": "loanFrOthBankFi", "col_show_name": "拆入资金", "col_comment": "拆入资金-描述"},
            {"col_name": "tradingFL", "col_show_name": "交易性金融负债", "col_comment": "交易性金融负债-描述"},
            {"col_name": "derivLiab", "col_show_name": "衍生金融负债", "col_comment": "衍生金融负债-描述"},
            {"col_name": "NotesPayable", "col_show_name": "应付票据", "col_comment": "应付票据-描述"},
            {"col_name": "AP", "col_show_name": "应付账款", "col_comment": "应付账款-描述"},
            {"col_name": "advanceReceipts", "col_show_name": "预收款项", "col_comment": "预收款项-描述"},
            {"col_name": "soldForRepurFa", "col_show_name": "卖出回购金融资产款", "col_comment": "卖出回购金融资产款-描述"},
            {"col_name": "commisPayable", "col_show_name": "应付手续费及佣金", "col_comment": "应付手续费及佣金-描述"},
            {"col_name": "payrollPayable", "col_show_name": "应付职工薪酬", "col_comment": "应付职工薪酬-描述"},
            {"col_name": "taxesPayable", "col_show_name": "应交税费", "col_comment": "应交税费-描述"},
            {"col_name": "intPayable", "col_show_name": "应付利息", "col_comment": "应付利息-描述"},
            {"col_name": "divPayable", "col_show_name": "应付股利", "col_comment": "应付股利-描述"},
            {"col_name": "othPayable", "col_show_name": "其他应付款", "col_comment": "其他应付款-描述"},
            {"col_name": "reinsurPayable", "col_show_name": "应付分保账款", "col_comment": "应付分保账款-描述"},
            {"col_name": "insurReser", "col_show_name": "保险合同准备金", "col_comment": "保险合同准备金-描述"},
            {"col_name": "fundsSecTradAgen", "col_show_name": "代理买卖证券款", "col_comment": "代理买卖证券款-描述"},
            {"col_name": "fundsSecUndwAgen", "col_show_name": "代理承销证券款", "col_comment": "代理承销证券款-描述"},
            {"col_name": "liabHeldForSale", "col_show_name": "划分为持有待售的负债", "col_comment": "划分为持有待售的负债-描述"},
            {"col_name": "NCLWithin1Y", "col_show_name": "一年内到期的非流动负债", "col_comment": "一年内到期的非流动负债-描述"},
            {"col_name": "accruedExp", "col_show_name": "预提费用", "col_comment": "预提费用-描述"},
            {"col_name": "othCL", "col_show_name": "其他流动负债", "col_comment": "其他流动负债-描述"},
            {"col_name": "CLE", "col_show_name": "流动负债的特殊项目", "col_comment": "流动负债的特殊项目-描述"},
            {"col_name": "CLA", "col_show_name": "流动负债的调整项目", "col_comment": "流动负债的调整项目-描述"},
            {"col_name": "TCL", "col_show_name": "流动负债合计", "col_comment": "流动负债合计-描述"},
            {"col_name": "LTBorr", "col_show_name": "长期借款", "col_comment": "长期借款-描述"},
            {"col_name": "bondPayable", "col_show_name": "应付债券", "col_comment": "应付债券-描述"},
            {"col_name": "preferredStockL", "col_show_name": "其中：优先股", "col_comment": "其中：优先股-描述"},
            {"col_name": "perpetualBondL", "col_show_name": "其中：永续债", "col_comment": "其中：永续债-描述"},
            {"col_name": "LTPayable", "col_show_name": "长期应付款", "col_comment": "长期应付款-描述"},
            {"col_name": "LTPayrollPayable", "col_show_name": "长期应付职工薪酬", "col_comment": "长期应付职工薪酬-描述"},
            {"col_name": "specificPayables", "col_show_name": "专项应付款", "col_comment": "专项应付款-描述"},
            {"col_name": "estimatedLiab", "col_show_name": "预计负债", "col_comment": "预计负债-描述"},
            {"col_name": "deferRevenue", "col_show_name": "递延收益", "col_comment": "递延收益-描述"},
            {"col_name": "deferTaxLiab", "col_show_name": "递延所得税负债", "col_comment": "递延所得税负债-描述"},
            {"col_name": "othNCL", "col_show_name": "其他非流动负债", "col_comment": "其他非流动负债-描述"},
            {"col_name": "NCLE", "col_show_name": "非流动负债的特殊项目", "col_comment": "非流动负债的特殊项目-描述"},
            {"col_name": "NCLA", "col_show_name": "非流动负债的调整项目", "col_comment": "非流动负债的调整项目-描述"},
            {"col_name": "TNCL", "col_show_name": "非流动负债合计", "col_comment": "非流动负债合计-描述"},
            {"col_name": "LE", "col_show_name": "负债的特殊项目", "col_comment": "负债的特殊项目-描述"},
            {"col_name": "LA", "col_show_name": "负债的调整金额", "col_comment": "负债的调整金额-描述"},
            {"col_name": "TLiab", "col_show_name": "负债合计", "col_comment": "负债合计-描述"},
            {"col_name": "paidInCapital", "col_show_name": "实收资本(或股本)", "col_comment": "实收资本(或股本)-描述"},
            {"col_name": "othEquityInstr", "col_show_name": "其他权益工具", "col_comment": "其他权益工具-描述"},
            {"col_name": "preferredStockE", "col_show_name": "其中：优先股", "col_comment": "其中：优先股-描述"},
            {"col_name": "perpetualBondE", "col_show_name": "其中：永续债", "col_comment": "其中：永续债-描述"},
            {"col_name": "capitalReser", "col_show_name": "资本公积", "col_comment": "资本公积-描述"},
            {"col_name": "treasuryShare", "col_show_name": "减:库存股", "col_comment": "减:库存股-描述"},
            {"col_name": "othCompreIncome", "col_show_name": "其他综合收益", "col_comment": "其他综合收益-描述"},
            {"col_name": "specialReser", "col_show_name": "专项储备", "col_comment": "专项储备-描述"},
            {"col_name": "surplusReser", "col_show_name": "盈余公积", "col_comment": "盈余公积-描述"},
            {"col_name": "ordinRiskReser", "col_show_name": "一般风险准备", "col_comment": "一般风险准备-描述"},
            {"col_name": "retainedEarnings", "col_show_name": "未分配利润", "col_comment": "未分配利润-描述"},
            {"col_name": "forexDiffer", "col_show_name": "外币报表折算差额", "col_comment": "外币报表折算差额-描述"},
            {"col_name": "SEE", "col_show_name": "归属于母公司所有者权益特殊项目", "col_comment": "归属于母公司所有者权益特殊项目-描述"},
            {"col_name": "SEA", "col_show_name": "归属于母公司所有者权益调整金额", "col_comment": "归属于母公司所有者权益调整金额-描述"},
            {"col_name": "TEquityAttrP", "col_show_name": "归属于母公司所有者权益合计", "col_comment": "归属于母公司所有者权益合计-描述"},
            {"col_name": "minorityInt", "col_show_name": "少数股东权益", "col_comment": "少数股东权益-描述"},
            {"col_name": "othEffectSE", "col_show_name": "所有者权益特殊项目", "col_comment": "所有者权益特殊项目-描述"},
            {"col_name": "othEffectSA", "col_show_name": "所有者权益调整金额", "col_comment": "所有者权益调整金额-描述"},
            {"col_name": "TShEquity", "col_show_name": "所有者权益合计", "col_comment": "所有者权益合计-描述"},
            {"col_name": "LEE", "col_show_name": "负债和所有者权益合计特殊项目", "col_comment": "负债和所有者权益合计特殊项目-描述"},
            {"col_name": "LEA", "col_show_name": "负债和所有者权益合计调整金额", "col_comment": "负债和所有者权益合计调整金额-描述"},
            {"col_name": "TLiabEquity", "col_show_name": "负债和所有者权益总计", "col_comment": "负债和所有者权益总计-描述"},
            {"col_name": "updateTime", "col_show_name": "更新时间", "col_comment": "更新时间-描述"}
            ]
        }
    define_json = json.dumps(fdmtbsindu_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def fdmtbsinsu_define(table_name):

    fdmtbsinsu_str = {
            "table_name": "fdmtbsinsu",
            "table_show_name": "保险业资产负债表(PIT)",
            "table_comment": "保险业资产负债表(PIT)-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "证券内部ID", "col_comment": "证券内部ID-描述"},
                {"col_name": "publishDate", "col_show_name": "发布日期", "col_comment": "发布日期-描述"},
                {"col_name": "endDate", "col_show_name": "截止日期", "col_comment": "截止日期-描述"},
                {"col_name": "endDateRep", "col_show_name": "报表截止日期", "col_comment": "报表截止日期-描述"},
                {"col_name": "partyID", "col_show_name": "机构内部ID", "col_comment": "机构内部ID-描述"},
                {"col_name": "ticker", "col_show_name": "股票代码", "col_comment": "股票代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD",
                 "col_show_name": "通联编制的证券市场编码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所等。对应DataAPI.SysCodeGet.codeTypeID=10002。",
                 "col_comment": "通联编制的证券市场编码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所等。对应DataAPI.SysCodeGet.codeTypeID=10002。-描述"},
                {"col_name": "actPubtime", "col_show_name": "实际披露时间", "col_comment": "实际披露时间-描述"},
                {"col_name": "mergedFlag", "col_show_name": "合并类型。1-合并,2-母公司。对应DataAPI.SysCodeGet.codeTypeID=70003。",
                 "col_comment": "合并类型。1-合并,2-母公司。对应DataAPI.SysCodeGet.codeTypeID=70003。-描述"},
                {"col_name": "reportType",
                 "col_show_name": "报告类型。Q1-一季度，S1-半年度，Q3-三季度，A-年度。对应DataAPI.SysCodeGet.codeTypeID=70001。",
                 "col_comment": "报告类型。Q1-一季度，S1-半年度，Q3-三季度，A-年度。对应DataAPI.SysCodeGet.codeTypeID=70001。-描述"},
                {"col_name": "fiscalPeriod", "col_show_name": "会计期间", "col_comment": "会计期间-描述"},
                {"col_name": "accoutingStandards", "col_show_name": "会计准则", "col_comment": "会计准则-描述"},
                {"col_name": "currencyCD",
                 "col_show_name": "货币代码。例如，USD-美元；CAD-加元等。对应DataAPI.SysCodeGet.codeTypeID=10004。",
                 "col_comment": "货币代码。例如，USD-美元；CAD-加元等。对应DataAPI.SysCodeGet.codeTypeID=10004。-描述"},
                {"col_name": "cashCEquiv", "col_show_name": "货币资金", "col_comment": "货币资金-描述"},
                {"col_name": "loanToOthBankFi", "col_show_name": "拆出资金", "col_comment": "拆出资金-描述"},
                {"col_name": "tradingFA", "col_show_name": "交易性金融资产", "col_comment": "交易性金融资产-描述"},
                {"col_name": "premiumReceiv", "col_show_name": "应收保费", "col_comment": "应收保费-描述"},
                {"col_name": "reinsurReceiv", "col_show_name": "应收分保账款", "col_comment": "应收分保账款-描述"},
                {"col_name": "intReceiv", "col_show_name": "应收利息", "col_comment": "应收利息-描述"},
                {"col_name": "purResaleFa", "col_show_name": "买入返售金融资产", "col_comment": "买入返售金融资产-描述"},
                {"col_name": "availForSaleFa", "col_show_name": "可供出售金融资产", "col_comment": "可供出售金融资产-描述"},
                {"col_name": "htmInvest", "col_show_name": "持有至到期投资", "col_comment": "持有至到期投资-描述"},
                {"col_name": "LTEquityInvest", "col_show_name": "长期股权投资", "col_comment": "长期股权投资-描述"},
                {"col_name": "investRealEstate", "col_show_name": "投资性房地产", "col_comment": "投资性房地产-描述"},
                {"col_name": "fixedAssets", "col_show_name": "固定资产", "col_comment": "固定资产-描述"},
                {"col_name": "intanAssets", "col_show_name": "无形资产", "col_comment": "无形资产-描述"},
                {"col_name": "deferTaxAssets", "col_show_name": "递延所得税资产", "col_comment": "递延所得税资产-描述"},
                {"col_name": "derivAssets", "col_show_name": "衍生金融资产", "col_comment": "衍生金融资产-描述"},
                {"col_name": "subrogRecoReceiv", "col_show_name": "应收代位追偿款", "col_comment": "应收代位追偿款-描述"},
                {"col_name": "RRReinsUnePrem", "col_show_name": "应收分保未到期责任准备金", "col_comment": "应收分保未到期责任准备金-描述"},
                {"col_name": "RRReinsOutstdCla", "col_show_name": "应收分保未决赔款准备金", "col_comment": "应收分保未决赔款准备金-描述"},
                {"col_name": "RRReinsLinsLiab", "col_show_name": "应收分保寿险责任准备金", "col_comment": "应收分保寿险责任准备金-描述"},
                {"col_name": "RRReinsLThinsLiab", "col_show_name": "应收分保长期健康险责任准备金",
                 "col_comment": "应收分保长期健康险责任准备金-描述"},
                {"col_name": "PHPledgeLoans", "col_show_name": "保户质押贷款", "col_comment": "保户质押贷款-描述"},
                {"col_name": "fixedTermDepos", "col_show_name": "定期存款", "col_comment": "定期存款-描述"},
                {"col_name": "refundCapDepos", "col_show_name": "存出资本保证金", "col_comment": "存出资本保证金-描述"},
                {"col_name": "indepAccAssets", "col_show_name": "独立账户资产", "col_comment": "独立账户资产-描述"},
                {"col_name": "othAssets", "col_show_name": "其他资产", "col_comment": "其他资产-描述"},
                {"col_name": "AE", "col_show_name": "资产的特殊项目", "col_comment": "资产的特殊项目-描述"},
                {"col_name": "AA", "col_show_name": "资产的调整金额", "col_comment": "资产的调整金额-描述"},
                {"col_name": "TAssets", "col_show_name": "资产总计", "col_comment": "资产总计-描述"},
                {"col_name": "STBorr", "col_show_name": "短期借款", "col_comment": "短期借款-描述"},
                {"col_name": "loanFrOthBankFi", "col_show_name": "拆入资金", "col_comment": "拆入资金-描述"},
                {"col_name": "tradingFL", "col_show_name": "交易性金融负债", "col_comment": "交易性金融负债-描述"},
                {"col_name": "soldForRepurFa", "col_show_name": "卖出回购金融资产款", "col_comment": "卖出回购金融资产款-描述"},
                {"col_name": "commisPayable", "col_show_name": "应付手续费及佣金", "col_comment": "应付手续费及佣金-描述"},
                {"col_name": "payrollPayable", "col_show_name": "应付职工薪酬", "col_comment": "应付职工薪酬-描述"},
                {"col_name": "taxesPayable", "col_show_name": "应交税费", "col_comment": "应交税费-描述"},
                {"col_name": "reinsurPayable", "col_show_name": "应付分保账款", "col_comment": "应付分保账款-描述"},
                {"col_name": "LTBorr", "col_show_name": "长期借款", "col_comment": "长期借款-描述"},
                {"col_name": "bondPayable", "col_show_name": "应付债券", "col_comment": "应付债券-描述"},
                {"col_name": "preferredStockL", "col_show_name": "其中：优先股", "col_comment": "其中：优先股-描述"},
                {"col_name": "perpetualBondL", "col_show_name": "其中：永续债", "col_comment": "其中：永续债-描述"},
                {"col_name": "deferTaxLiab", "col_show_name": "递延所得税负债", "col_comment": "递延所得税负债-描述"},
                {"col_name": "derivLiab", "col_show_name": "衍生金融负债", "col_comment": "衍生金融负债-描述"},
                {"col_name": "premReceivAdva", "col_show_name": "预收保费", "col_comment": "预收保费-描述"},
                {"col_name": "indemAccPayable", "col_show_name": "应付赔付款", "col_comment": "应付赔付款-描述"},
                {"col_name": "policyDivPayable", "col_show_name": "应付保单红利", "col_comment": "应付保单红利-描述"},
                {"col_name": "PHInvest", "col_show_name": "保户储金及投资款", "col_comment": "保户储金及投资款-描述"},
                {"col_name": "reserUnePrem", "col_show_name": "未到期责任准备金", "col_comment": "未到期责任准备金-描述"},
                {"col_name": "reserOutstdClaims", "col_show_name": "未决赔款准备金", "col_comment": "未决赔款准备金-描述"},
                {"col_name": "reserLinsLiab", "col_show_name": "寿险责任准备金", "col_comment": "寿险责任准备金-描述"},
                {"col_name": "reserLthinsLiab", "col_show_name": "长期健康险责任准备金", "col_comment": "长期健康险责任准备金-描述"},
                {"col_name": "indeptAccLiab", "col_show_name": "独立账户负债", "col_comment": "独立账户负债-描述"},
                {"col_name": "othLiab", "col_show_name": "其他负债", "col_comment": "其他负债-描述"},
                {"col_name": "LE", "col_show_name": "负债的特殊项目", "col_comment": "负债的特殊项目-描述"},
                {"col_name": "LA", "col_show_name": "负债的调整金额", "col_comment": "负债的调整金额-描述"},
                {"col_name": "TLiab", "col_show_name": "负债合计", "col_comment": "负债合计-描述"},
                {"col_name": "paidInCapital", "col_show_name": "实收资本(或股本)", "col_comment": "实收资本(或股本)-描述"},
                {"col_name": "othEquityInstr", "col_show_name": "其他权益工具", "col_comment": "其他权益工具-描述"},
                {"col_name": "preferredStockE", "col_show_name": "其中：优先股", "col_comment": "其中：优先股-描述"},
                {"col_name": "perpetualBondE", "col_show_name": "其中：永续债", "col_comment": "其中：永续债-描述"},
                {"col_name": "capitalReser", "col_show_name": "资本公积", "col_comment": "资本公积-描述"},
                {"col_name": "treasuryShare", "col_show_name": "减:库存股", "col_comment": "减:库存股-描述"},
                {"col_name": "othCompreIncome", "col_show_name": "其他综合收益", "col_comment": "其他综合收益-描述"},
                {"col_name": "surplusReser", "col_show_name": "盈余公积", "col_comment": "盈余公积-描述"},
                {"col_name": "ordinRiskReser", "col_show_name": "一般风险准备", "col_comment": "一般风险准备-描述"},
                {"col_name": "retainedEarnings", "col_show_name": "未分配利润", "col_comment": "未分配利润-描述"},
                {"col_name": "forexDiffer", "col_show_name": "外币报表折算差额", "col_comment": "外币报表折算差额-描述"},
                {"col_name": "SEE", "col_show_name": "归属于母公司所有者权益特殊项目", "col_comment": "归属于母公司所有者权益特殊项目-描述"},
                {"col_name": "SEA", "col_show_name": "归属于母公司所有者权益调整金额", "col_comment": "归属于母公司所有者权益调整金额-描述"},
                {"col_name": "TEquityAttrP", "col_show_name": "归属于母公司所有者权益合计", "col_comment": "归属于母公司所有者权益合计-描述"},
                {"col_name": "minorityInt", "col_show_name": "少数股东权益", "col_comment": "少数股东权益-描述"},
                {"col_name": "othEffectSE", "col_show_name": "所有者权益特殊项目", "col_comment": "所有者权益特殊项目-描述"},
                {"col_name": "othEffectSA", "col_show_name": "所有者权益调整金额", "col_comment": "所有者权益调整金额-描述"},
                {"col_name": "TShEquity", "col_show_name": "所有者权益合计", "col_comment": "所有者权益合计-描述"},
                {"col_name": "LEE", "col_show_name": "负债和所有者权益合计特殊项目", "col_comment": "负债和所有者权益合计特殊项目-描述"},
                {"col_name": "LEA", "col_show_name": "负债和所有者权益合计调整金额", "col_comment": "负债和所有者权益合计调整金额-描述"},
                {"col_name": "TLiabEquity", "col_show_name": "负债和所有者权益总计", "col_comment": "负债和所有者权益总计-描述"},
                {"col_name": "updateTime", "col_show_name": "更新时间", "col_comment": "更新时间-描述"}
            ]
        }
    define_json = json.dumps(fdmtbsinsu_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def fdmtbssecu_define(table_name):

    fdmtbssecu_str = {
            "table_name": "fdmtbssecu",
            "table_show_name": "",
            "table_comment": "-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "证券内部ID", "col_comment": "证券内部ID-描述"},
                {"col_name": "publishDate", "col_show_name": "发布日期", "col_comment": "发布日期-描述"},
                {"col_name": "endDate", "col_show_name": "截止日期", "col_comment": "截止日期-描述"},
                {"col_name": "endDateRep", "col_show_name": "报表截止日期", "col_comment": "报表截止日期-描述"},
                {"col_name": "partyID", "col_show_name": "机构内部ID", "col_comment": "机构内部ID-描述"},
                {"col_name": "ticker", "col_show_name": "股票代码", "col_comment": "股票代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD",
                 "col_show_name": "通联编制的证券市场编码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所等。对应DataAPI.SysCodeGet.codeTypeID=10002。",
                 "col_comment": "通联编制的证券市场编码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所等。对应DataAPI.SysCodeGet.codeTypeID=10002。-描述"},
                {"col_name": "actPubtime", "col_show_name": "实际披露时间", "col_comment": "实际披露时间-描述"},
                {"col_name": "mergedFlag", "col_show_name": "合并类型。1-合并,2-母公司。对应DataAPI.SysCodeGet.codeTypeID=70003。",
                 "col_comment": "合并类型。1-合并,2-母公司。对应DataAPI.SysCodeGet.codeTypeID=70003。-描述"},
                {"col_name": "reportType",
                 "col_show_name": "报告类型。Q1-一季度，S1-半年度，Q3-三季度，A-年度。对应DataAPI.SysCodeGet.codeTypeID=70001。",
                 "col_comment": "报告类型。Q1-一季度，S1-半年度，Q3-三季度，A-年度。对应DataAPI.SysCodeGet.codeTypeID=70001。-描述"},
                {"col_name": "fiscalPeriod", "col_show_name": "会计期间", "col_comment": "会计期间-描述"},
                {"col_name": "accoutingStandards", "col_show_name": "会计准则", "col_comment": "会计准则-描述"},
                {"col_name": "currencyCD",
                 "col_show_name": "货币代码。例如，USD-美元；CAD-加元等。对应DataAPI.SysCodeGet.codeTypeID=10004。",
                 "col_comment": "货币代码。例如，USD-美元；CAD-加元等。对应DataAPI.SysCodeGet.codeTypeID=10004。-描述"},
                {"col_name": "cashCEquiv", "col_show_name": "货币资金", "col_comment": "货币资金-描述"},
                {"col_name": "clientDepos", "col_show_name": "其中:客户资金存款", "col_comment": "其中:客户资金存款-描述"},
                {"col_name": "settProv", "col_show_name": "结算备付金", "col_comment": "结算备付金-描述"},
                {"col_name": "clientProv", "col_show_name": "其中:客户备付金", "col_comment": "其中:客户备付金-描述"},
                {"col_name": "loanToOthBankFi", "col_show_name": "拆出资金", "col_comment": "拆出资金-描述"},
                {"col_name": "tradingFA", "col_show_name": "交易性金融资产", "col_comment": "交易性金融资产-描述"},
                {"col_name": "intReceiv", "col_show_name": "应收利息", "col_comment": "应收利息-描述"},
                {"col_name": "purResaleFa", "col_show_name": "买入返售金融资产", "col_comment": "买入返售金融资产-描述"},
                {"col_name": "availForSaleFa", "col_show_name": "可供出售金融资产", "col_comment": "可供出售金融资产-描述"},
                {"col_name": "htmInvest", "col_show_name": "持有至到期投资", "col_comment": "持有至到期投资-描述"},
                {"col_name": "LTEquityInvest", "col_show_name": "长期股权投资", "col_comment": "长期股权投资-描述"},
                {"col_name": "investRealEstate", "col_show_name": "投资性房地产", "col_comment": "投资性房地产-描述"},
                {"col_name": "fixedAssets", "col_show_name": "固定资产", "col_comment": "固定资产-描述"},
                {"col_name": "intanAssets", "col_show_name": "无形资产", "col_comment": "无形资产-描述"},
                {"col_name": "transacSeatFee", "col_show_name": "其中:交易席位费", "col_comment": "其中:交易席位费-描述"},
                {"col_name": "deferTaxAssets", "col_show_name": "递延所得税资产", "col_comment": "递延所得税资产-描述"},
                {"col_name": "derivAssets", "col_show_name": "衍生金融资产", "col_comment": "衍生金融资产-描述"},
                {"col_name": "refundDepos", "col_show_name": "存出保证金", "col_comment": "存出保证金-描述"},
                {"col_name": "othAssets", "col_show_name": "其他资产", "col_comment": "其他资产-描述"},
                {"col_name": "AE", "col_show_name": "资产的特殊项目", "col_comment": "资产的特殊项目-描述"},
                {"col_name": "AA", "col_show_name": "资产的调整金额", "col_comment": "资产的调整金额-描述"},
                {"col_name": "TAssets", "col_show_name": "资产总计", "col_comment": "资产总计-描述"},
                {"col_name": "STBorr", "col_show_name": "短期借款", "col_comment": "短期借款-描述"},
                {"col_name": "pledgeBorr", "col_show_name": "其中:质押借款", "col_comment": "其中:质押借款-描述"},
                {"col_name": "loanFrOthBankFi", "col_show_name": "拆入资金", "col_comment": "拆入资金-描述"},
                {"col_name": "tradingFL", "col_show_name": "交易性金融负债", "col_comment": "交易性金融负债-描述"},
                {"col_name": "soldForRepurFa", "col_show_name": "卖出回购金融资产款", "col_comment": "卖出回购金融资产款-描述"},
                {"col_name": "payrollPayable", "col_show_name": "应付职工薪酬", "col_comment": "应付职工薪酬-描述"},
                {"col_name": "taxesPayable", "col_show_name": "应交税费", "col_comment": "应交税费-描述"},
                {"col_name": "intPayable", "col_show_name": "应付利息", "col_comment": "应付利息-描述"},
                {"col_name": "fundsSecTradAgen", "col_show_name": "代理买卖证券款", "col_comment": "代理买卖证券款-描述"},
                {"col_name": "fundsSecUndwAgen", "col_show_name": "代理承销证券款", "col_comment": "代理承销证券款-描述"},
                {"col_name": "LTBorr", "col_show_name": "长期借款", "col_comment": "长期借款-描述"},
                {"col_name": "bondPayable", "col_show_name": "应付债券", "col_comment": "应付债券-描述"},
                {"col_name": "preferredStockL", "col_show_name": "其中：优先股", "col_comment": "其中：优先股-描述"},
                {"col_name": "perpetualBondL", "col_show_name": "其中：永续债", "col_comment": "其中：永续债-描述"},
                {"col_name": "estimatedLiab", "col_show_name": "预计负债", "col_comment": "预计负债-描述"},
                {"col_name": "deferTaxLiab", "col_show_name": "递延所得税负债", "col_comment": "递延所得税负债-描述"},
                {"col_name": "derivLiab", "col_show_name": "衍生金融负债", "col_comment": "衍生金融负债-描述"},
                {"col_name": "othLiab", "col_show_name": "其他负债", "col_comment": "其他负债-描述"},
                {"col_name": "LE", "col_show_name": "负债的特殊项目", "col_comment": "负债的特殊项目-描述"},
                {"col_name": "LA", "col_show_name": "负债的调整金额", "col_comment": "负债的调整金额-描述"},
                {"col_name": "TLiab", "col_show_name": "负债合计", "col_comment": "负债合计-描述"},
                {"col_name": "paidInCapital", "col_show_name": "实收资本(或股本)", "col_comment": "实收资本(或股本)-描述"},
                {"col_name": "othEquityInstr", "col_show_name": "其他权益工具", "col_comment": "其他权益工具-描述"},
                {"col_name": "preferredStockE", "col_show_name": "其中：优先股", "col_comment": "其中：优先股-描述"},
                {"col_name": "perpetualBondE", "col_show_name": "其中：永续债", "col_comment": "其中：永续债-描述"},
                {"col_name": "capitalReser", "col_show_name": "资本公积", "col_comment": "资本公积-描述"},
                {"col_name": "treasuryShare", "col_show_name": "减:库存股", "col_comment": "减:库存股-描述"},
                {"col_name": "othCompreIncome", "col_show_name": "其他综合收益", "col_comment": "其他综合收益-描述"},
                {"col_name": "surplusReser", "col_show_name": "盈余公积", "col_comment": "盈余公积-描述"},
                {"col_name": "ordinRiskReser", "col_show_name": "一般风险准备", "col_comment": "一般风险准备-描述"},
                {"col_name": "transacRiskReser", "col_show_name": "交易风险准备", "col_comment": "交易风险准备-描述"},
                {"col_name": "retainedEarnings", "col_show_name": "未分配利润", "col_comment": "未分配利润-描述"},
                {"col_name": "forexDiffer", "col_show_name": "外币报表折算差额", "col_comment": "外币报表折算差额-描述"},
                {"col_name": "SEE", "col_show_name": "归属于母公司所有者权益特殊项目", "col_comment": "归属于母公司所有者权益特殊项目-描述"},
                {"col_name": "SEA", "col_show_name": "归属于母公司所有者权益调整金额", "col_comment": "归属于母公司所有者权益调整金额-描述"},
                {"col_name": "TEquityAttrP", "col_show_name": "归属于母公司所有者权益合计", "col_comment": "归属于母公司所有者权益合计-描述"},
                {"col_name": "minorityInt", "col_show_name": "少数股东权益", "col_comment": "少数股东权益-描述"},
                {"col_name": "othEffectSE", "col_show_name": "所有者权益特殊项目", "col_comment": "所有者权益特殊项目-描述"},
                {"col_name": "othEffectSA", "col_show_name": "所有者权益调整金额", "col_comment": "所有者权益调整金额-描述"},
                {"col_name": "TShEquity", "col_show_name": "所有者权益合计", "col_comment": "所有者权益合计-描述"},
                {"col_name": "TLiabEquity", "col_show_name": "负债和所有者权益总计", "col_comment": "负债和所有者权益总计-描述"},
                {"col_name": "updateTime", "col_show_name": "更新时间", "col_comment": "更新时间-描述"}
            ]
        }
    define_json = json.dumps(fdmtbssecu_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def fdmtcfbank2018_define(table_name):

    fdmtcfbank2018_str = {
            "table_name": "fdmtcfbank2018",
            "table_show_name": "(新)银行业现金流量表(PIT)",
            "table_comment": "(新)银行业现金流量表(PIT)-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "partyID", "col_show_name": "机构内部ID", "col_comment": "机构内部ID-描述"},
                {"col_name": "ticker", "col_show_name": "股票代码", "col_comment": "股票代码-描述"},
                {"col_name": "exchangeCD", "col_show_name": "交易市场代码", "col_comment": "交易市场代码-描述"},
                {"col_name": "secID", "col_show_name": "证券编码", "col_comment": "证券编码-描述"},
                {"col_name": "actPubtime", "col_show_name": "实际披露时间", "col_comment": "实际披露时间-描述"},
                {"col_name": "publishDate", "col_show_name": "发布日期", "col_comment": "发布日期-描述"},
                {"col_name": "endDateRep", "col_show_name": "报告截止日期", "col_comment": "报告截止日期-描述"},
                {"col_name": "endDate", "col_show_name": "截止日期", "col_comment": "截止日期-描述"},
                {"col_name": "reportType", "col_show_name": "报告类型", "col_comment": "报告类型-描述"},
                {"col_name": "fiscalPeriod", "col_show_name": "会计区间", "col_comment": "会计区间-描述"},
                {"col_name": "mergedFlag", "col_show_name": "合并标志", "col_comment": "合并标志-描述"},
                {"col_name": "accoutingStandards", "col_show_name": "会计准则", "col_comment": "会计准则-描述"},
                {"col_name": "currencyCD", "col_show_name": "货币代码", "col_comment": "货币代码-描述"},
                {"col_name": "industryCategory", "col_show_name": "行业分类", "col_comment": "行业分类-描述"},
                {"col_name": "nDeposIncrCFI", "col_show_name": "客户存款和同业存放款项净增加额", "col_comment": "客户存款和同业存放款项净增加额-描述"},
                {"col_name": "nIncrBorrFRCB", "col_show_name": "向中央银行借款净增加额", "col_comment": "向中央银行借款净增加额-描述"},
                {"col_name": "nIncBorrOthFI", "col_show_name": "向其他金融机构拆入资金净增加额", "col_comment": "向其他金融机构拆入资金净增加额-描述"},
                {"col_name": "nDecrInDisburOFLA", "col_show_name": "发放贷款及垫款净减少额", "col_comment": "发放贷款及垫款净减少额-描述"},
                {"col_name": "netDecrInDeposINFI", "col_show_name": "存放中央银行和同业款项净减少额",
                 "col_comment": "存放中央银行和同业款项净减少额-描述"},
                {"col_name": "nDecrLoanToOthFI", "col_show_name": "向其他金融机构拆出资金净减少额",
                 "col_comment": "向其他金融机构拆出资金净减少额-描述"},
                {"col_name": "ifcCashIncr", "col_show_name": "收取利息、手续费及佣金的现金", "col_comment": "收取利息、手续费及佣金的现金-描述"},
                {"col_name": "cFROthOperateA", "col_show_name": "收到其他与经营活动有关的现金", "col_comment": "收到其他与经营活动有关的现金-描述"},
                {"col_name": "specOCIF", "col_show_name": "经营活动现金流入特殊项目", "col_comment": "经营活动现金流入特殊项目-描述"},
                {"col_name": "AOCIF", "col_show_name": "经营活动现金流入调整金额", "col_comment": "经营活动现金流入调整金额-描述"},
                {"col_name": "cInfFrOperateA", "col_show_name": "经营活动现金流入小计", "col_comment": "经营活动现金流入小计-描述"},
                {"col_name": "nDeposDecrFRFI", "col_show_name": "客户存款和同业存放款项净减少额", "col_comment": "客户存款和同业存放款项净减少额-描述"},
                {"col_name": "nDecrBorrFRCB", "col_show_name": "向中央银行借款净减少额", "col_comment": "向中央银行借款净减少额-描述"},
                {"col_name": "nDecrBorrFROthFI", "col_show_name": "向其他金融机构拆入资金净减少额",
                 "col_comment": "向其他金融机构拆入资金净减少额-描述"},
                {"col_name": "nIncDisburOFLA", "col_show_name": "客户贷款及垫款净增加额", "col_comment": "客户贷款及垫款净增加额-描述"},
                {"col_name": "netIncrDeposINFI", "col_show_name": "存放中央银行和同业款项净增加额",
                 "col_comment": "存放中央银行和同业款项净增加额-描述"},
                {"col_name": "nIncrLoansToOthFI", "col_show_name": "向其他金融机构拆出资金净增加额",
                 "col_comment": "向其他金融机构拆出资金净增加额-描述"},
                {"col_name": "cPaidIFC", "col_show_name": "支付利息、手续费及佣金的现金", "col_comment": "支付利息、手续费及佣金的现金-描述"},
                {"col_name": "cPaidToForEmpl", "col_show_name": "支付给职工以及为职工支付的现金", "col_comment": "支付给职工以及为职工支付的现金-描述"},
                {"col_name": "cPaidForTaxes", "col_show_name": "支付的各项税费", "col_comment": "支付的各项税费-描述"},
                {"col_name": "cPaidForOthOpA", "col_show_name": "支付其他与经营活动有关的现金", "col_comment": "支付其他与经营活动有关的现金-描述"},
                {"col_name": "specOcof", "col_show_name": "经营活动现金流出特殊项目", "col_comment": "经营活动现金流出特殊项目-描述"},
                {"col_name": "AOCOF", "col_show_name": "经营活动现金流出调整金额", "col_comment": "经营活动现金流出调整金额-描述"},
                {"col_name": "cOutfOperateA", "col_show_name": "经营活动现金流出小计", "col_comment": "经营活动现金流出小计-描述"},
                {"col_name": "ANOCF", "col_show_name": "经营活动现金流量净额调整金额", "col_comment": "经营活动现金流量净额调整金额-描述"},
                {"col_name": "nCfOperateA", "col_show_name": "经营活动产生的现金流量净额", "col_comment": "经营活动产生的现金流量净额-描述"},
                {"col_name": "procSellInvest", "col_show_name": "收回投资收到的现金", "col_comment": "收回投资收到的现金-描述"},
                {"col_name": "gainInvest", "col_show_name": "取得投资收益收到的现金", "col_comment": "取得投资收益收到的现金-描述"},
                {"col_name": "dispFixAssetsOth", "col_show_name": "处置固定资产、无形资产和其他长期资产收回的现金净额",
                 "col_comment": "处置固定资产、无形资产和其他长期资产收回的现金净额-描述"},
                {"col_name": "nDispSubsOthBizC", "col_show_name": "处置子公司及其他营业单位收到的现金净额",
                 "col_comment": "处置子公司及其他营业单位收到的现金净额-描述"},
                {"col_name": "cFrOthInvestA", "col_show_name": "收到其他与投资活动有关的现金", "col_comment": "收到其他与投资活动有关的现金-描述"},
                {"col_name": "specCIF", "col_show_name": "投资活动现金流入特殊项目", "col_comment": "投资活动现金流入特殊项目-描述"},
                {"col_name": "ACIF", "col_show_name": "投资活动现金流入调整金额", "col_comment": "投资活动现金流入调整金额-描述"},
                {"col_name": "cInfFrInvestA", "col_show_name": "投资活动现金流入小计", "col_comment": "投资活动现金流入小计-描述"},
                {"col_name": "cPaidInvest", "col_show_name": "投资支付的现金", "col_comment": "投资支付的现金-描述"},
                {"col_name": "purFixAssetsOth", "col_show_name": "购建固定资产、无形资产和其他长期资产支付的现金",
                 "col_comment": "购建固定资产、无形资产和其他长期资产支付的现金-描述"},
                {"col_name": "nCPaidAcquis", "col_show_name": "取得子公司及其他营业单位支付的现金净额",
                 "col_comment": "取得子公司及其他营业单位支付的现金净额-描述"},
                {"col_name": "cPaidOthInvestA", "col_show_name": "支付其他与投资活动有关的现金", "col_comment": "支付其他与投资活动有关的现金-描述"},
                {"col_name": "specCOF", "col_show_name": "投资活动现金流出特殊项目", "col_comment": "投资活动现金流出特殊项目-描述"},
                {"col_name": "ACOF", "col_show_name": "投资活动现金流出调整金额", "col_comment": "投资活动现金流出调整金额-描述"},
                {"col_name": "cOutfFrInvestA", "col_show_name": "投资活动现金流出小计", "col_comment": "投资活动现金流出小计-描述"},
                {"col_name": "ANICF", "col_show_name": "投资活动现金流量净额调整金额", "col_comment": "投资活动现金流量净额调整金额-描述"},
                {"col_name": "nCFFRInvestA", "col_show_name": "投资活动产生的现金流量净额", "col_comment": "投资活动产生的现金流量净额-描述"},
                {"col_name": "cFRCapContr", "col_show_name": "吸收投资收到的现金", "col_comment": "吸收投资收到的现金-描述"},
                {"col_name": "cFRMinoSSubs", "col_show_name": "其中:子公司吸收少数股东投资收到的现金",
                 "col_comment": "其中:子公司吸收少数股东投资收到的现金-描述"},
                {"col_name": "cFRIssueBond", "col_show_name": "发行债券收到的现金", "col_comment": "发行债券收到的现金-描述"},
                {"col_name": "cFROthFinanA", "col_show_name": "收到其他与筹资活动有关的现金", "col_comment": "收到其他与筹资活动有关的现金-描述"},
                {"col_name": "specFCIF", "col_show_name": "筹资活动现金流入特殊项目", "col_comment": "筹资活动现金流入特殊项目-描述"},
                {"col_name": "AFCIF", "col_show_name": "筹资活动现金流入调整金额", "col_comment": "筹资活动现金流入调整金额-描述"},
                {"col_name": "cInfFRFinanA", "col_show_name": "筹资活动现金流入小计", "col_comment": "筹资活动现金流入小计-描述"},
                {"col_name": "cPaidForDebts", "col_show_name": "偿还债务支付的现金", "col_comment": "偿还债务支付的现金-描述"},
                {"col_name": "cPaidDivProfInt", "col_show_name": "分配股利、利润或偿付利息支付的现金",
                 "col_comment": "分配股利、利润或偿付利息支付的现金-描述"},
                {"col_name": "divProfSubsMinoS", "col_show_name": "其中:子公司支付给少数股东的股利、利润",
                 "col_comment": "其中:子公司支付给少数股东的股利、利润-描述"},
                {"col_name": "cPaidOthFinanA", "col_show_name": "支付其他与筹资活动有关的现金", "col_comment": "支付其他与筹资活动有关的现金-描述"},
                {"col_name": "specFCOF", "col_show_name": "筹资活动现金流出特殊项目", "col_comment": "筹资活动现金流出特殊项目-描述"},
                {"col_name": "AFCOF", "col_show_name": "筹资活动现金流出调整金额", "col_comment": "筹资活动现金流出调整金额-描述"},
                {"col_name": "cOutFRFinanA", "col_show_name": "筹资活动现金流出小计", "col_comment": "筹资活动现金流出小计-描述"},
                {"col_name": "ANFCF", "col_show_name": "筹资活动流量现金净额调整金额", "col_comment": "筹资活动流量现金净额调整金额-描述"},
                {"col_name": "nCFFRFinanA", "col_show_name": "筹资活动产生的现金流量净额", "col_comment": "筹资活动产生的现金流量净额-描述"},
                {"col_name": "forexEffects", "col_show_name": "汇率变动对现金及现金等价物的影响", "col_comment": "汇率变动对现金及现金等价物的影响-描述"},
                {"col_name": "othEffectCE", "col_show_name": "影响现金及现金等价物净增加额的特殊项目",
                 "col_comment": "影响现金及现金等价物净增加额的特殊项目-描述"},
                {"col_name": "ACE", "col_show_name": "影响现金及现金等价物的调整金额", "col_comment": "影响现金及现金等价物的调整金额-描述"},
                {"col_name": "nChangeInCash", "col_show_name": "现金及现金等价物净增加额", "col_comment": "现金及现金等价物净增加额-描述"},
                {"col_name": "nCEBegBal", "col_show_name": "加:期初现金及现金等价物余额", "col_comment": "加:期初现金及现金等价物余额-描述"},
                {"col_name": "othEffectCEI", "col_show_name": "现金及现金等价物净增加额的特殊项目",
                 "col_comment": "现金及现金等价物净增加额的特殊项目-描述"},
                {"col_name": "ACEI", "col_show_name": "现金及现金等价物净增加额的调整金额", "col_comment": "现金及现金等价物净增加额的调整金额-描述"},
                {"col_name": "nCeEndBAL", "col_show_name": "期末现金及现金等价物余额", "col_comment": "期末现金及现金等价物余额-描述"}
            ]
        }
    define_json = json.dumps(fdmtcfbank2018_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def fdmtcfindu2018_define(table_name):

    fdmtcfindu2018_str = {
            "table_name": "fdmtcfindu2018",
            "table_show_name": "(新)一般工商业现金流量表(PIT)",
            "table_comment": "(新)一般工商业现金流量表(PIT)-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "partyID", "col_show_name": "机构内部ID", "col_comment": "机构内部ID-描述"},
                {"col_name": "ticker", "col_show_name": "股票代码", "col_comment": "股票代码-描述"},
                {"col_name": "echangeCD", "col_show_name": "交易市场代码", "col_comment": "交易市场代码-描述"},
                {"col_name": "secID", "col_show_name": "证券编码", "col_comment": "证券编码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "actPubtime", "col_show_name": "实际披露时间", "col_comment": "实际披露时间-描述"},
                {"col_name": "publishDate", "col_show_name": "发布日期", "col_comment": "发布日期-描述"},
                {"col_name": "endDateRep", "col_show_name": "报告截止日期", "col_comment": "报告截止日期-描述"},
                {"col_name": "endDate", "col_show_name": "截止日期", "col_comment": "截止日期-描述"},
                {"col_name": "reportType", "col_show_name": "报告类型", "col_comment": "报告类型-描述"},
                {"col_name": "fiscalPeriod", "col_show_name": "会计区间", "col_comment": "会计区间-描述"},
                {"col_name": "mergedFlag", "col_show_name": "合并标志", "col_comment": "合并标志-描述"},
                {"col_name": "accountingStand", "col_show_name": "会计准则", "col_comment": "会计准则-描述"},
                {"col_name": "currencyCD", "col_show_name": "货币代码", "col_comment": "货币代码-描述"},
                {"col_name": "industryCategory", "col_show_name": "行业分类", "col_comment": "行业分类-描述"},
                {"col_name": "cFRSaleGS", "col_show_name": "销售商品、提供劳务收到的现金", "col_comment": "销售商品、提供劳务收到的现金-描述"},
                {"col_name": "nDeposIncrCFI", "col_show_name": "客户存款和同业存放款项净增加额", "col_comment": "客户存款和同业存放款项净增加额-描述"},
                {"col_name": "nIncrBorrFRCB", "col_show_name": "向中央银行借款净增加额", "col_comment": "向中央银行借款净增加额-描述"},
                {"col_name": "nIncBorrOthFI", "col_show_name": "向其他金融机构拆入资金净增加额", "col_comment": "向其他金融机构拆入资金净增加额-描述"},
                {"col_name": "premFROrigContr", "col_show_name": "收到原保险合同保费取得的现金", "col_comment": "收到原保险合同保费取得的现金-描述"},
                {"col_name": "nReinsurPrem", "col_show_name": "收到再保险业务现金净额", "col_comment": "收到再保险业务现金净额-描述"},
                {"col_name": "nIncPHDeposInv", "col_show_name": "保户储金及投资款净增加额", "col_comment": "保户储金及投资款净增加额-描述"},
                {"col_name": "nIncDispTradFA", "col_show_name": "处置交易性金融资产净增加额", "col_comment": "处置交易性金融资产净增加额-描述"},
                {"col_name": "ifcCashIncr", "col_show_name": "收取利息、手续费及佣金的现金", "col_comment": "收取利息、手续费及佣金的现金-描述"},
                {"col_name": "nIncFRBorr", "col_show_name": "拆入资金净增加额", "col_comment": "拆入资金净增加额-描述"},
                {"col_name": "nCapIncrRepur", "col_show_name": "回购业务资金净增加额", "col_comment": "回购业务资金净增加额-描述"},
                {"col_name": "refundOFTax", "col_show_name": "收到的税费返还", "col_comment": "收到的税费返还-描述"},
                {"col_name": "cFROthOperA", "col_show_name": "收到其他与经营活动有关的现金", "col_comment": "收到其他与经营活动有关的现金-描述"},
                {"col_name": "specOCIF", "col_show_name": "经营活动现金流入特殊项目", "col_comment": "经营活动现金流入特殊项目-描述"},
                {"col_name": "AOCIF", "col_show_name": "经营活动现金流入调整金额", "col_comment": "经营活动现金流入调整金额-描述"},
                {"col_name": "cInfFROperA", "col_show_name": "经营活动现金流入小计", "col_comment": "经营活动现金流入小计-描述"},
                {"col_name": "cPaidFROperA", "col_show_name": "购买商品、接受劳务支付的现金", "col_comment": "购买商品、接受劳务支付的现金-描述"},
                {"col_name": "nIncDisburOFLA", "col_show_name": "客户贷款及垫款净增加额", "col_comment": "客户贷款及垫款净增加额-描述"},
                {"col_name": "netIncrDeposINFI", "col_show_name": "存放中央银行和同业款项净增加额",
                 "col_comment": "存放中央银行和同业款项净增加额-描述"},
                {"col_name": "origContrCIndem", "col_show_name": "支付原保险合同赔付款项的现金", "col_comment": "支付原保险合同赔付款项的现金-描述"},
                {"col_name": "cPaidIFC", "col_show_name": "支付利息、手续费及佣金的现金", "col_comment": "支付利息、手续费及佣金的现金-描述"},
                {"col_name": "cPaidPOLDiv", "col_show_name": "支付保单红利的现金", "col_comment": "支付保单红利的现金-描述"},
                {"col_name": "cPaidToForEmpl", "col_show_name": "支付给职工以及为职工支付的现金", "col_comment": "支付给职工以及为职工支付的现金-描述"},
                {"col_name": "cPaidForTaxex", "col_show_name": "支付的各项税费", "col_comment": "支付的各项税费-描述"},
                {"col_name": "cPaidForOthOPA", "col_show_name": "支付其他与经营活动有关的现金", "col_comment": "支付其他与经营活动有关的现金-描述"},
                {"col_name": "specOCOF", "col_show_name": "经营活动现金流出特殊项目", "col_comment": "经营活动现金流出特殊项目-描述"},
                {"col_name": "AOCOF", "col_show_name": "经营活动现金流出调整金额", "col_comment": "经营活动现金流出调整金额-描述"},
                {"col_name": "cOutfOperA", "col_show_name": "经营活动现金流出小计", "col_comment": "经营活动现金流出小计-描述"},
                {"col_name": "ANOCF", "col_show_name": "经营活动现金流量净额调整金额", "col_comment": "经营活动现金流量净额调整金额-描述"},
                {"col_name": "nCFOperA", "col_show_name": "经营活动产生的现金流量净额", "col_comment": "经营活动产生的现金流量净额-描述"},
                {"col_name": "procSellInvest", "col_show_name": "收回投资收到的现金", "col_comment": "收回投资收到的现金-描述"},
                {"col_name": "gainInvest", "col_show_name": "取得投资收益收到的现金", "col_comment": "取得投资收益收到的现金-描述"},
                {"col_name": "dispFixAssetsOth", "col_show_name": "处置固定资产、无形资产和其他长期资产收回的现金净额",
                 "col_comment": "处置固定资产、无形资产和其他长期资产收回的现金净额-描述"},
                {"col_name": "nDispSubsOthBIZC", "col_show_name": "处置子公司及其他营业单位收到的现金净额",
                 "col_comment": "处置子公司及其他营业单位收到的现金净额-描述"},
                {"col_name": "cFROthInvestA", "col_show_name": "收到其他与投资活动有关的现金", "col_comment": "收到其他与投资活动有关的现金-描述"},
                {"col_name": "specCIF", "col_show_name": "投资活动现金流入特殊项目", "col_comment": "投资活动现金流入特殊项目-描述"},
                {"col_name": "ACIF", "col_show_name": "投资活动现金流入调整金额", "col_comment": "投资活动现金流入调整金额-描述"},
                {"col_name": "cInfFRInvestA", "col_show_name": "投资活动现金流入小计", "col_comment": "投资活动现金流入小计-描述"},
                {"col_name": "purFixAssetsOth", "col_show_name": "购建固定资产、无形资产和其他长期资产支付的现金",
                 "col_comment": "购建固定资产、无形资产和其他长期资产支付的现金-描述"},
                {"col_name": "cPaidInvest", "col_show_name": "投资支付的现金", "col_comment": "投资支付的现金-描述"},
                {"col_name": "nIncrPledgeLoan", "col_show_name": "质押贷款净增加额", "col_comment": "质押贷款净增加额-描述"},
                {"col_name": "nCPaidAcquis", "col_show_name": "取得子公司及其他营业单位支付的现金净额",
                 "col_comment": "取得子公司及其他营业单位支付的现金净额-描述"},
                {"col_name": "cPaidPOthInvestA", "col_show_name": "支付其他与投资活动有关的现金", "col_comment": "支付其他与投资活动有关的现金-描述"},
                {"col_name": "specCOF", "col_show_name": "投资活动现金流出特殊项目", "col_comment": "投资活动现金流出特殊项目-描述"},
                {"col_name": "ACOF", "col_show_name": "投资活动现金流出调整金额", "col_comment": "投资活动现金流出调整金额-描述"},
                {"col_name": "cOutfFRInvestA", "col_show_name": "投资活动现金流出小计", "col_comment": "投资活动现金流出小计-描述"},
                {"col_name": "ANICF", "col_show_name": "投资活动现金流量净额调整金额", "col_comment": "投资活动现金流量净额调整金额-描述"},
                {"col_name": "nCFFRInvestA", "col_show_name": "投资活动产生的现金流量净额", "col_comment": "投资活动产生的现金流量净额-描述"},
                {"col_name": "cFRCapContr", "col_show_name": "吸收投资收到的现金", "col_comment": "吸收投资收到的现金-描述"},
                {"col_name": "cFRMinoSSubs", "col_show_name": "其中:子公司吸收少数股东投资收到的现金",
                 "col_comment": "其中:子公司吸收少数股东投资收到的现金-描述"},
                {"col_name": "cFRBorr", "col_show_name": "取得借款收到的现金", "col_comment": "取得借款收到的现金-描述"},
                {"col_name": "cFRIssueBond", "col_show_name": "发行债券收到的现金", "col_comment": "发行债券收到的现金-描述"},
                {"col_name": "cFROthFinanA", "col_show_name": "收到其他与筹资活动有关的现金", "col_comment": "收到其他与筹资活动有关的现金-描述"},
                {"col_name": "specFCIF", "col_show_name": "筹资活动现金流入特殊项目", "col_comment": "筹资活动现金流入特殊项目-描述"},
                {"col_name": "AFCIF", "col_show_name": "筹资活动现金流入调整金额", "col_comment": "筹资活动现金流入调整金额-描述"},
                {"col_name": "cInfFRFinanA", "col_show_name": "筹资活动现金流入小计", "col_comment": "筹资活动现金流入小计-描述"},
                {"col_name": "cPaidForDebts", "col_show_name": "偿还债务支付的现金", "col_comment": "偿还债务支付的现金-描述"},
                {"col_name": "cPaidDivProfInt", "col_show_name": "分配股利、利润或偿付利息支付的现金",
                 "col_comment": "分配股利、利润或偿付利息支付的现金-描述"},
                {"col_name": "divProfSubsMinoS", "col_show_name": "其中:子公司支付给少数股东的股利、利润",
                 "col_comment": "其中:子公司支付给少数股东的股利、利润-描述"},
                {"col_name": "cPaidOthFinanA", "col_show_name": "支付其他与筹资活动有关的现金", "col_comment": "支付其他与筹资活动有关的现金-描述"},
                {"col_name": "specFCOF", "col_show_name": "筹资活动现金流出特殊项目", "col_comment": "筹资活动现金流出特殊项目-描述"},
                {"col_name": "AFCOF", "col_show_name": "筹资活动现金流出调整金额", "col_comment": "筹资活动现金流出调整金额-描述"},
                {"col_name": "cOutfFRFinanA", "col_show_name": "筹资活动现金流出小计", "col_comment": "筹资活动现金流出小计-描述"},
                {"col_name": "ANFCF", "col_show_name": "筹资活动流量现金净额调整金额", "col_comment": "筹资活动流量现金净额调整金额-描述"},
                {"col_name": "nCFFRFinanA", "col_show_name": "筹资活动产生的现金流量净额", "col_comment": "筹资活动产生的现金流量净额-描述"},
                {"col_name": "forexEffects", "col_show_name": "汇率变动对现金及现金等价物的影响", "col_comment": "汇率变动对现金及现金等价物的影响-描述"},
                {"col_name": "othEffectCE", "col_show_name": "影响现金及现金等价物净增加额的特殊项目",
                 "col_comment": "影响现金及现金等价物净增加额的特殊项目-描述"},
                {"col_name": "ACE", "col_show_name": "影响现金及现金等价物的调整金额", "col_comment": "影响现金及现金等价物的调整金额-描述"},
                {"col_name": "nChangeInCash", "col_show_name": "现金及现金等价物净增加额", "col_comment": "现金及现金等价物净增加额-描述"},
                {"col_name": "nCEBegBAL", "col_show_name": "加:期初现金及现金等价物余额", "col_comment": "加:期初现金及现金等价物余额-描述"},
                {"col_name": "othEffectCEI", "col_show_name": "现金及现金等价物净增加额的特殊项目",
                 "col_comment": "现金及现金等价物净增加额的特殊项目-描述"},
                {"col_name": "ACEI", "col_show_name": "现金及现金等价物净增加额的调整金额", "col_comment": "现金及现金等价物净增加额的调整金额-描述"},
                {"col_name": "nCEEndBal", "col_show_name": "期末现金及现金等价物余额", "col_comment": "期末现金及现金等价物余额-描述"}
            ]
        }
    define_json = json.dumps(fdmtcfindu2018_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def fdmtcfinsu2018_define(table_name):

    fdmtcfinsu2018_str = {
            "table_name": "fdmtcfinsu2018",
            "table_show_name": "(新)保险业现金流量表(PIT)",
            "table_comment": "(新)保险业现金流量表(PIT)-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "partyID", "col_show_name": "机构内部ID", "col_comment": "机构内部ID-描述"},
                {"col_name": "ticker", "col_show_name": "股票代码", "col_comment": "股票代码-描述"},
                {"col_name": "echangeCD", "col_show_name": "交易市场代码", "col_comment": "交易市场代码-描述"},
                {"col_name": "secID", "col_show_name": "证券编码", "col_comment": "证券编码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "actPubtime", "col_show_name": "实际披露时间", "col_comment": "实际披露时间-描述"},
                {"col_name": "publishDate", "col_show_name": "发布日期", "col_comment": "发布日期-描述"},
                {"col_name": "endDateRep", "col_show_name": "报告截止日期", "col_comment": "报告截止日期-描述"},
                {"col_name": "endDate", "col_show_name": "截止日期", "col_comment": "截止日期-描述"},
                {"col_name": "reportType", "col_show_name": "报告类型", "col_comment": "报告类型-描述"},
                {"col_name": "fiscalPeriod", "col_show_name": "会计区间", "col_comment": "会计区间-描述"},
                {"col_name": "mergedFlag", "col_show_name": "合并标志", "col_comment": "合并标志-描述"},
                {"col_name": "accountingStand", "col_show_name": "会计准则", "col_comment": "会计准则-描述"},
                {"col_name": "currencyCD", "col_show_name": "货币代码", "col_comment": "货币代码-描述"},
                {"col_name": "industryCategory", "col_show_name": "行业分类", "col_comment": "行业分类-描述"},
                {"col_name": "nDeposIncrCFI", "col_show_name": "客户存款和同业存放款项净增加额", "col_comment": "客户存款和同业存放款项净增加额-描述"},
                {"col_name": "nIncrBorrFRCB", "col_show_name": "向中央银行借款净增加额", "col_comment": "向中央银行借款净增加额-描述"},
                {"col_name": "premFROrigContr", "col_show_name": "收到原保险合同保费取得的现金", "col_comment": "收到原保险合同保费取得的现金-描述"},
                {"col_name": "nReinsurPrem", "col_show_name": "收到再保险业务现金净额", "col_comment": "收到再保险业务现金净额-描述"},
                {"col_name": "nIncPHDeposInv", "col_show_name": "保户储金及投资款净增加额", "col_comment": "保户储金及投资款净增加额-描述"},
                {"col_name": "ifcCashIncr", "col_show_name": "收取利息、手续费及佣金的现金", "col_comment": "收取利息、手续费及佣金的现金-描述"},
                {"col_name": "refundOFTax", "col_show_name": "收到的税费返还", "col_comment": "收到的税费返还-描述"},
                {"col_name": "cFROthOperateA", "col_show_name": "收到其他与经营活动有关的现金", "col_comment": "收到其他与经营活动有关的现金-描述"},
                {"col_name": "specOCIF", "col_show_name": "经营活动现金流入特殊项目", "col_comment": "经营活动现金流入特殊项目-描述"},
                {"col_name": "AOCIF", "col_show_name": "经营活动现金流入调整金额", "col_comment": "经营活动现金流入调整金额-描述"},
                {"col_name": "cInfFROperateA", "col_show_name": "经营活动现金流入小计", "col_comment": "经营活动现金流入小计-描述"},
                {"col_name": "nIncDisburOFLA", "col_show_name": "客户贷款及垫款净增加额", "col_comment": "客户贷款及垫款净增加额-描述"},
                {"col_name": "netIncrDeposINFI", "col_show_name": "存放中央银行和同业款项净增加额",
                 "col_comment": "存放中央银行和同业款项净增加额-描述"},
                {"col_name": "origContrCIndem", "col_show_name": "支付原保险合同赔付款项的现金", "col_comment": "支付原保险合同赔付款项的现金-描述"},
                {"col_name": "cPaidIFC", "col_show_name": "支付利息、手续费及佣金的现金", "col_comment": "支付利息、手续费及佣金的现金-描述"},
                {"col_name": "cPaidPolDiv", "col_show_name": "支付保单红利的现金", "col_comment": "支付保单红利的现金-描述"},
                {"col_name": "cPaidToForEmpl", "col_show_name": "支付给职工以及为职工支付的现金", "col_comment": "支付给职工以及为职工支付的现金-描述"},
                {"col_name": "cPaidForTaxes", "col_show_name": "支付的各项税费", "col_comment": "支付的各项税费-描述"},
                {"col_name": "cPaidForOthOpA", "col_show_name": "支付其他与经营活动有关的现金", "col_comment": "支付其他与经营活动有关的现金-描述"},
                {"col_name": "specOCOF", "col_show_name": "经营活动现金流出特殊项目", "col_comment": "经营活动现金流出特殊项目-描述"},
                {"col_name": "AOCOF", "col_show_name": "经营活动现金流出调整金额", "col_comment": "经营活动现金流出调整金额-描述"},
                {"col_name": "cOutfOperateA", "col_show_name": "经营活动现金流出小计", "col_comment": "经营活动现金流出小计-描述"},
                {"col_name": "ANOCF", "col_show_name": "经营活动现金流量净额调整金额", "col_comment": "经营活动现金流量净额调整金额-描述"},
                {"col_name": "nCFOperateA", "col_show_name": "经营活动产生的现金流量净额", "col_comment": "经营活动产生的现金流量净额-描述"},
                {"col_name": "procSellInvest", "col_show_name": "收回投资收到的现金", "col_comment": "收回投资收到的现金-描述"},
                {"col_name": "gainInvest", "col_show_name": "取得投资收益收到的现金", "col_comment": "取得投资收益收到的现金-描述"},
                {"col_name": "dispFixAssetsOth", "col_show_name": "处置固定资产、无形资产和其他长期资产收回的现金净额",
                 "col_comment": "处置固定资产、无形资产和其他长期资产收回的现金净额-描述"},
                {"col_name": "nDispSubsOthBIZC", "col_show_name": "处置子公司及其他营业单位收到的现金净额",
                 "col_comment": "处置子公司及其他营业单位收到的现金净额-描述"},
                {"col_name": "cFROthInvestA", "col_show_name": "收到其他与投资活动有关的现金", "col_comment": "收到其他与投资活动有关的现金-描述"},
                {"col_name": "specCIF", "col_show_name": "投资活动现金流入特殊项目", "col_comment": "投资活动现金流入特殊项目-描述"},
                {"col_name": "ACIF", "col_show_name": "投资活动现金流入调整金额", "col_comment": "投资活动现金流入调整金额-描述"},
                {"col_name": "cInfFRInvestA", "col_show_name": "投资活动现金流入小计", "col_comment": "投资活动现金流入小计-描述"},
                {"col_name": "purFixAssetsOth", "col_show_name": "购建固定资产、无形资产和其他长期资产支付的现金",
                 "col_comment": "购建固定资产、无形资产和其他长期资产支付的现金-描述"},
                {"col_name": "cPaidInvest", "col_show_name": "投资支付的现金", "col_comment": "投资支付的现金-描述"},
                {"col_name": "nIncrPledgeLoan", "col_show_name": "质押贷款净增加额", "col_comment": "质押贷款净增加额-描述"},
                {"col_name": "nCPaidAcquis", "col_show_name": "取得子公司及其他营业单位支付的现金净额",
                 "col_comment": "取得子公司及其他营业单位支付的现金净额-描述"},
                {"col_name": "cPaidOthInvestA", "col_show_name": "支付其他与投资活动有关的现金", "col_comment": "支付其他与投资活动有关的现金-描述"},
                {"col_name": "specCOF", "col_show_name": "投资活动现金流出特殊项目", "col_comment": "投资活动现金流出特殊项目-描述"},
                {"col_name": "ACOF", "col_show_name": "投资活动现金流出调整金额", "col_comment": "投资活动现金流出调整金额-描述"},
                {"col_name": "cOutfFRInvestA", "col_show_name": "投资活动现金流出小计", "col_comment": "投资活动现金流出小计-描述"},
                {"col_name": "ANICF", "col_show_name": "投资活动现金流量净额调整金额", "col_comment": "投资活动现金流量净额调整金额-描述"},
                {"col_name": "nCFFRInvestA", "col_show_name": "投资活动产生的现金流量净额", "col_comment": "投资活动产生的现金流量净额-描述"},
                {"col_name": "cFRCapContr", "col_show_name": "吸收投资收到的现金", "col_comment": "吸收投资收到的现金-描述"},
                {"col_name": "cFRMinoSSubs", "col_show_name": "其中:子公司吸收少数股东投资收到的现金",
                 "col_comment": "其中:子公司吸收少数股东投资收到的现金-描述"},
                {"col_name": "cFRBorr", "col_show_name": "取得借款收到的现金", "col_comment": "取得借款收到的现金-描述"},
                {"col_name": "cFRIssueBond", "col_show_name": "发行债券收到的现金", "col_comment": "发行债券收到的现金-描述"},
                {"col_name": "cFROthFinanA", "col_show_name": "收到其他与筹资活动有关的现金", "col_comment": "收到其他与筹资活动有关的现金-描述"},
                {"col_name": "specFCIF", "col_show_name": "筹资活动现金流入特殊项目", "col_comment": "筹资活动现金流入特殊项目-描述"},
                {"col_name": "AFCIF", "col_show_name": "筹资活动现金流入调整金额", "col_comment": "筹资活动现金流入调整金额-描述"},
                {"col_name": "cInfFRFinanA", "col_show_name": "筹资活动现金流入小计", "col_comment": "筹资活动现金流入小计-描述"},
                {"col_name": "cPaidForDebts", "col_show_name": "偿还债务支付的现金", "col_comment": "偿还债务支付的现金-描述"},
                {"col_name": "cPaidDivProfInt", "col_show_name": "分配股利、利润或偿付利息支付的现金",
                 "col_comment": "分配股利、利润或偿付利息支付的现金-描述"},
                {"col_name": "divProfSubsMinoS", "col_show_name": "其中:子公司支付给少数股东的股利、利润",
                 "col_comment": "其中:子公司支付给少数股东的股利、利润-描述"},
                {"col_name": "cPaidOthFinanA", "col_show_name": "支付其他与筹资活动有关的现金", "col_comment": "支付其他与筹资活动有关的现金-描述"},
                {"col_name": "specFCOF", "col_show_name": "筹资活动现金流出特殊项目", "col_comment": "筹资活动现金流出特殊项目-描述"},
                {"col_name": "AFCOF", "col_show_name": "筹资活动现金流出调整金额", "col_comment": "筹资活动现金流出调整金额-描述"},
                {"col_name": "cOutfFRFinanA", "col_show_name": "筹资活动现金流出小计", "col_comment": "筹资活动现金流出小计-描述"},
                {"col_name": "ANFCF", "col_show_name": "筹资活动流量现金净额调整金额", "col_comment": "筹资活动流量现金净额调整金额-描述"},
                {"col_name": "nCFFRFinanA", "col_show_name": "筹资活动产生的现金流量净额", "col_comment": "筹资活动产生的现金流量净额-描述"},
                {"col_name": "forexEffects", "col_show_name": "汇率变动对现金及现金等价物的影响", "col_comment": "汇率变动对现金及现金等价物的影响-描述"},
                {"col_name": "othEffectCE", "col_show_name": "影响现金及现金等价物净增加额的特殊项目",
                 "col_comment": "影响现金及现金等价物净增加额的特殊项目-描述"},
                {"col_name": "ACE", "col_show_name": "影响现金及现金等价物的调整金额", "col_comment": "影响现金及现金等价物的调整金额-描述"},
                {"col_name": "nChangeInCash", "col_show_name": "现金及现金等价物净增加额", "col_comment": "现金及现金等价物净增加额-描述"},
                {"col_name": "nCEBegBal", "col_show_name": "加:期初现金及现金等价物余额", "col_comment": "加:期初现金及现金等价物余额-描述"},
                {"col_name": "othEffectCEI", "col_show_name": "现金及现金等价物净增加额的特殊项目",
                 "col_comment": "现金及现金等价物净增加额的特殊项目-描述"},
                {"col_name": "ACEI", "col_show_name": "现金及现金等价物净增加额的调整金额", "col_comment": "现金及现金等价物净增加额的调整金额-描述"},
                {"col_name": "nCeEndBal", "col_show_name": "期末现金及现金等价物余额", "col_comment": "期末现金及现金等价物余额-描述"}
            ]
        }
    define_json = json.dumps(fdmtcfinsu2018_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def fdmtcfsecu2018_define(table_name):

    fdmtcfsecu2018_str = {
            "table_name": "fdmtcfsecu2018",
            "table_show_name": "(新)证券业现金流量表(PIT)",
            "table_comment": "(新)证券业现金流量表(PIT)-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "partyID", "col_show_name": "机构内部ID", "col_comment": "机构内部ID-描述"},
                {"col_name": "ticker", "col_show_name": "股票代码", "col_comment": "股票代码-描述"},
                {"col_name": "exchangeCD", "col_show_name": "交易市场代码", "col_comment": "交易市场代码-描述"},
                {"col_name": "secID", "col_show_name": "证券编码", "col_comment": "证券编码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "actPubtime", "col_show_name": "实际披露时间", "col_comment": "实际披露时间-描述"},
                {"col_name": "publishDate", "col_show_name": "发布日期", "col_comment": "发布日期-描述"},
                {"col_name": "endDateRep", "col_show_name": "报告截止日期", "col_comment": "报告截止日期-描述"},
                {"col_name": "endDate", "col_show_name": "截止日期", "col_comment": "截止日期-描述"},
                {"col_name": "reportType", "col_show_name": "报告类型", "col_comment": "报告类型-描述"},
                {"col_name": "fiscalPeriod", "col_show_name": "会计区间", "col_comment": "会计区间-描述"},
                {"col_name": "mergedFlag", "col_show_name": "合并标志", "col_comment": "合并标志-描述"},
                {"col_name": "accountingStand", "col_show_name": "会计准则", "col_comment": "会计准则-描述"},
                {"col_name": "currencyCD", "col_show_name": "货币代码", "col_comment": "货币代码-描述"},
                {"col_name": "industryCategory", "col_show_name": "行业分类", "col_comment": "行业分类-描述"},
                {"col_name": "nIncBorrOthFI", "col_show_name": "向其他金融机构拆入资金净增加额", "col_comment": "向其他金融机构拆入资金净增加额-描述"},
                {"col_name": "nIncDispTradFA", "col_show_name": "处置交易性金融资产净增加额", "col_comment": "处置交易性金融资产净增加额-描述"},
                {"col_name": "nIncDispFAFS", "col_show_name": "处置可供出售金融资产净增加额", "col_comment": "处置可供出售金融资产净增加额-描述"},
                {"col_name": "ifcCashIncr", "col_show_name": "收取利息、手续费及佣金的现金", "col_comment": "收取利息、手续费及佣金的现金-描述"},
                {"col_name": "nIncFRBorr", "col_show_name": "拆入资金净增加额", "col_comment": "拆入资金净增加额-描述"},
                {"col_name": "nCAPIncrRepur", "col_show_name": "回购业务资金净增加额", "col_comment": "回购业务资金净增加额-描述"},
                {"col_name": "reFundOfTax", "col_show_name": "收到的税费返还", "col_comment": "收到的税费返还-描述"},
                {"col_name": "cFROthOperateA", "col_show_name": "收到其他与经营活动有关的现金", "col_comment": "收到其他与经营活动有关的现金-描述"},
                {"col_name": "specOCIF", "col_show_name": "经营活动现金流入特殊项目", "col_comment": "经营活动现金流入特殊项目-描述"},
                {"col_name": "AOCIF", "col_show_name": "经营活动现金流入调整金额", "col_comment": "经营活动现金流入调整金额-描述"},
                {"col_name": "cInfFROperateA", "col_show_name": "经营活动现金流入小计", "col_comment": "经营活动现金流入小计-描述"},
                {"col_name": "cPaidIFC", "col_show_name": "支付利息、手续费及佣金的现金", "col_comment": "支付利息、手续费及佣金的现金-描述"},
                {"col_name": "cPaidToForEmpl", "col_show_name": "支付给职工以及为职工支付的现金", "col_comment": "支付给职工以及为职工支付的现金-描述"},
                {"col_name": "cPaidForTaxes", "col_show_name": "支付的各项税费", "col_comment": "支付的各项税费-描述"},
                {"col_name": "cPaidForOthOpA", "col_show_name": "支付其他与经营活动有关的现金", "col_comment": "支付其他与经营活动有关的现金-描述"},
                {"col_name": "specOCOF", "col_show_name": "经营活动现金流出特殊项目", "col_comment": "经营活动现金流出特殊项目-描述"},
                {"col_name": "AOCOF", "col_show_name": "经营活动现金流出调整金额", "col_comment": "经营活动现金流出调整金额-描述"},
                {"col_name": "cOutfOperateA", "col_show_name": "经营活动现金流出小计", "col_comment": "经营活动现金流出小计-描述"},
                {"col_name": "ANOCF", "col_show_name": "经营活动现金流量净额调整金额", "col_comment": "经营活动现金流量净额调整金额-描述"},
                {"col_name": "nCFOperateA", "col_show_name": "经营活动产生的现金流量净额", "col_comment": "经营活动产生的现金流量净额-描述"},
                {"col_name": "procSellInvest", "col_show_name": "收回投资收到的现金", "col_comment": "收回投资收到的现金-描述"},
                {"col_name": "gainInvest", "col_show_name": "取得投资收益收到的现金", "col_comment": "取得投资收益收到的现金-描述"},
                {"col_name": "dispFixAssetsOth", "col_show_name": "处置固定资产、无形资产和其他长期资产收回的现金净额",
                 "col_comment": "处置固定资产、无形资产和其他长期资产收回的现金净额-描述"},
                {"col_name": "nDispSubsOthBIZC", "col_show_name": "处置子公司及其他营业单位收到的现金净额",
                 "col_comment": "处置子公司及其他营业单位收到的现金净额-描述"},
                {"col_name": "cFROthInvestA", "col_show_name": "收到其他与投资活动有关的现金", "col_comment": "收到其他与投资活动有关的现金-描述"},
                {"col_name": "specCIF", "col_show_name": "投资活动现金流入特殊项目", "col_comment": "投资活动现金流入特殊项目-描述"},
                {"col_name": "ACIF", "col_show_name": "投资活动现金流入调整金额", "col_comment": "投资活动现金流入调整金额-描述"},
                {"col_name": "cInfFRInvestA", "col_show_name": "投资活动现金流入小计", "col_comment": "投资活动现金流入小计-描述"},
                {"col_name": "purFixAssetsOth", "col_show_name": "购建固定资产、无形资产和其他长期资产支付的现金",
                 "col_comment": "购建固定资产、无形资产和其他长期资产支付的现金-描述"},
                {"col_name": "cPaidInvest", "col_show_name": "投资支付的现金", "col_comment": "投资支付的现金-描述"},
                {"col_name": "nCPaidAcquis", "col_show_name": "取得子公司及其他营业单位支付的现金净额",
                 "col_comment": "取得子公司及其他营业单位支付的现金净额-描述"},
                {"col_name": "cPaidOthInvestA", "col_show_name": "支付其他与投资活动有关的现金", "col_comment": "支付其他与投资活动有关的现金-描述"},
                {"col_name": "specCOF", "col_show_name": "投资活动现金流出特殊项目", "col_comment": "投资活动现金流出特殊项目-描述"},
                {"col_name": "ACOF", "col_show_name": "投资活动现金流出调整金额", "col_comment": "投资活动现金流出调整金额-描述"},
                {"col_name": "cOutfFRInvestA", "col_show_name": "投资活动现金流出小计", "col_comment": "投资活动现金流出小计-描述"},
                {"col_name": "ANICF", "col_show_name": "投资活动现金流量净额调整金额", "col_comment": "投资活动现金流量净额调整金额-描述"},
                {"col_name": "nCFFRInvestA", "col_show_name": "投资活动产生的现金流量净额", "col_comment": "投资活动产生的现金流量净额-描述"},
                {"col_name": "cFRCapContr", "col_show_name": "吸收投资收到的现金", "col_comment": "吸收投资收到的现金-描述"},
                {"col_name": "cFRMinoSSubs", "col_show_name": "其中:子公司吸收少数股东投资收到的现金",
                 "col_comment": "其中:子公司吸收少数股东投资收到的现金-描述"},
                {"col_name": "cFRBorr", "col_show_name": "取得借款收到的现金", "col_comment": "取得借款收到的现金-描述"},
                {"col_name": "cFRIssueBond", "col_show_name": "发行债券收到的现金", "col_comment": "发行债券收到的现金-描述"},
                {"col_name": "cFROthFinanA", "col_show_name": "收到其他与筹资活动有关的现金", "col_comment": "收到其他与筹资活动有关的现金-描述"},
                {"col_name": "specFCIF", "col_show_name": "筹资活动现金流入特殊项目", "col_comment": "筹资活动现金流入特殊项目-描述"},
                {"col_name": "AFCIF", "col_show_name": "筹资活动现金流入调整金额", "col_comment": "筹资活动现金流入调整金额-描述"},
                {"col_name": "cINFFRFinanA", "col_show_name": "筹资活动现金流入小计", "col_comment": "筹资活动现金流入小计-描述"},
                {"col_name": "cPaidForDebts", "col_show_name": "偿还债务支付的现金", "col_comment": "偿还债务支付的现金-描述"},
                {"col_name": "cPaidDivProfInt", "col_show_name": "分配股利、利润或偿付利息支付的现金",
                 "col_comment": "分配股利、利润或偿付利息支付的现金-描述"},
                {"col_name": "divProfSubsMinoS", "col_show_name": "其中:子公司支付给少数股东的股利、利润",
                 "col_comment": "其中:子公司支付给少数股东的股利、利润-描述"},
                {"col_name": "cPaidOthFinanA", "col_show_name": "支付其他与筹资活动有关的现金", "col_comment": "支付其他与筹资活动有关的现金-描述"},
                {"col_name": "specFCOF", "col_show_name": "筹资活动现金流出特殊项目", "col_comment": "筹资活动现金流出特殊项目-描述"},
                {"col_name": "AFCOF", "col_show_name": "筹资活动现金流出调整金额", "col_comment": "筹资活动现金流出调整金额-描述"},
                {"col_name": "cOutfFRFinanA", "col_show_name": "筹资活动现金流出小计", "col_comment": "筹资活动现金流出小计-描述"},
                {"col_name": "ANFCF", "col_show_name": "筹资活动流量现金净额调整金额", "col_comment": "筹资活动流量现金净额调整金额-描述"},
                {"col_name": "nCFFRFinanA", "col_show_name": "筹资活动产生的现金流量净额", "col_comment": "筹资活动产生的现金流量净额-描述"},
                {"col_name": "forexEffects", "col_show_name": "汇率变动对现金及现金等价物的影响", "col_comment": "汇率变动对现金及现金等价物的影响-描述"},
                {"col_name": "othEffectCE", "col_show_name": "影响现金及现金等价物净增加额的特殊项目",
                 "col_comment": "影响现金及现金等价物净增加额的特殊项目-描述"},
                {"col_name": "ACE", "col_show_name": "影响现金及现金等价物的调整金额", "col_comment": "影响现金及现金等价物的调整金额-描述"},
                {"col_name": "nChangeInCash", "col_show_name": "现金及现金等价物净增加额", "col_comment": "现金及现金等价物净增加额-描述"},
                {"col_name": "nCEBegBal", "col_show_name": "加:期初现金及现金等价物余额", "col_comment": "加:期初现金及现金等价物余额-描述"},
                {"col_name": "othEffectCEI", "col_show_name": "现金及现金等价物净增加额的特殊项目",
                 "col_comment": "现金及现金等价物净增加额的特殊项目-描述"},
                {"col_name": "ACEI", "col_show_name": "现金及现金等价物净增加额的调整金额", "col_comment": "现金及现金等价物净增加额的调整金额-描述"},
                {"col_name": "nCEEndBal", "col_show_name": "期末现金及现金等价物余额", "col_comment": "期末现金及现金等价物余额-描述"}
            ]
        }
    define_json = json.dumps(fdmtcfsecu2018_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def fdmtcfbank_define(table_name):

    fdmtcfbank_str = {
            "table_name": "fdmtcfbank",
            "table_show_name": "银行业现金流量表(PIT)",
            "table_comment": "银行业现金流量表(PIT)-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "证券内部ID", "col_comment": "证券内部ID-描述"},
                {"col_name": "publishDate", "col_show_name": "发布日期", "col_comment": "发布日期-描述"},
                {"col_name": "endDate", "col_show_name": "截止日期", "col_comment": "截止日期-描述"},
                {"col_name": "endDateRep", "col_show_name": "报表截止日期", "col_comment": "报表截止日期-描述"},
                {"col_name": "partyID", "col_show_name": "机构内部ID", "col_comment": "机构内部ID-描述"},
                {"col_name": "ticker", "col_show_name": "股票代码", "col_comment": "股票代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD",
                 "col_show_name": "通联编制的证券市场编码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所等。对应DataAPI.SysCodeGet.codeTypeID=10002。",
                 "col_comment": "通联编制的证券市场编码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所等。对应DataAPI.SysCodeGet.codeTypeID=10002。-描述"},
                {"col_name": "actPubtime", "col_show_name": "实际披露时间", "col_comment": "实际披露时间-描述"},
                {"col_name": "mergedFlag", "col_show_name": "合并类型。1-合并,2-母公司。对应DataAPI.SysCodeGet.codeTypeID=70003。",
                 "col_comment": "合并类型。1-合并,2-母公司。对应DataAPI.SysCodeGet.codeTypeID=70003。-描述"},
                {"col_name": "reportType",
                 "col_show_name": "报告类型。Q1-第一季报，S1-半年报，Q3-第三季报，CQ3-三季报（累计1-9月），A-年报。对应DataAPI.SysCodeGet.codeTypeID=70001。",
                 "col_comment": "报告类型。Q1-第一季报，S1-半年报，Q3-第三季报，CQ3-三季报（累计1-9月），A-年报。对应DataAPI.SysCodeGet.codeTypeID=70001。-描述"},
                {"col_name": "fiscalPeriod", "col_show_name": "会计期间", "col_comment": "会计期间-描述"},
                {"col_name": "accoutingStandards", "col_show_name": "会计准则", "col_comment": "会计准则-描述"},
                {"col_name": "currencyCD",
                 "col_show_name": "货币代码。例如，USD-美元；CAD-加元等。对应DataAPI.SysCodeGet.codeTypeID=10004。",
                 "col_comment": "货币代码。例如，USD-美元；CAD-加元等。对应DataAPI.SysCodeGet.codeTypeID=10004。-描述"},
                {"col_name": "NDeposIncrCFI", "col_show_name": "客户存款和同业存放款项净增加额", "col_comment": "客户存款和同业存放款项净增加额-描述"},
                {"col_name": "NIncrBorrFrCB", "col_show_name": "向中央银行借款净增加额", "col_comment": "向中央银行借款净增加额-描述"},
                {"col_name": "NIncBorrOthFI", "col_show_name": "向其他金融机构拆入资金净增加额", "col_comment": "向其他金融机构拆入资金净增加额-描述"},
                {"col_name": "NDecrInDisburOfLa", "col_show_name": "发放贷款及垫款净减少额", "col_comment": "发放贷款及垫款净减少额-描述"},
                {"col_name": "NDecrInDeposInFI", "col_show_name": "存放中央银行和同业款项净减少额",
                 "col_comment": "存放中央银行和同业款项净减少额-描述"},
                {"col_name": "NDecrLoanToOthFI", "col_show_name": "向其他金融机构拆出资金净减少额",
                 "col_comment": "向其他金融机构拆出资金净减少额-描述"},
                {"col_name": "IFCCashIncr", "col_show_name": "收取利息、手续费及佣金的现金", "col_comment": "收取利息、手续费及佣金的现金-描述"},
                {"col_name": "CFrOthOperateA", "col_show_name": "收到其他与经营活动有关的现金", "col_comment": "收到其他与经营活动有关的现金-描述"},
                {"col_name": "specOCIF", "col_show_name": "经营活动流入特殊项目", "col_comment": "经营活动流入特殊项目-描述"},
                {"col_name": "AOCIF", "col_show_name": "经营活动流入调整金额", "col_comment": "经营活动流入调整金额-描述"},
                {"col_name": "CInfFrOperateA", "col_show_name": "经营活动现金流入小计", "col_comment": "经营活动现金流入小计-描述"},
                {"col_name": "NDeposDecrFrFI", "col_show_name": "客户存款和同业存放款项净减少额", "col_comment": "客户存款和同业存放款项净减少额-描述"},
                {"col_name": "NDecrBorrFrCB", "col_show_name": "向中央银行借款净减少额", "col_comment": "向中央银行借款净减少额-描述"},
                {"col_name": "NDecrBorrFrOthFI", "col_show_name": "向其他金融机构拆入资金净减少额",
                 "col_comment": "向其他金融机构拆入资金净减少额-描述"},
                {"col_name": "NIncDisburOfLA", "col_show_name": "客户贷款及垫款净增加额", "col_comment": "客户贷款及垫款净增加额-描述"},
                {"col_name": "NIncrDeposInFI", "col_show_name": "存放中央银行和同业款项净增加额", "col_comment": "存放中央银行和同业款项净增加额-描述"},
                {"col_name": "NIncrLoansToOthFi", "col_show_name": "向其他金融机构拆出资金净增加额",
                 "col_comment": "向其他金融机构拆出资金净增加额-描述"},
                {"col_name": "CPaidIFC", "col_show_name": "支付利息、手续费及佣金的现金", "col_comment": "支付利息、手续费及佣金的现金-描述"},
                {"col_name": "CPaidToForEmpl", "col_show_name": "支付给职工以及为职工支付的现金", "col_comment": "支付给职工以及为职工支付的现金-描述"},
                {"col_name": "CPaidForTaxes", "col_show_name": "支付的各项税费", "col_comment": "支付的各项税费-描述"},
                {"col_name": "CPaidForOthOpA", "col_show_name": "支付其他与经营活动有关的现金", "col_comment": "支付其他与经营活动有关的现金-描述"},
                {"col_name": "specOCOF", "col_show_name": "经营活动流出特殊项目", "col_comment": "经营活动流出特殊项目-描述"},
                {"col_name": "AOCOF", "col_show_name": "经营活动流出调整金额", "col_comment": "经营活动流出调整金额-描述"},
                {"col_name": "COutfOperateA", "col_show_name": "经营活动现金流出小计", "col_comment": "经营活动现金流出小计-描述"},
                {"col_name": "ANOCF", "col_show_name": "经营活动现金流量净额的调整金额", "col_comment": "经营活动现金流量净额的调整金额-描述"},
                {"col_name": "NCFOperateA", "col_show_name": "经营活动产生的现金流量净额", "col_comment": "经营活动产生的现金流量净额-描述"},
                {"col_name": "procSellInvest", "col_show_name": "收回投资收到的现金", "col_comment": "收回投资收到的现金-描述"},
                {"col_name": "gainInvest", "col_show_name": "取得投资收益收到的现金", "col_comment": "取得投资收益收到的现金-描述"},
                {"col_name": "dispFixAssetsOth", "col_show_name": "处置固定资产、无形资产和其他长期资产收回的现金净额",
                 "col_comment": "处置固定资产、无形资产和其他长期资产收回的现金净额-描述"},
                {"col_name": "NDispSubsOthBizC", "col_show_name": "处置子公司及其他营业单位收到的现金净额",
                 "col_comment": "处置子公司及其他营业单位收到的现金净额-描述"},
                {"col_name": "CFrOthInvestA", "col_show_name": "收到其他与投资活动有关的现金", "col_comment": "收到其他与投资活动有关的现金-描述"},
                {"col_name": "specICIF", "col_show_name": "投资活动流入特殊项目", "col_comment": "投资活动流入特殊项目-描述"},
                {"col_name": "AICIF", "col_show_name": "投资活动流入调整金额", "col_comment": "投资活动流入调整金额-描述"},
                {"col_name": "CInfFrInvestA", "col_show_name": "投资活动现金流入小计", "col_comment": "投资活动现金流入小计-描述"},
                {"col_name": "purFixAssetsOth", "col_show_name": "购建固定资产、无形资产和其他长期资产支付的现金",
                 "col_comment": "购建固定资产、无形资产和其他长期资产支付的现金-描述"},
                {"col_name": "CPaidInvest", "col_show_name": "投资支付的现金", "col_comment": "投资支付的现金-描述"},
                {"col_name": "NCPaidAcquis", "col_show_name": "取得子公司及其他营业单位支付的现金净额",
                 "col_comment": "取得子公司及其他营业单位支付的现金净额-描述"},
                {"col_name": "CPaidOthInvestA", "col_show_name": "支付其他与投资活动有关的现金", "col_comment": "支付其他与投资活动有关的现金-描述"},
                {"col_name": "specICOF", "col_show_name": "投资活动流出特殊项目", "col_comment": "投资活动流出特殊项目-描述"},
                {"col_name": "AICOF", "col_show_name": "投资活动流出调整金额", "col_comment": "投资活动流出调整金额-描述"},
                {"col_name": "COutfFrInvestA", "col_show_name": "投资活动现金流出小计", "col_comment": "投资活动现金流出小计-描述"},
                {"col_name": "ANICF", "col_show_name": "投资活动现金流量净额的调整金额", "col_comment": "投资活动现金流量净额的调整金额-描述"},
                {"col_name": "NCFFrInvestA", "col_show_name": "投资活动产生的现金流量净额", "col_comment": "投资活动产生的现金流量净额-描述"},
                {"col_name": "CFrCapContr", "col_show_name": "吸收投资收到的现金", "col_comment": "吸收投资收到的现金-描述"},
                {"col_name": "CFrMinoSSubs", "col_show_name": "其中:子公司吸收少数股东投资收到的现金",
                 "col_comment": "其中:子公司吸收少数股东投资收到的现金-描述"},
                {"col_name": "CFrIssueBond", "col_show_name": "发行债券收到的现金", "col_comment": "发行债券收到的现金-描述"},
                {"col_name": "CFrOthFinanA", "col_show_name": "收到其他与筹资活动有关的现金", "col_comment": "收到其他与筹资活动有关的现金-描述"},
                {"col_name": "specFCIF", "col_show_name": "筹资活动流入特殊项目", "col_comment": "筹资活动流入特殊项目-描述"},
                {"col_name": "AFCIF", "col_show_name": "筹资活动流入调整金额", "col_comment": "筹资活动流入调整金额-描述"},
                {"col_name": "CInfFrFinanA", "col_show_name": "筹资活动现金流入小计", "col_comment": "筹资活动现金流入小计-描述"},
                {"col_name": "CPaidForDebts", "col_show_name": "偿还债务支付的现金", "col_comment": "偿还债务支付的现金-描述"},
                {"col_name": "CPaidDivProfInt", "col_show_name": "分配股利、利润或偿付利息支付的现金",
                 "col_comment": "分配股利、利润或偿付利息支付的现金-描述"},
                {"col_name": "divProfSubsMinoS", "col_show_name": "其中:子公司支付给少数股东的股利、利润",
                 "col_comment": "其中:子公司支付给少数股东的股利、利润-描述"},
                {"col_name": "CPaidOthFinanA", "col_show_name": "支付其他与筹资活动有关的现金", "col_comment": "支付其他与筹资活动有关的现金-描述"},
                {"col_name": "specFCOF", "col_show_name": "筹资活动流出特殊项目", "col_comment": "筹资活动流出特殊项目-描述"},
                {"col_name": "AFCOF", "col_show_name": "筹资活动流出调整金额", "col_comment": "筹资活动流出调整金额-描述"},
                {"col_name": "COutfFrFinanA", "col_show_name": "筹资活动现金流出小计", "col_comment": "筹资活动现金流出小计-描述"},
                {"col_name": "ANFCF", "col_show_name": "筹资活动现金流量净额的调整金额", "col_comment": "筹资活动现金流量净额的调整金额-描述"},
                {"col_name": "NCFFrFinanA", "col_show_name": "筹资活动产生的现金流量净额", "col_comment": "筹资活动产生的现金流量净额-描述"},
                {"col_name": "forexEffects", "col_show_name": "汇率变动对现金及现金等价物的影响", "col_comment": "汇率变动对现金及现金等价物的影响-描述"},
                {"col_name": "othEffectCE", "col_show_name": "影响现金及现金等价物净增加额的特殊项目",
                 "col_comment": "影响现金及现金等价物净增加额的特殊项目-描述"},
                {"col_name": "ACE", "col_show_name": "影响现金及现金等价物净增加额的调整金额", "col_comment": "影响现金及现金等价物净增加额的调整金额-描述"},
                {"col_name": "NChangeInCash", "col_show_name": "现金及现金等价物净增加额", "col_comment": "现金及现金等价物净增加额-描述"},
                {"col_name": "NCEBegBal", "col_show_name": "加:期初现金及现金等价物余额", "col_comment": "加:期初现金及现金等价物余额-描述"},
                {"col_name": "othEffectCEI", "col_show_name": "影响期末现金及现金等价物余额的特殊项目",
                 "col_comment": "影响期末现金及现金等价物余额的特殊项目-描述"},
                {"col_name": "ACEI", "col_show_name": "影响期末现金及现金等价物余额的调整金额", "col_comment": "影响期末现金及现金等价物余额的调整金额-描述"},
                {"col_name": "NCEEndBal", "col_show_name": "期末现金及现金等价物余额", "col_comment": "期末现金及现金等价物余额-描述"},
                {"col_name": "updateTime", "col_show_name": "更新时间", "col_comment": "更新时间-描述"}
            ]
        }
    define_json = json.dumps(fdmtcfbank_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def fdmtcfindu_define(table_name):

    fdmtcfindu_str = {
            "table_name": "fdmtcfindu",
            "table_show_name": "一般工商业现金流量表(PIT)",
            "table_comment": "一般工商业现金流量表(PIT)-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "证券内部ID", "col_comment": "证券内部ID-描述"},
                {"col_name": "publishDate", "col_show_name": "发布日期", "col_comment": "发布日期-描述"},
                {"col_name": "endDate", "col_show_name": "截止日期", "col_comment": "截止日期-描述"},
                {"col_name": "endDateRep", "col_show_name": "报表截止日期", "col_comment": "报表截止日期-描述"},
                {"col_name": "partyID", "col_show_name": "机构内部ID", "col_comment": "机构内部ID-描述"},
                {"col_name": "ticker", "col_show_name": "股票代码", "col_comment": "股票代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD",
                 "col_show_name": "通联编制的证券市场编码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所等。对应DataAPI.SysCodeGet.codeTypeID=10002。",
                 "col_comment": "通联编制的证券市场编码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所等。对应DataAPI.SysCodeGet.codeTypeID=10002。-描述"},
                {"col_name": "actPubtime", "col_show_name": "实际披露时间", "col_comment": "实际披露时间-描述"},
                {"col_name": "mergedFlag", "col_show_name": "合并类型。1-合并,2-母公司。对应DataAPI.SysCodeGet.codeTypeID=70003。",
                 "col_comment": "合并类型。1-合并,2-母公司。对应DataAPI.SysCodeGet.codeTypeID=70003。-描述"},
                {"col_name": "reportType",
                 "col_show_name": "报告类型。Q1-第一季报，S1-半年报，Q3-第三季报，CQ3-三季报（累计1-9月），A-年报。对应DataAPI.SysCodeGet.codeTypeID=70001。",
                 "col_comment": "报告类型。Q1-第一季报，S1-半年报，Q3-第三季报，CQ3-三季报（累计1-9月），A-年报。对应DataAPI.SysCodeGet.codeTypeID=70001。-描述"},
                {"col_name": "fiscalPeriod", "col_show_name": "会计期间", "col_comment": "会计期间-描述"},
                {"col_name": "accoutingStandards", "col_show_name": "会计准则", "col_comment": "会计准则-描述"},
                {"col_name": "currencyCD",
                 "col_show_name": "货币代码。例如，USD-美元；CAD-加元等。对应DataAPI.SysCodeGet.codeTypeID=10004。",
                 "col_comment": "货币代码。例如，USD-美元；CAD-加元等。对应DataAPI.SysCodeGet.codeTypeID=10004。-描述"},
                {"col_name": "CFrSaleGS", "col_show_name": "销售商品、提供劳务收到的现金", "col_comment": "销售商品、提供劳务收到的现金-描述"},
                {"col_name": "NDeposIncrCFI", "col_show_name": "客户存款和同业存放款项净增加额", "col_comment": "客户存款和同业存放款项净增加额-描述"},
                {"col_name": "NIncrBorrFrCB", "col_show_name": "向中央银行借款净增加额", "col_comment": "向中央银行借款净增加额-描述"},
                {"col_name": "NIncBorrOthFI", "col_show_name": "向其他金融机构拆入资金净增加额", "col_comment": "向其他金融机构拆入资金净增加额-描述"},
                {"col_name": "premFrOrigContr", "col_show_name": "收到原保险合同保费取得的现金", "col_comment": "收到原保险合同保费取得的现金-描述"},
                {"col_name": "NReinsurPrem", "col_show_name": "收到再保险业务现金净额", "col_comment": "收到再保险业务现金净额-描述"},
                {"col_name": "NIncPhDeposInv", "col_show_name": "保户储金及投资款净增加额", "col_comment": "保户储金及投资款净增加额-描述"},
                {"col_name": "NIncDispTradFA", "col_show_name": "处置交易性金融资产净增加额", "col_comment": "处置交易性金融资产净增加额-描述"},
                {"col_name": "IFCCashIncr", "col_show_name": "收取利息、手续费及佣金的现金", "col_comment": "收取利息、手续费及佣金的现金-描述"},
                {"col_name": "NIncFrBorr", "col_show_name": "拆入资金净增加额", "col_comment": "拆入资金净增加额-描述"},
                {"col_name": "NCApIncrRepur", "col_show_name": "回购业务资金净增加额", "col_comment": "回购业务资金净增加额-描述"},
                {"col_name": "refundOfTax", "col_show_name": "收到的税费返还", "col_comment": "收到的税费返还-描述"},
                {"col_name": "CFrOthOperateA", "col_show_name": "收到其他与经营活动有关的现金", "col_comment": "收到其他与经营活动有关的现金-描述"},
                {"col_name": "specOCIF", "col_show_name": "经营活动流入特殊项目", "col_comment": "经营活动流入特殊项目-描述"},
                {"col_name": "AOCIF", "col_show_name": "经营活动流入调整金额", "col_comment": "经营活动流入调整金额-描述"},
                {"col_name": "CInfFrOperateA", "col_show_name": "经营活动现金流入小计", "col_comment": "经营活动现金流入小计-描述"},
                {"col_name": "CPaidGS", "col_show_name": "购买商品、接受劳务支付的现金", "col_comment": "购买商品、接受劳务支付的现金-描述"},
                {"col_name": "NIncDisburOfLA", "col_show_name": "客户贷款及垫款净增加额", "col_comment": "客户贷款及垫款净增加额-描述"},
                {"col_name": "NIncrDeposInFI", "col_show_name": "存放中央银行和同业款项净增加额", "col_comment": "存放中央银行和同业款项净增加额-描述"},
                {"col_name": "origContrCIndem", "col_show_name": "支付原保险合同赔付款项的现金", "col_comment": "支付原保险合同赔付款项的现金-描述"},
                {"col_name": "CPaidIFC", "col_show_name": "支付利息、手续费及佣金的现金", "col_comment": "支付利息、手续费及佣金的现金-描述"},
                {"col_name": "CPaidPolDiv", "col_show_name": "支付保单红利的现金", "col_comment": "支付保单红利的现金-描述"},
                {"col_name": "CPaidToForEmpl", "col_show_name": "支付给职工以及为职工支付的现金", "col_comment": "支付给职工以及为职工支付的现金-描述"},
                {"col_name": "CPaidForTaxes", "col_show_name": "支付的各项税费", "col_comment": "支付的各项税费-描述"},
                {"col_name": "CPaidForOthOpA", "col_show_name": "支付其他与经营活动有关的现金", "col_comment": "支付其他与经营活动有关的现金-描述"},
                {"col_name": "specOCOF", "col_show_name": "经营活动流出特殊项目", "col_comment": "经营活动流出特殊项目-描述"},
                {"col_name": "AOCOF", "col_show_name": "经营活动流出调整金额", "col_comment": "经营活动流出调整金额-描述"},
                {"col_name": "COutfOperateA", "col_show_name": "经营活动现金流出小计", "col_comment": "经营活动现金流出小计-描述"},
                {"col_name": "ANOCF", "col_show_name": "经营活动现金流量净额的调整金额", "col_comment": "经营活动现金流量净额的调整金额-描述"},
                {"col_name": "NCFOperateA", "col_show_name": "经营活动产生的现金流量净额", "col_comment": "经营活动产生的现金流量净额-描述"},
                {"col_name": "procSellInvest", "col_show_name": "收回投资收到的现金", "col_comment": "收回投资收到的现金-描述"},
                {"col_name": "gainInvest", "col_show_name": "取得投资收益收到的现金", "col_comment": "取得投资收益收到的现金-描述"},
                {"col_name": "dispFixAssetsOth", "col_show_name": "处置固定资产、无形资产和其他长期资产收回的现金净额",
                 "col_comment": "处置固定资产、无形资产和其他长期资产收回的现金净额-描述"},
                {"col_name": "NDispSubsOthBizC", "col_show_name": "处置子公司及其他营业单位收到的现金净额",
                 "col_comment": "处置子公司及其他营业单位收到的现金净额-描述"},
                {"col_name": "CFrOthInvestA", "col_show_name": "收到其他与投资活动有关的现金", "col_comment": "收到其他与投资活动有关的现金-描述"},
                {"col_name": "specICIF", "col_show_name": "投资活动流入特殊项目", "col_comment": "投资活动流入特殊项目-描述"},
                {"col_name": "AICIF", "col_show_name": "投资活动流入调整金额", "col_comment": "投资活动流入调整金额-描述"},
                {"col_name": "CInfFrInvestA", "col_show_name": "投资活动现金流入小计", "col_comment": "投资活动现金流入小计-描述"},
                {"col_name": "purFixAssetsOth", "col_show_name": "购建固定资产、无形资产和其他长期资产支付的现金",
                 "col_comment": "购建固定资产、无形资产和其他长期资产支付的现金-描述"},
                {"col_name": "CPaidInvest", "col_show_name": "投资支付的现金", "col_comment": "投资支付的现金-描述"},
                {"col_name": "NIncrPledgeLoan", "col_show_name": "质押贷款净增加额", "col_comment": "质押贷款净增加额-描述"},
                {"col_name": "NCPaidAcquis", "col_show_name": "取得子公司及其他营业单位支付的现金净额",
                 "col_comment": "取得子公司及其他营业单位支付的现金净额-描述"},
                {"col_name": "CPaidOthInvestA", "col_show_name": "支付其他与投资活动有关的现金", "col_comment": "支付其他与投资活动有关的现金-描述"},
                {"col_name": "specICOF", "col_show_name": "投资活动流出特殊项目", "col_comment": "投资活动流出特殊项目-描述"},
                {"col_name": "AICOF", "col_show_name": "投资活动流出调整金额", "col_comment": "投资活动流出调整金额-描述"},
                {"col_name": "COutfFrInvestA", "col_show_name": "投资活动现金流出小计", "col_comment": "投资活动现金流出小计-描述"},
                {"col_name": "ANICF", "col_show_name": "投资活动现金流量净额的调整金额", "col_comment": "投资活动现金流量净额的调整金额-描述"},
                {"col_name": "NCFFrInvestA", "col_show_name": "投资活动产生的现金流量净额", "col_comment": "投资活动产生的现金流量净额-描述"},
                {"col_name": "CFrCapContr", "col_show_name": "吸收投资收到的现金", "col_comment": "吸收投资收到的现金-描述"},
                {"col_name": "CFrMinoSSubs", "col_show_name": "其中:子公司吸收少数股东投资收到的现金",
                 "col_comment": "其中:子公司吸收少数股东投资收到的现金-描述"},
                {"col_name": "CFrBorr", "col_show_name": "取得借款收到的现金", "col_comment": "取得借款收到的现金-描述"},
                {"col_name": "CFrIssueBond", "col_show_name": "发行债券收到的现金", "col_comment": "发行债券收到的现金-描述"},
                {"col_name": "CFrOthFinanA", "col_show_name": "收到其他与筹资活动有关的现金", "col_comment": "收到其他与筹资活动有关的现金-描述"},
                {"col_name": "specFCIF", "col_show_name": "筹资活动流入特殊项目", "col_comment": "筹资活动流入特殊项目-描述"},
                {"col_name": "AFCIF", "col_show_name": "筹资活动流入调整金额", "col_comment": "筹资活动流入调整金额-描述"},
                {"col_name": "CInfFrFinanA", "col_show_name": "筹资活动现金流入小计", "col_comment": "筹资活动现金流入小计-描述"},
                {"col_name": "CPaidForDebts", "col_show_name": "偿还债务支付的现金", "col_comment": "偿还债务支付的现金-描述"},
                {"col_name": "CPaidDivProfInt", "col_show_name": "分配股利、利润或偿付利息支付的现金",
                 "col_comment": "分配股利、利润或偿付利息支付的现金-描述"},
                {"col_name": "divProfSubsMinoS", "col_show_name": "其中:子公司支付给少数股东的股利、利润",
                 "col_comment": "其中:子公司支付给少数股东的股利、利润-描述"},
                {"col_name": "CPaidOthFinanA", "col_show_name": "支付其他与筹资活动有关的现金", "col_comment": "支付其他与筹资活动有关的现金-描述"},
                {"col_name": "specFCOF", "col_show_name": "筹资活动流出特殊项目", "col_comment": "筹资活动流出特殊项目-描述"},
                {"col_name": "AFCOF", "col_show_name": "筹资活动流出调整金额", "col_comment": "筹资活动流出调整金额-描述"},
                {"col_name": "COutfFrFinanA", "col_show_name": "筹资活动现金流出小计", "col_comment": "筹资活动现金流出小计-描述"},
                {"col_name": "ANFCF", "col_show_name": "筹资活动现金流量净额的调整金额", "col_comment": "筹资活动现金流量净额的调整金额-描述"},
                {"col_name": "NCFFrFinanA", "col_show_name": "筹资活动产生的现金流量净额", "col_comment": "筹资活动产生的现金流量净额-描述"},
                {"col_name": "forexEffects", "col_show_name": "汇率变动对现金及现金等价物的影响", "col_comment": "汇率变动对现金及现金等价物的影响-描述"},
                {"col_name": "othEffectCE", "col_show_name": "影响现金及现金等价物净增加额的特殊项目",
                 "col_comment": "影响现金及现金等价物净增加额的特殊项目-描述"},
                {"col_name": "ACE", "col_show_name": "影响现金及现金等价物净增加额的调整金额", "col_comment": "影响现金及现金等价物净增加额的调整金额-描述"},
                {"col_name": "NChangeInCash", "col_show_name": "现金及现金等价物净增加额", "col_comment": "现金及现金等价物净增加额-描述"},
                {"col_name": "NCEBegBal", "col_show_name": "加:期初现金及现金等价物余额", "col_comment": "加:期初现金及现金等价物余额-描述"},
                {"col_name": "othEffectCEI", "col_show_name": "影响期末现金及现金等价物余额的特殊项目",
                 "col_comment": "影响期末现金及现金等价物余额的特殊项目-描述"},
                {"col_name": "ACEI", "col_show_name": "影响期末现金及现金等价物余额的调整金额", "col_comment": "影响期末现金及现金等价物余额的调整金额-描述"},
                {"col_name": "NCEEndBal", "col_show_name": "期末现金及现金等价物余额", "col_comment": "期末现金及现金等价物余额-描述"},
                {"col_name": "updateTime", "col_show_name": "更新时间", "col_comment": "更新时间-描述"}
            ]
        }
    define_json = json.dumps(fdmtcfindu_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def fdmtcfsecu_define(table_name):

    fdmtcfsecu_str = {
            "table_name": "fdmtcfsecu",
            "table_show_name": "证券业现金流量表(PIT)",
            "table_comment": "证券业现金流量表(PIT)-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "证券内部ID", "col_comment": "证券内部ID-描述"},
                {"col_name": "publishDate", "col_show_name": "发布日期", "col_comment": "发布日期-描述"},
                {"col_name": "endDate", "col_show_name": "截止日期", "col_comment": "截止日期-描述"},
                {"col_name": "endDateRep", "col_show_name": "报表截止日期", "col_comment": "报表截止日期-描述"},
                {"col_name": "partyID", "col_show_name": "机构内部ID", "col_comment": "机构内部ID-描述"},
                {"col_name": "ticker", "col_show_name": "股票代码", "col_comment": "股票代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD",
                 "col_show_name": "通联编制的证券市场编码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所等。对应DataAPI.SysCodeGet.codeTypeID=10002。",
                 "col_comment": "通联编制的证券市场编码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所等。对应DataAPI.SysCodeGet.codeTypeID=10002。-描述"},
                {"col_name": "actPubtime", "col_show_name": "实际披露时间", "col_comment": "实际披露时间-描述"},
                {"col_name": "mergedFlag", "col_show_name": "合并类型。1-合并,2-母公司。对应DataAPI.SysCodeGet.codeTypeID=70003。",
                 "col_comment": "合并类型。1-合并,2-母公司。对应DataAPI.SysCodeGet.codeTypeID=70003。-描述"},
                {"col_name": "reportType",
                 "col_show_name": "报告类型。Q1-第一季报，S1-半年报，Q3-第三季报，CQ3-三季报（累计1-9月），A-年报。对应DataAPI.SysCodeGet.codeTypeID=70001。",
                 "col_comment": "报告类型。Q1-第一季报，S1-半年报，Q3-第三季报，CQ3-三季报（累计1-9月），A-年报。对应DataAPI.SysCodeGet.codeTypeID=70001。-描述"},
                {"col_name": "fiscalPeriod", "col_show_name": "会计期间", "col_comment": "会计期间-描述"},
                {"col_name": "accoutingStandards", "col_show_name": "会计准则", "col_comment": "会计准则-描述"},
                {"col_name": "currencyCD",
                 "col_show_name": "货币代码。例如，USD-美元；CAD-加元等。对应DataAPI.SysCodeGet.codeTypeID=10004。",
                 "col_comment": "货币代码。例如，USD-美元；CAD-加元等。对应DataAPI.SysCodeGet.codeTypeID=10004。-描述"},
                {"col_name": "NIncBorrOthFI", "col_show_name": "向其他金融机构拆入资金净增加额", "col_comment": "向其他金融机构拆入资金净增加额-描述"},
                {"col_name": "NIncDispTradFA", "col_show_name": "处置交易性金融资产净增加额", "col_comment": "处置交易性金融资产净增加额-描述"},
                {"col_name": "NIncDispFaFS", "col_show_name": "处置可供出售金融资产净增加额", "col_comment": "处置可供出售金融资产净增加额-描述"},
                {"col_name": "IFCCashIncr", "col_show_name": "收取利息、手续费及佣金的现金", "col_comment": "收取利息、手续费及佣金的现金-描述"},
                {"col_name": "NIncFrBorr", "col_show_name": "拆入资金净增加额", "col_comment": "拆入资金净增加额-描述"},
                {"col_name": "NCApIncrRepur", "col_show_name": "回购业务资金净增加额", "col_comment": "回购业务资金净增加额-描述"},
                {"col_name": "refundOfTax", "col_show_name": "收到的税费返还", "col_comment": "收到的税费返还-描述"},
                {"col_name": "CFrOthOperateA", "col_show_name": "收到其他与经营活动有关的现金", "col_comment": "收到其他与经营活动有关的现金-描述"},
                {"col_name": "specOCIF", "col_show_name": "经营活动流入特殊项目", "col_comment": "经营活动流入特殊项目-描述"},
                {"col_name": "AOCIF", "col_show_name": "经营活动流入调整金额", "col_comment": "经营活动流入调整金额-描述"},
                {"col_name": "CInfFrOperateA", "col_show_name": "经营活动现金流入小计", "col_comment": "经营活动现金流入小计-描述"},
                {"col_name": "CPaidIFC", "col_show_name": "支付利息、手续费及佣金的现金", "col_comment": "支付利息、手续费及佣金的现金-描述"},
                {"col_name": "CPaidToForEmpl", "col_show_name": "支付给职工以及为职工支付的现金", "col_comment": "支付给职工以及为职工支付的现金-描述"},
                {"col_name": "CPaidForTaxes", "col_show_name": "支付的各项税费", "col_comment": "支付的各项税费-描述"},
                {"col_name": "CPaidForOthOpA", "col_show_name": "支付其他与经营活动有关的现金", "col_comment": "支付其他与经营活动有关的现金-描述"},
                {"col_name": "specOCOF", "col_show_name": "经营活动流出特殊项目", "col_comment": "经营活动流出特殊项目-描述"},
                {"col_name": "AOCOF", "col_show_name": "经营活动流出调整金额", "col_comment": "经营活动流出调整金额-描述"},
                {"col_name": "COutfOperateA", "col_show_name": "经营活动现金流出小计", "col_comment": "经营活动现金流出小计-描述"},
                {"col_name": "ANOCF", "col_show_name": "经营活动现金流量净额的调整金额", "col_comment": "经营活动现金流量净额的调整金额-描述"},
                {"col_name": "NCFOperateA", "col_show_name": "经营活动产生的现金流量净额", "col_comment": "经营活动产生的现金流量净额-描述"},
                {"col_name": "procSellInvest", "col_show_name": "收回投资收到的现金", "col_comment": "收回投资收到的现金-描述"},
                {"col_name": "gainInvest", "col_show_name": "取得投资收益收到的现金", "col_comment": "取得投资收益收到的现金-描述"},
                {"col_name": "dispFixAssetsOth", "col_show_name": "处置固定资产、无形资产和其他长期资产收回的现金净额",
                 "col_comment": "处置固定资产、无形资产和其他长期资产收回的现金净额-描述"},
                {"col_name": "NDispSubsOthBizC", "col_show_name": "处置子公司及其他营业单位收到的现金净额",
                 "col_comment": "处置子公司及其他营业单位收到的现金净额-描述"},
                {"col_name": "CFrOthInvestA", "col_show_name": "收到其他与投资活动有关的现金", "col_comment": "收到其他与投资活动有关的现金-描述"},
                {"col_name": "specICIF", "col_show_name": "投资活动流入特殊项目", "col_comment": "投资活动流入特殊项目-描述"},
                {"col_name": "AICIF", "col_show_name": "投资活动流入调整金额", "col_comment": "投资活动流入调整金额-描述"},
                {"col_name": "CInfFrInvestA", "col_show_name": "投资活动现金流入小计", "col_comment": "投资活动现金流入小计-描述"},
                {"col_name": "purFixAssetsOth", "col_show_name": "购建固定资产、无形资产和其他长期资产支付的现金",
                 "col_comment": "购建固定资产、无形资产和其他长期资产支付的现金-描述"},
                {"col_name": "CPaidInvest", "col_show_name": "投资支付的现金", "col_comment": "投资支付的现金-描述"},
                {"col_name": "NCPaidAcquis", "col_show_name": "取得子公司及其他营业单位支付的现金净额",
                 "col_comment": "取得子公司及其他营业单位支付的现金净额-描述"},
                {"col_name": "CPaidOthInvestA", "col_show_name": "支付其他与投资活动有关的现金", "col_comment": "支付其他与投资活动有关的现金-描述"},
                {"col_name": "specICOF", "col_show_name": "投资活动流出特殊项目", "col_comment": "投资活动流出特殊项目-描述"},
                {"col_name": "AICOF", "col_show_name": "投资活动流出调整金额", "col_comment": "投资活动流出调整金额-描述"},
                {"col_name": "COutfFrInvestA", "col_show_name": "投资活动现金流出小计", "col_comment": "投资活动现金流出小计-描述"},
                {"col_name": "ANICF", "col_show_name": "投资活动现金流量净额的调整金额", "col_comment": "投资活动现金流量净额的调整金额-描述"},
                {"col_name": "NCFFrInvestA", "col_show_name": "投资活动产生的现金流量净额", "col_comment": "投资活动产生的现金流量净额-描述"},
                {"col_name": "CFrCapContr", "col_show_name": "吸收投资收到的现金", "col_comment": "吸收投资收到的现金-描述"},
                {"col_name": "CFrMinoSSubs", "col_show_name": "其中:子公司吸收少数股东投资收到的现金",
                 "col_comment": "其中:子公司吸收少数股东投资收到的现金-描述"},
                {"col_name": "CFrBorr", "col_show_name": "取得借款收到的现金", "col_comment": "取得借款收到的现金-描述"},
                {"col_name": "CFrIssueBond", "col_show_name": "发行债券收到的现金", "col_comment": "发行债券收到的现金-描述"},
                {"col_name": "CFrOthFinanA", "col_show_name": "收到其他与筹资活动有关的现金", "col_comment": "收到其他与筹资活动有关的现金-描述"},
                {"col_name": "specFCIF", "col_show_name": "筹资活动流入特殊项目", "col_comment": "筹资活动流入特殊项目-描述"},
                {"col_name": "AFCIF", "col_show_name": "筹资活动流入调整金额", "col_comment": "筹资活动流入调整金额-描述"},
                {"col_name": "CInfFrFinanA", "col_show_name": "筹资活动现金流入小计", "col_comment": "筹资活动现金流入小计-描述"},
                {"col_name": "CPaidForDebts", "col_show_name": "偿还债务支付的现金", "col_comment": "偿还债务支付的现金-描述"},
                {"col_name": "CPaidDivProfInt", "col_show_name": "分配股利、利润或偿付利息支付的现金",
                 "col_comment": "分配股利、利润或偿付利息支付的现金-描述"},
                {"col_name": "divProfSubsMinoS", "col_show_name": "其中:子公司支付给少数股东的股利、利润",
                 "col_comment": "其中:子公司支付给少数股东的股利、利润-描述"},
                {"col_name": "CPaidOthFinanA", "col_show_name": "支付其他与筹资活动有关的现金", "col_comment": "支付其他与筹资活动有关的现金-描述"},
                {"col_name": "specFCOF", "col_show_name": "筹资活动流出特殊项目", "col_comment": "筹资活动流出特殊项目-描述"},
                {"col_name": "AFCOF", "col_show_name": "筹资活动流出调整金额", "col_comment": "筹资活动流出调整金额-描述"},
                {"col_name": "COutfFrFinanA", "col_show_name": "筹资活动现金流出小计", "col_comment": "筹资活动现金流出小计-描述"},
                {"col_name": "ANFCF", "col_show_name": "筹资活动现金流量净额的调整金额", "col_comment": "筹资活动现金流量净额的调整金额-描述"},
                {"col_name": "NCFFrFinanA", "col_show_name": "筹资活动产生的现金流量净额", "col_comment": "筹资活动产生的现金流量净额-描述"},
                {"col_name": "forexEffects", "col_show_name": "汇率变动对现金及现金等价物的影响", "col_comment": "汇率变动对现金及现金等价物的影响-描述"},
                {"col_name": "othEffectCE", "col_show_name": "影响现金及现金等价物净增加额的特殊项目",
                 "col_comment": "影响现金及现金等价物净增加额的特殊项目-描述"},
                {"col_name": "ACE", "col_show_name": "影响现金及现金等价物净增加额的调整金额", "col_comment": "影响现金及现金等价物净增加额的调整金额-描述"},
                {"col_name": "NChangeInCash", "col_show_name": "现金及现金等价物净增加额", "col_comment": "现金及现金等价物净增加额-描述"},
                {"col_name": "NCEBegBal", "col_show_name": "加:期初现金及现金等价物余额", "col_comment": "加:期初现金及现金等价物余额-描述"},
                {"col_name": "othEffectCEI", "col_show_name": "影响期末现金及现金等价物余额的特殊项目",
                 "col_comment": "影响期末现金及现金等价物余额的特殊项目-描述"},
                {"col_name": "ACEI", "col_show_name": "影响期末现金及现金等价物余额的调整金额", "col_comment": "影响期末现金及现金等价物余额的调整金额-描述"},
                {"col_name": "NCEEndBal", "col_show_name": "期末现金及现金等价物余额", "col_comment": "期末现金及现金等价物余额-描述"},
                {"col_name": "updateTime", "col_show_name": "更新时间", "col_comment": "更新时间-描述"}
            ]
        }
    define_json = json.dumps(fdmtcfsecu_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def fdmtcfinsu_define(table_name):

    fdmtcfinsu_str = {
            "table_name": "fdmtcfinsu",
            "table_show_name": "保险业现金流量表(PIT)",
            "table_comment": "保险业现金流量表(PIT)-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "证券内部ID", "col_comment": "证券内部ID-描述"},
                {"col_name": "publishDate", "col_show_name": "截止日期", "col_comment": "截止日期-描述"},
                {"col_name": "endDate", "col_show_name": "发布日期", "col_comment": "发布日期-描述"},
                {"col_name": "endDateRep", "col_show_name": "报表截止日期", "col_comment": "报表截止日期-描述"},
                {"col_name": "partyID", "col_show_name": "机构内部ID", "col_comment": "机构内部ID-描述"},
                {"col_name": "ticker", "col_show_name": "股票代码", "col_comment": "股票代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD",
                 "col_show_name": "通联编制的证券市场编码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所等。对应DataAPI.SysCodeGet.codeTypeID=10002。",
                 "col_comment": "通联编制的证券市场编码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所等。对应DataAPI.SysCodeGet.codeTypeID=10002。-描述"},
                {"col_name": "actPubtime", "col_show_name": "实际披露时间", "col_comment": "实际披露时间-描述"},
                {"col_name": "mergedFlag", "col_show_name": "合并类型。1-合并,2-母公司。对应DataAPI.SysCodeGet.codeTypeID=70003。",
                 "col_comment": "合并类型。1-合并,2-母公司。对应DataAPI.SysCodeGet.codeTypeID=70003。-描述"},
                {"col_name": "reportType",
                 "col_show_name": "报告类型。Q1-第一季报，S1-半年报，Q3-第三季报，CQ3-三季报（累计1-9月），A-年报。对应DataAPI.SysCodeGet.codeTypeID=70001。",
                 "col_comment": "报告类型。Q1-第一季报，S1-半年报，Q3-第三季报，CQ3-三季报（累计1-9月），A-年报。对应DataAPI.SysCodeGet.codeTypeID=70001。-描述"},
                {"col_name": "fiscalPeriod", "col_show_name": "会计期间", "col_comment": "会计期间-描述"},
                {"col_name": "accoutingStandards", "col_show_name": "会计准则", "col_comment": "会计准则-描述"},
                {"col_name": "currencyCD",
                 "col_show_name": "货币代码。例如，USD-美元；CAD-加元等。对应DataAPI.SysCodeGet.codeTypeID=10004。",
                 "col_comment": "货币代码。例如，USD-美元；CAD-加元等。对应DataAPI.SysCodeGet.codeTypeID=10004。-描述"},
                {"col_name": "NDeposIncrCFI", "col_show_name": "客户存款和同业存放款项净增加额", "col_comment": "客户存款和同业存放款项净增加额-描述"},
                {"col_name": "NIncrBorrFrCB", "col_show_name": "向中央银行借款净增加额", "col_comment": "向中央银行借款净增加额-描述"},
                {"col_name": "premFrOrigContr", "col_show_name": "收到原保险合同保费取得的现金", "col_comment": "收到原保险合同保费取得的现金-描述"},
                {"col_name": "NReinsurPrem", "col_show_name": "收到再保险业务现金净额", "col_comment": "收到再保险业务现金净额-描述"},
                {"col_name": "NIncPhDeposInv", "col_show_name": "保户储金及投资款净增加额", "col_comment": "保户储金及投资款净增加额-描述"},
                {"col_name": "IFCCashIncr", "col_show_name": "收取利息、手续费及佣金的现金", "col_comment": "收取利息、手续费及佣金的现金-描述"},
                {"col_name": "refundOfTax", "col_show_name": "收到的税费返还", "col_comment": "收到的税费返还-描述"},
                {"col_name": "CFrOthOperateA", "col_show_name": "收到其他与经营活动有关的现金", "col_comment": "收到其他与经营活动有关的现金-描述"},
                {"col_name": "specOCIF", "col_show_name": "经营活动流入特殊项目", "col_comment": "经营活动流入特殊项目-描述"},
                {"col_name": "AOCIF", "col_show_name": "经营活动流入调整金额", "col_comment": "经营活动流入调整金额-描述"},
                {"col_name": "CInfFrOperateA", "col_show_name": "经营活动现金流入小计", "col_comment": "经营活动现金流入小计-描述"},
                {"col_name": "NIncDisburOfLA", "col_show_name": "客户贷款及垫款净增加额", "col_comment": "客户贷款及垫款净增加额-描述"},
                {"col_name": "NIncrDeposInFI", "col_show_name": "存放中央银行和同业款项净增加额", "col_comment": "存放中央银行和同业款项净增加额-描述"},
                {"col_name": "origContrCIndem", "col_show_name": "支付原保险合同赔付款项的现金", "col_comment": "支付原保险合同赔付款项的现金-描述"},
                {"col_name": "CPaidIFC", "col_show_name": "支付利息、手续费及佣金的现金", "col_comment": "支付利息、手续费及佣金的现金-描述"},
                {"col_name": "CPaidPolDiv", "col_show_name": "支付保单红利的现金", "col_comment": "支付保单红利的现金-描述"},
                {"col_name": "CPaidToForEmpl", "col_show_name": "支付给职工以及为职工支付的现金", "col_comment": "支付给职工以及为职工支付的现金-描述"},
                {"col_name": "CPaidForTaxes", "col_show_name": "支付的各项税费", "col_comment": "支付的各项税费-描述"},
                {"col_name": "CPaidForOthOpA", "col_show_name": "支付其他与经营活动有关的现金", "col_comment": "支付其他与经营活动有关的现金-描述"},
                {"col_name": "specOCOF", "col_show_name": "经营活动流出特殊项目", "col_comment": "经营活动流出特殊项目-描述"},
                {"col_name": "AOCOF", "col_show_name": "经营活动流出调整金额", "col_comment": "经营活动流出调整金额-描述"},
                {"col_name": "COutfOperateA", "col_show_name": "经营活动现金流出小计", "col_comment": "经营活动现金流出小计-描述"},
                {"col_name": "ANOCF", "col_show_name": "经营活动现金流量净额的调整金额", "col_comment": "经营活动现金流量净额的调整金额-描述"},
                {"col_name": "NCFOperateA", "col_show_name": "经营活动产生的现金流量净额", "col_comment": "经营活动产生的现金流量净额-描述"},
                {"col_name": "procSellInvest", "col_show_name": "收回投资收到的现金", "col_comment": "收回投资收到的现金-描述"},
                {"col_name": "gainInvest", "col_show_name": "取得投资收益收到的现金", "col_comment": "取得投资收益收到的现金-描述"},
                {"col_name": "dispFixAssetsOth", "col_show_name": "处置固定资产、无形资产和其他长期资产收回的现金净额",
                 "col_comment": "处置固定资产、无形资产和其他长期资产收回的现金净额-描述"},
                {"col_name": "NDispSubsOthBizC", "col_show_name": "处置子公司及其他营业单位收到的现金净额",
                 "col_comment": "处置子公司及其他营业单位收到的现金净额-描述"},
                {"col_name": "CFrOthInvestA", "col_show_name": "收到其他与投资活动有关的现金", "col_comment": "收到其他与投资活动有关的现金-描述"},
                {"col_name": "specICIF", "col_show_name": "投资活动流入特殊项目", "col_comment": "投资活动流入特殊项目-描述"},
                {"col_name": "AICIF", "col_show_name": "投资活动流入调整金额", "col_comment": "投资活动流入调整金额-描述"},
                {"col_name": "CInfFrInvestA", "col_show_name": "投资活动现金流入小计", "col_comment": "投资活动现金流入小计-描述"},
                {"col_name": "PurFixAssetsOth", "col_show_name": "购建固定资产、无形资产和其他长期资产支付的现金",
                 "col_comment": "购建固定资产、无形资产和其他长期资产支付的现金-描述"},
                {"col_name": "CPaidInvest", "col_show_name": "投资支付的现金", "col_comment": "投资支付的现金-描述"},
                {"col_name": "NIncrPledgeLoan", "col_show_name": "质押贷款净增加额", "col_comment": "质押贷款净增加额-描述"},
                {"col_name": "NCPaidAcquis", "col_show_name": "取得子公司及其他营业单位支付的现金净额",
                 "col_comment": "取得子公司及其他营业单位支付的现金净额-描述"},
                {"col_name": "CPaidOthInvestA", "col_show_name": "支付其他与投资活动有关的现金", "col_comment": "支付其他与投资活动有关的现金-描述"},
                {"col_name": "specICOF", "col_show_name": "投资活动流出特殊项目", "col_comment": "投资活动流出特殊项目-描述"},
                {"col_name": "AICOF", "col_show_name": "投资活动流出调整金额", "col_comment": "投资活动流出调整金额-描述"},
                {"col_name": "COutfFrInvestA", "col_show_name": "投资活动现金流出小计", "col_comment": "投资活动现金流出小计-描述"},
                {"col_name": "ANICF", "col_show_name": "投资活动现金流量净额的调整金额", "col_comment": "投资活动现金流量净额的调整金额-描述"},
                {"col_name": "NCFFrInvestA", "col_show_name": "投资活动产生的现金流量净额", "col_comment": "投资活动产生的现金流量净额-描述"},
                {"col_name": "CFrCapContr", "col_show_name": "吸收投资收到的现金", "col_comment": "吸收投资收到的现金-描述"},
                {"col_name": "CFrMinoSSubs", "col_show_name": "其中:子公司吸收少数股东投资收到的现金",
                 "col_comment": "其中:子公司吸收少数股东投资收到的现金-描述"},
                {"col_name": "CFrBorr", "col_show_name": "取得借款收到的现金", "col_comment": "取得借款收到的现金-描述"},
                {"col_name": "CFrIssueBond", "col_show_name": "发行债券收到的现金", "col_comment": "发行债券收到的现金-描述"},
                {"col_name": "CFrOthFinanA", "col_show_name": "收到其他与筹资活动有关的现金", "col_comment": "收到其他与筹资活动有关的现金-描述"},
                {"col_name": "specFCIF", "col_show_name": "筹资活动流入特殊项目", "col_comment": "筹资活动流入特殊项目-描述"},
                {"col_name": "AFCIF", "col_show_name": "筹资活动流入调整金额", "col_comment": "筹资活动流入调整金额-描述"},
                {"col_name": "CInfFrFinanA", "col_show_name": "筹资活动现金流入小计", "col_comment": "筹资活动现金流入小计-描述"},
                {"col_name": "CPaidForDebts", "col_show_name": "偿还债务支付的现金", "col_comment": "偿还债务支付的现金-描述"},
                {"col_name": "CPaidDivProfInt", "col_show_name": "分配股利、利润或偿付利息支付的现金",
                 "col_comment": "分配股利、利润或偿付利息支付的现金-描述"},
                {"col_name": "divProfSubsMinoS", "col_show_name": "其中:子公司支付给少数股东的股利、利润",
                 "col_comment": "其中:子公司支付给少数股东的股利、利润-描述"},
                {"col_name": "CPaidOthFinanA", "col_show_name": "支付其他与筹资活动有关的现金", "col_comment": "支付其他与筹资活动有关的现金-描述"},
                {"col_name": "specFCOF", "col_show_name": "筹资活动流出特殊项目", "col_comment": "筹资活动流出特殊项目-描述"},
                {"col_name": "AFCOF", "col_show_name": "筹资活动流出调整金额", "col_comment": "筹资活动流出调整金额-描述"},
                {"col_name": "COutfFrFinanA", "col_show_name": "筹资活动现金流出小计", "col_comment": "筹资活动现金流出小计-描述"},
                {"col_name": "ANFCF", "col_show_name": "筹资活动现金流量净额的调整金额", "col_comment": "筹资活动现金流量净额的调整金额-描述"},
                {"col_name": "NCFFrFinanA", "col_show_name": "筹资活动产生的现金流量净额", "col_comment": "筹资活动产生的现金流量净额-描述"},
                {"col_name": "forexEffects", "col_show_name": "汇率变动对现金及现金等价物的影响", "col_comment": "汇率变动对现金及现金等价物的影响-描述"},
                {"col_name": "othEffectCE", "col_show_name": "影响现金及现金等价物净增加额的特殊项目",
                 "col_comment": "影响现金及现金等价物净增加额的特殊项目-描述"},
                {"col_name": "ACE", "col_show_name": "影响现金及现金等价物净增加额的调整金额", "col_comment": "影响现金及现金等价物净增加额的调整金额-描述"},
                {"col_name": "NChangeInCash", "col_show_name": "现金及现金等价物净增加额", "col_comment": "现金及现金等价物净增加额-描述"},
                {"col_name": "NCEBegBal", "col_show_name": "加:期初现金及现金等价物余额", "col_comment": "加:期初现金及现金等价物余额-描述"},
                {"col_name": "othEffectCEI", "col_show_name": "影响期末现金及现金等价物余额的特殊项目",
                 "col_comment": "影响期末现金及现金等价物余额的特殊项目-描述"},
                {"col_name": "ACEI", "col_show_name": "影响期末现金及现金等价物余额的调整金额", "col_comment": "影响期末现金及现金等价物余额的调整金额-描述"},
                {"col_name": "NCEEndBal", "col_show_name": "期末现金及现金等价物余额", "col_comment": "期末现金及现金等价物余额-描述"},
                {"col_name": "updateTime", "col_show_name": "更新时间", "col_comment": "更新时间-描述"}
            ]
        }
    define_json = json.dumps(fdmtcfinsu_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def industrystd_define(table_name):


    industrystd_str = {
        "table_name": "industrystd",
        "table_show_name": "行业分类标准表",
        "table_comment": "行业分类标准表-描述",
        "table_category1": "1",
        "table_category2": "2",
        "table_category3": "3",
        "columns": [
            {"col_name": "date", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
            {"col_name": "industryVersionCD", "col_show_name": "行业分类标准数字编码", "col_comment": "行业分类标准数字编码-描述"},
            {"col_name": "industryVersion", "col_show_name": "行业分类标准版本", "col_comment": "行业分类标准版本-描述"},
            {"col_name": "industry", "col_show_name": "行业分类标准名称", "col_comment": "行业分类标准名称-描述"},
            {"col_name": "industryID", "col_show_name": "通联编制的行业分类编码，两位为一个层级，前后有从属关系，位数越少层级越高",
             "col_comment": "通联编制的行业分类编码，两位为一个层级，前后有从属关系，位数越少层级越高-描述"},
            {"col_name": "industrySymbol", "col_show_name": "行业编制机构发布的行业编码", "col_comment": "行业编制机构发布的行业编码-描述"},
            {"col_name": "industryName", "col_show_name": "行业名称", "col_comment": "行业名称-描述"},
            {"col_name": "industryLevel", "col_show_name": "行业所在层级", "col_comment": "行业所在层级-描述"},
            {"col_name": "isNew", "col_show_name": "当前是否有效", "col_comment": "当前是否有效-描述"},
            {"col_name": "indexSymbol", "col_show_name": "对应行业指数的通用代码，目前仅提供申万行业",
             "col_comment": "对应行业指数的通用代码，目前仅提供申万行业-描述"},
            {"col_name": "prntIndustryID", "col_show_name": "上一级行业的数字编码", "col_comment": "上一级行业的数字编码-描述"},
            {"col_name": "beginDate", "col_show_name": "行业生效日期", "col_comment": "行业生效日期-描述"},
            {"col_name": "endDate", "col_show_name": "行业失效日期", "col_comment": "行业失效日期-描述"},
            {"col_name": "updateTime", "col_show_name": "最近一次更新时间", "col_comment": "最近一次更新时间-描述"}
        ]
    }
    define_json = json.dumps(industrystd_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def equindustry_define(table_name):

    equindustry_str = {
            "table_name": "equindustry",
            "table_show_name": "股票行业分类",
            "table_comment": "股票行业分类-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "date", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "secID", "col_show_name": "通联编制的证券编码，可在getSecID获取到。",
                 "col_comment": "通联编制的证券编码，可在getSecID获取到。-描述"},
                {"col_name": "ticker", "col_show_name": "通用交易代码", "col_comment": "通用交易代码-描述"},
                {"col_name": "exchangeCD", "col_show_name": "通联编制的交易市场编码", "col_comment": "通联编制的交易市场编码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "secFullName", "col_show_name": "证券全称", "col_comment": "证券全称-描述"},
                {"col_name": "partyID", "col_show_name": "通联编制的机构编码", "col_comment": "通联编制的机构编码-描述"},
                {"col_name": "industryVersionCD", "col_show_name": "行业分类标准数字编码", "col_comment": "行业分类标准数字编码-描述"},
                {"col_name": "industry", "col_show_name": "行业分类标准", "col_comment": "行业分类标准-描述"},
                {"col_name": "industryID", "col_show_name": "行业分类编码，成分记录在最后一级行业分类下，上级行业请查看对应的一二三四级行业编码",
                 "col_comment": "行业分类编码，成分记录在最后一级行业分类下，上级行业请查看对应的一二三四级行业编码-描述"},
                {"col_name": "industrySymbol", "col_show_name": "行业分类编码，行业编制机构发布的行业编码",
                 "col_comment": "行业分类编码，行业编制机构发布的行业编码-描述"},
                {"col_name": "intoDate", "col_show_name": "成分纳入日期", "col_comment": "成分纳入日期-描述"},
                {"col_name": "outDate", "col_show_name": "成分剔除日期", "col_comment": "成分剔除日期-描述"},
                {"col_name": "isNew", "col_show_name": "是否最新：1-是，0-否", "col_comment": "是否最新：1-是，0-否-描述"},
                {"col_name": "industryID1", "col_show_name": "一级行业编码", "col_comment": "一级行业编码-描述"},
                {"col_name": "industryName1", "col_show_name": "一级行业", "col_comment": "一级行业-描述"},
                {"col_name": "industryID2", "col_show_name": "二级行业编码", "col_comment": "二级行业编码-描述"},
                {"col_name": "industryName2", "col_show_name": "二级行业", "col_comment": "二级行业-描述"},
                {"col_name": "industryID3", "col_show_name": "三级行业编码", "col_comment": "三级行业编码-描述"},
                {"col_name": "industryName3", "col_show_name": "三级行业", "col_comment": "三级行业-描述"},
                {"col_name": "IndustryID4", "col_show_name": "四级行业编码", "col_comment": "四级行业编码-描述"},
                {"col_name": "IndustryName4", "col_show_name": "四级行业", "col_comment": "四级行业-描述"},
                {"col_name": "equType", "col_show_name": "个股所属市场板块", "col_comment": "个股所属市场板块-描述"}
            ]
        }
    define_json = json.dumps(equindustry_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def partyid_define(table_name):

    partyid_str = {
            "table_name": "partyid",
            "table_show_name": "公司基本信息",
            "table_comment": "公司基本信息-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "date", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "partyID", "col_show_name": "机构ID", "col_comment": "机构ID-描述"},
                {"col_name": "partyFullName", "col_show_name": "机构全称", "col_comment": "机构全称-描述"},
                {"col_name": "partyFullNameEn", "col_show_name": "机构英文全称", "col_comment": "机构英文全称-描述"},
                {"col_name": "partyShortName", "col_show_name": "机构简称", "col_comment": "机构简称-描述"},
                {"col_name": "partyShortNameEn", "col_show_name": "机构英文简称", "col_comment": "机构英文简称-描述"},
                {"col_name": "officeAddr", "col_show_name": "办公地址", "col_comment": "办公地址-描述"},
                {"col_name": "primeOperating", "col_show_name": "主营业务", "col_comment": "主营业务-描述"},
                {"col_name": "partyNatureCD", "col_show_name": "公司性质", "col_comment": "公司性质-描述"},
                {"col_name": "instStatus", "col_show_name": "机构状态。1-营业中。", "col_comment": "机构状态。1-营业中。-描述"},
                {"col_name": "isIssBond", "col_show_name": "是否发行债券", "col_comment": "是否发行债券-描述"},
                {"col_name": "regDate", "col_show_name": "注册日期", "col_comment": "注册日期-描述"},
                {"col_name": "legalRep", "col_show_name": "法定代表人", "col_comment": "法定代表人-描述"},
                {"col_name": "regCountryCD", "col_show_name": "注册国家代码，对应getSysCode.codeTypeID=10031",
                 "col_comment": "注册国家代码，对应getSysCode.codeTypeID=10031-描述"},
                {"col_name": "regProvince", "col_show_name": "注册省份，对应getSysCode.codeTypeID=10003",
                 "col_comment": "注册省份，对应getSysCode.codeTypeID=10003-描述"},
                {"col_name": "regCity", "col_show_name": "注册城市，对应getSysCode.codeTypeID=10003",
                 "col_comment": "注册城市，对应getSysCode.codeTypeID=10003-描述"},
                {"col_name": "regAddr", "col_show_name": "注册地址", "col_comment": "注册地址-描述"},
                {"col_name": "regCap", "col_show_name": "注册资金", "col_comment": "注册资金-描述"},
                {"col_name": "regCapCurrCD", "col_show_name": "注册资金货币代码，对应getSysCode.codeTypeID=10004",
                 "col_comment": "注册资金货币代码，对应getSysCode.codeTypeID=10004-描述"},
                {"col_name": "email", "col_show_name": "联系邮箱", "col_comment": "联系邮箱-描述"},
                {"col_name": "website", "col_show_name": "机构网站", "col_comment": "机构网站-描述"},
                {"col_name": "tel", "col_show_name": "联系电话", "col_comment": "联系电话-描述"},
                {"col_name": "fax", "col_show_name": "联系传真", "col_comment": "联系传真-描述"},
                {"col_name": "boardSecry", "col_show_name": "董事会秘书", "col_comment": "董事会秘书-描述"},
                {"col_name": "genMana", "col_show_name": "总经理", "col_comment": "总经理-描述"},
                {"col_name": "opaScope", "col_show_name": "经营范围", "col_comment": "经营范围-描述"},
                {"col_name": "legalEntityID", "col_show_name": "工商登记号", "col_comment": "工商登记号-描述"},
                {"col_name": "isIssMf", "col_show_name": "是否发行公募基金", "col_comment": "是否发行公募基金-描述"},
                {"col_name": "closeDate", "col_show_name": "机构终止日期", "col_comment": "机构终止日期-描述"},
                {"col_name": "profile", "col_show_name": "机构介绍", "col_comment": "机构介绍-描述"}
            ]
        }
    define_json = json.dumps(partyid_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def equdiv_define(table_name):

    equdiv_str = {
            "table_name": "equdiv",
            "table_show_name": "股票分红信息",
            "table_comment": "股票分红信息-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "内部编码", "col_comment": "内部编码-描述"},
                {"col_name": "ticker", "col_show_name": "交易代码", "col_comment": "交易代码-描述"},
                {"col_name": "exchangeCD",
                 "col_show_name": "交易市场。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所。对应getSysCode.codeTypeID=10002。",
                 "col_comment": "交易市场。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所。对应getSysCode.codeTypeID=10002。-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "endDate", "col_show_name": "分红年度截止日", "col_comment": "分红年度截止日-描述"},
                {"col_name": "publishDate", "col_show_name": "公告日期", "col_comment": "公告日期-描述"},
                {"col_name": "eventProcessCD",
                 "col_show_name": "事件进程。例如，1-董事预案；3-股东大会否决。对应getSysCode.codeTypeID=20001。",
                 "col_comment": "事件进程。例如，1-董事预案；3-股东大会否决。对应getSysCode.codeTypeID=20001。-描述"},
                {"col_name": "perShareDivRatio", "col_show_name": "每股送股比例", "col_comment": "每股送股比例-描述"},
                {"col_name": "perShareTransRatio", "col_show_name": "每股转增股比例", "col_comment": "每股转增股比例-描述"},
                {"col_name": "perCashDiv", "col_show_name": "每股派现(税前)", "col_comment": "每股派现(税前)-描述"},
                {"col_name": "perCashDivAfTax", "col_show_name": "每股派现(税后)", "col_comment": "每股派现(税后)-描述"},
                {"col_name": "currencyCD", "col_show_name": "货币种类。CNY-人民币元，对应getSysCode.codeTypeID=10004。",
                 "col_comment": "货币种类。CNY-人民币元，对应getSysCode.codeTypeID=10004。-描述"},
                {"col_name": "frPerCashDiv", "col_show_name": "每股派现(税前)外币结算", "col_comment": "每股派现(税前)外币结算-描述"},
                {"col_name": "frPerCashDivAfTax", "col_show_name": "每股派现(税后)外币结算", "col_comment": "每股派现(税后)外币结算-描述"},
                {"col_name": "frCurrencyCD", "col_show_name": "外币货币种类。例如，GBP-英镑；USD-美元。对应getSysCode.codeTypeID=10004。",
                 "col_comment": "外币货币种类。例如，GBP-英镑；USD-美元。对应getSysCode.codeTypeID=10004。-描述"},
                {"col_name": "recordDate", "col_show_name": "股权登记日", "col_comment": "股权登记日-描述"},
                {"col_name": "exDivDate", "col_show_name": "除权除息日", "col_comment": "除权除息日-描述"},
                {"col_name": "bLastTradeDate", "col_show_name": "B股最后交易日", "col_comment": "B股最后交易日-描述"},
                {"col_name": "payCashDate", "col_show_name": "派现日", "col_comment": "派现日-描述"},
                {"col_name": "bonusShareListDate", "col_show_name": "红股上市日", "col_comment": "红股上市日-描述"},
                {"col_name": "ftdAfExdiv", "col_show_name": "除权除息后交易首日", "col_comment": "除权除息后交易首日-描述"},
                {"col_name": "sharesBfDiv", "col_show_name": "分红前总股本", "col_comment": "分红前总股本-描述"},
                {"col_name": "sharesAfDiv", "col_show_name": "分红后总股本", "col_comment": "分红后总股本-描述"}
            ]
        }
    define_json = json.dumps(equdiv_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def mktequdeval_define(table_name):

    mktequdeval_str = {
            "table_name": "mktequdeval",
            "table_show_name": "",
            "table_comment": "-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "通联编制的证券编码，可使用getSecID获取",
                 "col_comment": "通联编制的证券编码，可使用getSecID获取-描述"},
                {"col_name": "ticker", "col_show_name": "通用交易代码", "col_comment": "通用交易代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD", "col_show_name": "通联编制的交易市场编码", "col_comment": "通联编制的交易市场编码-描述"},
                {"col_name": "tradeDate", "col_show_name": "交易日期", "col_comment": "交易日期-描述"},
                {"col_name": "marketValue", "col_show_name": "总市值=收盘价*总股本", "col_comment": "总市值=收盘价*总股本-描述"},
                {"col_name": "negMarketValue", "col_show_name": "流通市值，A股：收盘价*无限售A股流通股本，B股：收盘价*无限售B股流通股本",
                 "col_comment": "流通市值，A股：收盘价*无限售A股流通股本，B股：收盘价*无限售B股流通股本-描述"},
                {"col_name": "PE", "col_show_name": "市盈率TTM=总市值/净利润TTM", "col_comment": "市盈率TTM=总市值/净利润TTM-描述"},
                {"col_name": "PE1", "col_show_name": "市盈率(动态)=总市值/净利润(MRQ年化)",
                 "col_comment": "市盈率(动态)=总市值/净利润(MRQ年化)-描述"},
                {"col_name": "PE2", "col_show_name": "市盈率(扣非动态)=总市值/扣非净利润(MRQ年化)",
                 "col_comment": "市盈率(扣非动态)=总市值/扣非净利润(MRQ年化)-描述"},
                {"col_name": "PB", "col_show_name": "市净率=总市值/(净资产-其他权益工具)", "col_comment": "市净率=总市值/(净资产-其他权益工具)-描述"},
                {"col_name": "PS", "col_show_name": "市销率TTM=总市值/营业收入TTM", "col_comment": "市销率TTM=总市值/营业收入TTM-描述"},
                {"col_name": "PS1", "col_show_name": "市销率(动态)=总市值/营业收入(MRQ年化)",
                 "col_comment": "市销率(动态)=总市值/营业收入(MRQ年化)-描述"},
                {"col_name": "PCF", "col_show_name": "市现率(净额TTM)=总市值/现金净增加额TTM",
                 "col_comment": "市现率(净额TTM)=总市值/现金净增加额TTM-描述"},
                {"col_name": "PCF1", "col_show_name": "市现率(净额动态)=总市值/现金净增加额(MRQ年化)",
                 "col_comment": "市现率(净额动态)=总市值/现金净增加额(MRQ年化)-描述"},
                {"col_name": "PCF2", "col_show_name": "市现率(经营TTM)=总市值/经营现金净额TTM",
                 "col_comment": "市现率(经营TTM)=总市值/经营现金净额TTM-描述"},
                {"col_name": "PCF3", "col_show_name": "市现率(经营动态)=总市值/经营现金净额(MRQ年化)",
                 "col_comment": "市现率(经营动态)=总市值/经营现金净额(MRQ年化)-描述"},
                {"col_name": "EV", "col_show_name": "企业价值=总市值+负债合计-无息负债-货币资金",
                 "col_comment": "企业价值=总市值+负债合计-无息负债-货币资金-描述"},
                {"col_name": "EVEBITDA", "col_show_name": "企业价值倍数=企业价值/EBITDA(MRQ年化)",
                 "col_comment": "企业价值倍数=企业价值/EBITDA(MRQ年化)-描述"},
                {"col_name": "EVSales", "col_show_name": "企销率=企业价值/营业收入(最新一期财报)",
                 "col_comment": "企销率=企业价值/营业收入(最新一期财报)-描述"},
                {"col_name": "updateTime", "col_show_name": "最近一次更新时间", "col_comment": "最近一次更新时间-描述"}
            ]
        }
    define_json = json.dumps(mktequdeval_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def mktlimit_define(table_name):

    mktlimit_str = {
            "table_name": "mktlimit",
            "table_show_name": "沪深涨跌停限制",
            "table_comment": "沪深涨跌停限制-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "通联编制的证券编码， 可通过getSecID获取。",
                 "col_comment": "通联编制的证券编码， 可通过getSecID获取。-描述"},
                {"col_name": "ticker", "col_show_name": "通用交易代码", "col_comment": "通用交易代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "secShortNameEn", "col_show_name": "证券英文简称", "col_comment": "证券英文简称-描述"},
                {"col_name": "exchangeCD", "col_show_name": "通联编制的证券市场编码", "col_comment": "通联编制的证券市场编码-描述"},
                {"col_name": "tradeDate", "col_show_name": "交易日期", "col_comment": "交易日期-描述"},
                {"col_name": "limitUpPrice", "col_show_name": "涨停价，无涨停限制时等于99999.999",
                 "col_comment": "涨停价，无涨停限制时等于99999.999-描述"},
                {"col_name": "limitDownPrice", "col_show_name": "跌停价，无跌停限制时等于最小变动价位，如0.01",
                 "col_comment": "跌停价，无跌停限制时等于最小变动价位，如0.01-描述"},
                {"col_name": "upLimitReachedTimes", "col_show_name": "达到涨停次数", "col_comment": "达到涨停次数-描述"},
                {"col_name": "downLimitReachedTimes", "col_show_name": "达到跌停次数", "col_comment": "达到跌停次数-描述"}
            ]
        }
    define_json = json.dumps(mktlimit_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def mktequdind_define(table_name):

    mktequdind_str = {
            "table_name": "mktequdind",
            "table_show_name": "股票日行情指标",
            "table_comment": "股票日行情指标-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "通联编制的证券编码，可使用DataAPI.SecIDGet获取",
                 "col_comment": "通联编制的证券编码，可使用DataAPI.SecIDGet获取-描述"},
                {"col_name": "ticker", "col_show_name": "通用交易代码", "col_comment": "通用交易代码-描述"},
                {"col_name": "tradeDate", "col_show_name": "交易日期，格式为YYYYMMDD", "col_comment": "交易日期，格式为YYYYMMDD-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD", "col_show_name": "通联编制的交易市场编码", "col_comment": "通联编制的交易市场编码-描述"},
                {"col_name": "chgStatus",
                 "col_show_name": "收盘涨跌状态：-1-停牌(含暂停上市)，0-平盘，1-上涨(不含涨停)，2-涨停(不含一字涨停)，3-一字涨停，4-下跌(不含跌停)，5-跌停(不含一字跌停)，6-一字跌停",
                 "col_comment": "收盘涨跌状态：-1-停牌(含暂停上市)，0-平盘，1-上涨(不含涨停)，2-涨停(不含一字涨停)，3-一字涨停，4-下跌(不含跌停)，5-跌停(不含一字跌停)，6-一字跌停-描述"},
                {"col_name": "conChg", "col_show_name": "连续涨跌的交易日数，连续上涨以正数表示，连续下跌为负数。停牌不打断连续的计数，但不计入天数",
                 "col_comment": "连续涨跌的交易日数，连续上涨以正数表示，连续下跌为负数。停牌不打断连续的计数，但不计入天数-描述"},
                {"col_name": "conLimit", "col_show_name": "连续涨跌停的交易日数，连续涨停以正数表示，连续跌停为负数。停牌不打断连续的计数，但不计入天数",
                 "col_comment": "连续涨跌停的交易日数，连续涨停以正数表示，连续跌停为负数。停牌不打断连续的计数，但不计入天数-描述"},
                {"col_name": "days1", "col_show_name": "前复权历史最高价距今的天数，如当日创新高等于1，以此类推",
                 "col_comment": "前复权历史最高价距今的天数，如当日创新高等于1，以此类推-描述"},
                {"col_name": "days2", "col_show_name": "当日创近N日的新高，以自然日计。如180表示当日创近180日的新高",
                 "col_comment": "当日创近N日的新高，以自然日计。如180表示当日创近180日的新高-描述"},
                {"col_name": "days3", "col_show_name": "前复权历史最低价距今的天数，如当日创新低等于1，以此类推",
                 "col_comment": "前复权历史最低价距今的天数，如当日创新低等于1，以此类推-描述"},
                {"col_name": "days4", "col_show_name": "当日创近N日的新低，以自然日计。如180表示当日创近180日的新低",
                 "col_comment": "当日创近N日的新低，以自然日计。如180表示当日创近180日的新低-描述"},
                {"col_name": "chgPct3", "col_show_name": "近三个交易日的累计涨跌幅", "col_comment": "近三个交易日的累计涨跌幅-描述"},
                {"col_name": "turnRate3", "col_show_name": "近三个交易日的累计换手率", "col_comment": "近三个交易日的累计换手率-描述"},
                {"col_name": "dealValue", "col_show_name": "当日平均每笔的成交金额，总成交金额/成交笔数",
                 "col_comment": "当日平均每笔的成交金额，总成交金额/成交笔数-描述"},
                {"col_name": "dealValue20", "col_show_name": "近20个交易日的平均笔均额", "col_comment": "近20个交易日的平均笔均额-描述"},
                {"col_name": "updateTime", "col_show_name": "最近一次更新时间", "col_comment": "最近一次更新时间-描述"}
            ]
        }
    define_json = json.dumps(mktequdind_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def equpledge_define(table_name):

    equpledge_str = {
            "table_name": "equpledge",
            "table_show_name": "A股公司股权质押",
            "table_comment": "A股公司股权质押-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "partyID", "col_show_name": "通联编制的机构编码", "col_comment": "通联编制的机构编码-描述"},
                {"col_name": "secID", "col_show_name": "通联编制的证券编码", "col_comment": "通联编制的证券编码-描述"},
                {"col_name": "ticker", "col_show_name": "证券在证券市场通用的交易代码。", "col_comment": "证券在证券市场通用的交易代码。-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD", "col_show_name": "证券交易市场代码", "col_comment": "证券交易市场代码-描述"},
                {"col_name": "publishDate", "col_show_name": "公告日期", "col_comment": "公告日期-描述"},
                {"col_name": "shName", "col_show_name": "股东名称", "col_comment": "股东名称-描述"},
                {"col_name": "shNameType", "col_show_name": "股东类型", "col_comment": "股东类型-描述"},
                {"col_name": "orgName", "col_show_name": "质押方", "col_comment": "质押方-描述"},
                {"col_name": "involvesum", "col_show_name": "质押股数(万股)", "col_comment": "质押股数(万股)-描述"},
                {"col_name": "pledgeShare", "col_show_name": "本次质押占其所持股份比例(%)", "col_comment": "本次质押占其所持股份比例(%)-描述"},
                {"col_name": "shareType", "col_show_name": "质押股份类型，1-流通股，2-流通受限股，3-流通股，流通受限股",
                 "col_comment": "质押股份类型，1-流通股，2-流通受限股，3-流通股，流通受限股-描述"},
                {"col_name": "isCollateralRepo", "col_show_name": "是否质押式回购，0-否，1-是",
                 "col_comment": "是否质押式回购，0-否，1-是-描述"},
                {"col_name": "holdVol", "col_show_name": "持股总数(万股)", "col_comment": "持股总数(万股)-描述"},
                {"col_name": "holdPct", "col_show_name": "持股占总股本比例(%)", "col_comment": "持股占总股本比例(%)-描述"},
                {"col_name": "accPledge", "col_show_name": "累计质押股数(万股)", "col_comment": "累计质押股数(万股)-描述"},
                {"col_name": "accPledgeShare", "col_show_name": "累计质押占所持股份比例(%)", "col_comment": "累计质押占所持股份比例(%)-描述"},
                {"col_name": "accPledgeTotal", "col_show_name": "累计质押占公司总股本比例(%)", "col_comment": "累计质押占公司总股本比例(%)-描述"},
                {"col_name": "beginDate", "col_show_name": "质押起始日期", "col_comment": "质押起始日期-描述"},
                {"col_name": "endDate", "col_show_name": "质押截止日期", "col_comment": "质押截止日期-描述"},
                {"col_name": "thawDate", "col_show_name": "解押日期", "col_comment": "解押日期-描述"},
                {"col_name": "isThaw", "col_show_name": "是否解押，0-否，1-是", "col_comment": "是否解押，0-否，1-是-描述"},
                {"col_name": "statement", "col_show_name": "相关说明", "col_comment": "相关说明-描述"},
                {"col_name": "eventNum", "col_show_name": "事件编码", "col_comment": "事件编码-描述"},
                {"col_name": "updateTime", "col_show_name": "更新时间", "col_comment": "更新时间-描述"}
            ]
        }
    define_json = json.dumps(equpledge_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def equstockpledg_define(table_name):

    equstockpledg_str = {
            "table_name": "equstockpledg",
            "table_show_name": "股票周质押信息",
            "table_comment": "股票周质押信息-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "证券内部编码", "col_comment": "证券内部编码-描述"},
                {"col_name": "ticker", "col_show_name": "股票代码", "col_comment": "股票代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD", "col_show_name": "交易市场", "col_comment": "交易市场-描述"},
                {"col_name": "publishDate", "col_show_name": "公告日期", "col_comment": "公告日期-描述"},
                {"col_name": "nPledgedShares", "col_show_name": "无限售股份质押数量(万)", "col_comment": "无限售股份质押数量(万)-描述"},
                {"col_name": "yPledgedShares", "col_show_name": "有限售股份质押数量(万)", "col_comment": "有限售股份质押数量(万)-描述"},
                {"col_name": "aTotalShares", "col_show_name": "A股总股本(万)", "col_comment": "A股总股本(万)-描述"},
                {"col_name": "pledgeNumber", "col_show_name": "质押笔数", "col_comment": "质押笔数-描述"},
                {"col_name": "pledgeRatio", "col_show_name": "质押比例", "col_comment": "质押比例-描述"},
                {"col_name": "updateTime", "col_show_name": "更新时间", "col_comment": "更新时间-描述"}
            ]
        }
    define_json = json.dumps(equstockpledg_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


# 备注: 该表比通联数据字典少了个字段"actpubtime"
def fdmtmaindatapit_define(table_name):

    fdmtmaindatapit_str = {
            "table_name": "fdmtmaindatapit",
            "table_show_name": "财务指标（新）",
            "table_comment": "财务指标（新）-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID",
                 "col_show_name": "通联编制的证券编码，格式是“交易代码.证券市场代码”，如000002.XSHE。可传入证券交易代码使用getSecID接口获取到。",
                 "col_comment": "通联编制的证券编码，格式是“交易代码.证券市场代码”，如000002.XSHE。可传入证券交易代码使用getSecID接口获取到。-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD", "col_show_name": "通联编制的交易市场编码", "col_comment": "通联编制的交易市场编码-描述"},
                {"col_name": "ticker", "col_show_name": "证券在证券市场通用的交易代码。", "col_comment": "证券在证券市场通用的交易代码。-描述"},
                {"col_name": "partyID", "col_show_name": "机构ID", "col_comment": "机构ID-描述"},
                {"col_name": "publishDate", "col_show_name": "发布日期", "col_comment": "发布日期-描述"},
                {"col_name": "endDateRep", "col_show_name": "报告截止日期", "col_comment": "报告截止日期-描述"},
                {"col_name": "endDate", "col_show_name": "截止日期", "col_comment": "截止日期-描述"},
                {"col_name": "isNew", "col_show_name": "end_date是否为最新数据，是为1，否为0",
                 "col_comment": "end_date是否为最新数据，是为1，否为0-描述"},
                {"col_name": "reportType", "col_show_name": "Q1:一季报, S:半年报, Q3:三季报 , A:年报",
                 "col_comment": "Q1:一季报, S:半年报, Q3:三季报 , A:年报-描述"},
                {"col_name": "mergedFlag", "col_show_name": "1是合并，2是母公司", "col_comment": "1是合并，2是母公司-描述"},
                {"col_name": "fiscalPeriod", "col_show_name": "会计区间长度", "col_comment": "会计区间长度-描述"},
                {"col_name": "tFixedAssets", "col_show_name": "固定资产合计", "col_comment": "固定资产合计-描述"},
                {"col_name": "intFreeCl", "col_show_name": "无息流动负债", "col_comment": "无息流动负债-描述"},
                {"col_name": "intFreeNcl", "col_show_name": "无息非流动负债", "col_comment": "无息非流动负债-描述"},
                {"col_name": "intCl", "col_show_name": "带息流动负债", "col_comment": "带息流动负债-描述"},
                {"col_name": "intDebt", "col_show_name": "带息债务", "col_comment": "带息债务-描述"},
                {"col_name": "nDebt", "col_show_name": "净债务", "col_comment": "净债务-描述"},
                {"col_name": "nTanAssets", "col_show_name": "有形净资产", "col_comment": "有形净资产-描述"},
                {"col_name": "workCapital", "col_show_name": "营运资本", "col_comment": "营运资本-描述"},
                {"col_name": "nWorkCapital", "col_show_name": "净营运资本", "col_comment": "净营运资本-描述"},
                {"col_name": "ic", "col_show_name": "投入资本", "col_comment": "投入资本-描述"},
                {"col_name": "tRe", "col_show_name": "留存收益", "col_comment": "留存收益-描述"},
                {"col_name": "grossProfit", "col_show_name": "毛利", "col_comment": "毛利-描述"},
                {"col_name": "opaProfit", "col_show_name": "经营活动净收益", "col_comment": "经营活动净收益-描述"},
                {"col_name": "valChgProfit", "col_show_name": "价值变动净收益", "col_comment": "价值变动净收益-描述"},
                {"col_name": "nIntExp", "col_show_name": "净利息费用", "col_comment": "净利息费用-描述"},
                {"col_name": "ebit", "col_show_name": "息税前利润", "col_comment": "息税前利润-描述"},
                {"col_name": "ebitda", "col_show_name": "息税折旧摊销前利润", "col_comment": "息税折旧摊销前利润-描述"},
                {"col_name": "ebiat", "col_show_name": "息前税后利润", "col_comment": "息前税后利润-描述"},
                {"col_name": "nrProfitLoss", "col_show_name": "非经常性损益", "col_comment": "非经常性损益-描述"},
                {"col_name": "niAttrPCut", "col_show_name": "扣除非经常性损益后的归属于上市公司股东的净利润",
                 "col_comment": "扣除非经常性损益后的归属于上市公司股东的净利润-描述"},
                {"col_name": "fcff", "col_show_name": "企业自由现金流量", "col_comment": "企业自由现金流量-描述"},
                {"col_name": "fcfe", "col_show_name": "股权自由现金流量", "col_comment": "股权自由现金流量-描述"},
                {"col_name": "da", "col_show_name": "折旧与摊销", "col_comment": "折旧与摊销-描述"},
                {"col_name": "rd", "col_show_name": "研发支出合计", "col_comment": "研发支出合计-描述"},
                {"col_name": "rdENiAttrPCut", "col_show_name": "研发支出前利润", "col_comment": "研发支出前利润-描述"},
                {"col_name": "eps", "col_show_name": "每股收益(期末摊薄)", "col_comment": "每股收益(期末摊薄)-描述"},
                {"col_name": "epsCut", "col_show_name": "扣除每股收益(期末摊薄)", "col_comment": "扣除每股收益(期末摊薄)-描述"},
                {"col_name": "basicEps", "col_show_name": "基本每股收益", "col_comment": "基本每股收益-描述"},
                {"col_name": "dilutedEps", "col_show_name": "稀释每股收益", "col_comment": "稀释每股收益-描述"},
                {"col_name": "basicEpsCut", "col_show_name": "扣除基本每股收益", "col_comment": "扣除基本每股收益-描述"},
                {"col_name": "dilutedEpsCut", "col_show_name": "扣除稀释每股收益", "col_comment": "扣除稀释每股收益-描述"},
                {"col_name": "nAssetPs", "col_show_name": "每股净资产", "col_comment": "每股净资产-描述"},
                {"col_name": "tRevPs", "col_show_name": "每股营业总收入", "col_comment": "每股营业总收入-描述"},
                {"col_name": "revPs", "col_show_name": "每股营业收入", "col_comment": "每股营业收入-描述"},
                {"col_name": "opPs", "col_show_name": "每股营业利润", "col_comment": "每股营业利润-描述"},
                {"col_name": "ebitPs", "col_show_name": "每股息税前利润", "col_comment": "每股息税前利润-描述"},
                {"col_name": "ebitdaPs", "col_show_name": "每股EBITDA", "col_comment": "每股EBITDA-描述"},
                {"col_name": "cReserPs", "col_show_name": "每股资本公积", "col_comment": "每股资本公积-描述"},
                {"col_name": "sReserPs", "col_show_name": "每股盈余公积", "col_comment": "每股盈余公积-描述"},
                {"col_name": "reserPs", "col_show_name": "每股公积金", "col_comment": "每股公积金-描述"},
                {"col_name": "rePs", "col_show_name": "每股未分配利润", "col_comment": "每股未分配利润-描述"},
                {"col_name": "tRePs", "col_show_name": "每股留存收益", "col_comment": "每股留存收益-描述"},
                {"col_name": "nCFOperAPs", "col_show_name": "每股经营活动产生的现金流量净额", "col_comment": "每股经营活动产生的现金流量净额-描述"},
                {"col_name": "nCInCashPs", "col_show_name": "每股现金流量净额", "col_comment": "每股现金流量净额-描述"},
                {"col_name": "fcffPs", "col_show_name": "每股企业自由现金流量", "col_comment": "每股企业自由现金流量-描述"},
                {"col_name": "fcfePs", "col_show_name": "每股股东自由现金流量", "col_comment": "每股股东自由现金流量-描述"},
                {"col_name": "grossMargin", "col_show_name": "销售毛利率", "col_comment": "销售毛利率-描述"},
                {"col_name": "npMargin", "col_show_name": "销售净利润率", "col_comment": "销售净利润率-描述"},
                {"col_name": "scRatio", "col_show_name": "销售成本率", "col_comment": "销售成本率-描述"},
                {"col_name": "periodExpTr", "col_show_name": "销售期间费用率", "col_comment": "销售期间费用率-描述"},
                {"col_name": "pCostExp", "col_show_name": "成本费用利润率", "col_comment": "成本费用利润率-描述"},
                {"col_name": "roe", "col_show_name": "净资产收益率(摊薄)", "col_comment": "净资产收益率(摊薄)-描述"},
                {"col_name": "roeA", "col_show_name": "净资产收益率(平均)", "col_comment": "净资产收益率(平均)-描述"},
                {"col_name": "roeW", "col_show_name": "净资产收益率(加权平均)", "col_comment": "净资产收益率(加权平均)-描述"},
                {"col_name": "roeCut", "col_show_name": "净资产收益率(扣除摊薄)", "col_comment": "净资产收益率(扣除摊薄)-描述"},
                {"col_name": "roeCutA", "col_show_name": "净资产收益率ROE(扣除平均)", "col_comment": "净资产收益率ROE(扣除平均)-描述"},
                {"col_name": "roeCutW", "col_show_name": "净资产收益率(扣除加权平均)", "col_comment": "净资产收益率(扣除加权平均)-描述"},
                {"col_name": "roa", "col_show_name": "总资产净利率", "col_comment": "总资产净利率-描述"},
                {"col_name": "roaEbit", "col_show_name": "总资产报酬率", "col_comment": "总资产报酬率-描述"},
                {"col_name": "roic", "col_show_name": "投入资本回报率", "col_comment": "投入资本回报率-描述"},
                {"col_name": "rop", "col_show_name": "人力投入回报率ROP", "col_comment": "人力投入回报率ROP-描述"},
                {"col_name": "faTurnover", "col_show_name": "固定资产周转率", "col_comment": "固定资产周转率-描述"},
                {"col_name": "dayFa", "col_show_name": "固定资产周转天数", "col_comment": "固定资产周转天数-描述"},
                {"col_name": "tfaTurnover", "col_show_name": "固定资产合计周转率", "col_comment": "固定资产合计周转率-描述"},
                {"col_name": "dayTfa", "col_show_name": "固定资产合计周转天数", "col_comment": "固定资产合计周转天数-描述"},
                {"col_name": "caTurnover", "col_show_name": "流动资产周转率", "col_comment": "流动资产周转率-描述"},
                {"col_name": "ncaTurnover", "col_show_name": "非流动资产周转率", "col_comment": "非流动资产周转率-描述"},
                {"col_name": "taTurnover", "col_show_name": "总资产周转率", "col_comment": "总资产周转率-描述"},
                {"col_name": "invenTurnover", "col_show_name": "存货周转率", "col_comment": "存货周转率-描述"},
                {"col_name": "daysInven", "col_show_name": "存货周转天数", "col_comment": "存货周转天数-描述"},
                {"col_name": "nrArTurnover", "col_show_name": "应收票据及应收账款周转率", "col_comment": "应收票据及应收账款周转率-描述"},
                {"col_name": "daysNrAr", "col_show_name": "应收票据及应收账款周转天数", "col_comment": "应收票据及应收账款周转天数-描述"},
                {"col_name": "arTurnover", "col_show_name": "应收账款周转率", "col_comment": "应收账款周转率-描述"},
                {"col_name": "daysAr", "col_show_name": "应收账款周转天数", "col_comment": "应收账款周转天数-描述"},
                {"col_name": "npApTurnover", "col_show_name": "应付票据及应付账款周转率", "col_comment": "应付票据及应付账款周转率-描述"},
                {"col_name": "daysNpAp", "col_show_name": "应付票据及应付账款周转天数", "col_comment": "应付票据及应付账款周转天数-描述"},
                {"col_name": "apTurnover", "col_show_name": "应付账款周转率", "col_comment": "应付账款周转率-描述"},
                {"col_name": "daysAp", "col_show_name": "应付账款周转天数", "col_comment": "应付账款周转天数-描述"},
                {"col_name": "workCapitalTurnover", "col_show_name": "营运资本周转率", "col_comment": "营运资本周转率-描述"},
                {"col_name": "daysWorkCapital", "col_show_name": "营运资本周转天数", "col_comment": "营运资本周转天数-描述"},
                {"col_name": "nWorkCapitalTurnover", "col_show_name": "净营运资本周转率", "col_comment": "净营运资本周转率-描述"},
                {"col_name": "daysWorkCapital2018", "col_show_name": "净营运资本周转天数", "col_comment": "净营运资本周转天数-描述"},
                {"col_name": "operCycle", "col_show_name": "营业周期", "col_comment": "营业周期-描述"},
                {"col_name": "nOperCycle", "col_show_name": "净营业周期", "col_comment": "净营业周期-描述"},
                {"col_name": "currentRatio", "col_show_name": "流动比率", "col_comment": "流动比率-描述"},
                {"col_name": "quickRatio", "col_show_name": "速动比率", "col_comment": "速动比率-描述"},
                {"col_name": "squickRatio", "col_show_name": "保守速动比率", "col_comment": "保守速动比率-描述"},
                {"col_name": "opCl", "col_show_name": "营业利润/流动负债", "col_comment": "营业利润/流动负债-描述"},
                {"col_name": "opTl", "col_show_name": "营业利润/负债合计", "col_comment": "营业利润/负债合计-描述"},
                {"col_name": "assetLiabRatio", "col_show_name": "资产负债率", "col_comment": "资产负债率-描述"},
                {"col_name": "equityRatio", "col_show_name": "产权比率", "col_comment": "产权比率-描述"},
                {"col_name": "tlTeap", "col_show_name": "负债合计/归属于母公司的股东权益", "col_comment": "负债合计/归属于母公司的股东权益-描述"},
                {"col_name": "teapTl", "col_show_name": "股东权益对负债比率", "col_comment": "股东权益对负债比率-描述"},
                {"col_name": "teapID", "col_show_name": "归属于母公司的股东权益/带息债务", "col_comment": "归属于母公司的股东权益/带息债务-描述"},
                {"col_name": "nTanATl", "col_show_name": "有形净资产/负债合计", "col_comment": "有形净资产/负债合计-描述"},
                {"col_name": "nTanAID", "col_show_name": "有形净资产/带息债务", "col_comment": "有形净资产/带息债务-描述"},
                {"col_name": "nTanANd", "col_show_name": "有形净资产/净债务", "col_comment": "有形净资产/净债务-描述"},
                {"col_name": "ebitdaTl", "col_show_name": "息税折旧摊销前利润/负债合计", "col_comment": "息税折旧摊销前利润/负债合计-描述"},
                {"col_name": "ebitdaID", "col_show_name": "息税折旧摊销前利润/带息债务", "col_comment": "息税折旧摊销前利润/带息债务-描述"},
                {"col_name": "cashIcl", "col_show_name": "货币资金/带息流动负债", "col_comment": "货币资金/带息流动负债-描述"},
                {"col_name": "cashCl", "col_show_name": "货币资金/流动负债", "col_comment": "货币资金/流动负债-描述"},
                {"col_name": "nCFOpaCl", "col_show_name": "经营活动现金流量净额/流动负债", "col_comment": "经营活动现金流量净额/流动负债-描述"},
                {"col_name": "nCFOpaLiab", "col_show_name": "经营活动现金流量净额/负债合计", "col_comment": "经营活动现金流量净额/负债合计-描述"},
                {"col_name": "nCFOpaID", "col_show_name": "经营活动现金流量净额/带息债务", "col_comment": "经营活动现金流量净额/带息债务-描述"},
                {"col_name": "nCFOpaNd", "col_show_name": "经营活动现金流量净额/净债务", "col_comment": "经营活动现金流量净额/净债务-描述"},
                {"col_name": "nCFOpaNcl", "col_show_name": "经营活动现金流量净额/非流动负债", "col_comment": "经营活动现金流量净额/非流动负债-描述"},
                {"col_name": "nCFNfaCl", "col_show_name": "非筹资性现金流量净额/流动负债", "col_comment": "非筹资性现金流量净额/流动负债-描述"},
                {"col_name": "nCFNfaLiab", "col_show_name": "非筹资性现金流量净额/负债总额", "col_comment": "非筹资性现金流量净额/负债总额-描述"},
                {"col_name": "nclWc", "col_show_name": "非流动负债与营运资金比率", "col_comment": "非流动负债与营运资金比率-描述"},
                {"col_name": "timesInteEbit", "col_show_name": "EBIT利息保障倍数", "col_comment": "EBIT利息保障倍数-描述"},
                {"col_name": "timesInteEbitda", "col_show_name": "EBITDA利息保障倍数", "col_comment": "EBITDA利息保障倍数-描述"},
                {"col_name": "timesInteCF", "col_show_name": "现金流量利息保障倍数", "col_comment": "现金流量利息保障倍数-描述"},
                {"col_name": "cashRatio", "col_show_name": "现金比率", "col_comment": "现金比率-描述"},
                {"col_name": "nCFOpaDebtDue", "col_show_name": "现金到期债务比", "col_comment": "现金到期债务比-描述"},
                {"col_name": "ltLiabRatio", "col_show_name": "长期负债占比", "col_comment": "长期负债占比-描述"},
                {"col_name": "nrArRecR", "col_show_name": "应收票据及应收账款回款率", "col_comment": "应收票据及应收账款回款率-描述"},
                {"col_name": "nrArR", "col_show_name": "应收票据及应收账款/营业收入", "col_comment": "应收票据及应收账款/营业收入-描述"},
                {"col_name": "arRecR", "col_show_name": "应收账款回款率", "col_comment": "应收账款回款率-描述"},
                {"col_name": "arR", "col_show_name": "应收账款/营业收入", "col_comment": "应收账款/营业收入-描述"},
                {"col_name": "advRR", "col_show_name": "预收款项/营业收入", "col_comment": "预收款项/营业收入-描述"},
                {"col_name": "cfsgsR", "col_show_name": "销售商品提供劳务收到的现金/营业收入", "col_comment": "销售商品提供劳务收到的现金/营业收入-描述"},
                {"col_name": "nCFOpaTr", "col_show_name": "经营活动产生的现金流量净额/营业总收入",
                 "col_comment": "经营活动产生的现金流量净额/营业总收入-描述"},
                {"col_name": "nCFOpaR", "col_show_name": "经营活动产生的现金流量净额/营业收入", "col_comment": "经营活动产生的现金流量净额/营业收入-描述"},
                {"col_name": "nCFOpaOpap", "col_show_name": "经营活动产生的现金流量净额/经营活动净收益",
                 "col_comment": "经营活动产生的现金流量净额/经营活动净收益-描述"},
                {"col_name": "nCFOpaOp", "col_show_name": "经营活动产生的现金流量净额/营业利润", "col_comment": "经营活动产生的现金流量净额/营业利润-描述"},
                {"col_name": "nCFOpaNia", "col_show_name": "经营活动产生的现金流量净额/净利润", "col_comment": "经营活动产生的现金流量净额/净利润-描述"},
                {"col_name": "pFixaODa", "col_show_name": "投资支出/折旧和摊销", "col_comment": "投资支出/折旧和摊销-描述"},
                {"col_name": "cRcvryA", "col_show_name": "全部资产现金回收率", "col_comment": "全部资产现金回收率-描述"},
                {"col_name": "nCFOpaPropt", "col_show_name": "经营活动产生的现金流量净额占比", "col_comment": "经营活动产生的现金流量净额占比-描述"},
                {"col_name": "nCFIaPropt", "col_show_name": "投资活动产生的现金流量净额占比", "col_comment": "投资活动产生的现金流量净额占比-描述"},
                {"col_name": "nCFFaPropt", "col_show_name": "筹资活动产生的现金流量净额占比", "col_comment": "筹资活动产生的现金流量净额占比-描述"},
                {"col_name": "cashMInvRatio", "col_show_name": "现金满足投资比率", "col_comment": "现金满足投资比率-描述"},
                {"col_name": "cashOperRatio", "col_show_name": "现金营运指数", "col_comment": "现金营运指数-描述"},
                {"col_name": "cashDivCover", "col_show_name": "现金股利保障倍数", "col_comment": "现金股利保障倍数-描述"},
                {"col_name": "tRevenueYoy", "col_show_name": "营业总收入同比增长", "col_comment": "营业总收入同比增长-描述"},
                {"col_name": "revenueYoy", "col_show_name": "营业收入同比增长", "col_comment": "营业收入同比增长-描述"},
                {"col_name": "operProfitYoy", "col_show_name": "营业利润同比增长", "col_comment": "营业利润同比增长-描述"},
                {"col_name": "tProfitYoy", "col_show_name": "利润总额同比增长", "col_comment": "利润总额同比增长-描述"},
                {"col_name": "niYoy", "col_show_name": "净利润同比增长", "col_comment": "净利润同比增长-描述"},
                {"col_name": "niAttrPYoy", "col_show_name": "归属于母公司净利润同比增长", "col_comment": "归属于母公司净利润同比增长-描述"},
                {"col_name": "rDExpYoy", "col_show_name": "研发费用同比增长", "col_comment": "研发费用同比增长-描述"},
                {"col_name": "niAttrPCutYoy", "col_show_name": "归属于母公司净利润(扣除)同比增长",
                 "col_comment": "归属于母公司净利润(扣除)同比增长-描述"},
                {"col_name": "tFaYtd", "col_show_name": "固定资产相对年初增长", "col_comment": "固定资产相对年初增长-描述"},
                {"col_name": "roeYoy", "col_show_name": "净资产收益率(摊薄)同比增长", "col_comment": "净资产收益率(摊薄)同比增长-描述"},
                {"col_name": "nCFOpaYoy", "col_show_name": "经营活动产生的现金流量净额同比增长", "col_comment": "经营活动产生的现金流量净额同比增长-描述"},
                {"col_name": "basicEpsYoy", "col_show_name": "基本每股收益同比增长", "col_comment": "基本每股收益同比增长-描述"},
                {"col_name": "dilutedEpsYoy", "col_show_name": "稀释每股收益同比增长", "col_comment": "稀释每股收益同比增长-描述"},
                {"col_name": "nCFOpaPsYoy", "col_show_name": "每股经营活动产生的现金流量净额同比增长",
                 "col_comment": "每股经营活动产生的现金流量净额同比增长-描述"},
                {"col_name": "naPsYtd", "col_show_name": "每股净资产相对年初增长", "col_comment": "每股净资产相对年初增长-描述"},
                {"col_name": "taYtd", "col_show_name": "总资产相对年初增长", "col_comment": "总资产相对年初增长-描述"},
                {"col_name": "naYtd", "col_show_name": "净资产相对年初增长", "col_comment": "净资产相对年初增长-描述"},
                {"col_name": "teAttrPYtd", "col_show_name": "归属于母公司的股东权益相对年初增长", "col_comment": "归属于母公司的股东权益相对年初增长-描述"},
                {"col_name": "tlYtd", "col_show_name": "总负债相对年初增长", "col_comment": "总负债相对年初增长-描述"},
                {"col_name": "cashCeYtd", "col_show_name": "货币资金相对年初增长", "col_comment": "货币资金相对年初增长-描述"},
                {"col_name": "epsYoy", "col_show_name": "每股收益EPS同比增长", "col_comment": "每股收益EPS同比增长-描述"},
                {"col_name": "epsCutYoy", "col_show_name": "扣非后每股收益EPS同比增长", "col_comment": "扣非后每股收益EPS同比增长-描述"},
                {"col_name": "cogsYoy", "col_show_name": "营业成本同比增长", "col_comment": "营业成本同比增长-描述"},
                {"col_name": "grossProfitYoy", "col_show_name": "毛利同比增长", "col_comment": "毛利同比增长-描述"},
                {"col_name": "npMarginYoy", "col_show_name": "销售净利率同比增长", "col_comment": "销售净利率同比增长-描述"},
                {"col_name": "cFrSaleGSYoy", "col_show_name": "销售商品、提供劳务收到的现金同比增长",
                 "col_comment": "销售商品、提供劳务收到的现金同比增长-描述"},
                {"col_name": "cPaidGSYoy", "col_show_name": "购买商品、接受劳务支付的现金同比增长",
                 "col_comment": "购买商品、接受劳务支付的现金同比增长-描述"},
                {"col_name": "cPToForEmplYoy", "col_show_name": "支付给职工以及为职工支付的现金同比增长",
                 "col_comment": "支付给职工以及为职工支付的现金同比增长-描述"},
                {"col_name": "nCFOpaNiaYoy", "col_show_name": "净利润现金含量同比增长", "col_comment": "净利润现金含量同比增长-描述"},
                {"col_name": "cTa", "col_show_name": "货币资金/总资产", "col_comment": "货币资金/总资产-描述"},
                {"col_name": "nrArTa", "col_show_name": "应收票据及应收账款/总资产", "col_comment": "应收票据及应收账款/总资产-描述"},
                {"col_name": "arTa", "col_show_name": "应收账款/总资产", "col_comment": "应收账款/总资产-描述"},
                {"col_name": "repayTa", "col_show_name": "预付账款/总资产", "col_comment": "预付账款/总资产-描述"},
                {"col_name": "invenTa", "col_show_name": "存货/总资产", "col_comment": "存货/总资产-描述"},
                {"col_name": "caTa", "col_show_name": "流动资产/总资产", "col_comment": "流动资产/总资产-描述"},
                {"col_name": "fixedATTa", "col_show_name": "固定资产/总资产", "col_comment": "固定资产/总资产-描述"},
                {"col_name": "tFixedATa", "col_show_name": "固定资产合计/总资产", "col_comment": "固定资产合计/总资产-描述"},
                {"col_name": "intanATa", "col_show_name": "无形资产/总资产", "col_comment": "无形资产/总资产-描述"},
                {"col_name": "ltAmorExpTa", "col_show_name": "长期待摊费用/总资产", "col_comment": "长期待摊费用/总资产-描述"},
                {"col_name": "ncaTa", "col_show_name": "非流动资产/总资产", "col_comment": "非流动资产/总资产-描述"},
                {"col_name": "npApTa", "col_show_name": "应付票据及应付账款/总资产", "col_comment": "应付票据及应付账款/总资产-描述"},
                {"col_name": "apTa", "col_show_name": "应付账款/总资产", "col_comment": "应付账款/总资产-描述"},
                {"col_name": "advRTa", "col_show_name": "预收款项/总资产", "col_comment": "预收款项/总资产-描述"},
                {"col_name": "stBorrTa", "col_show_name": "短期借款/总资产", "col_comment": "短期借款/总资产-描述"},
                {"col_name": "ltBorrTa", "col_show_name": "长期借款/总资产", "col_comment": "长期借款/总资产-描述"},
                {"col_name": "bpTa", "col_show_name": "应付债券/总资产", "col_comment": "应付债券/总资产-描述"},
                {"col_name": "nTanATa", "col_show_name": "有形净资产/总资产", "col_comment": "有形净资产/总资产-描述"},
                {"col_name": "treTa", "col_show_name": "留存收益/总资产", "col_comment": "留存收益/总资产-描述"},
                {"col_name": "teapTa", "col_show_name": "归属于母公司的股东权益/总资产", "col_comment": "归属于母公司的股东权益/总资产-描述"},
                {"col_name": "tseTa", "col_show_name": "所有者权益/总资产", "col_comment": "所有者权益/总资产-描述"},
                {"col_name": "idIc", "col_show_name": "带息债务/投入资本", "col_comment": "带息债务/投入资本-描述"},
                {"col_name": "teapIc", "col_show_name": "归属于母公司的股东权益/投入资本", "col_comment": "归属于母公司的股东权益/投入资本-描述"},
                {"col_name": "clTa", "col_show_name": "流动负债/负债合计", "col_comment": "流动负债/负债合计-描述"},
                {"col_name": "nclTa", "col_show_name": "非流动负债/负债合计", "col_comment": "非流动负债/负债合计-描述"},
                {"col_name": "equMultiplier", "col_show_name": "权益乘数", "col_comment": "权益乘数-描述"},
                {"col_name": "capFixRatio", "col_show_name": "资本固定化比率", "col_comment": "资本固定化比率-描述"},
                {"col_name": "ltDebtCapRatio", "col_show_name": "长期资本负债率", "col_comment": "长期资本负债率-描述"},
                {"col_name": "ltAssetSuitRatio", "col_show_name": "长期资产适合率", "col_comment": "长期资产适合率-描述"},
                {"col_name": "nclTeap", "col_show_name": "非流动负债合计／归属母公司股东的权益", "col_comment": "非流动负债合计／归属母公司股东的权益-描述"},
                {"col_name": "clTeap", "col_show_name": "流动负债合计／归属母公司股东的权益", "col_comment": "流动负债合计／归属母公司股东的权益-描述"},
                {"col_name": "rTr", "col_show_name": "营业收入/营业总收入", "col_comment": "营业收入/营业总收入-描述"},
                {"col_name": "tcogsTr", "col_show_name": "营业总成本/营业总收入", "col_comment": "营业总成本/营业总收入-描述"},
                {"col_name": "cogsTr", "col_show_name": "营业成本/营业总收入", "col_comment": "营业成本/营业总收入-描述"},
                {"col_name": "btaxSurchgTr", "col_show_name": "营业税金及附加/营业总收入", "col_comment": "营业税金及附加/营业总收入-描述"},
                {"col_name": "sellExpTr", "col_show_name": "销售费用/营业总收入", "col_comment": "销售费用/营业总收入-描述"},
                {"col_name": "adminExpTr", "col_show_name": "管理费用/营业总收入", "col_comment": "管理费用/营业总收入-描述"},
                {"col_name": "rDExpTr", "col_show_name": "研发费用/营业总收入", "col_comment": "研发费用/营业总收入-描述"},
                {"col_name": "finanExpTr", "col_show_name": "财务费用/营业总收入", "col_comment": "财务费用/营业总收入-描述"},
                {"col_name": "ailTr", "col_show_name": "资产减值损失/营业总收入", "col_comment": "资产减值损失/营业总收入-描述"},
                {"col_name": "cilTr", "col_show_name": "信用减值损失/营业总收入", "col_comment": "信用减值损失/营业总收入-描述"},
                {"col_name": "opaPTr", "col_show_name": "经营活动净收益/营业总收入", "col_comment": "经营活动净收益/营业总收入-描述"},
                {"col_name": "valChgPTr", "col_show_name": "价值变动净收益/营业总收入", "col_comment": "价值变动净收益/营业总收入-描述"},
                {"col_name": "fvChgGTr", "col_show_name": "公允价值变动收益/营业总收入", "col_comment": "公允价值变动收益/营业总收入-描述"},
                {"col_name": "invIncTr", "col_show_name": "投资收益/营业总收入", "col_comment": "投资收益/营业总收入-描述"},
                {"col_name": "opTr", "col_show_name": "营业利润/营业总收入", "col_comment": "营业利润/营业总收入-描述"},
                {"col_name": "nopgTr", "col_show_name": "营业外收入/营业总收入", "col_comment": "营业外收入/营业总收入-描述"},
                {"col_name": "noplTr", "col_show_name": "营业外支出/营业总收入", "col_comment": "营业外支出/营业总收入-描述"},
                {"col_name": "tpTr", "col_show_name": "利润总额/营业总收入", "col_comment": "利润总额/营业总收入-描述"},
                {"col_name": "itTr", "col_show_name": "所得税/营业总收入", "col_comment": "所得税/营业总收入-描述"},
                {"col_name": "niTr", "col_show_name": "净利润/营业总收入", "col_comment": "净利润/营业总收入-描述"},
                {"col_name": "ebitdaTr", "col_show_name": "EBITDA/营业总收入", "col_comment": "EBITDA/营业总收入-描述"},
                {"col_name": "ebitTr", "col_show_name": "EBIT/营业总收入", "col_comment": "EBIT/营业总收入-描述"},
                {"col_name": "opaPTp", "col_show_name": "经营活动净收益/利润总额", "col_comment": "经营活动净收益/利润总额-描述"},
                {"col_name": "valChgPTp", "col_show_name": "价值变动净收益/利润总额", "col_comment": "价值变动净收益/利润总额-描述"},
                {"col_name": "opTp", "col_show_name": "营业利润/利润总额", "col_comment": "营业利润/利润总额-描述"},
                {"col_name": "nNopiTp", "col_show_name": "营业外收支净额/利润总额", "col_comment": "营业外收支净额/利润总额-描述"},
                {"col_name": "itTp", "col_show_name": "所得税/利润总额", "col_comment": "所得税/利润总额-描述"},
                {"col_name": "niCutNi", "col_show_name": "扣除非经常损益后的归母净利润/归母净利润",
                 "col_comment": "扣除非经常损益后的归母净利润/归母净利润-描述"}
            ]
        }
    define_json = json.dumps(fdmtmaindatapit_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def fdmtcfs_define(table_name):

    fdmtcfs_str = {
            "table_name": "fdmtcfs",
            "table_show_name": "现金流量表补充表(Point in time)",
            "table_comment": "现金流量表补充表(Point in time)-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "证券展示代码", "col_comment": "证券展示代码-描述"},
                {"col_name": "ticker", "col_show_name": "交易代码", "col_comment": "交易代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD",
                 "col_show_name": "通联编制的证券市场编码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所等。对应DataAPI.SysCodeGet.codeTypeID=10002。",
                 "col_comment": "通联编制的证券市场编码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所等。对应DataAPI.SysCodeGet.codeTypeID=10002。-描述"},
                {"col_name": "publishDate", "col_show_name": "发布日期", "col_comment": "发布日期-描述"},
                {"col_name": "endDate", "col_show_name": "截止日期", "col_comment": "截止日期-描述"},
                {"col_name": "endDateRep", "col_show_name": "报表截止时间", "col_comment": "报表截止时间-描述"},
                {"col_name": "reportType",
                 "col_show_name": "报告类型。Q1-第一季报，S1-半年报，CQ3-三季报（累计1-9月），A-年报。对应DataAPI.SysCodeGet.codeTypeID=70001。",
                 "col_comment": "报告类型。Q1-第一季报，S1-半年报，CQ3-三季报（累计1-9月），A-年报。对应DataAPI.SysCodeGet.codeTypeID=70001。-描述"},
                {"col_name": "fiscalPeriod", "col_show_name": "会计期间", "col_comment": "会计期间-描述"},
                {"col_name": "mergedFlag", "col_show_name": "合并类型。1-合并,2-母公司。对应DataAPI.SysCodeGet.codeTypeID=70003。",
                 "col_comment": "合并类型。1-合并,2-母公司。对应DataAPI.SysCodeGet.codeTypeID=70003。-描述"},
                {"col_name": "accoutingStandARds", "col_show_name": "会计准则", "col_comment": "会计准则-描述"},
                {"col_name": "currencyCD",
                 "col_show_name": "货币代码。例如，USD-美元；CAD-加元等。对应DataAPI.SysCodeGet.codeTypeID=10004。",
                 "col_comment": "货币代码。例如，USD-美元；CAD-加元等。对应DataAPI.SysCodeGet.codeTypeID=10004。-描述"},
                {"col_name": "NIncome", "col_show_name": "净利润", "col_comment": "净利润-描述"},
                {"col_name": "assetsImpairLoss", "col_show_name": "资产减值准备", "col_comment": "资产减值准备-描述"},
                {"col_name": "FAOGPBDepr", "col_show_name": "固定资产折旧、油气资产折耗、生产性生物资产折旧",
                 "col_comment": "固定资产折旧、油气资产折耗、生产性生物资产折旧-描述"},
                {"col_name": "intanAssetsAmor", "col_show_name": "无形资产摊销", "col_comment": "无形资产摊销-描述"},
                {"col_name": "LTAmorExpAmor", "col_show_name": "长期待摊费用摊销", "col_comment": "长期待摊费用摊销-描述"},
                {"col_name": "amorExpDecr", "col_show_name": "待摊费用减少", "col_comment": "待摊费用减少-描述"},
                {"col_name": "accrExpIncr", "col_show_name": "预提费用增加", "col_comment": "预提费用增加-描述"},
                {"col_name": "dispFaOthLoss", "col_show_name": "处置固定资产、无形资产和其他长期资产的损失",
                 "col_comment": "处置固定资产、无形资产和其他长期资产的损失-描述"},
                {"col_name": "FAWritOff", "col_show_name": "固定资产报废损失", "col_comment": "固定资产报废损失-描述"},
                {"col_name": "FValueChgLoss", "col_show_name": "公允价值变动损失", "col_comment": "公允价值变动损失-描述"},
                {"col_name": "finanExp", "col_show_name": "财务费用", "col_comment": "财务费用-描述"},
                {"col_name": "invLoss", "col_show_name": "投资损失", "col_comment": "投资损失-描述"},
                {"col_name": "deferTaDecr", "col_show_name": "递延所得税资产减少", "col_comment": "递延所得税资产减少-描述"},
                {"col_name": "deferTlIncr", "col_show_name": "递延所得税负债增加", "col_comment": "递延所得税负债增加-描述"},
                {"col_name": "invenDecr", "col_show_name": "存货的减少", "col_comment": "存货的减少-描述"},
                {"col_name": "operReceiDecr", "col_show_name": "经营性应收项目的减少", "col_comment": "经营性应收项目的减少-描述"},
                {"col_name": "operPayaIncr", "col_show_name": "经营性应付项目的增加", "col_comment": "经营性应付项目的增加-描述"},
                {"col_name": "other", "col_show_name": "其他", "col_comment": "其他-描述"},
                {"col_name": "specNOCF1", "col_show_name": "(附注)经营活动现金流量净额特殊项目",
                 "col_comment": "(附注)经营活动现金流量净额特殊项目-描述"},
                {"col_name": "ANOCF1", "col_show_name": "(附注)经营活动现金流量净额调整项目", "col_comment": "(附注)经营活动现金流量净额调整项目-描述"},
                {"col_name": "NCFOperateANotes", "col_show_name": "经营活动产生的现金流量净额", "col_comment": "经营活动产生的现金流量净额-描述"},
                {"col_name": "contrANOCF", "col_show_name": "加:经营流量净额前后对比调整项目", "col_comment": "加:经营流量净额前后对比调整项目-描述"},
                {"col_name": "convDebtCAPi", "col_show_name": "债务转为资本", "col_comment": "债务转为资本-描述"},
                {"col_name": "convBonds1Y", "col_show_name": "一年内到期的可转换公司债券", "col_comment": "一年内到期的可转换公司债券-描述"},
                {"col_name": "finanLeaFA", "col_show_name": "融资租入固定资产", "col_comment": "融资租入固定资产-描述"},
                {"col_name": "CEndBal", "col_show_name": "现金的期末余额", "col_comment": "现金的期末余额-描述"},
                {"col_name": "CBegBal", "col_show_name": "现金的期初余额", "col_comment": "现金的期初余额-描述"},
                {"col_name": "CEEndBal", "col_show_name": "现金等价物的期末余额", "col_comment": "现金等价物的期末余额-描述"},
                {"col_name": "CEBegBal", "col_show_name": "现金等价物的期初余额", "col_comment": "现金等价物的期初余额-描述"},
                {"col_name": "specC", "col_show_name": "现金特殊项目", "col_comment": "现金特殊项目-描述"},
                {"col_name": "AC", "col_show_name": "现金调整项目", "col_comment": "现金调整项目-描述"},
                {"col_name": "NChangeInCash", "col_show_name": "现金及现金等价物净增加额", "col_comment": "现金及现金等价物净增加额-描述"},
                {"col_name": "contrANC", "col_show_name": "加:现金净额前后对比调整项目", "col_comment": "加:现金净额前后对比调整项目-描述"}
            ]
        }
    define_json = json.dumps(fdmtcfs_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def fdmte_define(table_name):

    fdmte_str = {
            "table_name": "fdmte",
            "table_show_name": "业绩快报(PIT)",
            "table_comment": "-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "证券内部编码", "col_comment": "证券内部编码-描述"},
                {"col_name": "publishDate", "col_show_name": "发布日期", "col_comment": "发布日期-描述"},
                {"col_name": "endDate", "col_show_name": "截止日期", "col_comment": "截止日期-描述"},
                {"col_name": "partyID", "col_show_name": "公司代码", "col_comment": "公司代码-描述"},
                {"col_name": "ticker", "col_show_name": "交易代码", "col_comment": "交易代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD",
                 "col_show_name": "通联编制的证券市场编码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所等。对应DataAPI.SysCodeGet.codeTypeID=10002。",
                 "col_comment": "通联编制的证券市场编码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所等。对应DataAPI.SysCodeGet.codeTypeID=10002。-描述"},
                {"col_name": "actPubtime", "col_show_name": "实际发布时间", "col_comment": "实际发布时间-描述"},
                {"col_name": "mergedFlag", "col_show_name": "合并类型。1-合并,2-母公司。对应DataAPI.SysCodeGet.codeTypeID=70003。",
                 "col_comment": "合并类型。1-合并,2-母公司。对应DataAPI.SysCodeGet.codeTypeID=70003。-描述"},
                {"col_name": "reportType",
                 "col_show_name": "报告类型。Q1-第一季报，S1-半年报，Q3-第三季报，CQ3-三季报（累计1-9月），A-年报。对应DataAPI.SysCodeGet.codeTypeID=70001。",
                 "col_comment": "报告类型。Q1-第一季报，S1-半年报，Q3-第三季报，CQ3-三季报（累计1-9月），A-年报。对应DataAPI.SysCodeGet.codeTypeID=70001。-描述"},
                {"col_name": "fiscalPeriod", "col_show_name": "会计期间", "col_comment": "会计期间-描述"},
                {"col_name": "accoutingStandards", "col_show_name": "会计准则", "col_comment": "会计准则-描述"},
                {"col_name": "currencyCD",
                 "col_show_name": "货币代码。例如，USD-美元；CAD-加元等。对应DataAPI.SysCodeGet.codeTypeID=10004。",
                 "col_comment": "货币代码。例如，USD-美元；CAD-加元等。对应DataAPI.SysCodeGet.codeTypeID=10004。-描述"},
                {"col_name": "revenue", "col_show_name": "营业收入", "col_comment": "营业收入-描述"},
                {"col_name": "primeOperRev", "col_show_name": "主营业务收入", "col_comment": "主营业务收入-描述"},
                {"col_name": "grossProfit", "col_show_name": "主营业务利润", "col_comment": "主营业务利润-描述"},
                {"col_name": "operateProfit", "col_show_name": "营业利润", "col_comment": "营业利润-描述"},
                {"col_name": "TProfit", "col_show_name": "利润总额", "col_comment": "利润总额-描述"},
                {"col_name": "NIncomeAttrP", "col_show_name": "归属于母公司所有者的净利润", "col_comment": "归属于母公司所有者的净利润-描述"},
                {"col_name": "NIncomeCut", "col_show_name": "扣除非经常性损益后净利润", "col_comment": "扣除非经常性损益后净利润-描述"},
                {"col_name": "NCfOperA", "col_show_name": "经营活动现金流量净额", "col_comment": "经营活动现金流量净额-描述"},
                {"col_name": "basicEPS", "col_show_name": "基本每股收益(元/股)", "col_comment": "基本每股收益(元/股)-描述"},
                {"col_name": "EPSW", "col_show_name": "加权平均每股收益(元/股)", "col_comment": "加权平均每股收益(元/股)-描述"},
                {"col_name": "EPSCut", "col_show_name": "扣除非经常损益后的基本每股收益(元/股)",
                 "col_comment": "扣除非经常损益后的基本每股收益(元/股)-描述"},
                {"col_name": "EPSCutW", "col_show_name": "扣除非经常损益后的加权每股收益(元/股)",
                 "col_comment": "扣除非经常损益后的加权每股收益(元/股)-描述"},
                {"col_name": "ROE", "col_show_name": "全面摊薄净资产收益率(%)", "col_comment": "全面摊薄净资产收益率(%)-描述"},
                {"col_name": "ROEW", "col_show_name": "加权平均净资产收益率(%)", "col_comment": "加权平均净资产收益率(%)-描述"},
                {"col_name": "ROECut", "col_show_name": "扣除非经常性损益的全面摊薄净资产收益率(%)",
                 "col_comment": "扣除非经常性损益的全面摊薄净资产收益率(%)-描述"},
                {"col_name": "ROECutW", "col_show_name": "扣除非经常性损益后的加权平均净资产收益率(%)",
                 "col_comment": "扣除非经常性损益后的加权平均净资产收益率(%)-描述"},
                {"col_name": "NCfOperAPs", "col_show_name": "每股经营活动现金流量净额(元/股)", "col_comment": "每股经营活动现金流量净额(元/股)-描述"},
                {"col_name": "TAssets", "col_show_name": "总资产", "col_comment": "总资产-描述"},
                {"col_name": "TEquityAttrP", "col_show_name": "归属于母公司所有者权益合计", "col_comment": "归属于母公司所有者权益合计-描述"},
                {"col_name": "paidInCapital", "col_show_name": "股本", "col_comment": "股本-描述"},
                {"col_name": "NAssetPS", "col_show_name": "每股净资产(元)", "col_comment": "每股净资产(元)-描述"},
                {"col_name": "revenueLY", "col_show_name": "上年同期营业收入", "col_comment": "上年同期营业收入-描述"},
                {"col_name": "primeOperRevLY", "col_show_name": "上年同期主营业务收入", "col_comment": "上年同期主营业务收入-描述"},
                {"col_name": "grossProfitLY", "col_show_name": "上年同期主营业务利润", "col_comment": "上年同期主营业务利润-描述"},
                {"col_name": "operProfitLY", "col_show_name": "上年同期营业利润", "col_comment": "上年同期营业利润-描述"},
                {"col_name": "TProfitLY", "col_show_name": "上年同期利润总额", "col_comment": "上年同期利润总额-描述"},
                {"col_name": "NIncomeAttrPLY", "col_show_name": "上年同期归属于母公司所有者的净利润",
                 "col_comment": "上年同期归属于母公司所有者的净利润-描述"},
                {"col_name": "NIncomeCutLY", "col_show_name": "上年同期扣除非经常性损益后净利润", "col_comment": "上年同期扣除非经常性损益后净利润-描述"},
                {"col_name": "NCfOperALY", "col_show_name": "上年同期经营活动现金流量净额", "col_comment": "上年同期经营活动现金流量净额-描述"},
                {"col_name": "basicEPSLY", "col_show_name": "上年同期基本每股收益(元/股)", "col_comment": "上年同期基本每股收益(元/股)-描述"},
                {"col_name": "EPSWLY", "col_show_name": "上年同期加权平均每股收益(元/股)", "col_comment": "上年同期加权平均每股收益(元/股)-描述"},
                {"col_name": "EPSCutLY", "col_show_name": "上年同期扣除非经常损益后的基本每股收益(元/股)",
                 "col_comment": "上年同期扣除非经常损益后的基本每股收益(元/股)-描述"},
                {"col_name": "EPSCutWLY", "col_show_name": "上年同期扣除非经常损益后的加权每股收益(元/股)",
                 "col_comment": "上年同期扣除非经常损益后的加权每股收益(元/股)-描述"},
                {"col_name": "ROELY", "col_show_name": "上年同期期末净资产收益率(%)", "col_comment": "上年同期期末净资产收益率(%)-描述"},
                {"col_name": "ROEWLY", "col_show_name": "上年同期加权平均净资产收益率(%)", "col_comment": "上年同期加权平均净资产收益率(%)-描述"},
                {"col_name": "ROECutLY", "col_show_name": "上年同期扣除非经常性损益的期末净资产收益率(%)",
                 "col_comment": "上年同期扣除非经常性损益的期末净资产收益率(%)-描述"},
                {"col_name": "ROECutWLY", "col_show_name": "上年同期扣除非经常性损益后的加权平均净资产收益率(%)",
                 "col_comment": "上年同期扣除非经常性损益后的加权平均净资产收益率(%)-描述"},
                {"col_name": "NCfOperAPsLY", "col_show_name": "上年同期每股经营活动现金流量净额(元/股)",
                 "col_comment": "上年同期每股经营活动现金流量净额(元/股)-描述"},
                {"col_name": "TAssetsLY", "col_show_name": "期初总资产", "col_comment": "期初总资产-描述"},
                {"col_name": "TEquityAttrPLY", "col_show_name": "期初归属于母公司所有者权益合计", "col_comment": "期初归属于母公司所有者权益合计-描述"},
                {"col_name": "NAssetPsLY", "col_show_name": "期初每股净资产(元)", "col_comment": "期初每股净资产(元)-描述"},
                {"col_name": "revenueYOY", "col_show_name": "营业收入同比(%)", "col_comment": "营业收入同比(%)-描述"},
                {"col_name": "primeOperRevYOY", "col_show_name": "主营业务收入同比(%)", "col_comment": "主营业务收入同比(%)-描述"},
                {"col_name": "grossProfitYOY", "col_show_name": "主营业务利润同比(%)", "col_comment": "主营业务利润同比(%)-描述"},
                {"col_name": "operProfitYOY", "col_show_name": "营业利润同比(%)", "col_comment": "营业利润同比(%)-描述"},
                {"col_name": "TProfitYOY", "col_show_name": "利润总额同比(%)", "col_comment": "利润总额同比(%)-描述"},
                {"col_name": "NIncomeAttrPYOY", "col_show_name": "归属于母公司所有者的净利润同比(%)",
                 "col_comment": "归属于母公司所有者的净利润同比(%)-描述"},
                {"col_name": "NIncomeCutYOY", "col_show_name": "扣除非经常性损益后净利润同比(%)",
                 "col_comment": "扣除非经常性损益后净利润同比(%)-描述"},
                {"col_name": "NCFOperAYOY", "col_show_name": "经营活动现金流量净额同比(%)", "col_comment": "经营活动现金流量净额同比(%)-描述"},
                {"col_name": "basicEPSYOY", "col_show_name": "基本每股收益同比(%)", "col_comment": "基本每股收益同比(%)-描述"},
                {"col_name": "EPSWYOY", "col_show_name": "加权平均每股收益同比(%)", "col_comment": "加权平均每股收益同比(%)-描述"},
                {"col_name": "EPSCutYOY", "col_show_name": "扣除非经常损益后的基本每股收益同比(%)",
                 "col_comment": "扣除非经常损益后的基本每股收益同比(%)-描述"},
                {"col_name": "EPSCutWYOY", "col_show_name": "扣除非经常损益后的加权每股收益同比(%)",
                 "col_comment": "扣除非经常损益后的加权每股收益同比(%)-描述"},
                {"col_name": "ROEYOY", "col_show_name": "期末净资产收益率同比(%)", "col_comment": "期末净资产收益率同比(%)-描述"},
                {"col_name": "ROEWYOY", "col_show_name": "加权平均净资产收益率同比(%)", "col_comment": "加权平均净资产收益率同比(%)-描述"},
                {"col_name": "ROECutYOY", "col_show_name": "扣除非经常性损益的期末净资产收益率同比(%)",
                 "col_comment": "扣除非经常性损益的期末净资产收益率同比(%)-描述"},
                {"col_name": "ROECutWYOY", "col_show_name": "扣除非经常性损益后的加权平均净资产收益率同比(%)",
                 "col_comment": "扣除非经常性损益后的加权平均净资产收益率同比(%)-描述"},
                {"col_name": "NCfOperAPsYOY", "col_show_name": "每股经营活动现金流量净额同比(%)",
                 "col_comment": "每股经营活动现金流量净额同比(%)-描述"},
                {"col_name": "TAssetsYOY", "col_show_name": "总资产同比(%)", "col_comment": "总资产同比(%)-描述"},
                {"col_name": "TEquityAttrPYOY", "col_show_name": "归属于母公司所有者权益同比(%)",
                 "col_comment": "归属于母公司所有者权益同比(%)-描述"},
                {"col_name": "NAssetPsYOY", "col_show_name": "每股净资产同比(%)", "col_comment": "每股净资产同比(%)-描述"},
                {"col_name": "updateTime", "col_show_name": "更新时间", "col_comment": "更新时间-描述"}
            ]
        }
    define_json = json.dumps(fdmte_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def fdmtmainopern_define(table_name):

    fdmtmainopern_str = {
            "table_name": "fdmtmainopern",
            "table_show_name": "主营业务构成(基础数据)",
            "table_comment": "主营业务构成(基础数据)-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "partyID", "col_show_name": "通联编制的机构编码，可在DataAPI.PartyIDGet接口获取。",
                 "col_comment": "通联编制的机构编码，可在DataAPI.PartyIDGet接口获取。-描述"},
                {"col_name": "secID", "col_show_name": "通联编制的证券编码。可传入证券交易代码使用DataAPI.SecIDGet接口获取到。",
                 "col_comment": "通联编制的证券编码。可传入证券交易代码使用DataAPI.SecIDGet接口获取到。-描述"},
                {"col_name": "ticker", "col_show_name": "证券在证券市场通用的交易代码。", "col_comment": "证券在证券市场通用的交易代码。-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD",
                 "col_show_name": "证券交易市场代码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所。可在DataAPI.SysCodeGet接口输入codeTypeID=10002获取到",
                 "col_comment": "证券交易市场代码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所。可在DataAPI.SysCodeGet接口输入codeTypeID=10002获取到-描述"},
                {"col_name": "actPubtime", "col_show_name": "实际披露时间", "col_comment": "实际披露时间-描述"},
                {"col_name": "publishDate", "col_show_name": "发布日期", "col_comment": "发布日期-描述"},
                {"col_name": "endDate", "col_show_name": "截止日期", "col_comment": "截止日期-描述"},
                {"col_name": "fiscalPeriod", "col_show_name": "会计区间", "col_comment": "会计区间-描述"},
                {"col_name": "mergeFlag", "col_show_name": "合并标志", "col_comment": "合并标志-描述"},
                {"col_name": "classifCD", "col_show_name": "分类方式代码，1-按行业，2-按产品，3-按地区",
                 "col_comment": "分类方式代码，1-按行业，2-按产品，3-按地区-描述"},
                {"col_name": "isLatest", "col_show_name": "是否最新，1-是，0-否", "col_comment": "是否最新，1-是，0-否-描述"},
                {"col_name": "industry", "col_show_name": "行业分类", "col_comment": "行业分类-描述"},
                {"col_name": "itemParentNo", "col_show_name": "上级项目序号", "col_comment": "上级项目序号-描述"},
                {"col_name": "itemNo", "col_show_name": "项目序号", "col_comment": "项目序号-描述"},
                {"col_name": "itemName", "col_show_name": "项目名称", "col_comment": "项目名称-描述"},
                {"col_name": "revenue", "col_show_name": "收入", "col_comment": "收入-描述"},
                {"col_name": "revPctge", "col_show_name": "占收入合计比重(%)", "col_comment": "占收入合计比重(%)-描述"},
                {"col_name": "revIsPctge", "col_show_name": "占利润表营业收入比重(%)", "col_comment": "占利润表营业收入比重(%)-描述"},
                {"col_name": "tRevIsPctge", "col_show_name": "占利润表营业总收入比重(%)", "col_comment": "占利润表营业总收入比重(%)-描述"},
                {"col_name": "cogs", "col_show_name": "成本", "col_comment": "成本-描述"},
                {"col_name": "costPctge", "col_show_name": "占成本合计比重(%)", "col_comment": "占成本合计比重(%)-描述"},
                {"col_name": "cogsIsPctge", "col_show_name": "占利润表营业成本比重(%)", "col_comment": "占利润表营业成本比重(%)-描述"},
                {"col_name": "tCogsIsPctge", "col_show_name": "占利润表营业总成本比重(%)", "col_comment": "占利润表营业总成本比重(%)-描述"},
                {"col_name": "grossProfit", "col_show_name": "毛利润", "col_comment": "毛利润-描述"},
                {"col_name": "grossMargin", "col_show_name": "毛利率", "col_comment": "毛利率-描述"},
                {"col_name": "updateTime", "col_show_name": "更新时间", "col_comment": "更新时间-描述"}
            ]
        }
    define_json = json.dumps(fdmtmainopern_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)

# 备注：该表比通联数据字典多了个字段"isCalc"
def fdmtmostditem_define(table_name):

    fdmtmostditem_str = {
            "table_name": "fdmtmostditem",
            "table_show_name": "主营业务构成",
            "table_comment": "主营业务构成 -描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "证券编码", "col_comment": "证券编码-描述"},
                {"col_name": "ticker", "col_show_name": "交易代码", "col_comment": "交易代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD", "col_show_name": "证券市场", "col_comment": "证券市场-描述"},
                {"col_name": "partyID", "col_show_name": "公司代码", "col_comment": "公司代码-描述"},
                {"col_name": "endDate", "col_show_name": "会计期末", "col_comment": "会计期末-描述"},
                {"col_name": "classifCD", "col_show_name": "分类方式。1-按行业，2-按产品，3-按地区",
                 "col_comment": "分类方式。1-按行业，2-按产品，3-按地区-描述"},
                {"col_name": "itemID", "col_show_name": "项目代码", "col_comment": "项目代码-描述"},
                {"col_name": "itemName", "col_show_name": "项目名称", "col_comment": "项目名称-描述"},
                {"col_name": "itemIDSuperior", "col_show_name": "上级项目代码", "col_comment": "上级项目代码-描述"},
                {"col_name": "itemNameSuperior", "col_show_name": "上级项目名称", "col_comment": "上级项目名称-描述"},
                {"col_name": "revenue", "col_show_name": "营业收入", "col_comment": "营业收入-描述"},
                {"col_name": "revIsPctge", "col_show_name": "营业收入占比(%,占利润表营业收入)",
                 "col_comment": "营业收入占比(%,占利润表营业收入)-描述"},
                {"col_name": "tRevIsPctge", "col_show_name": "营业收入占比(%,占利润表营业总收入)",
                 "col_comment": "营业收入占比(%,占利润表营业总收入)-描述"},
                {"col_name": "revYOY", "col_show_name": "收入同比(%)", "col_comment": "收入同比(%)-描述"},
                {"col_name": "cogs", "col_show_name": "营业成本", "col_comment": "营业成本-描述"},
                {"col_name": "cogsIsPctge", "col_show_name": "营业成本占比(%,占利润表营业成本)",
                 "col_comment": "营业成本占比(%,占利润表营业成本)-描述"},
                {"col_name": "tCogsIsPctge", "col_show_name": "营业成本占比(%,占利润表营业总成本)",
                 "col_comment": "营业成本占比(%,占利润表营业总成本)-描述"},
                {"col_name": "cogsYOY", "col_show_name": "成本同比(%)", "col_comment": "成本同比(%)-描述"},
                {"col_name": "grossProfit", "col_show_name": "毛利润", "col_comment": "毛利润-描述"},
                {"col_name": "grossProfitYOY", "col_show_name": "毛利润同比(%)", "col_comment": "毛利润同比(%)-描述"},
                {"col_name": "grossMargin", "col_show_name": "毛利率(%)", "col_comment": "毛利率(%)-描述"},
                {"col_name": "grossMarginYOY", "col_show_name": "毛利率同比(%)", "col_comment": "毛利率同比(%)-描述"}
            ]
        }
    define_json = json.dumps(fdmtmostditem_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def fdmtderpit_define(table_name):

    fdmtderpit_str = {
            "table_name": "fdmtderpit",
            "table_show_name": "财务衍生数据 (Point in time)",
            "table_comment": "财务衍生数据 (Point in time)-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "证券内部编码", "col_comment": "证券内部编码-描述"},
                {"col_name": "partyID", "col_show_name": "机构ID", "col_comment": "机构ID-描述"},
                {"col_name": "ticker", "col_show_name": "交易代码", "col_comment": "交易代码-描述"},
                {"col_name": "exchangeCD",
                 "col_show_name": "通联编制的证券市场编码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所等。对应getSysCode.codeTypeID=10002。",
                 "col_comment": "通联编制的证券市场编码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所等。对应getSysCode.codeTypeID=10002。-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "publishDate", "col_show_name": "证券交易所披露的信息发布日期", "col_comment": "证券交易所披露的信息发布日期-描述"},
                {"col_name": "actPubtime", "col_show_name": "实际披露时间", "col_comment": "实际披露时间-描述"},
                {"col_name": "endDate", "col_show_name": "会计期间截止日期", "col_comment": "会计期间截止日期-描述"},
                {"col_name": "tFixedAssets",
                 "col_show_name": "固定资产合计 , 1、固定资产合计=固定资产+在建工程+工程物资+固定资产清理（金融企业不计算） 2、金融企业不计算",
                 "col_comment": "固定资产合计 , 1、固定资产合计=固定资产+在建工程+工程物资+固定资产清理（金融企业不计算） 2、金融企业不计算-描述"},
                {"col_name": "intFreeCl",
                 "col_show_name": "无息流动负债 , 1、无息流动负债=应付账款+预收账款+应付股利+应付利息+应交税费+应付职工薪酬+其他应付款+预提费用+其他流动负债 2、金融企业不计算 3、一般工商业公司合并报表中有金融类负债科目看作带息流动负债，例如：吸收存款",
                 "col_comment": "无息流动负债 , 1、无息流动负债=应付账款+预收账款+应付股利+应付利息+应交税费+应付职工薪酬+其他应付款+预提费用+其他流动负债 2、金融企业不计算 3、一般工商业公司合并报表中有金融类负债科目看作带息流动负债，例如：吸收存款-描述"},
                {"col_name": "intFreeNcl", "col_show_name": "无息非流动负债 , 1、无息非流动负债=非流动负债合计-（长期借款+应付债券） 2、金融企业不计算",
                 "col_comment": "无息非流动负债 , 1、无息非流动负债=非流动负债合计-（长期借款+应付债券） 2、金融企业不计算-描述"},
                {"col_name": "intCl",
                 "col_show_name": "带息流动负债 , 1、带息流动负债=流动负债-无息流动负债 2、金融企业不计算 3、一般工商业公司合并报表中有金融类负债科目看作有息流动负债，例如：吸收存款",
                 "col_comment": "带息流动负债 , 1、带息流动负债=流动负债-无息流动负债 2、金融企业不计算 3、一般工商业公司合并报表中有金融类负债科目看作有息流动负债，例如：吸收存款-描述"},
                {"col_name": "intDebt",
                 "col_show_name": "带息债务 , 1、带息债务=带息流动负债+长期借款+应付债券 2、金融企业不计算 3、一般工商业公司合并报表中有金融类负债科目看作带息流动债务，例如：吸收存款",
                 "col_comment": "带息债务 , 1、带息债务=带息流动负债+长期借款+应付债券 2、金融企业不计算 3、一般工商业公司合并报表中有金融类负债科目看作带息流动债务，例如：吸收存款-描述"},
                {"col_name": "nDebt",
                 "col_show_name": "净债务 , 1、净债务=带息负债-货币资金 2、金融企业不计算 3、一般工商业公司合并报表中有金融类负债科目看作带息负债，例如：吸收存款",
                 "col_comment": "净债务 , 1、净债务=带息负债-货币资金 2、金融企业不计算 3、一般工商业公司合并报表中有金融类负债科目看作带息负债，例如：吸收存款-描述"},
                {"col_name": "nTanAssets", "col_show_name": "有形净资产 , 有形净资产=归属于母公司的所有者权益-无形资产-研发支出-商誉-长期待摊费用-递延所得税资产",
                 "col_comment": "有形净资产 , 有形净资产=归属于母公司的所有者权益-无形资产-研发支出-商誉-长期待摊费用-递延所得税资产-描述"},
                {"col_name": "workCapital", "col_show_name": "营运资本 , 1、营运资本=流动资产-流动负债 2、金融企业不计算",
                 "col_comment": "营运资本 , 1、营运资本=流动资产-流动负债 2、金融企业不计算-描述"},
                {"col_name": "nWorkCapital",
                 "col_show_name": "净营运资本 , 1、净营运资本=流动资产-货币资金-无息流动负债 2、金融企业不计算 3、一般工商业公司合并报表中有金融类负债科目看作带息流动负债，例如：吸收存款",
                 "col_comment": "净营运资本 , 1、净营运资本=流动资产-货币资金-无息流动负债 2、金融企业不计算 3、一般工商业公司合并报表中有金融类负债科目看作带息流动负债，例如：吸收存款-描述"},
                {"col_name": "IC",
                 "col_show_name": "投入资本 , 1、投入成本=归属于母公司所有者权益+带息债务 2、金融企业不计算 3、一般工商业公司合并报表中有金融类负债科目看作带息债务，例如：吸收存款",
                 "col_comment": "投入资本 , 1、投入成本=归属于母公司所有者权益+带息债务 2、金融企业不计算 3、一般工商业公司合并报表中有金融类负债科目看作带息债务，例如：吸收存款-描述"},
                {"col_name": "tRe", "col_show_name": "留存收益 , 留存收益=盈余公积+未分配利润",
                 "col_comment": "留存收益 , 留存收益=盈余公积+未分配利润-描述"},
                {"col_name": "grossProfit", "col_show_name": "毛利 , 1、毛利=营业收入-营业成本 2、金融企业不计算",
                 "col_comment": "毛利 , 1、毛利=营业收入-营业成本 2、金融企业不计算-描述"},
                {"col_name": "opaProfit",
                 "col_show_name": "经营活动净收益 , 1、对于非金融企业： 经营活动净收益=营业总收入-营业总成本 2、对于金融企业： 经营活动净收益=营业收入-公允价值变动损益-投资收益-汇兑损益-营业支出",
                 "col_comment": "经营活动净收益 , 1、对于非金融企业： 经营活动净收益=营业总收入-营业总成本 2、对于金融企业： 经营活动净收益=营业收入-公允价值变动损益-投资收益-汇兑损益-营业支出-描述"},
                {"col_name": "valChgProfit", "col_show_name": "价值变动净收益 , 价值变动净收益=公允价值变动损益+投资收益+汇兑损益",
                 "col_comment": "价值变动净收益 , 价值变动净收益=公允价值变动损益+投资收益+汇兑损益-描述"},
                {"col_name": "nIntExp",
                 "col_show_name": "净利息费用 , 1、净利息费用=利息支出-利息收入（财务费用附注），若未披露财务费用附注，则直接取财务费用值 2、金融企业不计算",
                 "col_comment": "净利息费用 , 1、净利息费用=利息支出-利息收入（财务费用附注），若未披露财务费用附注，则直接取财务费用值 2、金融企业不计算-描述"},
                {"col_name": "EBIT", "col_show_name": "息税前利润 , 1、EBIT=利润总额+净利息费用 2、金融企业不计算",
                 "col_comment": "息税前利润 , 1、EBIT=利润总额+净利息费用 2、金融企业不计算-描述"},
                {"col_name": "EBITDA",
                 "col_show_name": "息税折旧摊销前利润 , 1、EBITDA=利润总额+净利息费用+固定资产折旧＋无形资产摊销＋长期待摊费用摊销 2、金融企业不计算",
                 "col_comment": "息税折旧摊销前利润 , 1、EBITDA=利润总额+净利息费用+固定资产折旧＋无形资产摊销＋长期待摊费用摊销 2、金融企业不计算-描述"},
                {"col_name": "EBIAT",
                 "col_show_name": "息前税后利润 , 1、EBIAT=净利润+净利息费用*（1-税率） 2、税率=所得税费用/利润总额（实际税率）； 若所得税费用或利润总额为负，税率=25%（名义税率） 3、金融企业不计算",
                 "col_comment": "息前税后利润 , 1、EBIAT=净利润+净利息费用*（1-税率） 2、税率=所得税费用/利润总额（实际税率）； 若所得税费用或利润总额为负，税率=25%（名义税率） 3、金融企业不计算-描述"},
                {"col_name": "nrProfitLoss", "col_show_name": "非经常性损益 , 直接取公告披露值",
                 "col_comment": "非经常性损益 , 直接取公告披露值-描述"},
                {"col_name": "niAttrPCut", "col_show_name": "扣除非经常性损益后的归属于上市公司股东的净利润 , 直接取公告披露值",
                 "col_comment": "扣除非经常性损益后的归属于上市公司股东的净利润 , 直接取公告披露值-描述"},
                {"col_name": "FCFF",
                 "col_show_name": "企业自由现金流量 , 1、FCFF=经营活动现金流量净额-资本支出-净利息费用*税率 2、资本支出=购建固定资产、无形资产和其他长期资产支付的现金-处置固定资产、无形资产和其他长期资产收回的现金净额 3、税率=所得税费用/利润总额（实际税率）； 若所得税费用或利润总额为负，税率=25%（名义税率） 4、金融企业不计算",
                 "col_comment": "企业自由现金流量 , 1、FCFF=经营活动现金流量净额-资本支出-净利息费用*税率 2、资本支出=购建固定资产、无形资产和其他长期资产支付的现金-处置固定资产、无形资产和其他长期资产收回的现金净额 3、税率=所得税费用/利润总额（实际税率）； 若所得税费用或利润总额为负，税率=25%（名义税率） 4、金融企业不计算-描述"},
                {"col_name": "FCFE",
                 "col_show_name": "股权自由现金流量 , 1、FCFE=经营活动现金流量净额-资本支出+债务增加额-净利息费用 2、资本支出=购建固定资产、无形资产和其他长期资产支付的现金-处置固定资产、无形资产和其他长期资产收回的现金净额 3、债务增加额=（期末短期借款+期末长期借款+期末应付债券）-（期初短期借款+期初长期借款+期初应付债券） 4、金融企业不计算",
                 "col_comment": "股权自由现金流量 , 1、FCFE=经营活动现金流量净额-资本支出+债务增加额-净利息费用 2、资本支出=购建固定资产、无形资产和其他长期资产支付的现金-处置固定资产、无形资产和其他长期资产收回的现金净额 3、债务增加额=（期末短期借款+期末长期借款+期末应付债券）-（期初短期借款+期初长期借款+期初应付债券） 4、金融企业不计算-描述"},
                {"col_name": "DA", "col_show_name": "折旧与摊销 , 1、折旧及摊销=固定资产折旧＋无形资产摊销＋长期待摊费用摊销 2、金融企业不计算",
                 "col_comment": "折旧与摊销 , 1、折旧及摊销=固定资产折旧＋无形资产摊销＋长期待摊费用摊销 2、金融企业不计算-描述"}
            ]
        }
    define_json = json.dumps(fdmtderpit_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def mktequfloworder_define(table_name):

    mktequfloworder_str = {
            "table_name": "mktequfloworder_str",
            "table_show_name": "股票日资金流向单类明细",
            "table_comment": "股票日资金流向单类明细-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "通联编制的证券编码，可使用getSecID获取",
                 "col_comment": "通联编制的证券编码，可使用getSecID获取-描述"},
                {"col_name": "ticker", "col_show_name": "通用交易代码", "col_comment": "通用交易代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "tradeDate", "col_show_name": "交易日期", "col_comment": "交易日期-描述"},
                {"col_name": "inflowS", "col_show_name": "资金流入(小单)", "col_comment": "资金流入(小单)-描述"},
                {"col_name": "inflowM", "col_show_name": "资金流入(中单)", "col_comment": "资金流入(中单)-描述"},
                {"col_name": "inflowL", "col_show_name": "资金流入(大单)", "col_comment": "资金流入(大单)-描述"},
                {"col_name": "inflowXl", "col_show_name": "资金流入(超大单)", "col_comment": "资金流入(超大单)-描述"},
                {"col_name": "outflowS", "col_show_name": "资金流出(小单)", "col_comment": "资金流出(小单)-描述"},
                {"col_name": "outflowM", "col_show_name": "资金流出(中单)", "col_comment": "资金流出(中单)-描述"},
                {"col_name": "outflowL", "col_show_name": "资金流出(大单)", "col_comment": "资金流出(大单)-描述"},
                {"col_name": "outflowXl", "col_show_name": "资金流出(超大单)", "col_comment": "资金流出(超大单)-描述"},
                {"col_name": "netInflowS", "col_show_name": "资金净流入(小单)", "col_comment": "资金净流入(小单)-描述"},
                {"col_name": "netInflowM", "col_show_name": "资金净流入(中单)", "col_comment": "资金净流入(中单)-描述"},
                {"col_name": "netInflowL", "col_show_name": "资金净流入(大单)", "col_comment": "资金净流入(大单)-描述"},
                {"col_name": "netInflowXl", "col_show_name": "资金净流入(超大单)", "col_comment": "资金净流入(超大单)-描述"},
                {"col_name": "netRateS", "col_show_name": "资金净流入占成交金额比重(小单)", "col_comment": "资金净流入占成交金额比重(小单)-描述"},
                {"col_name": "netRateM", "col_show_name": "资金净流入占成交金额比重(中单)", "col_comment": "资金净流入占成交金额比重(中单)-描述"},
                {"col_name": "netRateL", "col_show_name": "资金净流入占成交金额比重(大单)", "col_comment": "资金净流入占成交金额比重(大单)-描述"},
                {"col_name": "netRateXL", "col_show_name": "资金净流入占成交金额比重超大单)", "col_comment": "资金净流入占成交金额比重超大单)-描述"},
                {"col_name": "mainInflow", "col_show_name": "主力资金净流入(主力=中单+大单+超大单)",
                 "col_comment": "主力资金净流入(主力=中单+大单+超大单)-描述"},
                {"col_name": "mainRate", "col_show_name": "主力资金净流入占成交金额比重(主力=中单+大单+超大单)",
                 "col_comment": "主力资金净流入占成交金额比重(主力=中单+大单+超大单)-描述"}
            ]
        }
    define_json = json.dumps(mktequfloworder_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def mktequflow_define(table_name):

    mktequflow_str = {
            "table_name": "mktequflow",
            "table_show_name": "个股日资金流向",
            "table_comment": "个股日资金流向-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "通联编制的证券编码，可使用DataAPI.SecIDGet获取",
                 "col_comment": "通联编制的证券编码，可使用DataAPI.SecIDGet获取-描述"},
                {"col_name": "ticker", "col_show_name": "通用交易代码", "col_comment": "通用交易代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "secShortNameEn", "col_show_name": "证券英文简称", "col_comment": "证券英文简称-描述"},
                {"col_name": "exchangeCD", "col_show_name": "通联编制的交易市场编码", "col_comment": "通联编制的交易市场编码-描述"},
                {"col_name": "tradeDate", "col_show_name": "交易日期", "col_comment": "交易日期-描述"},
                {"col_name": "moneyInflow", "col_show_name": "资金流入", "col_comment": "资金流入-描述"},
                {"col_name": "moneyOutflow", "col_show_name": "资金流出", "col_comment": "资金流出-描述"},
                {"col_name": "netMoneyInflow", "col_show_name": "资金净流入=资金流入-资金流出", "col_comment": "资金净流入=资金流入-资金流出-描述"},
                {"col_name": "netInflowRate", "col_show_name": "资金净流入占当日成交金额比重", "col_comment": "资金净流入占当日成交金额比重-描述"},
                {"col_name": "netInflowOpen", "col_show_name": "开盘资金净流入，包含集合竞价至早10:00",
                 "col_comment": "开盘资金净流入，包含集合竞价至早10:00-描述"},
                {"col_name": "netInflowClose", "col_show_name": "尾盘资金净流入，下午14:30至收盘",
                 "col_comment": "尾盘资金净流入，下午14:30至收盘-描述"},
                {"col_name": "updateTime", "col_show_name": "最近一次更新时间", "col_comment": "最近一次更新时间-描述"}
            ]
        }
    define_json = json.dumps(mktequflow_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def mktindustryflow_define(table_name):

    mktindustryflow_str = {
            "table_name": "mktindustryflow",
            "table_show_name": "行业日资金流向",
            "table_comment": "行业日资金流向-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "industryID", "col_show_name": "通联编制的行业分类编码", "col_comment": "通联编制的行业分类编码-描述"},
                {"col_name": "industryName", "col_show_name": "行业名称", "col_comment": "行业名称-描述"},
                {"col_name": "tradeDate", "col_show_name": "交易日期", "col_comment": "交易日期-描述"},
                {"col_name": "moneyInflow", "col_show_name": "资金流入", "col_comment": "资金流入-描述"},
                {"col_name": "moneyOutflow", "col_show_name": "资金流出", "col_comment": "资金流出-描述"},
                {"col_name": "netMoneyInflow", "col_show_name": "资金净流入", "col_comment": "资金净流入-描述"},
                {"col_name": "netInflowRate", "col_show_name": "资金净流入占成交金额比重", "col_comment": "资金净流入占成交金额比重-描述"},
                {"col_name": "netInflowOpen", "col_show_name": "开盘资金净流入，包含集合竞价至早10:00",
                 "col_comment": "开盘资金净流入，包含集合竞价至早10:00-描述"},
                {"col_name": "netInflowClose", "col_show_name": "尾盘资金净流入，下午14:30至收盘",
                 "col_comment": "尾盘资金净流入，下午14:30至收盘-描述"},
                {"col_name": "updateTime", "col_show_name": "最近一次更新时间", "col_comment": "最近一次更新时间-描述"}
            ]
        }
    define_json = json.dumps(mktindustryflow_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def mktindustryfloworder_define(table_name):

    mktindustryfloworder_str = {
            "table_name": "mktindustryfloworder",
            "table_show_name": "行业日资金流向单类明细",
            "table_comment": "行业日资金流向单类明细-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "industryID", "col_show_name": "通联编制的行业分类编码", "col_comment": "通联编制的行业分类编码-描述"},
                {"col_name": "industryName", "col_show_name": "行业名称", "col_comment": "行业名称-描述"},
                {"col_name": "tradeDate", "col_show_name": "交易日", "col_comment": "交易日-描述"},
                {"col_name": "inflowS", "col_show_name": "资金流入(小单)", "col_comment": "资金流入(小单)-描述"},
                {"col_name": "inflowM", "col_show_name": "资金流入(中单)", "col_comment": "资金流入(中单)-描述"},
                {"col_name": "inflowL", "col_show_name": "资金流入(大单)", "col_comment": "资金流入(大单)-描述"},
                {"col_name": "inflowXl", "col_show_name": "资金流入(超大单)", "col_comment": "资金流入(超大单)-描述"},
                {"col_name": "outflowS", "col_show_name": "资金流出(小单)", "col_comment": "资金流出(小单)-描述"},
                {"col_name": "outflowM", "col_show_name": "资金流出(中单)", "col_comment": "资金流出(中单)-描述"},
                {"col_name": "outflowL", "col_show_name": "资金流出(大单)", "col_comment": "资金流出(大单)-描述"},
                {"col_name": "outflowXl", "col_show_name": "资金流出(超大单)", "col_comment": "资金流出(超大单)-描述"},
                {"col_name": "netInflowS", "col_show_name": "资金净流入(小单)", "col_comment": "资金净流入(小单)-描述"},
                {"col_name": "netInflowM", "col_show_name": "资金净流入(中单)", "col_comment": "资金净流入(中单)-描述"},
                {"col_name": "netInflowL", "col_show_name": "资金净流入(大单)", "col_comment": "资金净流入(大单)-描述"},
                {"col_name": "netInflowXl", "col_show_name": "资金净流入(超大单)", "col_comment": "资金净流入(超大单)-描述"},
                {"col_name": "netRateS", "col_show_name": "资金净流入占成交金额比重(小单)", "col_comment": "资金净流入占成交金额比重(小单)-描述"},
                {"col_name": "netRateM", "col_show_name": "资金净流入占成交金额比重(中单)", "col_comment": "资金净流入占成交金额比重(中单)-描述"},
                {"col_name": "netRateL", "col_show_name": "资金净流入占成交金额比重(大单)", "col_comment": "资金净流入占成交金额比重(大单)-描述"},
                {"col_name": "netRateXL", "col_show_name": "资金净流入占成交金额比重超大单)", "col_comment": "资金净流入占成交金额比重超大单)-描述"},
                {"col_name": "mainInflow", "col_show_name": "主力资金净流入(主力=中单+大单+超大单)",
                 "col_comment": "主力资金净流入(主力=中单+大单+超大单)-描述"},
                {"col_name": "mainRate", "col_show_name": "主力资金净流入占成交金额比重(主力=中单+大单+超大单)",
                 "col_comment": "主力资金净流入占成交金额比重(主力=中单+大单+超大单)-描述"}
            ]
        }
    define_json = json.dumps(mktindustryfloworder_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def mktequmf_define(table_name):

    mktequmf_str = {
            "table_name": "mktequmf",
            "table_show_name": "",
            "table_comment": "-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "通联编制的证券编码，可使用DataAPI.SecIDGet获取",
                 "col_comment": "通联编制的证券编码，可使用DataAPI.SecIDGet获取-描述"},
                {"col_name": "ticker", "col_show_name": "通用交易代码", "col_comment": "通用交易代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD", "col_show_name": "通联编制的交易市场编码", "col_comment": "通联编制的交易市场编码-描述"},
                {"col_name": "tradeDate", "col_show_name": "交易日期", "col_comment": "交易日期-描述"},
                {"col_name": "turnoverValue", "col_show_name": "总成交金额", "col_comment": "总成交金额-描述"},
                {"col_name": "turnoverVol", "col_show_name": "总成交量", "col_comment": "总成交量-描述"},
                {"col_name": "dealAmount", "col_show_name": "总成交笔数", "col_comment": "总成交笔数-描述"},
                {"col_name": "netFlow", "col_show_name": "净流入额，流入额+流出额（流出额为负数）",
                 "col_comment": "净流入额，流入额+流出额（流出额为负数）-描述"},
                {"col_name": "inflow", "col_show_name": "流入额", "col_comment": "流入额-描述"},
                {"col_name": "outflow", "col_show_name": "流出额，以负数计", "col_comment": "流出额，以负数计-描述"},
                {"col_name": "mainFlow", "col_show_name": "主力净流入额，大单净流入额+超大单净流入额",
                 "col_comment": "主力净流入额，大单净流入额+超大单净流入额-描述"},
                {"col_name": "smainFlow", "col_show_name": "散户净流入额，小单净流入额+中单净流入额",
                 "col_comment": "散户净流入额，小单净流入额+中单净流入额-描述"},
                {"col_name": "mainInflow", "col_show_name": "主力流入额，大单流入额+超大单流入额",
                 "col_comment": "主力流入额，大单流入额+超大单流入额-描述"},
                {"col_name": "mainOutflow", "col_show_name": "主力流出额，大单流出额+超大单流出额",
                 "col_comment": "主力流出额，大单流出额+超大单流出额-描述"},
                {"col_name": "netFlowS", "col_show_name": "小单净流入额，小单流入额+小单流出额（流出额为负数）",
                 "col_comment": "小单净流入额，小单流入额+小单流出额（流出额为负数）-描述"},
                {"col_name": "netFlowM", "col_show_name": "中单净流入额，中单流入额+中单流出额（流出额为负数）",
                 "col_comment": "中单净流入额，中单流入额+中单流出额（流出额为负数）-描述"},
                {"col_name": "netFlowL", "col_show_name": "大单净流入额，大单流入额+大单流出额（流出额为负数）",
                 "col_comment": "大单净流入额，大单流入额+大单流出额（流出额为负数）-描述"},
                {"col_name": "netFlowXL", "col_show_name": "超大单净流入额，超大单流入额+超大单流出额（流出额为负数）",
                 "col_comment": "超大单净流入额，超大单流入额+超大单流出额（流出额为负数）-描述"},
                {"col_name": "inflowS", "col_show_name": "小单流入额", "col_comment": "小单流入额-描述"},
                {"col_name": "inflowM", "col_show_name": "中单流入额", "col_comment": "中单流入额-描述"},
                {"col_name": "inflowL", "col_show_name": "大单流入额", "col_comment": "大单流入额-描述"},
                {"col_name": "inflowXL", "col_show_name": "超大单流入额", "col_comment": "超大单流入额-描述"},
                {"col_name": "outflowS", "col_show_name": "小单流出额", "col_comment": "小单流出额-描述"},
                {"col_name": "outflowM", "col_show_name": "中单流出额", "col_comment": "中单流出额-描述"},
                {"col_name": "outflowL", "col_show_name": "大单流出额", "col_comment": "大单流出额-描述"},
                {"col_name": "outflowXL", "col_show_name": "超大单流出额", "col_comment": "超大单流出额-描述"},
                {"col_name": "netVol", "col_show_name": "净流入量，流入量-流出量", "col_comment": "净流入量，流入量-流出量-描述"},
                {"col_name": "buyVol", "col_show_name": "流入量", "col_comment": "流入量-描述"},
                {"col_name": "sellVol", "col_show_name": "流出量，以正数计", "col_comment": "流出量，以正数计-描述"},
                {"col_name": "mainBuyVol", "col_show_name": "主力流入量", "col_comment": "主力流入量-描述"},
                {"col_name": "mainSellVol", "col_show_name": "主力流出量", "col_comment": "主力流出量-描述"},
                {"col_name": "buyVolS", "col_show_name": "小单流入量", "col_comment": "小单流入量-描述"},
                {"col_name": "buyVolM", "col_show_name": "中单流入量", "col_comment": "中单流入量-描述"},
                {"col_name": "buyVolL", "col_show_name": "大单流入量", "col_comment": "大单流入量-描述"},
                {"col_name": "buyVolXL", "col_show_name": "超大单流入量", "col_comment": "超大单流入量-描述"},
                {"col_name": "sellVolS", "col_show_name": "小单流出量", "col_comment": "小单流出量-描述"},
                {"col_name": "sellVolM", "col_show_name": "中单流出量", "col_comment": "中单流出量-描述"},
                {"col_name": "sellVolL", "col_show_name": "大单流出量", "col_comment": "大单流出量-描述"},
                {"col_name": "sellVolXL", "col_show_name": "超大单流出量", "col_comment": "超大单流出量-描述"},
                {"col_name": "netOrd", "col_show_name": "净流入笔数，流入笔数-流出笔数", "col_comment": "净流入笔数，流入笔数-流出笔数-描述"},
                {"col_name": "buyOrd", "col_show_name": "流入笔数", "col_comment": "流入笔数-描述"},
                {"col_name": "sellOrd", "col_show_name": "流出笔数，以正数计", "col_comment": "流出笔数，以正数计-描述"},
                {"col_name": "mainBuyOrd", "col_show_name": "主力流入笔数", "col_comment": "主力流入笔数-描述"},
                {"col_name": "mainSellOrd", "col_show_name": "主力流出笔数", "col_comment": "主力流出笔数-描述"},
                {"col_name": "buyOrdS", "col_show_name": "小单流入笔数", "col_comment": "小单流入笔数-描述"},
                {"col_name": "buyOrdM", "col_show_name": "中单流入笔数", "col_comment": "中单流入笔数-描述"},
                {"col_name": "buyOrdL", "col_show_name": "大单流入笔数", "col_comment": "大单流入笔数-描述"},
                {"col_name": "buyOrdXL", "col_show_name": "超大单流入笔数", "col_comment": "超大单流入笔数-描述"},
                {"col_name": "sellOrdS", "col_show_name": "小单流出笔数", "col_comment": "小单流出笔数-描述"},
                {"col_name": "sellOrdM", "col_show_name": "中单流出笔数", "col_comment": "中单流出笔数-描述"},
                {"col_name": "sellOrdL", "col_show_name": "大单流出笔数", "col_comment": "大单流出笔数-描述"},
                {"col_name": "sellOrdXL", "col_show_name": "超大单流出笔数", "col_comment": "超大单流出笔数-描述"},
                {"col_name": "netFlowRate", "col_show_name": "净流入占比，净流入额/总成交金额", "col_comment": "净流入占比，净流入额/总成交金额-描述"},
                {"col_name": "inflowRate", "col_show_name": "流入占比，流入额/总成交金额", "col_comment": "流入占比，流入额/总成交金额-描述"},
                {"col_name": "outflowRate", "col_show_name": "流出占比，流出额/总成交金额", "col_comment": "流出占比，流出额/总成交金额-描述"},
                {"col_name": "mainFlowRate", "col_show_name": "主力净流入占比，主力净流入额/总成交金额",
                 "col_comment": "主力净流入占比，主力净流入额/总成交金额-描述"},
                {"col_name": "smainFlowRate", "col_show_name": "散户净流入占比，散户净流入额/总成交金额",
                 "col_comment": "散户净流入占比，散户净流入额/总成交金额-描述"},
                {"col_name": "mainInflowRate", "col_show_name": "主力流入占比，主力流入额/总成交金额",
                 "col_comment": "主力流入占比，主力流入额/总成交金额-描述"},
                {"col_name": "mainOutflowRate", "col_show_name": "主力流出占比，主力流出额/总成交金额",
                 "col_comment": "主力流出占比，主力流出额/总成交金额-描述"},
                {"col_name": "netFlowSRate", "col_show_name": "小单净流入占比，小单净流入额/总成交金额",
                 "col_comment": "小单净流入占比，小单净流入额/总成交金额-描述"},
                {"col_name": "netFlowMRate", "col_show_name": "中单净流入占比，中单净流入额/总成交金额",
                 "col_comment": "中单净流入占比，中单净流入额/总成交金额-描述"},
                {"col_name": "netFlowLRate", "col_show_name": "大单净流入占比，大单净流入额/总成交金额",
                 "col_comment": "大单净流入占比，大单净流入额/总成交金额-描述"},
                {"col_name": "netFlowXLRate", "col_show_name": "超大单净流入占比，超大单净流入额/总成交金额",
                 "col_comment": "超大单净流入占比，超大单净流入额/总成交金额-描述"},
                {"col_name": "inflowSRate", "col_show_name": "小单流入占比，小单流入额/总成交金额",
                 "col_comment": "小单流入占比，小单流入额/总成交金额-描述"},
                {"col_name": "inflowMRate", "col_show_name": "中单流入占比，中单流入额/总成交金额",
                 "col_comment": "中单流入占比，中单流入额/总成交金额-描述"},
                {"col_name": "inflowLRate", "col_show_name": "大单流入占比，大单流入额/总成交金额",
                 "col_comment": "大单流入占比，大单流入额/总成交金额-描述"},
                {"col_name": "inflowXLRate", "col_show_name": "超大单流入占比，超大单流入额/总成交金额",
                 "col_comment": "超大单流入占比，超大单流入额/总成交金额-描述"},
                {"col_name": "outflowSRate", "col_show_name": "小单流出占比，小单流出额/总成交金额",
                 "col_comment": "小单流出占比，小单流出额/总成交金额-描述"},
                {"col_name": "outflowMRate", "col_show_name": "中单流出占比，中单流出额/总成交金额",
                 "col_comment": "中单流出占比，中单流出额/总成交金额-描述"},
                {"col_name": "outflowLRate", "col_show_name": "大单流出占比，大单流出额/总成交金额",
                 "col_comment": "大单流出占比，大单流出额/总成交金额-描述"},
                {"col_name": "outflowXLRate", "col_show_name": "超大单流出占比，超大单流出额/总成交金额",
                 "col_comment": "超大单流出占比，超大单流出额/总成交金额-描述"},
                {"col_name": "netVolRate", "col_show_name": "净流入量占比，净流入量/总成交量", "col_comment": "净流入量占比，净流入量/总成交量-描述"},
                {"col_name": "buyVolRate", "col_show_name": "流入量占比，流入量/总成交量", "col_comment": "流入量占比，流入量/总成交量-描述"},
                {"col_name": "sellVolRate", "col_show_name": "流出量占比，流出量/总成交量", "col_comment": "流出量占比，流出量/总成交量-描述"},
                {"col_name": "mainBuyVolRate", "col_show_name": "主力流入量占比，主力流入量/总成交量",
                 "col_comment": "主力流入量占比，主力流入量/总成交量-描述"},
                {"col_name": "mainSellVolRate", "col_show_name": "主力流出量占比，主力流出量/总成交量",
                 "col_comment": "主力流出量占比，主力流出量/总成交量-描述"},
                {"col_name": "netOrdRate", "col_show_name": "净流入笔数占比，净流入笔数/总成交笔数",
                 "col_comment": "净流入笔数占比，净流入笔数/总成交笔数-描述"},
                {"col_name": "buyOrdRate", "col_show_name": "流入笔数占比，流入笔数/总成交笔数", "col_comment": "流入笔数占比，流入笔数/总成交笔数-描述"},
                {"col_name": "sellOrdRate", "col_show_name": "流出笔数占比，买出笔数/总成交笔数",
                 "col_comment": "流出笔数占比，买出笔数/总成交笔数-描述"},
                {"col_name": "mainBuyOrdRate", "col_show_name": "主力流入笔数占比，主力流入笔数/总成交笔数",
                 "col_comment": "主力流入笔数占比，主力流入笔数/总成交笔数-描述"},
                {"col_name": "mainSellOrdRate", "col_show_name": "主力流出笔数占比，主力买出笔数/总成交笔数",
                 "col_comment": "主力流出笔数占比，主力买出笔数/总成交笔数-描述"},
                {"col_name": "updateTime", "col_show_name": "最近一次更新时间", "col_comment": "最近一次更新时间-描述"}
            ]
        }
    define_json = json.dumps(mktequmf_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def fdmtefnew_define(table_name):

    fdmtefnew_str = {
            "table_name": "fdmtefnew",
            "table_show_name": "业绩预告(新)",
            "table_comment": "业绩预告(新)-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "证券内部编码", "col_comment": "证券内部编码-描述"},
                {"col_name": "publishDate", "col_show_name": "发布日期", "col_comment": "发布日期-描述"},
                {"col_name": "endDate", "col_show_name": "截止日期", "col_comment": "截止日期-描述"},
                {"col_name": "partyID", "col_show_name": "公司代码", "col_comment": "公司代码-描述"},
                {"col_name": "ticker", "col_show_name": "交易代码", "col_comment": "交易代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD",
                 "col_show_name": "通联编制的证券市场编码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所等。对应getSysCode.codeTypeID=10002。",
                 "col_comment": "通联编制的证券市场编码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所等。对应getSysCode.codeTypeID=10002。-描述"},
                {"col_name": "actPubtime", "col_show_name": "实际发布时间", "col_comment": "实际发布时间-描述"},
                {"col_name": "mergedFlag", "col_show_name": "合并类型。1-合并。对应getSysCode.codeTypeID=70003。",
                 "col_comment": "合并类型。1-合并。对应getSysCode.codeTypeID=70003。-描述"},
                {"col_name": "reportType", "col_show_name": "报告类型。Q1-一季度,S1-半年度,Q3-第三季度或前三季度,A-年度。",
                 "col_comment": "报告类型。Q1-一季度,S1-半年度,Q3-第三季度或前三季度,A-年度。-描述"},
                {"col_name": "fiscalPeriod", "col_show_name": "会计期间", "col_comment": "会计期间-描述"},
                {"col_name": "accoutingStandards", "col_show_name": "会计准则", "col_comment": "会计准则-描述"},
                {"col_name": "currencyCD", "col_show_name": "货币代码。例如，USD-美元；CAD-加元等。对应getSysCode.codeTypeID=10004。",
                 "col_comment": "货币代码。例如，USD-美元；CAD-加元等。对应getSysCode.codeTypeID=10004。-描述"},
                {"col_name": "forecastType", "col_show_name": "业绩预期类型。对应getSysCode.codeTypeID=71012。",
                 "col_comment": "业绩预期类型。对应getSysCode.codeTypeID=71012。-描述"},
                {"col_name": "revChgrLL", "col_show_name": "收入增减幅度下限(%)", "col_comment": "收入增减幅度下限(%)-描述"},
                {"col_name": "revChgrUPL", "col_show_name": "收入增减幅度上限(%)", "col_comment": "收入增减幅度上限(%)-描述"},
                {"col_name": "expRevLL", "col_show_name": "预期收入下限", "col_comment": "预期收入下限-描述"},
                {"col_name": "expRevUPL", "col_show_name": "预期收入上限", "col_comment": "预期收入上限-描述"},
                {"col_name": "NIncomeChgrLL", "col_show_name": "净利润增减幅度下限(%)", "col_comment": "净利润增减幅度下限(%)-描述"},
                {"col_name": "NIncomeChgrUPL", "col_show_name": "净利润增减幅度上限(%)", "col_comment": "净利润增减幅度上限(%)-描述"},
                {"col_name": "expnIncomeLL", "col_show_name": "预期净利润下限", "col_comment": "预期净利润下限-描述"},
                {"col_name": "expnIncomeUPL", "col_show_name": "预期净利润上限", "col_comment": "预期净利润上限-描述"},
                {"col_name": "NIncAPChgrLL", "col_show_name": "归属于母公司所有者的净利润增减幅度下限(%)",
                 "col_comment": "归属于母公司所有者的净利润增减幅度下限(%)-描述"},
                {"col_name": "NIncAPChgrUPL", "col_show_name": "归属于母公司所有者的净利润增减幅度上限(%)",
                 "col_comment": "归属于母公司所有者的净利润增减幅度上限(%)-描述"},
                {"col_name": "expnIncAPLL", "col_show_name": "预期归属于母公司所有者的净利润下限",
                 "col_comment": "预期归属于母公司所有者的净利润下限-描述"},
                {"col_name": "expnIncAPUPL", "col_show_name": "预期归属于母公司所有者的净利润上限",
                 "col_comment": "预期归属于母公司所有者的净利润上限-描述"},
                {"col_name": "expEPSLL", "col_show_name": "预期每股收益下限", "col_comment": "预期每股收益下限-描述"},
                {"col_name": "expEPSUPL", "col_show_name": "预期每股收益上限", "col_comment": "预期每股收益上限-描述"},
                {"col_name": "updateTime", "col_show_name": "更新时间", "col_comment": "更新时间-描述"}
            ]
        }
    define_json = json.dumps(fdmtefnew_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def equholderchgcsf_define(table_name):

    equholderchgcsf_str = {
            "table_name": "equholderchgcsf",
            "table_show_name": "报告期证金汇金增减持",
            "table_comment": "报告期证金汇金增减持-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "证券内部编码", "col_comment": "证券内部编码-描述"},
                {"col_name": "ticker", "col_show_name": "股票代码", "col_comment": "股票代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "partyID", "col_show_name": "机构内部ID", "col_comment": "机构内部ID-描述"},
                {"col_name": "shareholderName", "col_show_name": "持股股东姓名", "col_comment": "持股股东姓名-描述"},
                {"col_name": "endDateL", "col_show_name": "上期持股日期，输入格式“YYYYMMDD”",
                 "col_comment": "上期持股日期，输入格式“YYYYMMDD”-描述"},
                {"col_name": "shareNumL", "col_show_name": "上期持股数", "col_comment": "上期持股数-描述"},
                {"col_name": "endDate", "col_show_name": "本期持股日期，输入格式“YYYYMMDD”",
                 "col_comment": "本期持股日期，输入格式“YYYYMMDD”-描述"},
                {"col_name": "shareNum", "col_show_name": "本期持股数", "col_comment": "本期持股数-描述"},
                {"col_name": "holdType", "col_show_name": "持股变动类型", "col_comment": "持股变动类型-描述"}
            ]
        }
    define_json = json.dumps(equholderchgcsf_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def mktinstequd_define(table_name):

    mktinstequd_str = {
            "table_name": "mktinstequd",
            "table_show_name": "行业板块日行情",
            "table_comment": "行业板块日行情-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "industrySymbol", "col_show_name": "申万行业代码", "col_comment": "申万行业代码-描述"},
                {"col_name": "industryName", "col_show_name": "行业名称", "col_comment": "行业名称-描述"},
                {"col_name": "secID", "col_show_name": "行业对应的申万指数内部编码", "col_comment": "行业对应的申万指数内部编码-描述"},
                {"col_name": "indexSymbol", "col_show_name": "行业对应的申万指数交易代码", "col_comment": "行业对应的申万指数交易代码-描述"},
                {"col_name": "tradeDate", "col_show_name": "交易日期", "col_comment": "交易日期-描述"},
                {"col_name": "preClosePrice", "col_show_name": "前收盘价", "col_comment": "前收盘价-描述"},
                {"col_name": "openPrice", "col_show_name": "开盘价", "col_comment": "开盘价-描述"},
                {"col_name": "highestPrice", "col_show_name": "最高价", "col_comment": "最高价-描述"},
                {"col_name": "lowestPrice", "col_show_name": "最低价", "col_comment": "最低价-描述"},
                {"col_name": "closePrice", "col_show_name": "收盘价", "col_comment": "收盘价-描述"},
                {"col_name": "turnoverVol", "col_show_name": "成交量", "col_comment": "成交量-描述"},
                {"col_name": "turnoverValue", "col_show_name": "成交金额", "col_comment": "成交金额-描述"},
                {"col_name": "chgPct", "col_show_name": "当日涨跌幅", "col_comment": "当日涨跌幅-描述"},
                {"col_name": "ticker", "col_show_name": "领涨股，行业中涨幅最大的成分交易代码", "col_comment": "领涨股，行业中涨幅最大的成分交易代码-描述"},
                {"col_name": "upNum", "col_show_name": "上涨股票数", "col_comment": "上涨股票数-描述"},
                {"col_name": "downNum", "col_show_name": "下跌股票数", "col_comment": "下跌股票数-描述"},
                {"col_name": "equalNum", "col_show_name": "平盘股票数", "col_comment": "平盘股票数-描述"},
                {"col_name": "upLimitNum", "col_show_name": "达到涨停股票数", "col_comment": "达到涨停股票数-描述"},
                {"col_name": "downLimitNum", "col_show_name": "达到跌停股票数", "col_comment": "达到跌停股票数-描述"},
                {"col_name": "turnoverRate", "col_show_name": "换手率", "col_comment": "换手率-描述"},
                {"col_name": "netInflow", "col_show_name": "资金净流入额", "col_comment": "资金净流入额-描述"},
                {"col_name": "netMainInflow", "col_show_name": "主力资金净流入额", "col_comment": "主力资金净流入额-描述"},
                {"col_name": "industryID", "col_show_name": "通联编制的行业分类编码", "col_comment": "通联编制的行业分类编码-描述"},
                {"col_name": "chgPct5", "col_show_name": "近5个交易日涨跌幅", "col_comment": "近5个交易日涨跌幅-描述"},
                {"col_name": "chgPct10", "col_show_name": "近10个交易日涨跌幅", "col_comment": "近10个交易日涨跌幅-描述"},
                {"col_name": "chgPct20", "col_show_name": "近20个交易日涨跌幅", "col_comment": "近20个交易日涨跌幅-描述"},
                {"col_name": "chgPctFY", "col_show_name": "今年以来涨跌幅", "col_comment": "今年以来涨跌幅-描述"},
                {"col_name": "updateTime", "col_show_name": "更新时间", "col_comment": "更新时间-描述"}
            ]
        }
    define_json = json.dumps(mktinstequd_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def fdmtisbank2018_define(table_name):

    fdmtisbank2018_str = {
            "table_name": "fdmtisbank2018",
            "table_show_name": "(新)银行业利润表 (Point in time)",
            "table_comment": "(新)银行业利润表 (Point in time)-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "partyID", "col_show_name": "机构内部ID", "col_comment": "机构内部ID-描述"},
                {"col_name": "ticker", "col_show_name": "股票代码", "col_comment": "股票代码-描述"},
                {"col_name": "exchangeCD", "col_show_name": "XSHG-上海证券交易所,XSHE-深圳证券交易所",
                 "col_comment": "XSHG-上海证券交易所,XSHE-深圳证券交易所-描述"},
                {"col_name": "actPubtime", "col_show_name": "实际披露时间", "col_comment": "实际披露时间-描述"},
                {"col_name": "secID", "col_show_name": "证券编码", "col_comment": "证券编码-描述"},
                {"col_name": "publishDate", "col_show_name": "发布日期", "col_comment": "发布日期-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "endDateRep", "col_show_name": "报告截止日期", "col_comment": "报告截止日期-描述"},
                {"col_name": "endDate", "col_show_name": "截止日期", "col_comment": "截止日期-描述"},
                {"col_name": "reportType", "col_show_name": "Q1-一季度,S1-半年度,Q3-第三季度或前三季度,A-年度",
                 "col_comment": "Q1-一季度,S1-半年度,Q3-第三季度或前三季度,A-年度-描述"},
                {"col_name": "fiscalPeriod", "col_show_name": "会计区间", "col_comment": "会计区间-描述"},
                {"col_name": "mergedFlag", "col_show_name": "1-合并；2-母公司", "col_comment": "1-合并；2-母公司-描述"},
                {"col_name": "accoutingStandards", "col_show_name": "CHAS_2018-中国会计准则_2018",
                 "col_comment": "CHAS_2018-中国会计准则_2018-描述"},
                {"col_name": "currencyCD", "col_show_name": "CNY-人民币", "col_comment": "CNY-人民币-描述"},
                {"col_name": "industryCategory", "col_show_name": "按照财务报表内容分类：银行业", "col_comment": "按照财务报表内容分类：银行业-描述"},
                {"col_name": "revenue", "col_show_name": "营业收入", "col_comment": "营业收入-描述"},
                {"col_name": "nIntIncome", "col_show_name": "利息净收入", "col_comment": "利息净收入-描述"},
                {"col_name": "intIncome", "col_show_name": "利息收入", "col_comment": "利息收入-描述"},
                {"col_name": "intExp", "col_show_name": "利息支出", "col_comment": "利息支出-描述"},
                {"col_name": "nCommisIncome", "col_show_name": "手续费及佣金净收入", "col_comment": "手续费及佣金净收入-描述"},
                {"col_name": "commisIncome", "col_show_name": "手续费及佣金收入", "col_comment": "手续费及佣金收入-描述"},
                {"col_name": "commisExp", "col_show_name": "手续费及佣金支出", "col_comment": "手续费及佣金支出-描述"},
                {"col_name": "othGain", "col_show_name": "其他收益", "col_comment": "其他收益-描述"},
                {"col_name": "investIncome", "col_show_name": "投资收益(损失以“－”号填列)", "col_comment": "投资收益(损失以“－”号填列)-描述"},
                {"col_name": "aJInvestIncome", "col_show_name": "其中:对联营企业和合营企业的投资收益",
                 "col_comment": "其中:对联营企业和合营企业的投资收益-描述"},
                {"col_name": "tafQuitGain", "col_show_name": "以摊余成本计量的金融资产终止确认收益（损失以“-”号填列）",
                 "col_comment": "以摊余成本计量的金融资产终止确认收益（损失以“-”号填列）-描述"},
                {"col_name": "netExpHIncome", "col_show_name": "净敞口套期收益（损失以“-”号填列）",
                 "col_comment": "净敞口套期收益（损失以“-”号填列）-描述"},
                {"col_name": "fValueChgGain", "col_show_name": "公允价值变动收益(损失以“－”号填列)",
                 "col_comment": "公允价值变动收益(损失以“－”号填列)-描述"},
                {"col_name": "assetsImpairLoss", "col_show_name": "资产减值损失（损失以“-”号填列）",
                 "col_comment": "资产减值损失（损失以“-”号填列）-描述"},
                {"col_name": "creditImpairLoss", "col_show_name": "信用减值损失（损失以“-”号填列）",
                 "col_comment": "信用减值损失（损失以“-”号填列）-描述"},
                {"col_name": "assetsDispGain", "col_show_name": "资产处置收益（损失以“-”号填列）",
                 "col_comment": "资产处置收益（损失以“-”号填列）-描述"},
                {"col_name": "forexGain", "col_show_name": "汇兑收益(损失以“-”号填列)", "col_comment": "汇兑收益(损失以“-”号填列)-描述"},
                {"col_name": "othOperRev", "col_show_name": "其他业务收入", "col_comment": "其他业务收入-描述"},
                {"col_name": "specOr", "col_show_name": "营业收入特殊项目", "col_comment": "营业收入特殊项目-描述"},
                {"col_name": "aor", "col_show_name": "营业收入调整金额", "col_comment": "营业收入调整金额-描述"},
                {"col_name": "cogs", "col_show_name": "营业支出", "col_comment": "营业支出-描述"},
                {"col_name": "bizTaxSurchg", "col_show_name": "税金及附加", "col_comment": "税金及附加-描述"},
                {"col_name": "genlAdminExp", "col_show_name": "业务及管理费", "col_comment": "业务及管理费-描述"},
                {"col_name": "othOperCosts", "col_show_name": "其他业务支出", "col_comment": "其他业务支出-描述"},
                {"col_name": "specOp", "col_show_name": "营业支出特殊项目", "col_comment": "营业支出特殊项目-描述"},
                {"col_name": "aop", "col_show_name": "营业支出调整金额", "col_comment": "营业支出调整金额-描述"},
                {"col_name": "othEffectOp", "col_show_name": "影响营业利润的调整项目", "col_comment": "影响营业利润的调整项目-描述"},
                {"col_name": "aeEffectOp", "col_show_name": "影响营业利润的差错金额", "col_comment": "影响营业利润的差错金额-描述"},
                {"col_name": "operateProfit", "col_show_name": "营业利润(亏损以“－”号填列)", "col_comment": "营业利润(亏损以“－”号填列)-描述"},
                {"col_name": "noperateIncome", "col_show_name": "营业外收入", "col_comment": "营业外收入-描述"},
                {"col_name": "noperateExp", "col_show_name": "营业外支出", "col_comment": "营业外支出-描述"},
                {"col_name": "othEffectTp", "col_show_name": "影响利润总额的调整金额", "col_comment": "影响利润总额的调整金额-描述"},
                {"col_name": "aeEffectTp", "col_show_name": "影响利润总额的差错金额", "col_comment": "影响利润总额的差错金额-描述"},
                {"col_name": "tProfit", "col_show_name": "利润总额(亏损总额以“－”号填列)", "col_comment": "利润总额(亏损总额以“－”号填列)-描述"},
                {"col_name": "incomeTax", "col_show_name": "所得税费用", "col_comment": "所得税费用-描述"},
                {"col_name": "othEffectNp", "col_show_name": "影响净利润的调整项目", "col_comment": "影响净利润的调整项目-描述"},
                {"col_name": "aeEffectNp", "col_show_name": "影响净利润的差错金额", "col_comment": "影响净利润的差错金额-描述"},
                {"col_name": "nIncome", "col_show_name": "净利润(净亏损以“－”号填列)", "col_comment": "净利润(净亏损以“－”号填列)-描述"},
                {"col_name": "nIncomeAttrP", "col_show_name": "归属于母公司所有者(或股东)的净利润",
                 "col_comment": "归属于母公司所有者(或股东)的净利润-描述"},
                {"col_name": "minorityGain", "col_show_name": "少数股东损益", "col_comment": "少数股东损益-描述"},
                {"col_name": "goingConcernNi", "col_show_name": "持续经营净利润", "col_comment": "持续经营净利润-描述"},
                {"col_name": "quitConcernNi", "col_show_name": "终止经营净利润", "col_comment": "终止经营净利润-描述"},
                {"col_name": "othEffectNpp", "col_show_name": "影响净利润分配的调整项目", "col_comment": "影响净利润分配的调整项目-描述"},
                {"col_name": "aeEffectNpp", "col_show_name": "影响净利润分配的差错金额", "col_comment": "影响净利润分配的差错金额-描述"},
                {"col_name": "basicEps", "col_show_name": "基本每股收益", "col_comment": "基本每股收益-描述"},
                {"col_name": "dilutedEps", "col_show_name": "稀释每股收益", "col_comment": "稀释每股收益-描述"},
                {"col_name": "othComprIncome", "col_show_name": "其他综合收益", "col_comment": "其他综合收益-描述"},
                {"col_name": "othEffectCi", "col_show_name": "影响综合收益总额的调整项目", "col_comment": "影响综合收益总额的调整项目-描述"},
                {"col_name": "aeEffectCi", "col_show_name": "影响综合收益总额的差错金额", "col_comment": "影响综合收益总额的差错金额-描述"},
                {"col_name": "tComprIncome", "col_show_name": "综合收益总额", "col_comment": "综合收益总额-描述"},
                {"col_name": "comprIncAttrP", "col_show_name": "归属于母公司所有者(或股东)的综合收益总额",
                 "col_comment": "归属于母公司所有者(或股东)的综合收益总额-描述"},
                {"col_name": "comprIncAttrMS", "col_show_name": "归属于少数股东的综合收益总额", "col_comment": "归属于少数股东的综合收益总额-描述"},
                {"col_name": "othEffectPci", "col_show_name": "影响综合收益总额分配的调整项目", "col_comment": "影响综合收益总额分配的调整项目-描述"},
                {"col_name": "aeEffectPci", "col_show_name": "影响综合收益总额分配的差错金额", "col_comment": "影响综合收益总额分配的差错金额-描述"}
            ]
        }
    define_json = json.dumps(fdmtisbank2018_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def fdmtisindu2018_define(table_name):

    fdmtisindu2018_str = {
            "table_name": "fdmtisindu2018",
            "table_show_name": "(新)保险业利润表 (Point in time)",
            "table_comment": "(新)保险业利润表 (Point in time)-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "partyID", "col_show_name": "机构内部ID", "col_comment": "机构内部ID-描述"},
                {"col_name": "ticker", "col_show_name": "股票代码", "col_comment": "股票代码-描述"},
                {"col_name": "exchangeCD", "col_show_name": "XSHG-上海证券交易所,XSHE-深圳证券交易所",
                 "col_comment": "XSHG-上海证券交易所,XSHE-深圳证券交易所-描述"},
                {"col_name": "secID", "col_show_name": "证券编码", "col_comment": "证券编码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "endDateRep", "col_show_name": "报告截止日期", "col_comment": "报告截止日期-描述"},
                {"col_name": "endDate", "col_show_name": "截止日期", "col_comment": "截止日期-描述"},
                {"col_name": "reportType", "col_show_name": "Q1-一季度,S1-半年度,Q3-第三季度或前三季度,A-年度",
                 "col_comment": "Q1-一季度,S1-半年度,Q3-第三季度或前三季度,A-年度-描述"},
                {"col_name": "fiscalPeriod", "col_show_name": "会计区间", "col_comment": "会计区间-描述"},
                {"col_name": "mergedFlag", "col_show_name": "1-合并；2-母公司", "col_comment": "1-合并；2-母公司-描述"},
                {"col_name": "accoutingStandards", "col_show_name": "CHAS_2018-中国会计准则_2018",
                 "col_comment": "CHAS_2018-中国会计准则_2018-描述"},
                {"col_name": "currencyCD", "col_show_name": "CNY-人民币", "col_comment": "CNY-人民币-描述"},
                {"col_name": "industryCategory", "col_show_name": "按照财务报表内容分类：一般工商业",
                 "col_comment": "按照财务报表内容分类：一般工商业-描述"},
                {"col_name": "tRevenue", "col_show_name": "营业总收入", "col_comment": "营业总收入-描述"},
                {"col_name": "revenue", "col_show_name": "营业收入", "col_comment": "营业收入-描述"},
                {"col_name": "intIncome", "col_show_name": "利息收入", "col_comment": "利息收入-描述"},
                {"col_name": "premEarned", "col_show_name": "已赚保费", "col_comment": "已赚保费-描述"},
                {"col_name": "commisIncome", "col_show_name": "手续费及佣金收入", "col_comment": "手续费及佣金收入-描述"},
                {"col_name": "specOr", "col_show_name": "营业总收入的调整项目", "col_comment": "营业总收入的调整项目-描述"},
                {"col_name": "aor", "col_show_name": "营业总收入的差错金额", "col_comment": "营业总收入的差错金额-描述"},
                {"col_name": "tCogs", "col_show_name": "营业总成本", "col_comment": "营业总成本-描述"},
                {"col_name": "cogs", "col_show_name": "营业成本", "col_comment": "营业成本-描述"},
                {"col_name": "intExp", "col_show_name": "利息支出", "col_comment": "利息支出-描述"},
                {"col_name": "commisExp", "col_show_name": "手续费及佣金支出", "col_comment": "手续费及佣金支出-描述"},
                {"col_name": "premRefund", "col_show_name": "退保金", "col_comment": "退保金-描述"},
                {"col_name": "nCompensPayout", "col_show_name": "赔付支出净额", "col_comment": "赔付支出净额-描述"},
                {"col_name": "reserInsurContr", "col_show_name": "提取保险合同准备金净额", "col_comment": "提取保险合同准备金净额-描述"},
                {"col_name": "policyDivPayt", "col_show_name": "保单红利支出", "col_comment": "保单红利支出-描述"},
                {"col_name": "reinsurExp", "col_show_name": "分保费用", "col_comment": "分保费用-描述"},
                {"col_name": "bizTaxSurchg", "col_show_name": "税金及附加", "col_comment": "税金及附加-描述"},
                {"col_name": "sellExp", "col_show_name": "销售费用", "col_comment": "销售费用-描述"},
                {"col_name": "adminExp", "col_show_name": "管理费用", "col_comment": "管理费用-描述"},
                {"col_name": "rDExp", "col_show_name": "研发费用", "col_comment": "研发费用-描述"},
                {"col_name": "finanExp", "col_show_name": "财务费用", "col_comment": "财务费用-描述"},
                {"col_name": "intExpFinanExp", "col_show_name": "其中:利息费用", "col_comment": "其中:利息费用-描述"},
                {"col_name": "intIncomeFinanExp", "col_show_name": "其中:利息收入", "col_comment": "其中:利息收入-描述"},
                {"col_name": "specToc", "col_show_name": "营业总成本的调整项目", "col_comment": "营业总成本的调整项目-描述"},
                {"col_name": "atoc", "col_show_name": "营业总成本的差错金额", "col_comment": "营业总成本的差错金额-描述"},
                {"col_name": "othGain", "col_show_name": "其他收益", "col_comment": "其他收益-描述"},
                {"col_name": "investIncome", "col_show_name": "投资收益(损失以“－”号填列)", "col_comment": "投资收益(损失以“－”号填列)-描述"},
                {"col_name": "aJInvestIncome", "col_show_name": "其中:对联营企业和合营企业的投资收益",
                 "col_comment": "其中:对联营企业和合营企业的投资收益-描述"},
                {"col_name": "tafQuitGain", "col_show_name": "以摊余成本计量的金融资产终止确认收益（损失以“-”号填列）",
                 "col_comment": "以摊余成本计量的金融资产终止确认收益（损失以“-”号填列）-描述"},
                {"col_name": "netExpHIncome", "col_show_name": "净敞口套期收益（损失以“-”号填列）",
                 "col_comment": "净敞口套期收益（损失以“-”号填列）-描述"},
                {"col_name": "fValueChgGain", "col_show_name": "公允价值变动收益(损失以“－”号填列)",
                 "col_comment": "公允价值变动收益(损失以“－”号填列)-描述"},
                {"col_name": "assetsImpairLoss", "col_show_name": "资产减值损失（损失以“-”号填列）",
                 "col_comment": "资产减值损失（损失以“-”号填列）-描述"},
                {"col_name": "creditImpairLoss", "col_show_name": "信用减值损失（损失以“-”号填列）",
                 "col_comment": "信用减值损失（损失以“-”号填列）-描述"},
                {"col_name": "assetsDispGain", "col_show_name": "资产处置收益（损失以“-”号填列）",
                 "col_comment": "资产处置收益（损失以“-”号填列）-描述"},
                {"col_name": "forexGain", "col_show_name": "汇兑收益(损失以“-”号填列)", "col_comment": "汇兑收益(损失以“-”号填列)-描述"},
                {"col_name": "othEffectOp", "col_show_name": "影响营业利润的调整项目", "col_comment": "影响营业利润的调整项目-描述"},
                {"col_name": "aeEffectOp", "col_show_name": "影响营业利润的差错金额", "col_comment": "影响营业利润的差错金额-描述"},
                {"col_name": "operateProfit", "col_show_name": "营业利润(亏损以“－”号填列)", "col_comment": "营业利润(亏损以“－”号填列)-描述"},
                {"col_name": "noperateIncome", "col_show_name": "营业外收入", "col_comment": "营业外收入-描述"},
                {"col_name": "noperateExp", "col_show_name": "营业外支出", "col_comment": "营业外支出-描述"},
                {"col_name": "ncaDisploss", "col_show_name": "其中:非流动资产处置损失", "col_comment": "其中:非流动资产处置损失-描述"},
                {"col_name": "othEffectTp", "col_show_name": "影响利润总额的调整项目", "col_comment": "影响利润总额的调整项目-描述"},
                {"col_name": "aeEffectTp", "col_show_name": "影响利润总额的差错金额", "col_comment": "影响利润总额的差错金额-描述"},
                {"col_name": "tProfit", "col_show_name": "利润总额(亏损总额以“－”号填列)", "col_comment": "利润总额(亏损总额以“－”号填列)-描述"},
                {"col_name": "incomeTax", "col_show_name": "所得税费用", "col_comment": "所得税费用-描述"},
                {"col_name": "othEffectNp", "col_show_name": "影响净利润的调整项目", "col_comment": "影响净利润的调整项目-描述"},
                {"col_name": "aeEffectNp", "col_show_name": "影响净利润的差错金额", "col_comment": "影响净利润的差错金额-描述"},
                {"col_name": "nIncome", "col_show_name": "净利润(净亏损以“－”号填列)", "col_comment": "净利润(净亏损以“－”号填列)-描述"},
                {"col_name": "nIncomeBma", "col_show_name": "其中:被合并方在合并前实现的净利润", "col_comment": "其中:被合并方在合并前实现的净利润-描述"},
                {"col_name": "nIncomeAttrP", "col_show_name": "归属于母公司所有者(或股东)的净利润",
                 "col_comment": "归属于母公司所有者(或股东)的净利润-描述"},
                {"col_name": "minorityGain", "col_show_name": "少数股东损益", "col_comment": "少数股东损益-描述"},
                {"col_name": "goingConcernNi", "col_show_name": "持续经营净利润", "col_comment": "持续经营净利润-描述"},
                {"col_name": "quitConcernNi", "col_show_name": "终止经营净利润", "col_comment": "终止经营净利润-描述"},
                {"col_name": "othEffectNpp", "col_show_name": "影响净利润分配的调整项目", "col_comment": "影响净利润分配的调整项目-描述"},
                {"col_name": "aeEffectNpp", "col_show_name": "影响净利润分配的差错金额", "col_comment": "影响净利润分配的差错金额-描述"},
                {"col_name": "basicEps", "col_show_name": "基本每股收益", "col_comment": "基本每股收益-描述"},
                {"col_name": "dilutedEps", "col_show_name": "稀释每股收益", "col_comment": "稀释每股收益-描述"},
                {"col_name": "othComprIncome", "col_show_name": "其他综合收益", "col_comment": "其他综合收益-描述"},
                {"col_name": "othEffectCi", "col_show_name": "影响综合收益总额的调整项目", "col_comment": "影响综合收益总额的调整项目-描述"},
                {"col_name": "aeEffectCi", "col_show_name": "影响综合收益总额的差错金额", "col_comment": "影响综合收益总额的差错金额-描述"},
                {"col_name": "tComprIncome", "col_show_name": "综合收益总额", "col_comment": "综合收益总额-描述"},
                {"col_name": "comprIncAttrP", "col_show_name": "归属于母公司所有者(或股东)的综合收益总额",
                 "col_comment": "归属于母公司所有者(或股东)的综合收益总额-描述"},
                {"col_name": "comprIncAttrMS", "col_show_name": "归属于少数股东的综合收益总额", "col_comment": "归属于少数股东的综合收益总额-描述"},
                {"col_name": "othEffectPci", "col_show_name": "影响综合收益总额分配的调整项目", "col_comment": "影响综合收益总额分配的调整项目-描述"},
                {"col_name": "aeEffectPci", "col_show_name": "影响综合收益总额分配的差错金额", "col_comment": "影响综合收益总额分配的差错金额-描述"},
                {"col_name": "actPubtime", "col_show_name": "实际披露时间", "col_comment": "实际披露时间-描述"},
                {"col_name": "publishDate", "col_show_name": "发布日期", "col_comment": "发布日期-描述"}
            ]
        }
    define_json = json.dumps(fdmtisindu2018_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def fdmtissecu2018_define(table_name):

    fdmtissecu2018_str = {
            "table_name": "fdmtissecu2018",
            "table_show_name": "(新)证券业利润表 (Point in time)",
            "table_comment": "(新)证券业利润表 (Point in time)-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "partyID", "col_show_name": "机构内部ID", "col_comment": "机构内部ID-描述"},
                {"col_name": "ticker", "col_show_name": "股票代码", "col_comment": "股票代码-描述"},
                {"col_name": "exchangeCD", "col_show_name": "XSHG-上海证券交易所,XSHE-深圳证券交易所",
                 "col_comment": "XSHG-上海证券交易所,XSHE-深圳证券交易所-描述"},
                {"col_name": "actPubtime", "col_show_name": "实际披露时间", "col_comment": "实际披露时间-描述"},
                {"col_name": "secID", "col_show_name": "证券编码", "col_comment": "证券编码-描述"},
                {"col_name": "publishDate", "col_show_name": "发布日期", "col_comment": "发布日期-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "endDateRep", "col_show_name": "报告截止日期", "col_comment": "报告截止日期-描述"},
                {"col_name": "endDate", "col_show_name": "截止日期", "col_comment": "截止日期-描述"},
                {"col_name": "reportType", "col_show_name": "Q1-一季度,S1-半年度,Q3-第三季度或前三季度,A-年度",
                 "col_comment": "Q1-一季度,S1-半年度,Q3-第三季度或前三季度,A-年度-描述"},
                {"col_name": "fiscalPeriod", "col_show_name": "会计区间", "col_comment": "会计区间-描述"},
                {"col_name": "mergedFlag", "col_show_name": "1-合并；2-母公司", "col_comment": "1-合并；2-母公司-描述"},
                {"col_name": "accoutingStandards", "col_show_name": "CHAS_2018-中国会计准则_2018",
                 "col_comment": "CHAS_2018-中国会计准则_2018-描述"},
                {"col_name": "currencyCD", "col_show_name": "CNY-人民币", "col_comment": "CNY-人民币-描述"},
                {"col_name": "industryCategory", "col_show_name": "按照财务报表内容分类：证券业", "col_comment": "按照财务报表内容分类：证券业-描述"},
                {"col_name": "revenue", "col_show_name": "营业收入", "col_comment": "营业收入-描述"},
                {"col_name": "nCommisIncome", "col_show_name": "手续费及佣金净收入", "col_comment": "手续费及佣金净收入-描述"},
                {"col_name": "nSecTaIncome", "col_show_name": "其中:代理买卖证券业务净收入", "col_comment": "其中:代理买卖证券业务净收入-描述"},
                {"col_name": "nUndwrtSecIncome", "col_show_name": "证券承销业务净收入", "col_comment": "证券承销业务净收入-描述"},
                {"col_name": "nTrustIncome", "col_show_name": "委托客户资产管理业务净收入", "col_comment": "委托客户资产管理业务净收入-描述"},
                {"col_name": "nIntIncome", "col_show_name": "利息净收入", "col_comment": "利息净收入-描述"},
                {"col_name": "othGain", "col_show_name": "其他收益", "col_comment": "其他收益-描述"},
                {"col_name": "investIncome", "col_show_name": "投资收益(损失以“－”号填列)", "col_comment": "投资收益(损失以“－”号填列)-描述"},
                {"col_name": "aJInvestIncome", "col_show_name": "其中:对联营企业和合营企业的投资收益",
                 "col_comment": "其中:对联营企业和合营企业的投资收益-描述"},
                {"col_name": "tafQuitGain", "col_show_name": "以摊余成本计量的金融资产终止确认收益（损失以“-”号填列）",
                 "col_comment": "以摊余成本计量的金融资产终止确认收益（损失以“-”号填列）-描述"},
                {"col_name": "netExpHIncome", "col_show_name": "净敞口套期收益（损失以“-”号填列）",
                 "col_comment": "净敞口套期收益（损失以“-”号填列）-描述"},
                {"col_name": "fValueChgGain", "col_show_name": "公允价值变动收益(损失以“－”号填列)",
                 "col_comment": "公允价值变动收益(损失以“－”号填列)-描述"},
                {"col_name": "assetsImpairLoss", "col_show_name": "资产减值损失（损失以“-”号填列）",
                 "col_comment": "资产减值损失（损失以“-”号填列）-描述"},
                {"col_name": "creditImpairLoss", "col_show_name": "信用减值损失（损失以“-”号填列）",
                 "col_comment": "信用减值损失（损失以“-”号填列）-描述"},
                {"col_name": "assetsDispGain", "col_show_name": "资产处置收益（损失以“-”号填列）",
                 "col_comment": "资产处置收益（损失以“-”号填列）-描述"},
                {"col_name": "forexGain", "col_show_name": "汇兑收益(损失以“-”号填列)", "col_comment": "汇兑收益(损失以“-”号填列)-描述"},
                {"col_name": "othOperRev", "col_show_name": "其他业务收入", "col_comment": "其他业务收入-描述"},
                {"col_name": "specOr", "col_show_name": "营业收入特殊项目", "col_comment": "营业收入特殊项目-描述"},
                {"col_name": "aor", "col_show_name": "营业收入调整金额", "col_comment": "营业收入调整金额-描述"},
                {"col_name": "cogs", "col_show_name": "营业支出", "col_comment": "营业支出-描述"},
                {"col_name": "bizTaxSurchg", "col_show_name": "税金及附加", "col_comment": "税金及附加-描述"},
                {"col_name": "genlAdminExp", "col_show_name": "业务及管理费", "col_comment": "业务及管理费-描述"},
                {"col_name": "othOperCosts", "col_show_name": "其他业务支出", "col_comment": "其他业务支出-描述"},
                {"col_name": "specOp", "col_show_name": "营业支出特殊项目", "col_comment": "营业支出特殊项目-描述"},
                {"col_name": "aop", "col_show_name": "营业支出调整金额", "col_comment": "营业支出调整金额-描述"},
                {"col_name": "othEffectOp", "col_show_name": "影响营业利润的调整项目", "col_comment": "影响营业利润的调整项目-描述"},
                {"col_name": "aeEffectOp", "col_show_name": "影响营业利润的差错金额", "col_comment": "影响营业利润的差错金额-描述"},
                {"col_name": "operateProfit", "col_show_name": "营业利润(亏损以“－”号填列)", "col_comment": "营业利润(亏损以“－”号填列)-描述"},
                {"col_name": "noperateIncome", "col_show_name": "营业外收入", "col_comment": "营业外收入-描述"},
                {"col_name": "noperateExp", "col_show_name": "营业外支出", "col_comment": "营业外支出-描述"},
                {"col_name": "othEffectTp", "col_show_name": "影响利润总额的调整项目", "col_comment": "影响利润总额的调整项目-描述"},
                {"col_name": "aeEffectTp", "col_show_name": "影响利润总额的差错金额", "col_comment": "影响利润总额的差错金额-描述"},
                {"col_name": "tProfit", "col_show_name": "利润总额(亏损总额以“－”号填列)", "col_comment": "利润总额(亏损总额以“－”号填列)-描述"},
                {"col_name": "incomeTax", "col_show_name": "所得税费用", "col_comment": "所得税费用-描述"},
                {"col_name": "othEffectNp", "col_show_name": "影响净利润的调整项目", "col_comment": "影响净利润的调整项目-描述"},
                {"col_name": "aeEffectNp", "col_show_name": "影响净利润的差错金额", "col_comment": "影响净利润的差错金额-描述"},
                {"col_name": "nIncome", "col_show_name": "净利润(净亏损以“－”号填列)", "col_comment": "净利润(净亏损以“－”号填列)-描述"},
                {"col_name": "nIncomeAttrP", "col_show_name": "归属于母公司所有者(或股东)的净利润",
                 "col_comment": "归属于母公司所有者(或股东)的净利润-描述"},
                {"col_name": "minorityGain", "col_show_name": "少数股东损益", "col_comment": "少数股东损益-描述"},
                {"col_name": "goingConcernNi", "col_show_name": "持续经营净利润", "col_comment": "持续经营净利润-描述"},
                {"col_name": "quitConcernNi", "col_show_name": "终止经营净利润", "col_comment": "终止经营净利润-描述"},
                {"col_name": "othEffectNpp", "col_show_name": "影响净利润分配的调整项目", "col_comment": "影响净利润分配的调整项目-描述"},
                {"col_name": "aeEffectNpp", "col_show_name": "影响净利润分配的差错金额", "col_comment": "影响净利润分配的差错金额-描述"},
                {"col_name": "basicEps", "col_show_name": "基本每股收益", "col_comment": "基本每股收益-描述"},
                {"col_name": "dilutedEps", "col_show_name": "稀释每股收益", "col_comment": "稀释每股收益-描述"},
                {"col_name": "othComprIncome", "col_show_name": "其他综合收益", "col_comment": "其他综合收益-描述"},
                {"col_name": "othEffectCi", "col_show_name": "影响综合收益总额的调整项目", "col_comment": "影响综合收益总额的调整项目-描述"},
                {"col_name": "aeEffectCi", "col_show_name": "影响综合收益总额的差错金额", "col_comment": "影响综合收益总额的差错金额-描述"},
                {"col_name": "tComprIncome", "col_show_name": "综合收益总额", "col_comment": "综合收益总额-描述"},
                {"col_name": "comprIncAttrP", "col_show_name": "归属于母公司所有者(或股东)的综合收益总额",
                 "col_comment": "归属于母公司所有者(或股东)的综合收益总额-描述"},
                {"col_name": "comprIncAttrMS", "col_show_name": "归属于少数股东的综合收益总额", "col_comment": "归属于少数股东的综合收益总额-描述"},
                {"col_name": "othEffectPci", "col_show_name": "影响综合收益总额分配的调整项目", "col_comment": "影响综合收益总额分配的调整项目-描述"},
                {"col_name": "aeEffectPci", "col_show_name": "影响综合收益总额分配的差错金额", "col_comment": "影响综合收益总额分配的差错金额-描述"}
            ]
        }
    define_json = json.dumps(fdmtissecu2018_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def fdmtisinsu2018_define(table_name):

    fdmtisinsu2018_str = {
            "table_name": "fdmtisinsu2018",
            "table_show_name": "(新)一般工商业利润表 (Point in time)",
            "table_comment": "(新)一般工商业利润表 (Point in time)-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "partyID", "col_show_name": "机构内部ID", "col_comment": "机构内部ID-描述"},
                {"col_name": "ticker", "col_show_name": "股票代码", "col_comment": "股票代码-描述"},
                {"col_name": "exchangeCD", "col_show_name": "XSHG-上海证券交易所,XSHE-深圳证券交易所",
                 "col_comment": "XSHG-上海证券交易所,XSHE-深圳证券交易所-描述"},
                {"col_name": "actPubtime", "col_show_name": "实际披露时间", "col_comment": "实际披露时间-描述"},
                {"col_name": "secID", "col_show_name": "证券编码", "col_comment": "证券编码-描述"},
                {"col_name": "publishDate", "col_show_name": "发布日期", "col_comment": "发布日期-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "endDateRep", "col_show_name": "报告截止日期", "col_comment": "报告截止日期-描述"},
                {"col_name": "endDate", "col_show_name": "截止日期", "col_comment": "截止日期-描述"},
                {"col_name": "reportType", "col_show_name": "Q1-一季度,S1-半年度,Q3-第三季度或前三季度,A-年度",
                 "col_comment": "Q1-一季度,S1-半年度,Q3-第三季度或前三季度,A-年度-描述"},
                {"col_name": "fiscalPeriod", "col_show_name": "会计区间", "col_comment": "会计区间-描述"},
                {"col_name": "mergedFlag", "col_show_name": "1-合并；2-母公司", "col_comment": "1-合并；2-母公司-描述"},
                {"col_name": "accoutingStandards", "col_show_name": "CHAS_2018-中国会计准则_2018",
                 "col_comment": "CHAS_2018-中国会计准则_2018-描述"},
                {"col_name": "currencyCD", "col_show_name": "CNY-人民币", "col_comment": "CNY-人民币-描述"},
                {"col_name": "industryCategory", "col_show_name": "按照财务报表内容分类：保险业", "col_comment": "按照财务报表内容分类：保险业-描述"},
                {"col_name": "revenue", "col_show_name": "营业收入", "col_comment": "营业收入-描述"},
                {"col_name": "premEarned", "col_show_name": "已赚保费", "col_comment": "已赚保费-描述"},
                {"col_name": "grossPremWrit", "col_show_name": "保险业务收入", "col_comment": "保险业务收入-描述"},
                {"col_name": "reinsIncome", "col_show_name": "其中:分保费收入", "col_comment": "其中:分保费收入-描述"},
                {"col_name": "reinsur", "col_show_name": "减:分出保费", "col_comment": "减:分出保费-描述"},
                {"col_name": "unePremReser", "col_show_name": "提取未到期责任准备金", "col_comment": "提取未到期责任准备金-描述"},
                {"col_name": "othGain", "col_show_name": "其他收益", "col_comment": "其他收益-描述"},
                {"col_name": "investIncome", "col_show_name": "投资收益(损失以“－”号填列)", "col_comment": "投资收益(损失以“－”号填列)-描述"},
                {"col_name": "aJInvestIncome", "col_show_name": "其中:对联营企业和合营企业的投资收益",
                 "col_comment": "其中:对联营企业和合营企业的投资收益-描述"},
                {"col_name": "tafQuitGain", "col_show_name": "以摊余成本计量的金融资产终止确认收益（损失以“-”号填列）",
                 "col_comment": "以摊余成本计量的金融资产终止确认收益（损失以“-”号填列）-描述"},
                {"col_name": "netExpHIncome", "col_show_name": "净敞口套期收益（损失以“-”号填列）",
                 "col_comment": "净敞口套期收益（损失以“-”号填列）-描述"},
                {"col_name": "fValueChgGain", "col_show_name": "公允价值变动收益(损失以“－”号填列)",
                 "col_comment": "公允价值变动收益(损失以“－”号填列)-描述"},
                {"col_name": "assetsImpairLoss", "col_show_name": "资产减值损失（损失以“-”号填列）",
                 "col_comment": "资产减值损失（损失以“-”号填列）-描述"},
                {"col_name": "creditImpairLoss", "col_show_name": "信用减值损失（损失以“-”号填列）",
                 "col_comment": "信用减值损失（损失以“-”号填列）-描述"},
                {"col_name": "assetsDispGain", "col_show_name": "资产处置收益（损失以“-”号填列）",
                 "col_comment": "资产处置收益（损失以“-”号填列）-描述"},
                {"col_name": "forexGain", "col_show_name": "汇兑收益(损失以“-”号填列)", "col_comment": "汇兑收益(损失以“-”号填列)-描述"},
                {"col_name": "othOperRev", "col_show_name": "其他业务收入", "col_comment": "其他业务收入-描述"},
                {"col_name": "specOr", "col_show_name": "营业收入特殊项目", "col_comment": "营业收入特殊项目-描述"},
                {"col_name": "aor", "col_show_name": "营业收入调整金额", "col_comment": "营业收入调整金额-描述"},
                {"col_name": "cogs", "col_show_name": "营业支出", "col_comment": "营业支出-描述"},
                {"col_name": "premRefund", "col_show_name": "退保金", "col_comment": "退保金-描述"},
                {"col_name": "compensPayout", "col_show_name": "赔付支出", "col_comment": "赔付支出-描述"},
                {"col_name": "compensPayoutRefu", "col_show_name": "减:摊回赔付支出", "col_comment": "减:摊回赔付支出-描述"},
                {"col_name": "reserInsurLiab", "col_show_name": "提取保险责任准备金", "col_comment": "提取保险责任准备金-描述"},
                {"col_name": "insurLiabReserRefu", "col_show_name": "减:摊回保险责任准备金", "col_comment": "减:摊回保险责任准备金-描述"},
                {"col_name": "policyDivPayt", "col_show_name": "保单红利支出", "col_comment": "保单红利支出-描述"},
                {"col_name": "reinsurExp", "col_show_name": "分保费用", "col_comment": "分保费用-描述"},
                {"col_name": "bizTaxSurchg", "col_show_name": "税金及附加", "col_comment": "税金及附加-描述"},
                {"col_name": "commisExp", "col_show_name": "手续费及佣金支出", "col_comment": "手续费及佣金支出-描述"},
                {"col_name": "genlAdminExp", "col_show_name": "业务及管理费", "col_comment": "业务及管理费-描述"},
                {"col_name": "reinsCostRefund", "col_show_name": "减:摊回分保费用", "col_comment": "减:摊回分保费用-描述"},
                {"col_name": "othOperCosts", "col_show_name": "其他业务支出", "col_comment": "其他业务支出-描述"},
                {"col_name": "specOp", "col_show_name": "营业支出特殊项目", "col_comment": "营业支出特殊项目-描述"},
                {"col_name": "aop", "col_show_name": "营业支出调整金额", "col_comment": "营业支出调整金额-描述"},
                {"col_name": "othEffectOp", "col_show_name": "影响营业利润的调整项目", "col_comment": "影响营业利润的调整项目-描述"},
                {"col_name": "aeEffectOp", "col_show_name": "影响营业利润的差错金额", "col_comment": "影响营业利润的差错金额-描述"},
                {"col_name": "operateProfit", "col_show_name": "营业利润(亏损以“－”号填列)", "col_comment": "营业利润(亏损以“－”号填列)-描述"},
                {"col_name": "noperateIncome", "col_show_name": "营业外收入", "col_comment": "营业外收入-描述"},
                {"col_name": "noperateExp", "col_show_name": "营业外支出", "col_comment": "营业外支出-描述"},
                {"col_name": "othEffectTp", "col_show_name": "影响利润总额的调整项目", "col_comment": "影响利润总额的调整项目-描述"},
                {"col_name": "aeEffectTp", "col_show_name": "影响利润总额的差错金额", "col_comment": "影响利润总额的差错金额-描述"},
                {"col_name": "tProfit", "col_show_name": "利润总额(亏损总额以“－”号填列)", "col_comment": "利润总额(亏损总额以“－”号填列)-描述"},
                {"col_name": "incomeTax", "col_show_name": "所得税费用", "col_comment": "所得税费用-描述"},
                {"col_name": "othEffectNp", "col_show_name": "影响净利润的调整项目", "col_comment": "影响净利润的调整项目-描述"},
                {"col_name": "aeEffectNp", "col_show_name": "影响净利润的差错金额", "col_comment": "影响净利润的差错金额-描述"},
                {"col_name": "nIncome", "col_show_name": "净利润(净亏损以“－”号填列)", "col_comment": "净利润(净亏损以“－”号填列)-描述"},
                {"col_name": "goingConcernNi", "col_show_name": "持续经营净利润", "col_comment": "持续经营净利润-描述"},
                {"col_name": "quitConcernNi", "col_show_name": "终止经营净利润", "col_comment": "终止经营净利润-描述"},
                {"col_name": "nIncomeAttrP", "col_show_name": "归属于母公司所有者(或股东)的净利润",
                 "col_comment": "归属于母公司所有者(或股东)的净利润-描述"},
                {"col_name": "minorityGain", "col_show_name": "少数股东损益", "col_comment": "少数股东损益-描述"},
                {"col_name": "othEffectNpp", "col_show_name": "影响净利润分配的调整项目", "col_comment": "影响净利润分配的调整项目-描述"},
                {"col_name": "aeEffectNpp", "col_show_name": "影响净利润分配的差错金额", "col_comment": "影响净利润分配的差错金额-描述"},
                {"col_name": "basicEps", "col_show_name": "基本每股收益", "col_comment": "基本每股收益-描述"},
                {"col_name": "dilutedEps", "col_show_name": "稀释每股收益", "col_comment": "稀释每股收益-描述"},
                {"col_name": "othComprIncome", "col_show_name": "其他综合收益", "col_comment": "其他综合收益-描述"},
                {"col_name": "othEffectCi", "col_show_name": "影响综合收益总额的调整项目", "col_comment": "影响综合收益总额的调整项目-描述"},
                {"col_name": "aeEffectCi", "col_show_name": "影响综合收益总额的差错金额", "col_comment": "影响综合收益总额的差错金额-描述"},
                {"col_name": "tComprIncome", "col_show_name": "综合收益总额", "col_comment": "综合收益总额-描述"},
                {"col_name": "comprIncAttrP", "col_show_name": "归属于母公司所有者(或股东)的综合收益总额",
                 "col_comment": "归属于母公司所有者(或股东)的综合收益总额-描述"},
                {"col_name": "comprIncAttrMS", "col_show_name": "归属于少数股东的综合收益总额", "col_comment": "归属于少数股东的综合收益总额-描述"},
                {"col_name": "othEffectPci", "col_show_name": "影响综合收益总额分配的调整项目", "col_comment": "影响综合收益总额分配的调整项目-描述"},
                {"col_name": "aeEffectPci", "col_show_name": "影响综合收益总额分配的差错金额", "col_comment": "影响综合收益总额分配的差错金额-描述"}
            ]
        }
    define_json = json.dumps(fdmtisinsu2018_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def fdmtisbank_define(table_name):

    fdmtisbank_str = {
            "table_name": "fdmtisbank",
            "table_show_name": "银行业利润表(PIT)",
            "table_comment": "银行业利润表(PIT)-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "证券内部ID", "col_comment": "证券内部ID-描述"},
                {"col_name": "publishDate", "col_show_name": "发布日期", "col_comment": "发布日期-描述"},
                {"col_name": "endDate", "col_show_name": "截止日期", "col_comment": "截止日期-描述"},
                {"col_name": "endDateRep", "col_show_name": "报表截止日期", "col_comment": "报表截止日期-描述"},
                {"col_name": "partyID", "col_show_name": "机构内部ID", "col_comment": "机构内部ID-描述"},
                {"col_name": "ticker", "col_show_name": "股票代码", "col_comment": "股票代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD",
                 "col_show_name": "通联编制的证券市场编码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所等。对应DataAPI.SysCodeGet.codeTypeID=10002。",
                 "col_comment": "通联编制的证券市场编码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所等。对应DataAPI.SysCodeGet.codeTypeID=10002。-描述"},
                {"col_name": "actPubtime", "col_show_name": "实际披露时间", "col_comment": "实际披露时间-描述"},
                {"col_name": "mergedFlag", "col_show_name": "合并类型。1-合并,2-母公司。对应DataAPI.SysCodeGet.codeTypeID=70003。",
                 "col_comment": "合并类型。1-合并,2-母公司。对应DataAPI.SysCodeGet.codeTypeID=70003。-描述"},
                {"col_name": "reportType",
                 "col_show_name": "报告类型。Q1-第一季报，S1-半年报，Q3-第三季报，CQ3-三季报（累计1-9月），A-年报。对应DataAPI.SysCodeGet.codeTypeID=70001。",
                 "col_comment": "报告类型。Q1-第一季报，S1-半年报，Q3-第三季报，CQ3-三季报（累计1-9月），A-年报。对应DataAPI.SysCodeGet.codeTypeID=70001。-描述"},
                {"col_name": "fiscalPeriod", "col_show_name": "会计期间", "col_comment": "会计期间-描述"},
                {"col_name": "accoutingStandards", "col_show_name": "会计准则", "col_comment": "会计准则-描述"},
                {"col_name": "currencyCD",
                 "col_show_name": "货币代码。例如，USD-美元；CAD-加元等。对应DataAPI.SysCodeGet.codeTypeID=10004。",
                 "col_comment": "货币代码。例如，USD-美元；CAD-加元等。对应DataAPI.SysCodeGet.codeTypeID=10004。-描述"},
                {"col_name": "revenue", "col_show_name": "营业收入", "col_comment": "营业收入-描述"},
                {"col_name": "NIntIncome", "col_show_name": "利息净收入", "col_comment": "利息净收入-描述"},
                {"col_name": "intIncome", "col_show_name": "利息收入", "col_comment": "利息收入-描述"},
                {"col_name": "intExp", "col_show_name": "利息支出", "col_comment": "利息支出-描述"},
                {"col_name": "NCommisIncome", "col_show_name": "手续费及佣金净收入", "col_comment": "手续费及佣金净收入-描述"},
                {"col_name": "commisIncome", "col_show_name": "手续费及佣金收入", "col_comment": "手续费及佣金收入-描述"},
                {"col_name": "commisExp", "col_show_name": "手续费及佣金支出", "col_comment": "手续费及佣金支出-描述"},
                {"col_name": "othOperRev", "col_show_name": "其他业务收入", "col_comment": "其他业务收入-描述"},
                {"col_name": "specOR", "col_show_name": "营业收入的特殊项目", "col_comment": "营业收入的特殊项目-描述"},
                {"col_name": "AOR", "col_show_name": "营业收入的调整金额", "col_comment": "营业收入的调整金额-描述"},
                {"col_name": "COGS", "col_show_name": "营业支出", "col_comment": "营业支出-描述"},
                {"col_name": "bizTaxSurchg", "col_show_name": "营业税金及附加", "col_comment": "营业税金及附加-描述"},
                {"col_name": "genlAdminExp", "col_show_name": "业务及管理费", "col_comment": "业务及管理费-描述"},
                {"col_name": "assetsImpairLoss", "col_show_name": "资产减值损失", "col_comment": "资产减值损失-描述"},
                {"col_name": "othOperCosts", "col_show_name": "其他业务成本", "col_comment": "其他业务成本-描述"},
                {"col_name": "specOC", "col_show_name": "营业支出的特殊项目", "col_comment": "营业支出的特殊项目-描述"},
                {"col_name": "AOC", "col_show_name": "营业支出的调整金额", "col_comment": "营业支出的调整金额-描述"},
                {"col_name": "fValueChgGain", "col_show_name": "公允价值变动收益", "col_comment": "公允价值变动收益-描述"},
                {"col_name": "investIncome", "col_show_name": "投资收益", "col_comment": "投资收益-描述"},
                {"col_name": "AJInvestIncome", "col_show_name": "其中:对联营企业和合营企业的投资收益",
                 "col_comment": "其中:对联营企业和合营企业的投资收益-描述"},
                {"col_name": "forexGain", "col_show_name": "汇兑收益", "col_comment": "汇兑收益-描述"},
                {"col_name": "assetsDispGain", "col_show_name": "资产处置收益", "col_comment": "资产处置收益-描述"},
                {"col_name": "othGain", "col_show_name": "其他收益", "col_comment": "其他收益-描述"},
                {"col_name": "othEffectOP", "col_show_name": "影响营业利润的特殊项目", "col_comment": "影响营业利润的特殊项目-描述"},
                {"col_name": "aeEffectOp", "col_show_name": "影响营业利润的调整金额", "col_comment": "影响营业利润的调整金额-描述"},
                {"col_name": "operateProfit", "col_show_name": "营业利润", "col_comment": "营业利润-描述"},
                {"col_name": "NoperateIncome", "col_show_name": "营业外收入", "col_comment": "营业外收入-描述"},
                {"col_name": "NoperateExp", "col_show_name": "营业外支出", "col_comment": "营业外支出-描述"},
                {"col_name": "othEffectTP", "col_show_name": "影响利润总额的特殊项目", "col_comment": "影响利润总额的特殊项目-描述"},
                {"col_name": "AEEffectTP", "col_show_name": "影响利润总额的调整金额", "col_comment": "影响利润总额的调整金额-描述"},
                {"col_name": "TProfit", "col_show_name": "利润总额", "col_comment": "利润总额-描述"},
                {"col_name": "incomeTax", "col_show_name": "所得税费用", "col_comment": "所得税费用-描述"},
                {"col_name": "othEffectNP", "col_show_name": "影响净利润的特殊项目", "col_comment": "影响净利润的特殊项目-描述"},
                {"col_name": "AEEffectNP", "col_show_name": "影响净利润的调整金额", "col_comment": "影响净利润的调整金额-描述"},
                {"col_name": "NIncome", "col_show_name": "净利润", "col_comment": "净利润-描述"},
                {"col_name": "goingConcernNI", "col_show_name": "持续经营净利润", "col_comment": "持续经营净利润-描述"},
                {"col_name": "quitConcernNI", "col_show_name": "终止经营净利润", "col_comment": "终止经营净利润-描述"},
                {"col_name": "NIncomeAttrP", "col_show_name": "归属于母公司所有者的净利润", "col_comment": "归属于母公司所有者的净利润-描述"},
                {"col_name": "minorityGain", "col_show_name": "少数股东损益", "col_comment": "少数股东损益-描述"},
                {"col_name": "othEffectNPP", "col_show_name": "影响净利润分配的特殊项目", "col_comment": "影响净利润分配的特殊项目-描述"},
                {"col_name": "AEEffectNPP", "col_show_name": "影响净利润分配的调整金额", "col_comment": "影响净利润分配的调整金额-描述"},
                {"col_name": "basicEPS", "col_show_name": "基本每股收益", "col_comment": "基本每股收益-描述"},
                {"col_name": "dilutedEPS", "col_show_name": "稀释每股收益", "col_comment": "稀释每股收益-描述"},
                {"col_name": "othComprIncome", "col_show_name": "其他综合收益", "col_comment": "其他综合收益-描述"},
                {"col_name": "othEffectCI", "col_show_name": "影响综合收益总额的特殊项目", "col_comment": "影响综合收益总额的特殊项目-描述"},
                {"col_name": "AEEffectCI", "col_show_name": "影响综合收益总额的调整金额", "col_comment": "影响综合收益总额的调整金额-描述"},
                {"col_name": "TComprIncome", "col_show_name": "综合收益总额", "col_comment": "综合收益总额-描述"},
                {"col_name": "comprIncAttrP", "col_show_name": "归属于母公司所有者的综合收益总额",
                 "col_comment": "归属于母公司所有者的综合收益总额-描述"},
                {"col_name": "comprIncAttrMS", "col_show_name": "归属于少数股东的综合收益总额", "col_comment": "归属于少数股东的综合收益总额-描述"},
                {"col_name": "othEffectPCI", "col_show_name": "影响综合收益总额分配的特殊项目", "col_comment": "影响综合收益总额分配的特殊项目-描述"},
                {"col_name": "AEEffectPCI", "col_show_name": "影响综合收益总额分配的调整金额", "col_comment": "影响综合收益总额分配的调整金额-描述"},
                {"col_name": "updateTime", "col_show_name": "更新时间", "col_comment": "更新时间-描述"}
            ]
        }
    define_json = json.dumps(fdmtisbank_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def fdmtisindu_define(table_name):

    fdmtisindu_str = {
            "table_name": "fdmtisindu",
            "table_show_name": "一般工商业利润表(PIT)",
            "table_comment": "一般工商业利润表(PIT)-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "证券内部ID", "col_comment": "证券内部ID-描述"},
                {"col_name": "publishDate", "col_show_name": "发布日期", "col_comment": "发布日期-描述"},
                {"col_name": "endDate", "col_show_name": "截止日期", "col_comment": "截止日期-描述"},
                {"col_name": "endDateRep", "col_show_name": "报表截止日期", "col_comment": "报表截止日期-描述"},
                {"col_name": "partyID", "col_show_name": "机构内部ID", "col_comment": "机构内部ID-描述"},
                {"col_name": "ticker", "col_show_name": "股票代码", "col_comment": "股票代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD",
                 "col_show_name": "通联编制的证券市场编码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所等。对应DataAPI.SysCodeGet.codeTypeID=10002。",
                 "col_comment": "通联编制的证券市场编码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所等。对应DataAPI.SysCodeGet.codeTypeID=10002。-描述"},
                {"col_name": "actPubtime", "col_show_name": "实际披露时间", "col_comment": "实际披露时间-描述"},
                {"col_name": "mergedFlag", "col_show_name": "合并类型。1-合并,2-母公司。对应DataAPI.SysCodeGet.codeTypeID=70003。",
                 "col_comment": "合并类型。1-合并,2-母公司。对应DataAPI.SysCodeGet.codeTypeID=70003。-描述"},
                {"col_name": "reportType",
                 "col_show_name": "报告类型。Q1-第一季报，S1-半年报，Q3-第三季报，CQ3-三季报（累计1-9月），A-年报。对应DataAPI.SysCodeGet.codeTypeID=70001。",
                 "col_comment": "报告类型。Q1-第一季报，S1-半年报，Q3-第三季报，CQ3-三季报（累计1-9月），A-年报。对应DataAPI.SysCodeGet.codeTypeID=70001。-描述"},
                {"col_name": "fiscalPeriod", "col_show_name": "会计期间", "col_comment": "会计期间-描述"},
                {"col_name": "accoutingStandards", "col_show_name": "会计准则", "col_comment": "会计准则-描述"},
                {"col_name": "currencyCD",
                 "col_show_name": "货币代码。例如，USD-美元；CAD-加元等。对应DataAPI.SysCodeGet.codeTypeID=10004。",
                 "col_comment": "货币代码。例如，USD-美元；CAD-加元等。对应DataAPI.SysCodeGet.codeTypeID=10004。-描述"},
                {"col_name": "tRevenue", "col_show_name": "营业总收入", "col_comment": "营业总收入-描述"},
                {"col_name": "revenue", "col_show_name": "营业收入", "col_comment": "营业收入-描述"},
                {"col_name": "intIncome", "col_show_name": "利息收入", "col_comment": "利息收入-描述"},
                {"col_name": "intExp", "col_show_name": "利息支出", "col_comment": "利息支出-描述"},
                {"col_name": "premEarned", "col_show_name": "已赚保费", "col_comment": "已赚保费-描述"},
                {"col_name": "commisIncome", "col_show_name": "手续费及佣金收入", "col_comment": "手续费及佣金收入-描述"},
                {"col_name": "commisExp", "col_show_name": "手续费及佣金支出", "col_comment": "手续费及佣金支出-描述"},
                {"col_name": "specTOR", "col_show_name": "营业总收入的特殊项目", "col_comment": "营业总收入的特殊项目-描述"},
                {"col_name": "ATOR", "col_show_name": "营业总收入的调整金额", "col_comment": "营业总收入的调整金额-描述"},
                {"col_name": "TCogs", "col_show_name": "营业总成本", "col_comment": "营业总成本-描述"},
                {"col_name": "COGS", "col_show_name": "营业成本", "col_comment": "营业成本-描述"},
                {"col_name": "premRefund", "col_show_name": "退保金", "col_comment": "退保金-描述"},
                {"col_name": "NCompensPayout", "col_show_name": "赔付支出净额", "col_comment": "赔付支出净额-描述"},
                {"col_name": "reserInsurContr", "col_show_name": "提取保险合同准备金净额", "col_comment": "提取保险合同准备金净额-描述"},
                {"col_name": "policyDivPayt", "col_show_name": "保单红利支出", "col_comment": "保单红利支出-描述"},
                {"col_name": "reinsurExp", "col_show_name": "分保费用", "col_comment": "分保费用-描述"},
                {"col_name": "bizTaxSurchg", "col_show_name": "营业税金及附加", "col_comment": "营业税金及附加-描述"},
                {"col_name": "sellExp", "col_show_name": "销售费用", "col_comment": "销售费用-描述"},
                {"col_name": "adminExp", "col_show_name": "管理费用", "col_comment": "管理费用-描述"},
                {"col_name": "finanExp", "col_show_name": "财务费用", "col_comment": "财务费用-描述"},
                {"col_name": "assetsImpairLoss", "col_show_name": "资产减值损失", "col_comment": "资产减值损失-描述"},
                {"col_name": "specTOC", "col_show_name": "营业总成本的特殊项目", "col_comment": "营业总成本的特殊项目-描述"},
                {"col_name": "ATOC", "col_show_name": "营业总成本的调整金额", "col_comment": "营业总成本的调整金额-描述"},
                {"col_name": "fValueChgGain", "col_show_name": "公允价值变动收益", "col_comment": "公允价值变动收益-描述"},
                {"col_name": "investIncome", "col_show_name": "投资收益", "col_comment": "投资收益-描述"},
                {"col_name": "AJInvestIncome", "col_show_name": "其中:对联营企业和合营企业的投资收益",
                 "col_comment": "其中:对联营企业和合营企业的投资收益-描述"},
                {"col_name": "forexGain", "col_show_name": "汇兑收益", "col_comment": "汇兑收益-描述"},
                {"col_name": "assetsDispGain", "col_show_name": "资产处置收益", "col_comment": "资产处置收益-描述"},
                {"col_name": "othGain", "col_show_name": "其他收益", "col_comment": "其他收益-描述"},
                {"col_name": "othEffectOP", "col_show_name": "影响营业利润的特殊项目", "col_comment": "影响营业利润的特殊项目-描述"},
                {"col_name": "aeEffectOp", "col_show_name": "影响营业利润的调整金额", "col_comment": "影响营业利润的调整金额-描述"},
                {"col_name": "operateProfit", "col_show_name": "营业利润", "col_comment": "营业利润-描述"},
                {"col_name": "NoperateIncome", "col_show_name": "营业外收入", "col_comment": "营业外收入-描述"},
                {"col_name": "NoperateExp", "col_show_name": "营业外支出", "col_comment": "营业外支出-描述"},
                {"col_name": "NCADisploss", "col_show_name": "非流动资产处置损失", "col_comment": "非流动资产处置损失-描述"},
                {"col_name": "othEffectTP", "col_show_name": "影响利润总额的特殊项目", "col_comment": "影响利润总额的特殊项目-描述"},
                {"col_name": "AEEffectTP", "col_show_name": "影响利润总额的调整金额", "col_comment": "影响利润总额的调整金额-描述"},
                {"col_name": "TProfit", "col_show_name": "利润总额", "col_comment": "利润总额-描述"},
                {"col_name": "incomeTax", "col_show_name": "所得税费用", "col_comment": "所得税费用-描述"},
                {"col_name": "othEffectNP", "col_show_name": "影响净利润的特殊项目", "col_comment": "影响净利润的特殊项目-描述"},
                {"col_name": "AEEffectNP", "col_show_name": "影响净利润的调整金额", "col_comment": "影响净利润的调整金额-描述"},
                {"col_name": "NIncome", "col_show_name": "净利润", "col_comment": "净利润-描述"},
                {"col_name": "goingConcernNI", "col_show_name": "持续经营净利润", "col_comment": "持续经营净利润-描述"},
                {"col_name": "quitConcernNI", "col_show_name": "终止经营净利润", "col_comment": "终止经营净利润-描述"},
                {"col_name": "NIncomeAttrP", "col_show_name": "归属于母公司所有者的净利润", "col_comment": "归属于母公司所有者的净利润-描述"},
                {"col_name": "NIncomeBMA", "col_show_name": "其中:被合并方在合并前实现的净利润", "col_comment": "其中:被合并方在合并前实现的净利润-描述"},
                {"col_name": "minorityGain", "col_show_name": "少数股东损益", "col_comment": "少数股东损益-描述"},
                {"col_name": "othEffectNPP", "col_show_name": "影响净利润分配的特殊项目", "col_comment": "影响净利润分配的特殊项目-描述"},
                {"col_name": "AEEffectNPP", "col_show_name": "影响净利润分配的调整金额", "col_comment": "影响净利润分配的调整金额-描述"},
                {"col_name": "basicEPS", "col_show_name": "基本每股收益", "col_comment": "基本每股收益-描述"},
                {"col_name": "dilutedEPS", "col_show_name": "稀释每股收益", "col_comment": "稀释每股收益-描述"},
                {"col_name": "othComprIncome", "col_show_name": "其他综合收益", "col_comment": "其他综合收益-描述"}
            ]
        }
    define_json = json.dumps(fdmtisindu_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def fdmtissecu_define(table_name):

    fdmtissecu_str = {
            "table_name": "fdmtissecu",
            "table_show_name": "证券业利润表(PIT)",
            "table_comment": "证券业利润表(PIT)-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "证券内部ID", "col_comment": "证券内部ID-描述"},
                {"col_name": "publishDate", "col_show_name": "发布日期", "col_comment": "发布日期-描述"},
                {"col_name": "endDate", "col_show_name": "截止日期", "col_comment": "截止日期-描述"},
                {"col_name": "endDateRep", "col_show_name": "报表截止日期", "col_comment": "报表截止日期-描述"},
                {"col_name": "partyID", "col_show_name": "机构内部ID", "col_comment": "机构内部ID-描述"},
                {"col_name": "ticker", "col_show_name": "股票代码", "col_comment": "股票代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD",
                 "col_show_name": "通联编制的证券市场编码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所等。对应DataAPI.SysCodeGet.codeTypeID=10002。",
                 "col_comment": "通联编制的证券市场编码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所等。对应DataAPI.SysCodeGet.codeTypeID=10002。-描述"},
                {"col_name": "actPubtime", "col_show_name": "实际披露时间", "col_comment": "实际披露时间-描述"},
                {"col_name": "mergedFlag", "col_show_name": "合并类型。1-合并,2-母公司。对应DataAPI.SysCodeGet.codeTypeID=70003。",
                 "col_comment": "合并类型。1-合并,2-母公司。对应DataAPI.SysCodeGet.codeTypeID=70003。-描述"},
                {"col_name": "reportType",
                 "col_show_name": "报告类型。Q1-第一季报，S1-半年报，Q3-第三季报，CQ3-三季报（累计1-9月），A-年报。对应DataAPI.SysCodeGet.codeTypeID=70001。",
                 "col_comment": "报告类型。Q1-第一季报，S1-半年报，Q3-第三季报，CQ3-三季报（累计1-9月），A-年报。对应DataAPI.SysCodeGet.codeTypeID=70001。-描述"},
                {"col_name": "fiscalPeriod", "col_show_name": "会计期间", "col_comment": "会计期间-描述"},
                {"col_name": "accoutingStandards", "col_show_name": "会计准则", "col_comment": "会计准则-描述"},
                {"col_name": "currencyCD",
                 "col_show_name": "货币代码。例如，USD-美元；CAD-加元等。对应DataAPI.SysCodeGet.codeTypeID=10004。",
                 "col_comment": "货币代码。例如，USD-美元；CAD-加元等。对应DataAPI.SysCodeGet.codeTypeID=10004。-描述"},
                {"col_name": "revenue", "col_show_name": "营业收入", "col_comment": "营业收入-描述"},
                {"col_name": "NIntIncome", "col_show_name": "利息净收入", "col_comment": "利息净收入-描述"},
                {"col_name": "NCommisIncome", "col_show_name": "手续费及佣金净收入", "col_comment": "手续费及佣金净收入-描述"},
                {"col_name": "NSecTaIncome", "col_show_name": "代理买卖证券业务净收入", "col_comment": "代理买卖证券业务净收入-描述"},
                {"col_name": "NUndwrtSecIncome", "col_show_name": "证券承销业务净收入", "col_comment": "证券承销业务净收入-描述"},
                {"col_name": "NTrustIncome", "col_show_name": "委托客户资产管理业务净收入", "col_comment": "委托客户资产管理业务净收入-描述"},
                {"col_name": "othOperRev", "col_show_name": "其他业务收入", "col_comment": "其他业务收入-描述"},
                {"col_name": "specOR", "col_show_name": "营业收入的特殊项目", "col_comment": "营业收入的特殊项目-描述"},
                {"col_name": "AOR", "col_show_name": "营业收入的调整金额", "col_comment": "营业收入的调整金额-描述"},
                {"col_name": "COGS", "col_show_name": "营业支出", "col_comment": "营业支出-描述"},
                {"col_name": "bizTaxSurchg", "col_show_name": "营业税金及附加", "col_comment": "营业税金及附加-描述"},
                {"col_name": "genlAdminExp", "col_show_name": "业务及管理费", "col_comment": "业务及管理费-描述"},
                {"col_name": "assetsImpairLoss", "col_show_name": "资产减值损失", "col_comment": "资产减值损失-描述"},
                {"col_name": "othOperCosts", "col_show_name": "其他业务成本", "col_comment": "其他业务成本-描述"},
                {"col_name": "specOC", "col_show_name": "营业支出的特殊项目", "col_comment": "营业支出的特殊项目-描述"},
                {"col_name": "AOC", "col_show_name": "营业支出的调整金额", "col_comment": "营业支出的调整金额-描述"},
                {"col_name": "fValueChgGain", "col_show_name": "公允价值变动收益", "col_comment": "公允价值变动收益-描述"},
                {"col_name": "investIncome", "col_show_name": "投资收益", "col_comment": "投资收益-描述"},
                {"col_name": "AJInvestIncome", "col_show_name": "其中:对联营企业和合营企业的投资收益",
                 "col_comment": "其中:对联营企业和合营企业的投资收益-描述"},
                {"col_name": "forexGain", "col_show_name": "汇兑收益", "col_comment": "汇兑收益-描述"},
                {"col_name": "assetsDispGain", "col_show_name": "资产处置收益", "col_comment": "资产处置收益-描述"},
                {"col_name": "othGain", "col_show_name": "其他收益", "col_comment": "其他收益-描述"},
                {"col_name": "othEffectOP", "col_show_name": "影响营业利润的特殊项目", "col_comment": "影响营业利润的特殊项目-描述"},
                {"col_name": "aeEffectOp", "col_show_name": "影响营业利润的调整金额", "col_comment": "影响营业利润的调整金额-描述"},
                {"col_name": "operateProfit", "col_show_name": "营业利润", "col_comment": "营业利润-描述"},
                {"col_name": "NoperateIncome", "col_show_name": "营业外收入", "col_comment": "营业外收入-描述"},
                {"col_name": "NoperateExp", "col_show_name": "营业外支出", "col_comment": "营业外支出-描述"},
                {"col_name": "othEffectTP", "col_show_name": "影响利润总额的特殊项目", "col_comment": "影响利润总额的特殊项目-描述"},
                {"col_name": "AEEffectTP", "col_show_name": "影响利润总额的调整金额", "col_comment": "影响利润总额的调整金额-描述"},
                {"col_name": "TProfit", "col_show_name": "利润总额", "col_comment": "利润总额-描述"},
                {"col_name": "incomeTax", "col_show_name": "所得税费用", "col_comment": "所得税费用-描述"},
                {"col_name": "othEffectNP", "col_show_name": "影响净利润的特殊项目", "col_comment": "影响净利润的特殊项目-描述"},
                {"col_name": "AEEffectNP", "col_show_name": "影响净利润的调整金额", "col_comment": "影响净利润的调整金额-描述"},
                {"col_name": "NIncome", "col_show_name": "净利润", "col_comment": "净利润-描述"},
                {"col_name": "goingConcernNI", "col_show_name": "持续经营净利润", "col_comment": "持续经营净利润-描述"},
                {"col_name": "quitConcernNI", "col_show_name": "终止经营净利润", "col_comment": "终止经营净利润-描述"},
                {"col_name": "NIncomeAttrP", "col_show_name": "归属于母公司所有者的净利润", "col_comment": "归属于母公司所有者的净利润-描述"},
                {"col_name": "minorityGain", "col_show_name": "少数股东损益", "col_comment": "少数股东损益-描述"},
                {"col_name": "othEffectNPP", "col_show_name": "影响净利润分配的特殊项目", "col_comment": "影响净利润分配的特殊项目-描述"},
                {"col_name": "AEEffectNPP", "col_show_name": "影响净利润分配的调整金额", "col_comment": "影响净利润分配的调整金额-描述"},
                {"col_name": "basicEPS", "col_show_name": "基本每股收益", "col_comment": "基本每股收益-描述"},
                {"col_name": "dilutedEPS", "col_show_name": "稀释每股收益", "col_comment": "稀释每股收益-描述"},
                {"col_name": "othComprIncome", "col_show_name": "其他综合收益", "col_comment": "其他综合收益-描述"},
                {"col_name": "othEffectCI", "col_show_name": "影响综合收益总额的特殊项目", "col_comment": "影响综合收益总额的特殊项目-描述"},
                {"col_name": "AEEffectCI", "col_show_name": "影响综合收益总额的调整金额", "col_comment": "影响综合收益总额的调整金额-描述"},
                {"col_name": "TComprIncome", "col_show_name": "综合收益总额", "col_comment": "综合收益总额-描述"},
                {"col_name": "comprIncAttrP", "col_show_name": "归属于母公司所有者的综合收益总额",
                 "col_comment": "归属于母公司所有者的综合收益总额-描述"},
                {"col_name": "comprIncAttrMS", "col_show_name": "归属于少数股东的综合收益总额", "col_comment": "归属于少数股东的综合收益总额-描述"},
                {"col_name": "othEffectPCI", "col_show_name": "影响综合收益总额分配的特殊项目", "col_comment": "影响综合收益总额分配的特殊项目-描述"},
                {"col_name": "AEEffectPCI", "col_show_name": "影响综合收益总额分配的调整金额", "col_comment": "影响综合收益总额分配的调整金额-描述"},
                {"col_name": "updateTime", "col_show_name": "更新时间", "col_comment": "更新时间-描述"}
            ]
        }
    define_json = json.dumps(fdmtissecu_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def fdmtisinsu_define(table_name):

    fdmtisinsu_str = {
            "table_name": "fdmtisinsu",
            "table_show_name": "保险业利润表(PIT)",
            "table_comment": "保险业利润表(PIT)-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "证券内部ID", "col_comment": "证券内部ID-描述"},
                {"col_name": "publishDate", "col_show_name": "发布日期", "col_comment": "发布日期-描述"},
                {"col_name": "endDate", "col_show_name": "截止日期", "col_comment": "截止日期-描述"},
                {"col_name": "endDateRep", "col_show_name": "报表截止日期", "col_comment": "报表截止日期-描述"},
                {"col_name": "partyID", "col_show_name": "机构内部ID", "col_comment": "机构内部ID-描述"},
                {"col_name": "ticker", "col_show_name": "股票代码", "col_comment": "股票代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD",
                 "col_show_name": "通联编制的证券市场编码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所等。对应DataAPI.SysCodeGet.codeTypeID=10002。",
                 "col_comment": "通联编制的证券市场编码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所等。对应DataAPI.SysCodeGet.codeTypeID=10002。-描述"},
                {"col_name": "actPubtime", "col_show_name": "实际披露时间", "col_comment": "实际披露时间-描述"},
                {"col_name": "mergedFlag", "col_show_name": "合并类型。1-合并,2-母公司。对应DataAPI.SysCodeGet.codeTypeID=70003。",
                 "col_comment": "合并类型。1-合并,2-母公司。对应DataAPI.SysCodeGet.codeTypeID=70003。-描述"},
                {"col_name": "reportType",
                 "col_show_name": "报告类型。Q1-第一季报，S1-半年报，Q3-第三季报，CQ3-三季报（累计1-9月），A-年报。对应DataAPI.SysCodeGet.codeTypeID=70001。",
                 "col_comment": "报告类型。Q1-第一季报，S1-半年报，Q3-第三季报，CQ3-三季报（累计1-9月），A-年报。对应DataAPI.SysCodeGet.codeTypeID=70001。-描述"},
                {"col_name": "fiscalPeriod", "col_show_name": "会计期间", "col_comment": "会计期间-描述"},
                {"col_name": "accoutingStandards", "col_show_name": "会计准则", "col_comment": "会计准则-描述"},
                {"col_name": "currencyCD",
                 "col_show_name": "货币代码。例如，USD-美元；CAD-加元等。对应DataAPI.SysCodeGet.codeTypeID=10004。",
                 "col_comment": "货币代码。例如，USD-美元；CAD-加元等。对应DataAPI.SysCodeGet.codeTypeID=10004。-描述"},
                {"col_name": "revenue", "col_show_name": "营业收入", "col_comment": "营业收入-描述"},
                {"col_name": "premEarned", "col_show_name": "已赚保费", "col_comment": "已赚保费-描述"},
                {"col_name": "grossPremWrit", "col_show_name": "保险业务收入", "col_comment": "保险业务收入-描述"},
                {"col_name": "reinsIncome", "col_show_name": "其中:分保费收入", "col_comment": "其中:分保费收入-描述"},
                {"col_name": "reinsur", "col_show_name": "减:分出保费", "col_comment": "减:分出保费-描述"},
                {"col_name": "unePremReser", "col_show_name": "提取未到期责任准备金", "col_comment": "提取未到期责任准备金-描述"},
                {"col_name": "commisExp", "col_show_name": "手续费及佣金支出", "col_comment": "手续费及佣金支出-描述"},
                {"col_name": "othOperRev", "col_show_name": "其他业务收入", "col_comment": "其他业务收入-描述"},
                {"col_name": "specOR", "col_show_name": "营业收入的特殊项目", "col_comment": "营业收入的特殊项目-描述"},
                {"col_name": "AOR", "col_show_name": "营业收入的调整金额", "col_comment": "营业收入的调整金额-描述"},
                {"col_name": "COGS", "col_show_name": "营业支出", "col_comment": "营业支出-描述"},
                {"col_name": "premRefund", "col_show_name": "退保金", "col_comment": "退保金-描述"},
                {"col_name": "compensPayout", "col_show_name": "赔付支出", "col_comment": "赔付支出-描述"},
                {"col_name": "compensPayoutRefu", "col_show_name": "减:摊回赔付支出", "col_comment": "减:摊回赔付支出-描述"},
                {"col_name": "reserInsurLiab", "col_show_name": "提取保险责任准备金", "col_comment": "提取保险责任准备金-描述"},
                {"col_name": "insurLiabReserRefu", "col_show_name": "减:摊回保险责任准备金", "col_comment": "减:摊回保险责任准备金-描述"},
                {"col_name": "policyDivPayt", "col_show_name": "保单红利支出", "col_comment": "保单红利支出-描述"},
                {"col_name": "reinsurExp", "col_show_name": "分保费用", "col_comment": "分保费用-描述"},
                {"col_name": "bizTaxSurchg", "col_show_name": "营业税金及附加", "col_comment": "营业税金及附加-描述"},
                {"col_name": "genlAdminExp", "col_show_name": "业务及管理费", "col_comment": "业务及管理费-描述"},
                {"col_name": "reinsCostRefund", "col_show_name": "减:摊回分保费用", "col_comment": "减:摊回分保费用-描述"},
                {"col_name": "assetsImpairLoss", "col_show_name": "资产减值损失", "col_comment": "资产减值损失-描述"},
                {"col_name": "othOperCosts", "col_show_name": "其他业务成本", "col_comment": "其他业务成本-描述"},
                {"col_name": "specOC", "col_show_name": "营业支出的特殊项目", "col_comment": "营业支出的特殊项目-描述"},
                {"col_name": "AOC", "col_show_name": "营业支出的调整金额", "col_comment": "营业支出的调整金额-描述"},
                {"col_name": "fValueChgGain", "col_show_name": "公允价值变动收益", "col_comment": "公允价值变动收益-描述"},
                {"col_name": "investIncome", "col_show_name": "投资收益", "col_comment": "投资收益-描述"},
                {"col_name": "AJInvestIncome", "col_show_name": "其中:对联营企业和合营企业的投资收益",
                 "col_comment": "其中:对联营企业和合营企业的投资收益-描述"},
                {"col_name": "forexGain", "col_show_name": "汇兑收益", "col_comment": "汇兑收益-描述"},
                {"col_name": "assetsDispGain", "col_show_name": "资产处置收益", "col_comment": "资产处置收益-描述"},
                {"col_name": "othGain", "col_show_name": "其他收益", "col_comment": "其他收益-描述"},
                {"col_name": "othEffectOP", "col_show_name": "影响营业利润的特殊项目", "col_comment": "影响营业利润的特殊项目-描述"},
                {"col_name": "aeEffectOp", "col_show_name": "影响营业利润的调整金额", "col_comment": "影响营业利润的调整金额-描述"},
                {"col_name": "operateProfit", "col_show_name": "营业利润", "col_comment": "营业利润-描述"},
                {"col_name": "NoperateIncome", "col_show_name": "营业外收入", "col_comment": "营业外收入-描述"},
                {"col_name": "NoperateExp", "col_show_name": "营业外支出", "col_comment": "营业外支出-描述"},
                {"col_name": "othEffectTP", "col_show_name": "影响利润总额的特殊项目", "col_comment": "影响利润总额的特殊项目-描述"},
                {"col_name": "AEEffectTP", "col_show_name": "影响利润总额的调整金额", "col_comment": "影响利润总额的调整金额-描述"},
                {"col_name": "TProfit", "col_show_name": "利润总额", "col_comment": "利润总额-描述"},
                {"col_name": "incomeTax", "col_show_name": "所得税费用", "col_comment": "所得税费用-描述"},
                {"col_name": "othEffectNP", "col_show_name": "影响净利润的特殊项目", "col_comment": "影响净利润的特殊项目-描述"},
                {"col_name": "AEEffectNP", "col_show_name": "影响净利润的调整金额", "col_comment": "影响净利润的调整金额-描述"},
                {"col_name": "NIncome", "col_show_name": "净利润", "col_comment": "净利润-描述"},
                {"col_name": "goingConcernNI", "col_show_name": "持续经营净利润", "col_comment": "持续经营净利润-描述"},
                {"col_name": "quitConcernNI", "col_show_name": "终止经营净利润", "col_comment": "终止经营净利润-描述"},
                {"col_name": "NIncomeAttrP", "col_show_name": "归属于母公司所有者的净利润", "col_comment": "归属于母公司所有者的净利润-描述"},
                {"col_name": "minorityGain", "col_show_name": "少数股东损益", "col_comment": "少数股东损益-描述"},
                {"col_name": "othEffectNPP", "col_show_name": "影响净利润分配的特殊项目", "col_comment": "影响净利润分配的特殊项目-描述"},
                {"col_name": "AEEffectNPP", "col_show_name": "影响净利润分配的调整金额", "col_comment": "影响净利润分配的调整金额-描述"},
                {"col_name": "basicEPS", "col_show_name": "基本每股收益", "col_comment": "基本每股收益-描述"},
                {"col_name": "dilutedEPS", "col_show_name": "稀释每股收益", "col_comment": "稀释每股收益-描述"},
                {"col_name": "othComprIncome", "col_show_name": "其他综合收益", "col_comment": "其他综合收益-描述"},
                {"col_name": "othEffectCI", "col_show_name": "影响综合收益总额的特殊项目", "col_comment": "影响综合收益总额的特殊项目-描述"},
                {"col_name": "AEEffectCI", "col_show_name": "影响综合收益总额的调整金额", "col_comment": "影响综合收益总额的调整金额-描述"},
                {"col_name": "TComprIncome", "col_show_name": "综合收益总额", "col_comment": "综合收益总额-描述"},
                {"col_name": "comprIncAttrP", "col_show_name": "归属于母公司所有者的综合收益总额",
                 "col_comment": "归属于母公司所有者的综合收益总额-描述"},
                {"col_name": "comprIncAttrMS", "col_show_name": "归属于少数股东的综合收益总额", "col_comment": "归属于少数股东的综合收益总额-描述"},
                {"col_name": "othEffectPCI", "col_show_name": "影响综合收益总额分配的特殊项目", "col_comment": "影响综合收益总额分配的特殊项目-描述"},
                {"col_name": "AEEffectPCI", "col_show_name": "影响综合收益总额分配的调整金额", "col_comment": "影响综合收益总额分配的调整金额-描述"},
                {"col_name": "updateTime", "col_show_name": "更新时间", "col_comment": "更新时间-描述"}
            ]
        }
    define_json = json.dumps(fdmtisinsu_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def equinstssta_define(table_name):

    equinstssta_str = {
            "table_name": "equinstssta",
            "table_show_name": "上市公司特殊状态",
            "table_comment": "上市公司特殊状态-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "证券内部编码", "col_comment": "证券内部编码-描述"},
                {"col_name": "ticker", "col_show_name": "股票代码", "col_comment": "股票代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD", "col_show_name": "交易市场", "col_comment": "交易市场-描述"},
                {"col_name": "partyState", "col_show_name": "公司状态", "col_comment": "公司状态-描述"},
                {"col_name": "effDate", "col_show_name": "生效日期", "col_comment": "生效日期-描述"},
                {"col_name": "reason", "col_show_name": "原因", "col_comment": "原因-描述"},
                {"col_name": "updateTime", "col_show_name": "更新时间", "col_comment": "更新时间-描述"}
            ]
        }
    define_json = json.dumps(equinstssta_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def mktblockd_define(table_name):

    mktblockd_str = {
            "table_name": "mktblockd",
            "table_show_name": "沪深大宗交易",
            "table_comment": "沪深大宗交易-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "tradeDate", "col_show_name": "交易日期", "col_comment": "交易日期-描述"},
                {"col_name": "secID", "col_show_name": "通联编制的证券编码， 可通过DataAPI.SecIDGet获取。",
                 "col_comment": "通联编制的证券编码， 可通过DataAPI.SecIDGet获取。-描述"},
                {"col_name": "ticker", "col_show_name": "通用交易代码", "col_comment": "通用交易代码-描述"},
                {"col_name": "assetClass", "col_show_name": "通联编制的证券类型编码", "col_comment": "通联编制的证券类型编码-描述"},
                {"col_name": "exchangeCD", "col_show_name": "通联编制的证券市场编码", "col_comment": "通联编制的证券市场编码-描述"},
                {"col_name": "secFullName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "currencyCD", "col_show_name": "货币种类编码", "col_comment": "货币种类编码-描述"},
                {"col_name": "tradePrice", "col_show_name": "成交价(元)", "col_comment": "成交价(元)-描述"},
                {"col_name": "tradeVal", "col_show_name": "成交金额(万元)", "col_comment": "成交金额(万元)-描述"},
                {"col_name": "tradeVol", "col_show_name": "成交量， 股票-万股；基金-万份；债券-万手",
                 "col_comment": "成交量， 股票-万股；基金-万份；债券-万手-描述"},
                {"col_name": "buyerBD", "col_show_name": "买方营业部名称", "col_comment": "买方营业部名称-描述"},
                {"col_name": "sellerBD", "col_show_name": "卖方营业部名称", "col_comment": "卖方营业部名称-描述"}
            ]
        }
    define_json = json.dumps(mktblockd_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def mktequd_define(table_name):

    mktequd_str = {
            "table_name": "mktequd",
            "table_show_name": "沪深股票日行情",
            "table_comment": "沪深股票日行情-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "通联编制的证券编码，可使用getSecID获取",
                 "col_comment": "通联编制的证券编码，可使用getSecID获取-描述"},
                {"col_name": "ticker", "col_show_name": "通用交易代码", "col_comment": "通用交易代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD", "col_show_name": "通联编制的交易市场编码", "col_comment": "通联编制的交易市场编码-描述"},
                {"col_name": "tradeDate", "col_show_name": "交易日期", "col_comment": "交易日期-描述"},
                {"col_name": "preClosePrice", "col_show_name": "昨收盘(前复权)", "col_comment": "昨收盘(前复权)-描述"},
                {"col_name": "actPreClosePrice", "col_show_name": "实际昨收盘价(未复权)", "col_comment": "实际昨收盘价(未复权)-描述"},
                {"col_name": "openPrice", "col_show_name": "开盘价", "col_comment": "开盘价-描述"},
                {"col_name": "highestPrice", "col_show_name": "最高价", "col_comment": "最高价-描述"},
                {"col_name": "lowestPrice", "col_show_name": "最低价", "col_comment": "最低价-描述"},
                {"col_name": "closePrice", "col_show_name": "收盘价", "col_comment": "收盘价-描述"},
                {"col_name": "turnoverVol", "col_show_name": "成交量", "col_comment": "成交量-描述"},
                {"col_name": "turnoverValue", "col_show_name": "成交金额，A股单位为元，B股单位为美元或港币",
                 "col_comment": "成交金额，A股单位为元，B股单位为美元或港币-描述"},
                {"col_name": "dealAmount", "col_show_name": "成交笔数", "col_comment": "成交笔数-描述"},
                {"col_name": "turnoverRate", "col_show_name": "日换手率，成交量/无限售流通股数", "col_comment": "日换手率，成交量/无限售流通股数-描述"},
                {"col_name": "accumAdjFactor",
                 "col_show_name": "累积前复权因子，前复权价=未复权价*累积前复权因子。前复权是对历史行情进行调整，除权除息当日的行情无需调整。最近一次除权除息日至最新交易日期间的价格也无需调整，该期间前复权因子等于1。",
                 "col_comment": "累积前复权因子，前复权价=未复权价*累积前复权因子。前复权是对历史行情进行调整，除权除息当日的行情无需调整。最近一次除权除息日至最新交易日期间的价格也无需调整，该期间前复权因子等于1。-描述"},
                {"col_name": "negMarketValue", "col_show_name": "流通市值，收盘价*无限售流通股数",
                 "col_comment": "流通市值，收盘价*无限售流通股数-描述"},
                {"col_name": "marketValue", "col_show_name": "总市值，收盘价*总股本数", "col_comment": "总市值，收盘价*总股本数-描述"},
                {"col_name": "chgPct", "col_show_name": "涨跌幅，收盘价/昨收盘价-1", "col_comment": "涨跌幅，收盘价/昨收盘价-1-描述"},
                {"col_name": "PE", "col_show_name": "滚动市盈率，即市盈率TTM，总市值/归属于母公司所有者的净利润TTM",
                 "col_comment": "滚动市盈率，即市盈率TTM，总市值/归属于母公司所有者的净利润TTM-描述"},
                {"col_name": "PE1", "col_show_name": "动态市盈率，总市值/归属于母公司所有者的净利润（最新一期财报年化）",
                 "col_comment": "动态市盈率，总市值/归属于母公司所有者的净利润（最新一期财报年化）-描述"},
                {"col_name": "PB", "col_show_name": "市净率，总市值/归属于母公司所有者权益合计", "col_comment": "市净率，总市值/归属于母公司所有者权益合计-描述"},
                {"col_name": "isOpen", "col_show_name": "股票今日是否开盘标记：0-未开盘，1-交易日",
                 "col_comment": "股票今日是否开盘标记：0-未开盘，1-交易日-描述"},
                {"col_name": "vwap", "col_show_name": "VWAP，成交金额/成交量", "col_comment": "VWAP，成交金额/成交量-描述"}
            ]
        }
    define_json = json.dumps(mktequd_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def mktequdadjadj_define(table_name):

    mktequdadjadj_str = {
            "table_name": "mktequdadjadj",
            "table_show_name": "沪深股票前复权行情",
            "table_comment": "沪深股票前复权行情-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "通联编制的证券编码，可使用getSecID获取",
                 "col_comment": "通联编制的证券编码，可使用getSecID获取-描述"},
                {"col_name": "ticker", "col_show_name": "通用交易代码", "col_comment": "通用交易代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD", "col_show_name": "通联编制的交易市场编码", "col_comment": "通联编制的交易市场编码-描述"},
                {"col_name": "tradeDate", "col_show_name": "交易日期", "col_comment": "交易日期-描述"},
                {"col_name": "preClosePrice", "col_show_name": "昨收盘(前复权)", "col_comment": "昨收盘(前复权)-描述"},
                {"col_name": "actPreClosePrice", "col_show_name": "昨收盘(未复权)", "col_comment": "昨收盘(未复权)-描述"},
                {"col_name": "openPrice", "col_show_name": "今开盘(前复权)", "col_comment": "今开盘(前复权)-描述"},
                {"col_name": "highestPrice", "col_show_name": "最高价(前复权)", "col_comment": "最高价(前复权)-描述"},
                {"col_name": "lowestPrice", "col_show_name": "最低价(前复权)", "col_comment": "最低价(前复权)-描述"},
                {"col_name": "closePrice", "col_show_name": "今收盘(前复权)", "col_comment": "今收盘(前复权)-描述"},
                {"col_name": "turnoverVol", "col_show_name": "成交量(前复权)", "col_comment": "成交量(前复权)-描述"},
                {"col_name": "negMarketValue", "col_show_name": "流通市值，收盘价*无限售流通股数",
                 "col_comment": "流通市值，收盘价*无限售流通股数-描述"},
                {"col_name": "dealAmount", "col_show_name": "成交笔数", "col_comment": "成交笔数-描述"},
                {"col_name": "turnoverRate", "col_show_name": "日换手率", "col_comment": "日换手率-描述"},
                {"col_name": "accumAdjFactor",
                 "col_show_name": "累积前复权因子，前复权价=未复权价*对应的累积前复权因子。最新一次除权除息日至最新行情期间的价格不需要进行任何的调整，该期间前复权因子都是1。",
                 "col_comment": "累积前复权因子，前复权价=未复权价*对应的累积前复权因子。最新一次除权除息日至最新行情期间的价格不需要进行任何的调整，该期间前复权因子都是1。-描述"},
                {"col_name": "turnoverValue", "col_show_name": "成交金额", "col_comment": "成交金额-描述"},
                {"col_name": "marketValue", "col_show_name": "总市值，收盘价*总股本数", "col_comment": "总市值，收盘价*总股本数-描述"},
                {"col_name": "isOpen", "col_show_name": "股票今日是否开盘标记：0-未开盘，1-交易日",
                 "col_comment": "股票今日是否开盘标记：0-未开盘，1-交易日-描述"},
                {"col_name": "vwap", "col_show_name": "VWAP，成交金额/成交量*累积前复权因子",
                 "col_comment": "VWAP，成交金额/成交量*累积前复权因子-描述"}
            ]
        }
    define_json = json.dumps(mktequdadjadj_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def mktequdadjaf_define(table_name):

    mktequdadjaf_str = {
            "table_name": "mktequdadjaf",
            "table_show_name": "沪深股票后复权行情",
            "table_comment": "沪深股票后复权行情-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "通联编制的证券编码，可使用DataAPI.SecIDGet获取",
                 "col_comment": "通联编制的证券编码，可使用DataAPI.SecIDGet获取-描述"},
                {"col_name": "ticker", "col_show_name": "通用交易代码", "col_comment": "通用交易代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD", "col_show_name": "通联编制的交易市场编码", "col_comment": "通联编制的交易市场编码-描述"},
                {"col_name": "tradeDate", "col_show_name": "交易日期", "col_comment": "交易日期-描述"},
                {"col_name": "preClosePrice", "col_show_name": "昨收盘(后复权)", "col_comment": "昨收盘(后复权)-描述"},
                {"col_name": "actPreClosePrice", "col_show_name": "昨收盘(未复权)", "col_comment": "昨收盘(未复权)-描述"},
                {"col_name": "openPrice", "col_show_name": "今开盘(后复权)", "col_comment": "今开盘(后复权)-描述"},
                {"col_name": "highestPrice", "col_show_name": "最高价(后复权)", "col_comment": "最高价(后复权)-描述"},
                {"col_name": "lowestPrice", "col_show_name": "最低价(后复权)", "col_comment": "最低价(后复权)-描述"},
                {"col_name": "closePrice", "col_show_name": "今收盘(后复权)", "col_comment": "今收盘(后复权)-描述"},
                {"col_name": "turnoverVol", "col_show_name": "成交量(后复权)=未复权成交量*累积复权因子",
                 "col_comment": "成交量(后复权)=未复权成交量*累积复权因子-描述"},
                {"col_name": "turnoverValue", "col_show_name": "成交金额", "col_comment": "成交金额-描述"},
                {"col_name": "dealAmount", "col_show_name": "成交笔数", "col_comment": "成交笔数-描述"},
                {"col_name": "turnoverRate", "col_show_name": "日换手率", "col_comment": "日换手率-描述"},
                {"col_name": "accumAdjFactor", "col_show_name": "累积后复权因子，后复权是对除权除息日以后的行情进行调整，无需调整历史。后复权价=未复权价*累积后复权因子",
                 "col_comment": "累积后复权因子，后复权是对除权除息日以后的行情进行调整，无需调整历史。后复权价=未复权价*累积后复权因子-描述"},
                {"col_name": "negMarketValue", "col_show_name": "流通市值，收盘价*无限售流通股数",
                 "col_comment": "流通市值，收盘价*无限售流通股数-描述"},
                {"col_name": "marketValue", "col_show_name": "总市值，收盘价*总股本数", "col_comment": "总市值，收盘价*总股本数-描述"},
                {"col_name": "isOpen", "col_show_name": "股票今日是否开盘标记：0-未开盘，1-交易日",
                 "col_comment": "股票今日是否开盘标记：0-未开盘，1-交易日-描述"},
                {"col_name": "vwap", "col_show_name": "VWAP，成交金额/成交量*累积后复权因子",
                 "col_comment": "VWAP，成交金额/成交量*累积后复权因子-描述"}
            ]
        }
    define_json = json.dumps(mktequdadjaf_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def equcompproduction_define(table_name):

    equcompproduction_str = {
            "table_name": "equcompproduction",
            "table_show_name": "公司主营产品",
            "table_comment": "公司主营产品-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "item", "col_show_name": "关联产品", "col_comment": "关联产品-描述"},
                {"col_name": "ticker", "col_show_name": "股票代码", "col_comment": "股票代码-描述"},
                {"col_name": "secShortName", "col_show_name": "股票名称", "col_comment": "股票名称-描述"},
                {"col_name": "prodName", "col_show_name": "主营产品", "col_comment": "主营产品-描述"},
                {"col_name": "prodPct", "col_show_name": "主营比例", "col_comment": "主营比例-描述"},
                {"col_name": "periodDate", "col_show_name": "数据时间", "col_comment": "数据时间-描述"},
                {"col_name": "updateTime", "col_show_name": "更新时间", "col_comment": "更新时间-描述"}
            ]
        }
    define_json = json.dumps(equcompproduction_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def mktrankliststocks_define(table_name):

    mktrankliststocks_str = {
            "table_name": "mktrankliststocks",
            "table_show_name": "龙虎榜_股票",
            "table_comment": "龙虎榜_股票-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "通联编制的证券编码，可使用DataAPI.SecIDGet获取",
                 "col_comment": "通联编制的证券编码，可使用DataAPI.SecIDGet获取-描述"},
                {"col_name": "ticker", "col_show_name": "通用交易代码", "col_comment": "通用交易代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD", "col_show_name": "通联编制的交易市场编码", "col_comment": "通联编制的交易市场编码-描述"},
                {"col_name": "tradeDate", "col_show_name": "交易日期", "col_comment": "交易日期-描述"},
                {"col_name": "abnormalTypeCD", "col_show_name": "异动类型代码，可从参数集合获取DataAPI.SysCodeGet.codeTypeID=12006",
                 "col_comment": "异动类型代码，可从参数集合获取DataAPI.SysCodeGet.codeTypeID=12006-描述"},
                {"col_name": "abnormalType", "col_show_name": "异动类型名称，上榜原因", "col_comment": "异动类型名称，上榜原因-描述"},
                {"col_name": "deviation", "col_show_name": "偏离值，异动类型具体偏离的数值，如涨幅、振幅、换手率等。单位：%",
                 "col_comment": "偏离值，异动类型具体偏离的数值，如涨幅、振幅、换手率等。单位：%-描述"},
                {"col_name": "turnoverVol", "col_show_name": "当日成交量，单位：股", "col_comment": "当日成交量，单位：股-描述"},
                {"col_name": "turnoverValue", "col_show_name": "当日成交金额，单位：元", "col_comment": "当日成交金额，单位：元-描述"},
                {"col_name": "abnormalBeginDate", "col_show_name": "异动起始日期，对应覆盖多个交易日的异动类型",
                 "col_comment": "异动起始日期，对应覆盖多个交易日的异动类型-描述"},
                {"col_name": "abnormalEndDate", "col_show_name": "异动截至日期，对应覆盖多个交易日的异动类型",
                 "col_comment": "异动截至日期，对应覆盖多个交易日的异动类型-描述"}
            ]
        }
    define_json = json.dumps(mktrankliststocks_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def mktranklistsales_define(table_name):

    mktranklistsales_str = {
            "table_name": "mktranklistsales",
            "table_show_name": "龙虎榜_营业部",
            "table_comment": "龙虎榜_营业部-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "通联编制的证券编码，可使用DataAPI.SecIDGet获取",
                 "col_comment": "通联编制的证券编码，可使用DataAPI.SecIDGet获取-描述"},
                {"col_name": "ticker", "col_show_name": "通用交易代码", "col_comment": "通用交易代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD", "col_show_name": "通联编制的交易市场编码", "col_comment": "通联编制的交易市场编码-描述"},
                {"col_name": "tradeDate", "col_show_name": "交易日期", "col_comment": "交易日期-描述"},
                {"col_name": "side", "col_show_name": "买卖方向，B-买入；S-卖出", "col_comment": "买卖方向，B-买入；S-卖出-描述"},
                {"col_name": "rank", "col_show_name": "排名，提供第1~5名的排名。以对应买卖方向的买入/卖出金额排名",
                 "col_comment": "排名，提供第1~5名的排名。以对应买卖方向的买入/卖出金额排名-描述"},
                {"col_name": "sales", "col_show_name": "营业部名称", "col_comment": "营业部名称-描述"},
                {"col_name": "buyValue", "col_show_name": "买入金额，未公布填充0，同一营业部可能在同一天同时上榜买卖两个方向",
                 "col_comment": "买入金额，未公布填充0，同一营业部可能在同一天同时上榜买卖两个方向-描述"},
                {"col_name": "sellValue", "col_show_name": "买入金额，未公布填充0，同一营业部可能在同一天同时上榜买卖两个方向",
                 "col_comment": "买入金额，未公布填充0，同一营业部可能在同一天同时上榜买卖两个方向-描述"},
                {"col_name": "totalValue", "col_show_name": "买卖总金额", "col_comment": "买卖总金额-描述"},
                {"col_name": "abnormalTypeCD", "col_show_name": "异动类型代码，可从参数集合获取DataAPI.SysCodeGet.codeTypeID=12006",
                 "col_comment": "异动类型代码，可从参数集合获取DataAPI.SysCodeGet.codeTypeID=12006-描述"},
                {"col_name": "updateTime", "col_show_name": "更新时间", "col_comment": "更新时间-描述"}
            ]
        }
    define_json = json.dumps(mktranklistsales_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def equreportpredisclo_define(table_name):

    equreportpredisclo_str = {
            "table_name": "equreportpredisclo",
            "table_show_name": "上市A股定期报告预披露",
            "table_comment": "上市A股定期报告预披露-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "证券内部编码", "col_comment": "证券内部编码-描述"},
                {"col_name": "ticker", "col_show_name": "股票代码", "col_comment": "股票代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD", "col_show_name": "交易市场", "col_comment": "交易市场-描述"},
                {"col_name": "preDate", "col_show_name": "预计披露日", "col_comment": "预计披露日-描述"},
                {"col_name": "endDate", "col_show_name": "报告期", "col_comment": "报告期-描述"},
                {"col_name": "actDate", "col_show_name": "实际披露日", "col_comment": "实际披露日-描述"},
                {"col_name": "updateDate1", "col_show_name": "第一次变更日期", "col_comment": "第一次变更日期-描述"},
                {"col_name": "updateDate2", "col_show_name": "第二次变更日期", "col_comment": "第二次变更日期-描述"},
                {"col_name": "updateDate3", "col_show_name": "第三次变更日期", "col_comment": "第三次变更日期-描述"}
            ]
        }
    define_json = json.dumps(equreportpredisclo_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def secchghistory_define(table_name):

    secchghistory_str = {
            "table_name": "secchghistory",
            "table_show_name": "股票简称与代码变更",
            "table_comment": "股票简称与代码变更-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "date", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "secID", "col_show_name": "通联编制的证券编码。", "col_comment": "通联编制的证券编码。-描述"},
                {"col_name": "ticker", "col_show_name": "证券在证券市场通用的交易代码（目前的最新代码）。",
                 "col_comment": "证券在证券市场通用的交易代码（目前的最新代码）。-描述"},
                {"col_name": "changType", "col_show_name": "变更类型，包括“简称变更”和“代码变更”两种。",
                 "col_comment": "变更类型，包括“简称变更”和“代码变更”两种。-描述"},
                {"col_name": "value", "col_show_name": "值（包含历史简称、历史代码信息等）", "col_comment": "值（包含历史简称、历史代码信息等）-描述"},
                {"col_name": "beginDate", "col_show_name": "股票简称/代码的起始使用日期。", "col_comment": "股票简称/代码的起始使用日期。-描述"},
                {"col_name": "endDate", "col_show_name": "历史简称/代码的最后使用日期。为空表示现在仍在使用。",
                 "col_comment": "历史简称/代码的最后使用日期。为空表示现在仍在使用。-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称（最新）", "col_comment": "证券简称（最新）-描述"},
                {"col_name": "assetClass", "col_show_name": "证券类型", "col_comment": "证券类型-描述"},
                {"col_name": "exchangeCD", "col_show_name": "交易市场", "col_comment": "交易市场-描述"}
            ]
        }
    define_json = json.dumps(secchghistory_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


# tradeDate为新增索引
def sechalt_define(table_name):

    sechalt_str = {
            "table_name": "sechalt",
            "table_show_name": "沪深证券停复牌",
            "table_comment": "沪深证券停复牌-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "tradeDate", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "secID", "col_show_name": "证券ID", "col_comment": "证券ID-描述"},
                {"col_name": "haltBeginTime", "col_show_name": "停牌起始时间", "col_comment": "停牌起始时间-描述"},
                {"col_name": "haltEndTime", "col_show_name": "停牌结束时间", "col_comment": "停牌结束时间-描述"},
                {"col_name": "ticker", "col_show_name": "交易代码", "col_comment": "交易代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD", "col_show_name": "交易市场", "col_comment": "交易市场-描述"},
                {"col_name": "listStatusCD", "col_show_name": "上市状态。L-上市；S-暂停；DE-终止上市；UN-未上市。",
                 "col_comment": "上市状态。L-上市；S-暂停；DE-终止上市；UN-未上市。-描述"},
                {"col_name": "delistDate", "col_show_name": "退市时间", "col_comment": "退市时间-描述"},
                {"col_name": "assetClass", "col_show_name": "通联编制的证券类别编码。例如，E-股票；B-债券；F-基金；FU-期货等。",
                 "col_comment": "通联编制的证券类别编码。例如，E-股票；B-债券；F-基金；FU-期货等。-描述"}
            ]
        }
    define_json = json.dumps(sechalt_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def equsharesfloat_define(table_name):

    equsharesfloat_str = {
            "table_name": "equsharesfloat",
            "table_show_name": "限售股解禁",
            "table_comment": "限售股解禁-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "证券内部编码", "col_comment": "证券内部编码-描述"},
                {"col_name": "ticker", "col_show_name": "股票代码", "col_comment": "股票代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD", "col_show_name": "交易市场", "col_comment": "交易市场-描述"},
                {"col_name": "publishDate", "col_show_name": "公告日期", "col_comment": "公告日期-描述"},
                {"col_name": "floatDate", "col_show_name": "流通日期", "col_comment": "流通日期-描述"},
                {"col_name": "floatNum", "col_show_name": "流通数量", "col_comment": "流通数量-描述"},
                {"col_name": "shareProperty", "col_show_name": "限售流通股份性质", "col_comment": "限售流通股份性质-描述"}
            ]
        }
    define_json = json.dumps(equsharesfloat_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def equshareschg_define(table_name):

    equshareschg_str = {
            "table_name": "equshareschg",
            "table_show_name": "公司股本变动(新)",
            "table_comment": "公司股本变动(新)-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "partyID", "col_show_name": "通联编制的机构编码，可在DataAPI.PartyIDGet接口获取。",
                 "col_comment": "通联编制的机构编码，可在DataAPI.PartyIDGet接口获取。-描述"},
                {"col_name": "secID", "col_show_name": "通联编制的证券编码。可传入证券交易代码使用DataAPI.SecIDGet接口获取到。",
                 "col_comment": "通联编制的证券编码。可传入证券交易代码使用DataAPI.SecIDGet接口获取到。-描述"},
                {"col_name": "ticker", "col_show_name": "证券在证券市场通用的交易代码。", "col_comment": "证券在证券市场通用的交易代码。-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD",
                 "col_show_name": "证券交易市场代码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所。可在DataAPI.SysCodeGet接口输入codeTypeID=10002获取到",
                 "col_comment": "证券交易市场代码。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所。可在DataAPI.SysCodeGet接口输入codeTypeID=10002获取到-描述"},
                {"col_name": "publishDate", "col_show_name": "公告日期", "col_comment": "公告日期-描述"},
                {"col_name": "changeDate", "col_show_name": "变动日期", "col_comment": "变动日期-描述"},
                {"col_name": "changeType", "col_show_name": "变动原因", "col_comment": "变动原因-描述"},
                {"col_name": "totalShares", "col_show_name": "总股本(股)", "col_comment": "总股本(股)-描述"},
                {"col_name": "floatShares", "col_show_name": "流通股(股)", "col_comment": "流通股(股)-描述"},
                {"col_name": "floatA", "col_show_name": "流通A股(股)", "col_comment": "流通A股(股)-描述"},
                {"col_name": "floatB", "col_show_name": "流通B股(股)", "col_comment": "流通B股(股)-描述"},
                {"col_name": "floatH", "col_show_name": "流通H股(股)", "col_comment": "流通H股(股)-描述"},
                {"col_name": "floatOverseas", "col_show_name": "境外流通股(股)", "col_comment": "境外流通股(股)-描述"},
                {"col_name": "restShares", "col_show_name": "限售股(股)", "col_comment": "限售股(股)-描述"},
                {"col_name": "restA", "col_show_name": "限售A股(股)", "col_comment": "限售A股(股)-描述"},
                {"col_name": "restState", "col_show_name": "国家股(股)", "col_comment": "国家股(股)-描述"},
                {"col_name": "restStateLegal", "col_show_name": "国有法人股(股)", "col_comment": "国有法人股(股)-描述"},
                {"col_name": "restOtherDome", "col_show_name": "其他内资持股合计(股)", "col_comment": "其他内资持股合计(股)-描述"},
                {"col_name": "restLegalPer", "col_show_name": "境内法人持股(股)", "col_comment": "境内法人持股(股)-描述"},
                {"col_name": "restPer", "col_show_name": "境内自然人持股(股)", "col_comment": "境内自然人持股(股)-描述"},
                {"col_name": "restManager", "col_show_name": "高管持股(股)", "col_comment": "高管持股(股)-描述"},
                {"col_name": "restFr", "col_show_name": "外资持股合计(股)", "col_comment": "外资持股合计(股)-描述"},
                {"col_name": "restFrLegalPer", "col_show_name": "境外法人股(股)", "col_comment": "境外法人股(股)-描述"},
                {"col_name": "restFrPer", "col_show_name": "境外自然人股(股)", "col_comment": "境外自然人股(股)-描述"},
                {"col_name": "restB", "col_show_name": "限售B股(股)", "col_comment": "限售B股(股)-描述"},
                {"col_name": "restH", "col_show_name": "限售H股(股)", "col_comment": "限售H股(股)-描述"},
                {"col_name": "nonfShares", "col_show_name": "未流通股份(股)", "col_comment": "未流通股份(股)-描述"},
                {"col_name": "nonfStateShares", "col_show_name": "国家股(股)", "col_comment": "国家股(股)-描述"},
                {"col_name": "nonfStateLegal", "col_show_name": "国有法人股(股)", "col_comment": "国有法人股(股)-描述"},
                {"col_name": "nonfDomeCap", "col_show_name": "境内法人股(股)", "col_comment": "境内法人股(股)-描述"},
                {"col_name": "nonfFr", "col_show_name": "外资股(股)", "col_comment": "外资股(股)-描述"},
                {"col_name": "nonfFrLegalPer", "col_show_name": "外资法人股(股)", "col_comment": "外资法人股(股)-描述"},
                {"col_name": "nonfOtherFr", "col_show_name": "其他外资股(股)", "col_comment": "其他外资股(股)-描述"},
                {"col_name": "nonfOthSpoShares", "col_show_name": "其它发起人股(股)", "col_comment": "其它发起人股(股)-描述"},
                {"col_name": "nonfCorpRa", "col_show_name": "募集法人股(股)", "col_comment": "募集法人股(股)-描述"},
                {"col_name": "nonfStateLegalRa", "col_show_name": "募集国有法人股(股)", "col_comment": "募集国有法人股(股)-描述"},
                {"col_name": "nonfPerson", "col_show_name": "自然人股(股)", "col_comment": "自然人股(股)-描述"},
                {"col_name": "nonfEmployee", "col_show_name": "职工股(股)", "col_comment": "职工股(股)-描述"},
                {"col_name": "nonfTransfer", "col_show_name": "转配股(股)", "col_comment": "转配股(股)-描述"},
                {"col_name": "nonfPreOther", "col_show_name": "优先股及其他(股)", "col_comment": "优先股及其他(股)-描述"},
                {"col_name": "nonfPre", "col_show_name": "优先股(股)", "col_comment": "优先股(股)-描述"},
                {"col_name": "updateTime", "col_show_name": "更新时间", "col_comment": "更新时间-描述"}
            ]
        }
    define_json = json.dumps(equshareschg_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def equfreeshares_define(table_name):

    equfreeshares_str = {
            "table_name": "equfreeshares",
            "table_show_name": "自由流通股本",
            "table_comment": "自由流通股本-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "ticker", "col_show_name": "股票代码", "col_comment": "股票代码-描述"},
                {"col_name": "partyID", "col_show_name": "公司ID", "col_comment": "公司ID-描述"},
                {"col_name": "partyShortName", "col_show_name": "机构简称", "col_comment": "机构简称-描述"},
                {"col_name": "partyFullName", "col_show_name": "机构全称", "col_comment": "机构全称-描述"},
                {"col_name": "publishDate", "col_show_name": "公告日期", "col_comment": "公告日期-描述"},
                {"col_name": "changeDate", "col_show_name": "变动日期", "col_comment": "变动日期-描述"},
                {"col_name": "freeShares", "col_show_name": "自由流通股", "col_comment": "自由流通股-描述"}
            ]
        }
    define_json = json.dumps(equfreeshares_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def equallot_define(table_name):

    equallot_str = {
            "table_name": "equallot",
            "table_show_name": "股票配股信息",
            "table_comment": "股票配股信息-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "date", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "secID", "col_show_name": "证券内部ID", "col_comment": "证券内部ID-描述"},
                {"col_name": "ticker", "col_show_name": "交易代码", "col_comment": "交易代码-描述"},
                {"col_name": "exchangeCD",
                 "col_show_name": "交易市场。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所。对应getSysCode.codeTypeID=10002。",
                 "col_comment": "交易市场。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所。对应getSysCode.codeTypeID=10002。-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "publishDate", "col_show_name": "公告日期", "col_comment": "公告日期-描述"},
                {"col_name": "isAllotment", "col_show_name": "是否最终配股成功，0-不成功，1-成功。",
                 "col_comment": "是否最终配股成功，0-不成功，1-成功。-描述"},
                {"col_name": "equType", "col_show_name": "发行股份类型", "col_comment": "发行股份类型-描述"},
                {"col_name": "allotmentRatio", "col_show_name": "每股配股比例", "col_comment": "每股配股比例-描述"},
                {"col_name": "allotmentPrice", "col_show_name": "配股价", "col_comment": "配股价-描述"},
                {"col_name": "currencyCD", "col_show_name": "货币种类。CNY-人民币元，对应getSysCode.codeTypeID=10004。",
                 "col_comment": "货币种类。CNY-人民币元，对应getSysCode.codeTypeID=10004。-描述"},
                {"col_name": "allotFrPrice", "col_show_name": "外币配股价", "col_comment": "外币配股价-描述"},
                {"col_name": "frCurrencyCD", "col_show_name": "外币货币种类。例如，GBP-英镑；USD-美元。对应getSysCode.codeTypeID=10004。",
                 "col_comment": "外币货币种类。例如，GBP-英镑；USD-美元。对应getSysCode.codeTypeID=10004。-描述"},
                {"col_name": "recordDate", "col_show_name": "股权登记日", "col_comment": "股权登记日-描述"},
                {"col_name": "exRightsDate", "col_show_name": "除权日", "col_comment": "除权日-描述"},
                {"col_name": "payBeginDate", "col_show_name": "配股缴款起始日", "col_comment": "配股缴款起始日-描述"},
                {"col_name": "payEndDate", "col_show_name": "配股缴款截止日", "col_comment": "配股缴款截止日-描述"},
                {"col_name": "listDate", "col_show_name": "配股上市日", "col_comment": "配股上市日-描述"},
                {"col_name": "allotShares", "col_show_name": "配股数量", "col_comment": "配股数量-描述"},
                {"col_name": "sharesBfAllot", "col_show_name": "配股前总股本", "col_comment": "配股前总股本-描述"},
                {"col_name": "sharesAfAllot", "col_show_name": "配股后总股本", "col_comment": "配股后总股本-描述"}
            ]
        }
    define_json = json.dumps(equallot_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def equshten_define(table_name):

    equshten_str = {
            "table_name": "equshten",
            "table_show_name": "",
            "table_comment": "-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "证券内部编码", "col_comment": "证券内部编码-描述"},
                {"col_name": "ticker", "col_show_name": "股票代码", "col_comment": "股票代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD", "col_show_name": "交易市场", "col_comment": "交易市场-描述"},
                {"col_name": "endDate", "col_show_name": "截止日期", "col_comment": "截止日期-描述"},
                {"col_name": "shNum", "col_show_name": "股东序号", "col_comment": "股东序号-描述"},
                {"col_name": "shName", "col_show_name": "股东名称", "col_comment": "股东名称-描述"},
                {"col_name": "holdVol", "col_show_name": "持股数", "col_comment": "持股数-描述"},
                {"col_name": "holdPct", "col_show_name": "持股比例", "col_comment": "持股比例-描述"},
                {"col_name": "shareType", "col_show_name": "股份性质", "col_comment": "股份性质-描述"},
                {"col_name": "updateTime", "col_show_name": "更新时间", "col_comment": "更新时间-描述"},
                {"col_name": "publishDate", "col_show_name": "发布时间", "col_comment": "发布时间-描述"}
            ]
        }
    define_json = json.dumps(equshten_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def stockfctindiconeday_define(table_name):

    stockfctindiconeday_str = {
            "table_name": "stockfctindiconeday",
            "table_show_name": "沪深个股当天指标数据",
            "table_comment": "沪深个股当天指标数据-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "证券ID", "col_comment": "证券ID-描述"},
                {"col_name": "ticker", "col_show_name": "股票代码", "col_comment": "股票代码-描述"},
                {"col_name": "tradeDate", "col_show_name": "交易日期", "col_comment": "交易日期-描述"},
                {"col_name": "EBITPS", "col_show_name": "息税前利润与总股本比率。息税前利润是扣除利息、所得税之前的利润。",
                 "col_comment": "息税前利润与总股本比率。息税前利润是扣除利息、所得税之前的利润。-描述"},
                {"col_name": "RESERPS",
                 "col_show_name": "公积金与总股本比率。公积金分资本公积金和盈余公积金。资本公积金：溢价发行债券的差额和无偿捐赠资金实物作为资本公积金。盈余公积金：从偿还债务和的税后利润中提取10%作为盈余公积金。",
                 "col_comment": "公积金与总股本比率。公积金分资本公积金和盈余公积金。资本公积金：溢价发行债券的差额和无偿捐赠资金实物作为资本公积金。盈余公积金：从偿还债务和的税后利润中提取10%作为盈余公积金。-描述"},
                {"col_name": "dividendPS", "col_show_name": "每股在上一年的现金分红，等于股息率*收盘价",
                 "col_comment": "每股在上一年的现金分红，等于股息率*收盘价-描述"},
                {"col_name": "invCFNetInc", "col_show_name": "过去12个月投资现金流量净额相对4季度前的12个月投资现金流量净额",
                 "col_comment": "过去12个月投资现金流量净额相对4季度前的12个月投资现金流量净额-描述"},
                {"col_name": "finCFNetInc", "col_show_name": "过去12个月筹资现金流量净额相对4季度前的12个月筹资现金流量净额",
                 "col_comment": "过去12个月筹资现金流量净额相对4季度前的12个月筹资现金流量净额-描述"},
                {"col_name": "finCFps", "col_show_name": "过去12个月筹资现金流量净额与总股本比率。",
                 "col_comment": "过去12个月筹资现金流量净额与总股本比率。-描述"},
                {"col_name": "invCFps", "col_show_name": "过去12个月的投资现金流净额与总股本比率。",
                 "col_comment": "过去12个月的投资现金流净额与总股本比率。-描述"},
                {"col_name": "revenueC3", "col_show_name": "过去12个月营业收入相对3年前12个月营业收入的年化增长率。",
                 "col_comment": "过去12个月营业收入相对3年前12个月营业收入的年化增长率。-描述"},
                {"col_name": "revenueC5", "col_show_name": "过去12个月营业收入相对5年前12个月营业收入的年化增长率。",
                 "col_comment": "过去12个月营业收入相对5年前12个月营业收入的年化增长率。-描述"},
                {"col_name": "netProfitC3", "col_show_name": "过去12个月净利润相对3年前12个月净利润的年化增长率。",
                 "col_comment": "过去12个月净利润相对3年前12个月净利润的年化增长率。-描述"},
                {"col_name": "netProfitC5", "col_show_name": "过去12个月净利润相对5年前12个月净利润的年化增长率。",
                 "col_comment": "过去12个月净利润相对5年前12个月净利润的年化增长率。-描述"},
                {"col_name": "roe5", "col_show_name": "过去5年净利润之和除以一年之前5年的所有者权益之和。",
                 "col_comment": "过去5年净利润之和除以一年之前5年的所有者权益之和。-描述"},
                {"col_name": "CEps", "col_show_name": "期末现金及现金等价物余额与总股本比率。", "col_comment": "期末现金及现金等价物余额与总股本比率。-描述"},
                {"col_name": "TAps", "col_show_name": "最近一季度的（资产总计-无形资产-商誉）与总股本比率。",
                 "col_comment": "最近一季度的（资产总计-无形资产-商誉）与总股本比率。-描述"},
                {"col_name": "chgPct", "col_show_name": "股价当日涨跌幅，显示数值为百分比。", "col_comment": "股价当日涨跌幅，显示数值为百分比。-描述"},
                {"col_name": "totalShares", "col_show_name": "股票当日总股数", "col_comment": "股票当日总股数-描述"},
                {"col_name": "nonrestFloat", "col_show_name": "股票当日总流通股数", "col_comment": "股票当日总流通股数-描述"},
                {"col_name": "dealAmount", "col_show_name": "股票当日成交笔数", "col_comment": "股票当日成交笔数-描述"},
                {"col_name": "priceAmp", "col_show_name": "股票当日最高价最低价之差除以前日收盘价。",
                 "col_comment": "股票当日最高价最低价之差除以前日收盘价。-描述"},
                {"col_name": "daysOnMkt", "col_show_name": "从上市日到当日的自然日天数", "col_comment": "从上市日到当日的自然日天数-描述"},
                {"col_name": "tradeDays", "col_show_name": "从上市日到当日到交易天数", "col_comment": "从上市日到当日到交易天数-描述"},
                {"col_name": "inflowT", "col_show_name": "当日所有主动性买盘成交额合计", "col_comment": "当日所有主动性买盘成交额合计-描述"},
                {"col_name": "outflowT", "col_show_name": "当日所有主动性卖盘成交额合计", "col_comment": "当日所有主动性卖盘成交额合计-描述"},
                {"col_name": "netInflowT", "col_show_name": "资金流入-资金流出=资金净流入", "col_comment": "资金流入-资金流出=资金净流入-描述"},
                {"col_name": "inflowS", "col_show_name": "当日小于100万交易单资金的流入", "col_comment": "当日小于100万交易单资金的流入-描述"},
                {"col_name": "inflowM", "col_show_name": "当日100万到500万的交易单资金的流入",
                 "col_comment": "当日100万到500万的交易单资金的流入-描述"},
                {"col_name": "inflowL", "col_show_name": "当日500万到1000万的交易单资金的流入",
                 "col_comment": "当日500万到1000万的交易单资金的流入-描述"},
                {"col_name": "inflowXl", "col_show_name": "当日1000万以上的交易单资金的流入", "col_comment": "当日1000万以上的交易单资金的流入-描述"},
                {"col_name": "outflowS", "col_show_name": "当日小于100万交易单资金的流出", "col_comment": "当日小于100万交易单资金的流出-描述"},
                {"col_name": "outflowM", "col_show_name": "当日100万到500万的交易单资金的流出",
                 "col_comment": "当日100万到500万的交易单资金的流出-描述"},
                {"col_name": "outflowL", "col_show_name": "当日500万到1000万的交易单资金的流出",
                 "col_comment": "当日500万到1000万的交易单资金的流出-描述"},
                {"col_name": "outflowXl", "col_show_name": "当日1000万以上的交易单资金的流出",
                 "col_comment": "当日1000万以上的交易单资金的流出-描述"},
                {"col_name": "netInflowS", "col_show_name": "当日小于100万交易单资金的净流入", "col_comment": "当日小于100万交易单资金的净流入-描述"},
                {"col_name": "netInflowS5", "col_show_name": "近5日小单流入金额与小单流出金额之差的累计和",
                 "col_comment": "近5日小单流入金额与小单流出金额之差的累计和-描述"},
                {"col_name": "netInflowS20", "col_show_name": "近20日小单流入金额与小单流出金额之差的累计和",
                 "col_comment": "近20日小单流入金额与小单流出金额之差的累计和-描述"},
                {"col_name": "netInflowM", "col_show_name": "当日100万到500万的交易单资金的净流入",
                 "col_comment": "当日100万到500万的交易单资金的净流入-描述"},
                {"col_name": "netInflowM5", "col_show_name": "5日中单净流入金额之和", "col_comment": "5日中单净流入金额之和-描述"},
                {"col_name": "netInflowM20", "col_show_name": "20日中单净流入金额之和", "col_comment": "20日中单净流入金额之和-描述"},
                {"col_name": "netInflowL", "col_show_name": "当日500万到1000万的交易单资金的净流入",
                 "col_comment": "当日500万到1000万的交易单资金的净流入-描述"},
                {"col_name": "netInflowL5", "col_show_name": "5日大单净流入金额之和", "col_comment": "5日大单净流入金额之和-描述"},
                {"col_name": "netInflowL20", "col_show_name": "20日大单净流入金额之和。", "col_comment": "20日大单净流入金额之和。-描述"},
                {"col_name": "netInflowXl", "col_show_name": "当日1000万以上的交易单资金的净流入",
                 "col_comment": "当日1000万以上的交易单资金的净流入-描述"},
                {"col_name": "netInflowXl5", "col_show_name": "5日超大单净流入金额之和。", "col_comment": "5日超大单净流入金额之和。-描述"},
                {"col_name": "netInflowXl20", "col_show_name": "20日超大单净流入金额之和。", "col_comment": "20日超大单净流入金额之和。-描述"},
                {"col_name": "upLimitTimes", "col_show_name": "当日股票涨停的次数", "col_comment": "当日股票涨停的次数-描述"},
                {"col_name": "upLimitOpen", "col_show_name": "第一笔成交价就到达了涨停板，开盘价就是涨停板的价格的股票。",
                 "col_comment": "第一笔成交价就到达了涨停板，开盘价就是涨停板的价格的股票。-描述"},
                {"col_name": "upLimitDay", "col_show_name": "开盘即涨停，从未打开，一直持续到收盘为止的股票。标记：一字涨停为1，未一字涨停为0",
                 "col_comment": "开盘即涨停，从未打开，一直持续到收盘为止的股票。标记：一字涨停为1，未一字涨停为0-描述"},
                {"col_name": "udLimitTimes", "col_show_name": "当日股票涨停的次数", "col_comment": "当日股票涨停的次数-描述"},
                {"col_name": "dnLimitTimes", "col_show_name": "当日股票跌停的次数", "col_comment": "当日股票跌停的次数-描述"},
                {"col_name": "dnLimitOpen", "col_show_name": "第一笔成交价就到达了跌停板，开盘价就是跌停板的价格的股票。标记：跌停为1，未跌停为0",
                 "col_comment": "第一笔成交价就到达了跌停板，开盘价就是跌停板的价格的股票。标记：跌停为1，未跌停为0-描述"},
                {"col_name": "dnLimitDay", "col_show_name": "开盘即跌停，从未打开，一直持续到收盘为止的股票。标记：一字跌停为1，未一字跌停为0",
                 "col_comment": "开盘即跌停，从未打开，一直持续到收盘为止的股票。标记：一字跌停为1，未一字跌停为0-描述"},
                {"col_name": "top5NetIn", "col_show_name": "买入额前5名营业部净买入之和", "col_comment": "买入额前5名营业部净买入之和-描述"},
                {"col_name": "top5NetOut", "col_show_name": "卖出额前5名营业部净卖出之和", "col_comment": "卖出额前5名营业部净卖出之和-描述"},
                {"col_name": "tWorth", "col_show_name": "价值股/非价值股。价值股是指相对于它们的现有收益，股价被低估的一类股票。非价值股是价值股的对立面。",
                 "col_comment": "价值股/非价值股。价值股是指相对于它们的现有收益，股价被低估的一类股票。非价值股是价值股的对立面。-描述"},
                {"col_name": "tROE",
                 "col_show_name": "亏损股/微利股/绩优股亏损股：企业盈利为负数的，亏损企业的股票。微利股：处于赢利状态，但每股收益非常小（0.1元）以下的股票。绩优股：业绩优良公司的股票。",
                 "col_comment": "亏损股/微利股/绩优股亏损股：企业盈利为负数的，亏损企业的股票。微利股：处于赢利状态，但每股收益非常小（0.1元）以下的股票。绩优股：业绩优良公司的股票。-描述"},
                {"col_name": "tProfit",
                 "col_show_name": "低盈利股/高盈利股低市盈率股：市盈率很低的股票。高市盈率股：市盈率很高的股票。一般市盈率股：低市盈率股与高市盈率股区间内的股票。",
                 "col_comment": "低盈利股/高盈利股低市盈率股：市盈率很低的股票。高市盈率股：市盈率很高的股票。一般市盈率股：低市盈率股与高市盈率股区间内的股票。-描述"},
                {"col_name": "tPrice", "col_show_name": "低价股/一般价股/高价股低价股：价格很低的股票。高价股：价格很高的股票。一般价股：低价股与高价股区间内价格的股票。",
                 "col_comment": "低价股/一般价股/高价股低价股：价格很低的股票。高价股：价格很高的股票。一般价股：低价股与高价股区间内价格的股票。-描述"},
                {"col_name": "tPE",
                 "col_show_name": "低市盈率股/一般市盈率股/高市盈率股低市盈率股：市盈率很低的股票。高市盈率股：市盈率很高的股票。一般市盈率股：低市盈率股与高市盈率股区间内的股票。",
                 "col_comment": "低市盈率股/一般市盈率股/高市盈率股低市盈率股：市盈率很低的股票。高市盈率股：市盈率很高的股票。一般市盈率股：低市盈率股与高市盈率股区间内的股票。-描述"},
                {"col_name": "tMobility", "col_show_name": "活跃股／冷门股区间内日均换手率的平均值高的股票。（备注：活跃度一般是多维度来评估）",
                 "col_comment": "活跃股／冷门股区间内日均换手率的平均值高的股票。（备注：活跃度一般是多维度来评估）-描述"},
                {"col_name": "tMVStyle",
                 "col_show_name": "小盘股/中盘股/大盘股/超级大盘股按上市公司股票最新流通市值的大小来划分，通常分为超大盘股（市值的累加至所有流通市值合计的50%的时候，为超大盘股），大盘股（市值的累加至所有流通市值合计的50%到70%的时候为大盘股），中盘股（70%到90%时为中盘股）和小盘股（90%到100%时为小盘股）。",
                 "col_comment": "小盘股/中盘股/大盘股/超级大盘股按上市公司股票最新流通市值的大小来划分，通常分为超大盘股（市值的累加至所有流通市值合计的50%的时候，为超大盘股），大盘股（市值的累加至所有流通市值合计的50%到70%的时候为大盘股），中盘股（70%到90%时为中盘股）和小盘股（90%到100%时为小盘股）。-描述"},
                {"col_name": "tLeverage", "col_show_name": "低杠杆股/一般杠杆股/高杠杆股", "col_comment": "低杠杆股/一般杠杆股/高杠杆股-描述"},
                {"col_name": "tHbeta", "col_show_name": "跟随大盘股/背离大盘股跟随大盘走势的股票。",
                 "col_comment": "跟随大盘股/背离大盘股跟随大盘走势的股票。-描述"},
                {"col_name": "tGrowth", "col_show_name": "成长股/非成长股成长股：公司销售额和利润额持续增长，而且其速度快于整个国家和本行业的增长的股票。非成长股即成长股对立面。",
                 "col_comment": "成长股/非成长股成长股：公司销售额和利润额持续增长，而且其速度快于整个国家和本行业的增长的股票。非成长股即成长股对立面。-描述"},
                {"col_name": "bulkFundNum", "col_show_name": "重仓持有这支股票的基金个数。根据基金每季度公布的头10名持仓股票算出。",
                 "col_comment": "重仓持有这支股票的基金个数。根据基金每季度公布的头10名持仓股票算出。-描述"},
                {"col_name": "bulkFundPct", "col_show_name": "重仓基金持有这只股票的总市值除以股票流通市值。根据基金每季度公布的头10名持仓股票算出。",
                 "col_comment": "重仓基金持有这只股票的总市值除以股票流通市值。根据基金每季度公布的头10名持仓股票算出。-描述"},
                {"col_name": "bollUpBreak", "col_show_name": "前复权收盘价大于当天布林线上轨返回1，否则返回0",
                 "col_comment": "前复权收盘价大于当天布林线上轨返回1，否则返回0-描述"},
                {"col_name": "bollDnBreak", "col_show_name": "前复权收盘价小于当天布林线下轨返回1，否则返回0",
                 "col_comment": "前复权收盘价小于当天布林线下轨返回1，否则返回0-描述"},
                {"col_name": "rsiGoldCross", "col_show_name": "RSI金叉：短期（6日）RSI由下往上突破长期（12日）RSI。",
                 "col_comment": "RSI金叉：短期（6日）RSI由下往上突破长期（12日）RSI。-描述"},
                {"col_name": "rsiDeathCross", "col_show_name": "RSI死叉：短期（6日）RSI由上往下跌破长期（12日）RSI。",
                 "col_comment": "RSI死叉：短期（6日）RSI由上往下跌破长期（12日）RSI。-描述"},
                {"col_name": "rsiTopDiver", "col_show_name": "股价一波比一波高,RSI却一波比一波低时,为顶背离。",
                 "col_comment": "股价一波比一波高,RSI却一波比一波低时,为顶背离。-描述"},
                {"col_name": "rsiBtmDiver", "col_show_name": "股价一波比一波低,RSI却一波比一波高时,为底背离。",
                 "col_comment": "股价一波比一波低,RSI却一波比一波高时,为底背离。-描述"},
                {"col_name": "rsiShort", "col_show_name": "当短期（6日）RSI>长期（12日）RSI时，市场则属于多头市场",
                 "col_comment": "当短期（6日）RSI>长期（12日）RSI时，市场则属于多头市场-描述"},
                {"col_name": "rsiLong", "col_show_name": "当短期（6日）RSI<长期（12日）RSI时，市场则属于空头市场。",
                 "col_comment": "当短期（6日）RSI<长期（12日）RSI时，市场则属于空头市场。-描述"},
                {"col_name": "volGoldCross", "col_show_name": "成交量栏里的2条线，5日线下穿10日线叫死叉。",
                 "col_comment": "成交量栏里的2条线，5日线下穿10日线叫死叉。-描述"},
                {"col_name": "volDeathCross", "col_show_name": "成交量栏里的2条线，10日线上穿5日线叫金叉。",
                 "col_comment": "成交量栏里的2条线，10日线上穿5日线叫金叉。-描述"},
                {"col_name": "volLong", "col_show_name": "股价突破盘整，成交量大增，而股价仍继续上涨，因此形成多头市场征兆。",
                 "col_comment": "股价突破盘整，成交量大增，而股价仍继续上涨，因此形成多头市场征兆。-描述"},
                {"col_name": "volShort", "col_show_name": "股价下跌，导致买盘不积极，成交量随股价创新低而萎缩，因此形成的空头市场征兆。",
                 "col_comment": "股价下跌，导致买盘不积极，成交量随股价创新低而萎缩，因此形成的空头市场征兆。-描述"},
                {"col_name": "maLong", "col_show_name": "MA即移动平均线。MA短线在MA长线上方为MA多头",
                 "col_comment": "MA即移动平均线。MA短线在MA长线上方为MA多头-描述"},
                {"col_name": "maShort", "col_show_name": "MA即移动平均线。MA短线在MA长线下方为MA空头",
                 "col_comment": "MA即移动平均线。MA短线在MA长线下方为MA空头-描述"},
                {"col_name": "maDeathCross", "col_show_name": "MA短线（5日线）下穿MA长线（10日线）",
                 "col_comment": "MA短线（5日线）下穿MA长线（10日线）-描述"},
                {"col_name": "maGoldCross", "col_show_name": "MA短线（5日线）上穿MA长线（10日线）",
                 "col_comment": "MA短线（5日线）上穿MA长线（10日线）-描述"},
                {"col_name": "emaLong", "col_show_name": "EMA短线在MA长线上方", "col_comment": "EMA短线在MA长线上方-描述"},
                {"col_name": "emaShort", "col_show_name": "EMA短线在MA长线下方", "col_comment": "EMA短线在MA长线下方-描述"},
                {"col_name": "emaGoldCross", "col_show_name": "EMA短线上穿EMA长线", "col_comment": "EMA短线上穿EMA长线-描述"},
                {"col_name": "emaDeathCross", "col_show_name": "EMA短线下穿EMA长线", "col_comment": "EMA短线下穿EMA长线-描述"},
                {"col_name": "macdLong", "col_show_name": "MACD_DIF在MACD_DEF上方",
                 "col_comment": "MACD_DIF在MACD_DEF上方-描述"},
                {"col_name": "macdShort", "col_show_name": "MACD_DIF在MACD_DEF下方",
                 "col_comment": "MACD_DIF在MACD_DEF下方-描述"},
                {"col_name": "macdTopDiver", "col_show_name": "股价创新高但MACD未突破新高", "col_comment": "股价创新高但MACD未突破新高-描述"},
                {"col_name": "macdBtmDiver", "col_show_name": "股价创新低但MACD未突破新低", "col_comment": "股价创新低但MACD未突破新低-描述"},
                {"col_name": "macdGoldCross", "col_show_name": "MACD_DIF上穿MACD_DEF",
                 "col_comment": "MACD_DIF上穿MACD_DEF-描述"},
                {"col_name": "macdDeathCross", "col_show_name": "MACD_DIF下穿MACD_DEF",
                 "col_comment": "MACD_DIF下穿MACD_DEF-描述"},
                {"col_name": "macdTopDiverW",
                 "col_show_name": "股价创新高但周MACD未突破新高。若价格出现顶背离格局,多方力量减弱,预示上升动能衰竭,股价短期内下跌几率大。",
                 "col_comment": "股价创新高但周MACD未突破新高。若价格出现顶背离格局,多方力量减弱,预示上升动能衰竭,股价短期内下跌几率大。-描述"},
                {"col_name": "macdBtmDiverW",
                 "col_show_name": "股价创新低但周MACD未突破新低。若价格出现底背离格局,空方力量减弱,预示下降趋势减缓,股价短期内上升几率大。",
                 "col_comment": "股价创新低但周MACD未突破新低。若价格出现底背离格局,空方力量减弱,预示下降趋势减缓,股价短期内上升几率大。-描述"},
                {"col_name": "macdGoldCrossW", "col_show_name": "周MACD_DIFF上穿周MACD_DEF",
                 "col_comment": "周MACD_DIFF上穿周MACD_DEF-描述"},
                {"col_name": "macdDeathCrossW", "col_show_name": "周MACD_DIFF下穿周MACD_DEF",
                 "col_comment": "周MACD_DIFF下穿周MACD_DEF-描述"},
                {"col_name": "mfiOB", "col_show_name": "MFI大于80为超买，在其回头向下跌破80时，为短线卖出时机。",
                 "col_comment": "MFI大于80为超买，在其回头向下跌破80时，为短线卖出时机。-描述"},
                {"col_name": "mfiOS", "col_show_name": "MFI小于20为超卖，当其回头向上突破20时，为短线买进时机",
                 "col_comment": "MFI小于20为超卖，当其回头向上突破20时，为短线买进时机-描述"},
                {"col_name": "crOB", "col_show_name": "以上一个计算周期（为20日）的中间价比较当前周期的最高价、最低价，计算出一段时期内股价的“强弱”。",
                 "col_comment": "以上一个计算周期（为20日）的中间价比较当前周期的最高价、最低价，计算出一段时期内股价的“强弱”。-描述"},
                {"col_name": "crOS", "col_show_name": "以上一个计算周期（为20日）的中间价比较当前周期的最高价、最低价，计算出一段时期内股价的“强弱”。",
                 "col_comment": "以上一个计算周期（为20日）的中间价比较当前周期的最高价、最低价，计算出一段时期内股价的“强弱”。-描述"},
                {"col_name": "cciOB", "col_show_name": "CCI大于100", "col_comment": "CCI大于100-描述"},
                {"col_name": "cciOS", "col_show_name": "CCI小于-100", "col_comment": "CCI小于-100-描述"},
                {"col_name": "kdjLong", "col_show_name": "KDJ_K线在KDJ_D线上方", "col_comment": "KDJ_K线在KDJ_D线上方-描述"},
                {"col_name": "kdjShort", "col_show_name": "KDJ_K线在KDJ_D线下方", "col_comment": "KDJ_K线在KDJ_D线下方-描述"},
                {"col_name": "kdjLGoldCross", "col_show_name": "KDJ_K线上穿KDJ_D线", "col_comment": "KDJ_K线上穿KDJ_D线-描述"},
                {"col_name": "kdjHDeathCross", "col_show_name": "KDJ_K线下穿KDJ_D线", "col_comment": "KDJ_K线下穿KDJ_D线-描述"},
                {"col_name": "kdjBtmDiver", "col_show_name": "股价创新低但KDJ_D未突破新低", "col_comment": "股价创新低但KDJ_D未突破新低-描述"},
                {"col_name": "kdjTopDiver", "col_show_name": "股价创新高但KDJ_D未突破新高", "col_comment": "股价创新高但KDJ_D未突破新高-描述"},
                {"col_name": "volatility20", "col_show_name": "20日收益波动率（标准差）", "col_comment": "20日收益波动率（标准差）-描述"},
                {"col_name": "volatility60", "col_show_name": "60日收益波动率（标准差）", "col_comment": "60日收益波动率（标准差）-描述"},
                {"col_name": "volatility120", "col_show_name": "120日收益波动率（标准差）", "col_comment": "120日收益波动率（标准差）-描述"},
                {"col_name": "boldHead", "col_show_name": "最高价为开盘价或收盘价", "col_comment": "最高价为开盘价或收盘价-描述"},
                {"col_name": "boldBottom", "col_show_name": "最低价位开盘价或收盘价", "col_comment": "最低价位开盘价或收盘价-描述"},
                {"col_name": "longUpShadow", "col_show_name": "最高价/MAX(开盘价,收盘价)-1.0 >= 0.03",
                 "col_comment": "最高价/MAX(开盘价,收盘价)-1.0 >= 0.03-描述"},
                {"col_name": "midUpShadow", "col_show_name": "0.01 <= 最高价/MAX(开盘价,收盘价)-1.0 < 0.03",
                 "col_comment": "0.01 <= 最高价/MAX(开盘价,收盘价)-1.0 < 0.03-描述"},
                {"col_name": "longLowShadow", "col_show_name": "MIN(开盘价,收盘价)/最低价-1.0 >= 0.03",
                 "col_comment": "MIN(开盘价,收盘价)/最低价-1.0 >= 0.03-描述"},
                {"col_name": "midLowShadow", "col_show_name": "0.01 <= MIN(开盘价,收盘价)/最低价-1.0 < 0.03",
                 "col_comment": "0.01 <= MIN(开盘价,收盘价)/最低价-1.0 < 0.03-描述"},
                {"col_name": "openLow", "col_show_name": "开盘价小与昨日收盘价", "col_comment": "开盘价小与昨日收盘价-描述"},
                {"col_name": "jumpOpenLow", "col_show_name": "开盘价小于昨日开盘价和昨日收盘价", "col_comment": "开盘价小于昨日开盘价和昨日收盘价-描述"},
                {"col_name": "sunK", "col_show_name": "开盘价小于收盘价", "col_comment": "开盘价小于收盘价-描述"},
                {"col_name": "microSun", "col_show_name": "1.开盘价小于收盘价2.ABS(收盘价/开盘价-1.0) < 0.01",
                 "col_comment": "1.开盘价小于收盘价2.ABS(收盘价/开盘价-1.0) < 0.01-描述"},
                {"col_name": "shortSun", "col_show_name": "1.开盘价小于收盘价2.0.01 <= (收盘价/开盘价-1.0)的绝对值 < 0.03",
                 "col_comment": "1.开盘价小于收盘价2.0.01 <= (收盘价/开盘价-1.0)的绝对值 < 0.03-描述"},
                {"col_name": "midSun", "col_show_name": "1.开盘价小于收盘价2.0.03 <=(收盘价/开盘价-1.0)的绝对值< 0.05",
                 "col_comment": "1.开盘价小于收盘价2.0.03 <=(收盘价/开盘价-1.0)的绝对值< 0.05-描述"},
                {"col_name": "longSun", "col_show_name": "1.开盘价小于收盘价2.(收盘价/开盘价-1.0)的绝对值>=0.5",
                 "col_comment": "1.开盘价小于收盘价2.(收盘价/开盘价-1.0)的绝对值>=0.5-描述"},
                {"col_name": "lunarK", "col_show_name": "开盘价大于收盘价", "col_comment": "开盘价大于收盘价-描述"},
                {"col_name": "microLunar", "col_show_name": "1开盘价大于收盘价2(收盘价/开盘价-1.0)的绝对值< 0.01",
                 "col_comment": "1开盘价大于收盘价2(收盘价/开盘价-1.0)的绝对值< 0.01-描述"},
                {"col_name": "shortLunar", "col_show_name": "1)开盘价大于收盘价2)0.01 <=(收盘价/开盘价-1.0)的绝对值< 0.03",
                 "col_comment": "1)开盘价大于收盘价2)0.01 <=(收盘价/开盘价-1.0)的绝对值< 0.03-描述"},
                {"col_name": "midLunar", "col_show_name": "1)开盘价大于收盘价2)0.03 <=(收盘价/开盘价-1.0)的绝对值< 0.05",
                 "col_comment": "1)开盘价大于收盘价2)0.03 <=(收盘价/开盘价-1.0)的绝对值< 0.05-描述"},
                {"col_name": "longLunar", "col_show_name": "1)开盘价大于收盘价2)0.05 <=(收盘价/开盘价-1.0)的绝对值",
                 "col_comment": "1)开盘价大于收盘价2)0.05 <=(收盘价/开盘价-1.0)的绝对值-描述"},
                {"col_name": "longT",
                 "col_show_name": "1)长下影线 2)短上影线(最高价/MAX(开盘价,收盘价)-1.0 < 0.01) 3)ABS(收盘价/开盘价-1.0) < 0.01",
                 "col_comment": "1)长下影线 2)短上影线(最高价/MAX(开盘价,收盘价)-1.0 < 0.01) 3)ABS(收盘价/开盘价-1.0) < 0.01-描述"},
                {"col_name": "revLongT",
                 "col_show_name": "1)长上影线 2)短下影线(MIN(开盘价,收盘价)/最低价-1.0 < 0.01) 3)ABS(收盘价/开盘价-1.0) < 0.01",
                 "col_comment": "1)长上影线 2)短下影线(MIN(开盘价,收盘价)/最低价-1.0 < 0.01) 3)ABS(收盘价/开盘价-1.0) < 0.01-描述"},
                {"col_name": "oneFlag", "col_show_name": "收盘价=开盘价=最低价=最高价", "col_comment": "收盘价=开盘价=最低价=最高价-描述"},
                {"col_name": "cross", "col_show_name": "1)收盘价=开盘价 2)最高价>收盘价 3)最低价<收盘价",
                 "col_comment": "1)收盘价=开盘价 2)最高价>收盘价 3)最低价<收盘价-描述"},
                {"col_name": "shootStar", "col_show_name": "1)无下影线2)长上影线3)均线转头向上趋势",
                 "col_comment": "1)无下影线2)长上影线3)均线转头向上趋势-描述"},
                {"col_name": "crossDying",
                 "col_show_name": "1)ABS(开盘价/昨日收盘价-1.0) < 0.012)ABS(收盘价/昨日收盘价-1.0) < 0.013)收盘价=最低价4)收盘价<最高价",
                 "col_comment": "1)ABS(开盘价/昨日收盘价-1.0) < 0.012)ABS(收盘价/昨日收盘价-1.0) < 0.013)收盘价=最低价4)收盘价<最高价-描述"},
                {"col_name": "longCross", "col_show_name": "1)平盘,今日开盘价/收盘价与昨日收盘价相近2)最高价/最低价>1.03",
                 "col_comment": "1)平盘,今日开盘价/收盘价与昨日收盘价相近2)最高价/最低价>1.03-描述"},
                {"col_name": "bearishEngulf",
                 "col_show_name": "1)(昨日收盘价/昨日开盘价>1.03 AND收盘价/开盘价<0.96 AND收盘价<昨日开盘价 AND开盘价>昨日收盘价)或者2)(昨日收盘价/昨日开盘价<0.97 AND收盘价/开盘价>1.04 AND收盘价>昨日开盘价 AND开盘价<昨日收盘价)",
                 "col_comment": "1)(昨日收盘价/昨日开盘价>1.03 AND收盘价/开盘价<0.96 AND收盘价<昨日开盘价 AND开盘价>昨日收盘价)或者2)(昨日收盘价/昨日开盘价<0.97 AND收盘价/开盘价>1.04 AND收盘价>昨日开盘价 AND开盘价<昨日收盘价)-描述"},
                {"col_name": "shrinkVol", "col_show_name": "成交量<20日成交均量*0.333", "col_comment": "成交量<20日成交均量*0.333-描述"},
                {"col_name": "enlargeVol", "col_show_name": "成交量>20日成交均量*5", "col_comment": "成交量>20日成交均量*5-描述"},
                {"col_name": "above20High", "col_show_name": "收盘价>20日最高收盘价", "col_comment": "收盘价>20日最高收盘价-描述"},
                {"col_name": "above60High", "col_show_name": "收盘价>60日最高收盘价", "col_comment": "收盘价>60日最高收盘价-描述"},
                {"col_name": "below20Low", "col_show_name": "收盘价<20日最低收盘价", "col_comment": "收盘价<20日最低收盘价-描述"},
                {"col_name": "below60Low", "col_show_name": "收盘价<60日最低收盘价", "col_comment": "收盘价<60日最低收盘价-描述"},
                {"col_name": "openHigh", "col_show_name": "开盘价大于昨日收盘价", "col_comment": "开盘价大于昨日收盘价-描述"},
                {"col_name": "multiLongMark", "col_show_name": "5/10/20日多头排列标记，短期均线在长期均线上方，股价呈上升趋势",
                 "col_comment": "5/10/20日多头排列标记，短期均线在长期均线上方，股价呈上升趋势-描述"},
                {"col_name": "jumpOpenHigh", "col_show_name": "开盘价大于昨日开盘价和昨日收盘价", "col_comment": "开盘价大于昨日开盘价和昨日收盘价-描述"},
                {"col_name": "mgrHIncNum",
                 "col_show_name": "公司高管在一天内通过大宗交易或二级市场净增持股数，股数大于0时为净增持，股数小于0时为净减持，深市股票晚于实际增持日2日发布，沪市发布时间与实际增持时间间隔不确定。",
                 "col_comment": "公司高管在一天内通过大宗交易或二级市场净增持股数，股数大于0时为净增持，股数小于0时为净减持，深市股票晚于实际增持日2日发布，沪市发布时间与实际增持时间间隔不确定。-描述"},
                {"col_name": "mgrHIncAmt",
                 "col_show_name": "公司高管在一天内通过大宗交易或二级市场净增持金额，金额大于0时为净增持，金额小于0时为净减持，深市股票晚于实际增持日2日发布，沪市发布时间与实际增持时间间隔不确定。",
                 "col_comment": "公司高管在一天内通过大宗交易或二级市场净增持金额，金额大于0时为净增持，金额小于0时为净减持，深市股票晚于实际增持日2日发布，沪市发布时间与实际增持时间间隔不确定。-描述"},
                {"col_name": "mgrHIncTimes",
                 "col_show_name": "公司高管在一天内通过大宗交易或二级市场净增持交易次数，次数大于0时为净增持，次数小于0时为净减持，深市股票晚于实际增持日2日发布，沪市发布时间与实际增持时间间隔不确定。",
                 "col_comment": "公司高管在一天内通过大宗交易或二级市场净增持交易次数，次数大于0时为净增持，次数小于0时为净减持，深市股票晚于实际增持日2日发布，沪市发布时间与实际增持时间间隔不确定。-描述"},
                {"col_name": "mgrHIncPct",
                 "col_show_name": "公司高管在一天内通过大宗交易或二级市场净增持股本占比流通股本比例，比例大于0时为净增持，比例小于0时为净减持，深市股票晚于实际增持日2日发布，沪市发布时间与实际增持时间间隔不确定。",
                 "col_comment": "公司高管在一天内通过大宗交易或二级市场净增持股本占比流通股本比例，比例大于0时为净增持，比例小于0时为净减持，深市股票晚于实际增持日2日发布，沪市发布时间与实际增持时间间隔不确定。-描述"},
                {"col_name": "mgrHIncNum5", "col_show_name": "公司高管在过去5个交易日内通过大宗交易或二级市场净增持股数，股数大于0时为净增持，股数小于0时为净减持。",
                 "col_comment": "公司高管在过去5个交易日内通过大宗交易或二级市场净增持股数，股数大于0时为净增持，股数小于0时为净减持。-描述"},
                {"col_name": "mgrHIncAmt5", "col_show_name": "公司高管在过去5个交易日内通过大宗交易或二级市场净增持金额，金额大于0时为净增持，金额小于0时为净减持。",
                 "col_comment": "公司高管在过去5个交易日内通过大宗交易或二级市场净增持金额，金额大于0时为净增持，金额小于0时为净减持。-描述"},
                {"col_name": "mgrHIncTimes5",
                 "col_show_name": "公司高管在过去5个交易日内通过大宗交易或二级市场增持交易的次数，次数大于0时为净增持次数，次数小于0时为净减持次数。",
                 "col_comment": "公司高管在过去5个交易日内通过大宗交易或二级市场增持交易的次数，次数大于0时为净增持次数，次数小于0时为净减持次数。-描述"},
                {"col_name": "mgrHIncPct5", "col_show_name": "公司高管在过去5个交易日内增持股数占流通股的比例，比例大于0时为净增持，比例小于0时为净减持。",
                 "col_comment": "公司高管在过去5个交易日内增持股数占流通股的比例，比例大于0时为净增持，比例小于0时为净减持。-描述"},
                {"col_name": "mgrHIncNum20", "col_show_name": "公司高管在过去20个交易日内通过大宗交易或二级市场净增持股数，股数大于0时为净增持，股数小于0时为净减持。",
                 "col_comment": "公司高管在过去20个交易日内通过大宗交易或二级市场净增持股数，股数大于0时为净增持，股数小于0时为净减持。-描述"},
                {"col_name": "mgrHIncAmt20", "col_show_name": "公司高管在过去20个交易日内通过大宗交易或二级市场净增持金额，金额大于0时为净增持，金额小于0时为净减持。",
                 "col_comment": "公司高管在过去20个交易日内通过大宗交易或二级市场净增持金额，金额大于0时为净增持，金额小于0时为净减持。-描述"},
                {"col_name": "mgrHIncTimes20",
                 "col_show_name": "公司高管在过去20个交易日内通过大宗交易或二级市场增持交易的次数，次数大于0时为净增持次数，次数小于0时为净减持次数。",
                 "col_comment": "公司高管在过去20个交易日内通过大宗交易或二级市场增持交易的次数，次数大于0时为净增持次数，次数小于0时为净减持次数。-描述"},
                {"col_name": "mgrHIncPct20", "col_show_name": "公司高管在过去20个交易日内增持股数占流通股的比例，比例大于0时为净增持，比例小于0时为净减持。",
                 "col_comment": "公司高管在过去20个交易日内增持股数占流通股的比例，比例大于0时为净增持，比例小于0时为净减持。-描述"},
                {"col_name": "rFloatNum", "col_show_name": "当日新增的流通股数。", "col_comment": "当日新增的流通股数。-描述"},
                {"col_name": "rFloatPct", "col_show_name": "当日新增流通股占比，等于新增流通股数除以流通股本。",
                 "col_comment": "当日新增流通股占比，等于新增流通股数除以流通股本。-描述"},
                {"col_name": "rFloatNum20", "col_show_name": "未来20日新增流通股数之和。", "col_comment": "未来20日新增流通股数之和。-描述"},
                {"col_name": "rFloatPct20", "col_show_name": "未来20日新增流通股数之和除以流通股本。",
                 "col_comment": "未来20日新增流通股数之和除以流通股本。-描述"},
                {"col_name": "rFloatNum60", "col_show_name": "未来60日新增流通股数之和。", "col_comment": "未来60日新增流通股数之和。-描述"},
                {"col_name": "rFloatPct60", "col_show_name": "未来60日新增流通股数之和除以流通股本。",
                 "col_comment": "未来60日新增流通股数之和除以流通股本。-描述"},
                {"col_name": "accuPFloor",
                 "col_show_name": "预告年内累积利润和去年同期相比的涨幅下限。预告对应的季度由预告季度ID标出。为公告原披露值，或根据公告计算得出。值为空时，没有下限",
                 "col_comment": "预告年内累积利润和去年同期相比的涨幅下限。预告对应的季度由预告季度ID标出。为公告原披露值，或根据公告计算得出。值为空时，没有下限-描述"},
                {"col_name": "accuPCeil",
                 "col_show_name": "预告年内累积利润和去年同期相比的涨幅上限。预告对应的季度由预告季度ID标出。为公告原披露值，或根据公告计算得出。值为空时，没有上限",
                 "col_comment": "预告年内累积利润和去年同期相比的涨幅上限。预告对应的季度由预告季度ID标出。为公告原披露值，或根据公告计算得出。值为空时，没有上限-描述"},
                {"col_name": "preAccuPFloor", "col_show_name": "预告年内累积利润的下限。预告对应的季度由预告季度ID标出。为公告原披露值，或根据公告计算得出。",
                 "col_comment": "预告年内累积利润的下限。预告对应的季度由预告季度ID标出。为公告原披露值，或根据公告计算得出。-描述"},
                {"col_name": "preAccuPCeil", "col_show_name": "预告年内累积利润的上限。预告对应的季度由预告季度ID标出。为公告原披露值，或根据公告计算得出。",
                 "col_comment": "预告年内累积利润的上限。预告对应的季度由预告季度ID标出。为公告原披露值，或根据公告计算得出。-描述"},
                {"col_name": "preDays", "col_show_name": "从公告日开始算起的交易天数，0表示公告日当天，1表示公告在前一个交易日公布",
                 "col_comment": "从公告日开始算起的交易天数，0表示公告日当天，1表示公告在前一个交易日公布-描述"},
                {"col_name": "preSTIn",
                 "col_show_name": "1表示现在不是ST但预期在年报公布日ST戴帽的股票，0表示不预期ST戴帽或者已经是ST的股票。在公司年报业绩预告发布前，预期ST戴帽有可能为1。ST戴帽可能为1的时期一般在11月到次年的4月。",
                 "col_comment": "1表示现在不是ST但预期在年报公布日ST戴帽的股票，0表示不预期ST戴帽或者已经是ST的股票。在公司年报业绩预告发布前，预期ST戴帽有可能为1。ST戴帽可能为1的时期一般在11月到次年的4月。-描述"},
                {"col_name": "preSTSpd",
                 "col_show_name": "1表示ST股票预期在年报公告日暂停上市，ST股票预期连续三年亏损，0表示不预期暂停上市。ST暂停上市可能为1的时期一般在11月到次年的4月。",
                 "col_comment": "1表示ST股票预期在年报公告日暂停上市，ST股票预期连续三年亏损，0表示不预期暂停上市。ST暂停上市可能为1的时期一般在11月到次年的4月。-描述"},
                {"col_name": "punishMark", "col_show_name": "1表示当天发生重大事项违规处罚，包括对公司及其重要人员的立案调查、市场禁入、判刑，0表示没有重大事项违规处罚。",
                 "col_comment": "1表示当天发生重大事项违规处罚，包括对公司及其重要人员的立案调查、市场禁入、判刑，0表示没有重大事项违规处罚。-描述"},
                {"col_name": "holderNum", "col_show_name": "近期公告中持有A股的股东户总数", "col_comment": "近期公告中持有A股的股东户总数-描述"},
                {"col_name": "avgHoldings", "col_show_name": "总股东除以股东数=户均持股数", "col_comment": "总股东除以股东数=户均持股数-描述"},
                {"col_name": "holderChgPct60", "col_show_name": "股东总数当日和60个交易日前相比的变化率",
                 "col_comment": "股东总数当日和60个交易日前相比的变化率-描述"},
                {"col_name": "instHoldPct", "col_show_name": "机构最近一季度的持股数占总股本比例",
                 "col_comment": "机构最近一季度的持股数占总股本比例-描述"},
                {"col_name": "instHoldLrr", "col_show_name": "机构持股比例最近一季度比上一季度的增长率",
                 "col_comment": "机构持股比例最近一季度比上一季度的增长率-描述"},
                {"col_name": "stateHoldPct", "col_show_name": "汇金、证金及其所属资管计划、5只国家队基金、社保基金、国家部门等加在一起在最近季度的持股数占总股本的比例。",
                 "col_comment": "汇金、证金及其所属资管计划、5只国家队基金、社保基金、国家部门等加在一起在最近季度的持股数占总股本的比例。-描述"},
                {"col_name": "stateHoldLrr", "col_show_name": "国家队持股比例最近一季度比上一季度的增长率。",
                 "col_comment": "国家队持股比例最近一季度比上一季度的增长率。-描述"},
                {"col_name": "socialHoldPct", "col_show_name": "社保基金最近季度持股数占总股本比例。",
                 "col_comment": "社保基金最近季度持股数占总股本比例。-描述"},
                {"col_name": "socialHoldLrr", "col_show_name": "股票社保持股比例最近一季度比上一季度的增长率",
                 "col_comment": "股票社保持股比例最近一季度比上一季度的增长率-描述"},
                {"col_name": "top10HoldPct", "col_show_name": "股票前十大股东持股最近一季度持股比例",
                 "col_comment": "股票前十大股东持股最近一季度持股比例-描述"},
                {"col_name": "top10HoldLrr", "col_show_name": "股票前十大股东持股比例的最近一季度比上一季度的增长率",
                 "col_comment": "股票前十大股东持股比例的最近一季度比上一季度的增长率-描述"}
            ]
        }
    define_json = json.dumps(stockfctindiconeday_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def sectips_define(table_name):

    sectips_str = {
            "table_name": "sectips",
            "table_show_name": "沪深股票今日停复牌",
            "table_comment": "沪深股票今日停复牌-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "证券ID", "col_comment": "证券ID-描述"},
                {"col_name": "ticker", "col_show_name": "交易代码", "col_comment": "交易代码-描述"},
                {"col_name": "exchangeCD", "col_show_name": "交易市场编码", "col_comment": "交易市场编码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "tipsDesc", "col_show_name": "交易提示描述", "col_comment": "交易提示描述-描述"},
                {"col_name": "tipsTypeCD", "col_show_name": "交易提示类型", "col_comment": "交易提示类型-描述"},
                {"col_name": "tipsType", "col_show_name": "交易提示类型中文", "col_comment": "交易提示类型中文-描述"},
                {"col_name": "tradeDate", "col_show_name": "日期", "col_comment": "日期-描述"}
            ]
        }
    define_json = json.dumps(sectips_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def tradecal_define(table_name):

    tradecal_str = {
            "table_name": "tradecal",
            "table_show_name": "交易所交易日历",
            "table_comment": "交易所交易日历-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "exchangeCD", "col_show_name": "证券交易所", "col_comment": "证券交易所-描述"},
                {"col_name": "calendarDate", "col_show_name": "日期", "col_comment": "日期-描述"},
                {"col_name": "isOpen", "col_show_name": "日期当天是否开市。0表示否，1表示是", "col_comment": "日期当天是否开市。0表示否，1表示是-描述"},
                {"col_name": "prevTradeDate", "col_show_name": "当前日期前一交易日", "col_comment": "当前日期前一交易日-描述"},
                {"col_name": "isWeekEnd", "col_show_name": "当前日期是否当周最后交易日。0表示否，1表示是",
                 "col_comment": "当前日期是否当周最后交易日。0表示否，1表示是-描述"},
                {"col_name": "isMonthEnd", "col_show_name": "当前日期是否当月最后交易日。0表示否，1表示是",
                 "col_comment": "当前日期是否当月最后交易日。0表示否，1表示是-描述"},
                {"col_name": "isQuarterEnd", "col_show_name": "当前日期是否当季最后交易日。0表示否，1表示是",
                 "col_comment": "当前日期是否当季最后交易日。0表示否，1表示是-描述"},
                {"col_name": "isYearEnd", "col_show_name": "当前日期是否当年最后交易日。0表示否，1表示是",
                 "col_comment": "当前日期是否当年最后交易日。0表示否，1表示是-描述"}
            ]
        }
    define_json = json.dumps(tradecal_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def workingcal_define(table_name):

    workingcal_str = {
            "table_name": "workingcal",
            "table_show_name": "工作日安排日历",
            "table_comment": "工作日安排日历-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "calendarDate", "col_show_name": "日期", "col_comment": "日期-描述"},
                {"col_name": "isWork", "col_show_name": "是否为工作日", "col_comment": "是否为工作日-描述"},
                {"col_name": "prevWorkDate", "col_show_name": "前一工作日", "col_comment": "前一工作日-描述"},
                {"col_name": "weekStartDate", "col_show_name": "本周开始日", "col_comment": "本周开始日-描述"},
                {"col_name": "weekEndDate", "col_show_name": "本周结束日", "col_comment": "本周结束日-描述"},
                {"col_name": "monthStartDate", "col_show_name": "本月开始日", "col_comment": "本月开始日-描述"},
                {"col_name": "monthEndDate", "col_show_name": "本月结束日", "col_comment": "本月结束日-描述"},
                {"col_name": "quarterStartDate", "col_show_name": "本季开始日", "col_comment": "本季开始日-描述"},
                {"col_name": "quarterEndDate", "col_show_name": "本季结束日", "col_comment": "本季结束日-描述"},
                {"col_name": "yearStartDate", "col_show_name": "本年开始日", "col_comment": "本年开始日-描述"},
                {"col_name": "yearEndDate", "col_show_name": "本年结束日", "col_comment": "本年结束日-描述"},
                {"col_name": "updateTime", "col_show_name": "更新时间", "col_comment": "更新时间-描述"}
            ]
        }
    define_json = json.dumps(workingcal_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def fdmtcfinduttmpit_define(table_name):

    fdmtcfinduttmpit_str = {
            "table_name": "fdmtcfinduttmpit",
            "table_show_name": "一般工商业现金流量表(TTM Point in time)",
            "table_comment": "一般工商业现金流量表(TTM Point in time)-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "证券编码", "col_comment": "证券编码-描述"},
                {"col_name": "partyID", "col_show_name": "机构编码", "col_comment": "机构编码-描述"},
                {"col_name": "ticker", "col_show_name": "证券交易代码", "col_comment": "证券交易代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD",
                 "col_show_name": "通联编制的证券市场编码。XSHG-上海证券交易所；XSHE-深圳证券交易所。对应DataAPI.SysCodeGet.codeTypeID=10002。",
                 "col_comment": "通联编制的证券市场编码。XSHG-上海证券交易所；XSHE-深圳证券交易所。对应DataAPI.SysCodeGet.codeTypeID=10002。-描述"},
                {"col_name": "endDate", "col_show_name": "截止日期", "col_comment": "截止日期-描述"},
                {"col_name": "publishDate", "col_show_name": "证券交易所披露的信息发布日期", "col_comment": "证券交易所披露的信息发布日期-描述"},
                {"col_name": "isNew", "col_show_name": "是否最新。1-是；0-否。对应DataAPI.SysCodeGet.codeTypeID=10007。",
                 "col_comment": "是否最新。1-是；0-否。对应DataAPI.SysCodeGet.codeTypeID=10007。-描述"},
                {"col_name": "isCalc", "col_show_name": "是否计算。1-是；0-否。对应DataAPI.SysCodeGet.codeTypeID=10007。",
                 "col_comment": "是否计算。1-是；0-否。对应DataAPI.SysCodeGet.codeTypeID=10007。-描述"},
                {"col_name": "CFrSaleGS", "col_show_name": "销售商品、提供劳务收到的现金", "col_comment": "销售商品、提供劳务收到的现金-描述"},
                {"col_name": "NDeposIncrCFI", "col_show_name": "客户存款和同业存放款项净增加额", "col_comment": "客户存款和同业存放款项净增加额-描述"},
                {"col_name": "NIncrBorrFrCB", "col_show_name": "向中央银行借款净增加额", "col_comment": "向中央银行借款净增加额-描述"},
                {"col_name": "NIncBorrOthFI", "col_show_name": "向其他金融机构拆入资金净增加额", "col_comment": "向其他金融机构拆入资金净增加额-描述"},
                {"col_name": "premFrOrigContr", "col_show_name": "收到原保险合同保费取得的现金", "col_comment": "收到原保险合同保费取得的现金-描述"},
                {"col_name": "NReinsurPrem", "col_show_name": "收到再保险业务现金净额", "col_comment": "收到再保险业务现金净额-描述"},
                {"col_name": "NIncPhDeposInv", "col_show_name": "保户储金及投资款净增加额", "col_comment": "保户储金及投资款净增加额-描述"},
                {"col_name": "NIncDispTradFA", "col_show_name": "处置交易性金融资产净增加额", "col_comment": "处置交易性金融资产净增加额-描述"},
                {"col_name": "IFCCashIncr", "col_show_name": "收取利息、手续费及佣金的现金", "col_comment": "收取利息、手续费及佣金的现金-描述"},
                {"col_name": "NIncFrBorr", "col_show_name": "拆入资金净增加额", "col_comment": "拆入资金净增加额-描述"},
                {"col_name": "NCApIncrRepur", "col_show_name": "回购业务资金净增加额", "col_comment": "回购业务资金净增加额-描述"},
                {"col_name": "refundOfTax", "col_show_name": "收到的税费返还", "col_comment": "收到的税费返还-描述"},
                {"col_name": "CFrOthOperateA", "col_show_name": "收到其他与经营活动有关的现金", "col_comment": "收到其他与经营活动有关的现金-描述"},
                {"col_name": "CInfFrOperateA", "col_show_name": "经营活动现金流入小计", "col_comment": "经营活动现金流入小计-描述"},
                {"col_name": "CPaidGS", "col_show_name": "购买商品、接受劳务支付的现金", "col_comment": "购买商品、接受劳务支付的现金-描述"},
                {"col_name": "NIncDisburOfLA", "col_show_name": "客户贷款及垫款净增加额", "col_comment": "客户贷款及垫款净增加额-描述"},
                {"col_name": "NIncrDeposInFI", "col_show_name": "存放中央银行和同业款项净增加额", "col_comment": "存放中央银行和同业款项净增加额-描述"},
                {"col_name": "origContrCIndem", "col_show_name": "支付原保险合同赔付款项的现金", "col_comment": "支付原保险合同赔付款项的现金-描述"},
                {"col_name": "CPaidIFC", "col_show_name": "支付利息、手续费及佣金的现金", "col_comment": "支付利息、手续费及佣金的现金-描述"},
                {"col_name": "CPaidPolDiv", "col_show_name": "支付保单红利的现金", "col_comment": "支付保单红利的现金-描述"},
                {"col_name": "CPaidToForEmpl", "col_show_name": "支付给职工以及为职工支付的现金", "col_comment": "支付给职工以及为职工支付的现金-描述"},
                {"col_name": "CPaidForTaxes", "col_show_name": "支付的各项税费", "col_comment": "支付的各项税费-描述"},
                {"col_name": "CPaidForOthOpA", "col_show_name": "支付其他与经营活动有关的现金", "col_comment": "支付其他与经营活动有关的现金-描述"},
                {"col_name": "COutfOperateA", "col_show_name": "经营活动现金流出小计", "col_comment": "经营活动现金流出小计-描述"},
                {"col_name": "NCFOperateA", "col_show_name": "经营活动产生的现金流量净额", "col_comment": "经营活动产生的现金流量净额-描述"},
                {"col_name": "procSellInvest", "col_show_name": "收回投资收到的现金", "col_comment": "收回投资收到的现金-描述"},
                {"col_name": "gainInvest", "col_show_name": "取得投资收益收到的现金", "col_comment": "取得投资收益收到的现金-描述"},
                {"col_name": "dispFixAssetsOth", "col_show_name": "处置固定资产、无形资产和其他长期资产收回的现金净额",
                 "col_comment": "处置固定资产、无形资产和其他长期资产收回的现金净额-描述"},
                {"col_name": "NDispSubsOthBizC", "col_show_name": "处置子公司及其他营业单位收到的现金净额",
                 "col_comment": "处置子公司及其他营业单位收到的现金净额-描述"},
                {"col_name": "CFrOthInvestA", "col_show_name": "收到其他与投资活动有关的现金", "col_comment": "收到其他与投资活动有关的现金-描述"},
                {"col_name": "CInfFrInvestA", "col_show_name": "投资活动现金流入小计", "col_comment": "投资活动现金流入小计-描述"},
                {"col_name": "purFixAssetsOth", "col_show_name": "购建固定资产、无形资产和其他长期资产支付的现金",
                 "col_comment": "购建固定资产、无形资产和其他长期资产支付的现金-描述"},
                {"col_name": "CPaidInvest", "col_show_name": "投资支付的现金", "col_comment": "投资支付的现金-描述"},
                {"col_name": "NIncrPledgeLoan", "col_show_name": "质押贷款净增加额", "col_comment": "质押贷款净增加额-描述"},
                {"col_name": "NCPaidAcquis", "col_show_name": "取得子公司及其他营业单位支付的现金净额",
                 "col_comment": "取得子公司及其他营业单位支付的现金净额-描述"},
                {"col_name": "CPaidOthInvestA", "col_show_name": "支付其他与投资活动有关的现金", "col_comment": "支付其他与投资活动有关的现金-描述"},
                {"col_name": "COutfFrInvestA", "col_show_name": "投资活动现金流出小计", "col_comment": "投资活动现金流出小计-描述"},
                {"col_name": "NCFFrInvestA", "col_show_name": "投资活动产生的现金流量净额", "col_comment": "投资活动产生的现金流量净额-描述"},
                {"col_name": "CFrCapContr", "col_show_name": "吸收投资收到的现金", "col_comment": "吸收投资收到的现金-描述"},
                {"col_name": "CFrMinoSSubs", "col_show_name": "其中:子公司吸收少数股东投资收到的现金",
                 "col_comment": "其中:子公司吸收少数股东投资收到的现金-描述"},
                {"col_name": "CFrBorr", "col_show_name": "取得借款收到的现金", "col_comment": "取得借款收到的现金-描述"},
                {"col_name": "CFrIssueBond", "col_show_name": "发行债券收到的现金", "col_comment": "发行债券收到的现金-描述"},
                {"col_name": "CFrOthFinanA", "col_show_name": "收到其他与筹资活动有关的现金", "col_comment": "收到其他与筹资活动有关的现金-描述"},
                {"col_name": "CInfFrFinanA", "col_show_name": "筹资活动现金流入小计", "col_comment": "筹资活动现金流入小计-描述"},
                {"col_name": "CPaidForDebts", "col_show_name": "偿还债务支付的现金", "col_comment": "偿还债务支付的现金-描述"},
                {"col_name": "CPaidDivProfInt", "col_show_name": "分配股利、利润或偿付利息支付的现金",
                 "col_comment": "分配股利、利润或偿付利息支付的现金-描述"},
                {"col_name": "divProfSubsMinoS", "col_show_name": "其中:子公司支付给少数股东的股利、利润",
                 "col_comment": "其中:子公司支付给少数股东的股利、利润-描述"},
                {"col_name": "CPaidOthFinanA", "col_show_name": "支付其他与筹资活动有关的现金", "col_comment": "支付其他与筹资活动有关的现金-描述"},
                {"col_name": "COutfFrFinanA", "col_show_name": "筹资活动现金流出小计", "col_comment": "筹资活动现金流出小计-描述"},
                {"col_name": "NCFFrFinanA", "col_show_name": "筹资活动产生的现金流量净额", "col_comment": "筹资活动产生的现金流量净额-描述"},
                {"col_name": "forexEffects", "col_show_name": "汇率变动对现金及现金等价物的影响", "col_comment": "汇率变动对现金及现金等价物的影响-描述"},
                {"col_name": "NChangeInCash", "col_show_name": "现金及现金等价物净增加额", "col_comment": "现金及现金等价物净增加额-描述"},
                {"col_name": "NCEBegBal", "col_show_name": "加:期初现金及现金等价物余额", "col_comment": "加:期初现金及现金等价物余额-描述"},
                {"col_name": "NCEEndBal", "col_show_name": "期末现金及现金等价物余额", "col_comment": "期末现金及现金等价物余额-描述"}
            ]
        }
    define_json = json.dumps(fdmtcfinduttmpit_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def fdmtisinduttmpit_define(table_name):

    fdmtisinduttmpit_str = {
            "table_name": "fdmtisinduttmpit",
            "table_show_name": "一般工商业利润表(TTM Point in time)",
            "table_comment": "一般工商业利润表(TTM Point in time)-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "证券编码", "col_comment": "证券编码-描述"},
                {"col_name": "partyID", "col_show_name": "机构编码", "col_comment": "机构编码-描述"},
                {"col_name": "ticker", "col_show_name": "证券交易代码", "col_comment": "证券交易代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD",
                 "col_show_name": "通联编制的证券市场编码。XSHG-上海证券交易所；XSHE-深圳证券交易所。对应DataAPI.SysCodeGet.codeTypeID=10002。",
                 "col_comment": "通联编制的证券市场编码。XSHG-上海证券交易所；XSHE-深圳证券交易所。对应DataAPI.SysCodeGet.codeTypeID=10002。-描述"},
                {"col_name": "endDate", "col_show_name": "截止日期", "col_comment": "截止日期-描述"},
                {"col_name": "publishDate", "col_show_name": "证券交易所披露的信息发布日期", "col_comment": "证券交易所披露的信息发布日期-描述"},
                {"col_name": "isNew", "col_show_name": "是否最新。1-是；0-否。对应DataAPI.SysCodeGet.codeTypeID=10007。",
                 "col_comment": "是否最新。1-是；0-否。对应DataAPI.SysCodeGet.codeTypeID=10007。-描述"},
                {"col_name": "isCalc", "col_show_name": "是否计算。1-是；0-否。对应DataAPI.SysCodeGet.codeTypeID=10007。",
                 "col_comment": "是否计算。1-是；0-否。对应DataAPI.SysCodeGet.codeTypeID=10007。-描述"},
                {"col_name": "tRevenue", "col_show_name": "营业总收入", "col_comment": "营业总收入-描述"},
                {"col_name": "revenue", "col_show_name": "营业收入", "col_comment": "营业收入-描述"},
                {"col_name": "intIncome", "col_show_name": "利息收入", "col_comment": "利息收入-描述"},
                {"col_name": "premEarned", "col_show_name": "已赚保费", "col_comment": "已赚保费-描述"},
                {"col_name": "commisIncome", "col_show_name": "手续费及佣金收入", "col_comment": "手续费及佣金收入-描述"},
                {"col_name": "TCogs", "col_show_name": "营业总成本", "col_comment": "营业总成本-描述"},
                {"col_name": "COGS", "col_show_name": "营业成本", "col_comment": "营业成本-描述"},
                {"col_name": "intExp", "col_show_name": "利息支出", "col_comment": "利息支出-描述"},
                {"col_name": "commisExp", "col_show_name": "手续费及佣金支出", "col_comment": "手续费及佣金支出-描述"},
                {"col_name": "premRefund", "col_show_name": "退保金", "col_comment": "退保金-描述"},
                {"col_name": "NCompensPayout", "col_show_name": "赔付支出净额", "col_comment": "赔付支出净额-描述"},
                {"col_name": "reserInsurContr", "col_show_name": "提取保险合同准备金净额", "col_comment": "提取保险合同准备金净额-描述"},
                {"col_name": "policyDivPayt", "col_show_name": "保单红利支出", "col_comment": "保单红利支出-描述"},
                {"col_name": "reinsurExp", "col_show_name": "分保费用", "col_comment": "分保费用-描述"},
                {"col_name": "bizTaxSurchg", "col_show_name": "营业税金及附加", "col_comment": "营业税金及附加-描述"},
                {"col_name": "sellExp", "col_show_name": "销售费用", "col_comment": "销售费用-描述"},
                {"col_name": "adminExp", "col_show_name": "管理费用", "col_comment": "管理费用-描述"},
                {"col_name": "finanExp", "col_show_name": "财务费用", "col_comment": "财务费用-描述"},
                {"col_name": "assetsImpairLoss", "col_show_name": "资产减值损失", "col_comment": "资产减值损失-描述"},
                {"col_name": "fValueChgGain", "col_show_name": "公允价值变动收益", "col_comment": "公允价值变动收益-描述"},
                {"col_name": "investIncome", "col_show_name": "投资收益", "col_comment": "投资收益-描述"},
                {"col_name": "AJInvestIncome", "col_show_name": "其中:对联营企业和合营企业的投资收益",
                 "col_comment": "其中:对联营企业和合营企业的投资收益-描述"},
                {"col_name": "forexGain", "col_show_name": "汇兑收益", "col_comment": "汇兑收益-描述"},
                {"col_name": "assetsDispGain", "col_show_name": "资产处置收益", "col_comment": "资产处置收益-描述"},
                {"col_name": "othGain", "col_show_name": "其他收益", "col_comment": "其他收益-描述"},
                {"col_name": "operateProfit", "col_show_name": "营业利润", "col_comment": "营业利润-描述"},
                {"col_name": "NoperateIncome", "col_show_name": "营业外收入", "col_comment": "营业外收入-描述"},
                {"col_name": "NoperateExp", "col_show_name": "营业外支出", "col_comment": "营业外支出-描述"},
                {"col_name": "NCADisploss", "col_show_name": "非流动资产处置损失", "col_comment": "非流动资产处置损失-描述"},
                {"col_name": "TProfit", "col_show_name": "利润总额", "col_comment": "利润总额-描述"},
                {"col_name": "incomeTax", "col_show_name": "所得税费用", "col_comment": "所得税费用-描述"},
                {"col_name": "NIncome", "col_show_name": "净利润", "col_comment": "净利润-描述"},
                {"col_name": "goingConcernNI", "col_show_name": "持续经营净利润", "col_comment": "持续经营净利润-描述"},
                {"col_name": "quitConcernNI", "col_show_name": "终止经营净利润", "col_comment": "终止经营净利润-描述"},
                {"col_name": "NIncomeAttrP", "col_show_name": "归属于母公司所有者的净利润", "col_comment": "归属于母公司所有者的净利润-描述"},
                {"col_name": "minorityGain", "col_show_name": "少数股东损益", "col_comment": "少数股东损益-描述"},
                {"col_name": "othComprIncome", "col_show_name": "其他综合收益", "col_comment": "其他综合收益-描述"},
                {"col_name": "TComprIncome", "col_show_name": "综合收益总额", "col_comment": "综合收益总额-描述"},
                {"col_name": "comprIncAttrP", "col_show_name": "归属于母公司所有者的综合收益总额",
                 "col_comment": "归属于母公司所有者的综合收益总额-描述"},
                {"col_name": "comprIncAttrMS", "col_show_name": "归属于少数股东的综合收益总额", "col_comment": "归属于少数股东的综合收益总额-描述"}
            ]
        }
    define_json = json.dumps(fdmtisinduttmpit_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def mktequwadjaf_define(table_name):

    mktequwadjaf_str = {
            "table_name": "mktequwadjaf",
            "table_show_name": "股票周后复权行情",
            "table_comment": "股票周后复权行情-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "通联编制的证券编码，可使用DataAPI.SecIDGet获取",
                 "col_comment": "通联编制的证券编码，可使用DataAPI.SecIDGet获取-描述"},
                {"col_name": "ticker", "col_show_name": "通用交易代码", "col_comment": "通用交易代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD", "col_show_name": "通联编制的交易市场编码", "col_comment": "通联编制的交易市场编码-描述"},
                {"col_name": "weekBeginDate", "col_show_name": "当周首个交易日", "col_comment": "当周首个交易日-描述"},
                {"col_name": "endDate", "col_show_name": "当周最后一个交易日", "col_comment": "当周最后一个交易日-描述"},
                {"col_name": "tradeDays", "col_show_name": "期间有交易的天数", "col_comment": "期间有交易的天数-描述"},
                {"col_name": "preClosePrice", "col_show_name": "上周收盘价", "col_comment": "上周收盘价-描述"},
                {"col_name": "openPrice", "col_show_name": "当周开盘价", "col_comment": "当周开盘价-描述"},
                {"col_name": "highestPrice", "col_show_name": "当周最高价", "col_comment": "当周最高价-描述"},
                {"col_name": "lowestPrice", "col_show_name": "当周最低价", "col_comment": "当周最低价-描述"},
                {"col_name": "closePrice", "col_show_name": "当周收盘价", "col_comment": "当周收盘价-描述"},
                {"col_name": "turnoverVol", "col_show_name": "周成交量，期间成交量求和", "col_comment": "周成交量，期间成交量求和-描述"},
                {"col_name": "turnoverValue", "col_show_name": "周成交金额，期间成交金额求和", "col_comment": "周成交金额，期间成交金额求和-描述"},
                {"col_name": "chg", "col_show_name": "当周涨跌，当周收盘价-当周前收盘价", "col_comment": "当周涨跌，当周收盘价-当周前收盘价-描述"},
                {"col_name": "chgPct", "col_show_name": "当周涨跌幅，当周收盘价/当周前收盘价-1",
                 "col_comment": "当周涨跌幅，当周收盘价/当周前收盘价-1-描述"},
                {"col_name": "return", "col_show_name": "周回报率，期间复合收益率", "col_comment": "周回报率，期间复合收益率-描述"},
                {"col_name": "turnoverRate", "col_show_name": "周累计换手率，期间换手率求和", "col_comment": "周累计换手率，期间换手率求和-描述"},
                {"col_name": "avgTurnoverRate", "col_show_name": "当周平均换手率", "col_comment": "当周平均换手率-描述"},
                {"col_name": "varReturn100", "col_show_name": "近100个周回报率的方差", "col_comment": "近100个周回报率的方差-描述"},
                {"col_name": "sdReturn100", "col_show_name": "近100个周回报率的标准差", "col_comment": "近100个周回报率的标准差-描述"},
                {"col_name": "avgReturn100", "col_show_name": "近100周的平均周回报率", "col_comment": "近100周的平均周回报率-描述"}
            ]
        }
    define_json = json.dumps(mktequwadjaf_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def mktequmadjaf_define(table_name):

    mktequmadjaf_str = {
            "table_name": "mktequmadjaf",
            "table_show_name": "股票月后复权行情",
            "table_comment": "股票月后复权行情-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "通联编制的证券编码， 可使用DataAPI.SecIDGet接口获取到",
                 "col_comment": "通联编制的证券编码， 可使用DataAPI.SecIDGet接口获取到-描述"},
                {"col_name": "ticker", "col_show_name": "通用交易代码", "col_comment": "通用交易代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD", "col_show_name": "通联编制的交易市场编码", "col_comment": "通联编制的交易市场编码-描述"},
                {"col_name": "monthBeginDate", "col_show_name": "当月首个交易日", "col_comment": "当月首个交易日-描述"},
                {"col_name": "endDate", "col_show_name": "当月最后一个交易日", "col_comment": "当月最后一个交易日-描述"},
                {"col_name": "tradeDays", "col_show_name": "期间有交易的天数", "col_comment": "期间有交易的天数-描述"},
                {"col_name": "preClosePrice", "col_show_name": "上月收盘价", "col_comment": "上月收盘价-描述"},
                {"col_name": "openPrice", "col_show_name": "当月开盘价", "col_comment": "当月开盘价-描述"},
                {"col_name": "highestPrice", "col_show_name": "当月最高价", "col_comment": "当月最高价-描述"},
                {"col_name": "lowestPrice", "col_show_name": "当月最低价", "col_comment": "当月最低价-描述"},
                {"col_name": "closePrice", "col_show_name": "当月收盘价", "col_comment": "当月收盘价-描述"},
                {"col_name": "turnoverVol", "col_show_name": "月成交量，期间成交量求和", "col_comment": "月成交量，期间成交量求和-描述"},
                {"col_name": "turnoverValue", "col_show_name": "月成交金额，期间成交金额求和", "col_comment": "月成交金额，期间成交金额求和-描述"},
                {"col_name": "chg", "col_show_name": "当月涨跌，当月收盘价-当月前收盘价", "col_comment": "当月涨跌，当月收盘价-当月前收盘价-描述"},
                {"col_name": "chgPct", "col_show_name": "当月涨跌幅，当月收盘价/当月前收盘价-1",
                 "col_comment": "当月涨跌幅，当月收盘价/当月前收盘价-1-描述"},
                {"col_name": "return", "col_show_name": "月回报率，期间复合收益率", "col_comment": "月回报率，期间复合收益率-描述"},
                {"col_name": "turnoverRate", "col_show_name": "月累计换手率，期间换手率求和", "col_comment": "月累计换手率，期间换手率求和-描述"},
                {"col_name": "avgTurnoverRate", "col_show_name": "当月平均换手率", "col_comment": "当月平均换手率-描述"},
                {"col_name": "varReturn24", "col_show_name": "近24个月回报率的方差", "col_comment": "近24个月回报率的方差-描述"},
                {"col_name": "sdReturn24", "col_show_name": "近24个月回报率的标准差", "col_comment": "近24个月回报率的标准差-描述"},
                {"col_name": "avgReturn24", "col_show_name": "近24个月的平均月回报率", "col_comment": "近24个月的平均月回报率-描述"},
                {"col_name": "varReturn60", "col_show_name": "近60个月回报率的方差", "col_comment": "近60个月回报率的方差-描述"},
                {"col_name": "sdReturn60", "col_show_name": "近60个月回报率的标准差", "col_comment": "近60个月回报率的标准差-描述"},
                {"col_name": "avgReturn60", "col_show_name": "近60个月的平均月回报率", "col_comment": "近60个月的平均月回报率-描述"}
            ]
        }
    define_json = json.dumps(mktequmadjaf_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def mktequqadjaf_define(table_name):

    mktequqadjaf_str = {
            "table_name": "mktequqadjaf",
            "table_show_name": "股票季后复权行情",
            "table_comment": "股票季后复权行情-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "通联编制的证券编码， 可使用DataAPI.SecIDGet接口获取到",
                 "col_comment": "通联编制的证券编码， 可使用DataAPI.SecIDGet接口获取到-描述"},
                {"col_name": "ticker", "col_show_name": "通用交易代码", "col_comment": "通用交易代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD", "col_show_name": "通联编制的交易市场编码", "col_comment": "通联编制的交易市场编码-描述"},
                {"col_name": "endDate", "col_show_name": "年最后交易日", "col_comment": "年最后交易日-描述"},
                {"col_name": "tradeDays", "col_show_name": "期间有交易的天数", "col_comment": "期间有交易的天数-描述"},
                {"col_name": "preClosePrice", "col_show_name": "年前收盘价", "col_comment": "年前收盘价-描述"},
                {"col_name": "openPrice", "col_show_name": "年开盘价", "col_comment": "年开盘价-描述"},
                {"col_name": "highestPrice", "col_show_name": "年最高价", "col_comment": "年最高价-描述"},
                {"col_name": "lowestPrice", "col_show_name": "年最低价", "col_comment": "年最低价-描述"},
                {"col_name": "closePrice", "col_show_name": "年收盘价", "col_comment": "年收盘价-描述"},
                {"col_name": "turnoverVol", "col_show_name": "年成交量，期间成交量求和", "col_comment": "年成交量，期间成交量求和-描述"},
                {"col_name": "turnoverValue", "col_show_name": "年成交金额，期间成交金额求和", "col_comment": "年成交金额，期间成交金额求和-描述"},
                {"col_name": "chg", "col_show_name": "年涨跌，年收盘价-年前收盘价", "col_comment": "年涨跌，年收盘价-年前收盘价-描述"},
                {"col_name": "chgPct", "col_show_name": "年涨跌幅，年收盘价/年前收盘价-1", "col_comment": "年涨跌幅，年收盘价/年前收盘价-1-描述"}
            ]
        }
    define_json = json.dumps(mktequqadjaf_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def mktequaadjaf_define(table_name):

    mktequaadjaf_str = {
            "table_name": "mktequaadjaf",
            "table_show_name": "股票年后复权行情",
            "table_comment": "股票年后复权行情-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "通联编制的证券编码， 可使用DataAPI.SecIDGet接口获取到",
                 "col_comment": "通联编制的证券编码， 可使用DataAPI.SecIDGet接口获取到-描述"},
                {"col_name": "ticker", "col_show_name": "通用交易代码", "col_comment": "通用交易代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD", "col_show_name": "通联编制的交易市场编码", "col_comment": "通联编制的交易市场编码-描述"},
                {"col_name": "endDate", "col_show_name": "年最后交易日", "col_comment": "年最后交易日-描述"},
                {"col_name": "tradeDays", "col_show_name": "期间有交易的天数", "col_comment": "期间有交易的天数-描述"},
                {"col_name": "preClosePrice", "col_show_name": "年前收盘价", "col_comment": "年前收盘价-描述"},
                {"col_name": "openPrice", "col_show_name": "年开盘价", "col_comment": "年开盘价-描述"},
                {"col_name": "highestPrice", "col_show_name": "年最高价", "col_comment": "年最高价-描述"},
                {"col_name": "lowestPrice", "col_show_name": "年最低价", "col_comment": "年最低价-描述"},
                {"col_name": "closePrice", "col_show_name": "年收盘价", "col_comment": "年收盘价-描述"},
                {"col_name": "turnoverVol", "col_show_name": "年成交量，期间成交量求和", "col_comment": "年成交量，期间成交量求和-描述"},
                {"col_name": "turnoverValue", "col_show_name": "年成交金额，期间成交金额求和", "col_comment": "年成交金额，期间成交金额求和-描述"},
                {"col_name": "chg", "col_show_name": "年涨跌，年收盘价-年前收盘价", "col_comment": "年涨跌，年收盘价-年前收盘价-描述"},
                {"col_name": "chgPct", "col_show_name": "年涨跌幅，年收盘价/年前收盘价-1", "col_comment": "年涨跌幅，年收盘价/年前收盘价-1-描述"}
            ]
        }
    define_json = json.dumps(mktequaadjaf_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


def mktequsadjaf_define(table_name):

    mktequsadjaf_str = {
            "table_name": "mktequsadjaf",
            "table_show_name": "股票半年后复权行情",
            "table_comment": "股票半年后复权行情-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID", "col_show_name": "通联编制的证券编码， 可使用DataAPI.SecIDGet接口获取到",
                 "col_comment": "通联编制的证券编码， 可使用DataAPI.SecIDGet接口获取到-描述"},
                {"col_name": "ticker", "col_show_name": "通用交易代码", "col_comment": "通用交易代码-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD", "col_show_name": "通联编制的交易市场编码", "col_comment": "通联编制的交易市场编码-描述"},
                {"col_name": "endDate", "col_show_name": "半年最后交易日", "col_comment": "半年最后交易日-描述"},
                {"col_name": "tradeDays", "col_show_name": "期间有交易的天数", "col_comment": "期间有交易的天数-描述"},
                {"col_name": "preClosePrice", "col_show_name": "半年前收盘价", "col_comment": "半年前收盘价-描述"},
                {"col_name": "openPrice", "col_show_name": "半年开盘价", "col_comment": "半年开盘价-描述"},
                {"col_name": "highestPrice", "col_show_name": "半年最高价", "col_comment": "半年最高价-描述"},
                {"col_name": "lowestPrice", "col_show_name": "半年最低价", "col_comment": "半年最低价-描述"},
                {"col_name": "closePrice", "col_show_name": "半年收盘价", "col_comment": "半年收盘价-描述"},
                {"col_name": "turnoverVol", "col_show_name": "半年成交量，期间成交量求和", "col_comment": "半年成交量，期间成交量求和-描述"},
                {"col_name": "turnoverValue", "col_show_name": "半年成交金额，期间成交金额求和", "col_comment": "半年成交金额，期间成交金额求和-描述"},
                {"col_name": "chg", "col_show_name": "半年涨跌，半年收盘价-半年前收盘价", "col_comment": "半年涨跌，半年收盘价-半年前收盘价-描述"},
                {"col_name": "chgPct", "col_show_name": "半年涨跌幅，半年收盘价/半年前收盘价-1",
                 "col_comment": "半年涨跌幅，半年收盘价/半年前收盘价-1-描述"}
            ]
        }
    define_json = json.dumps(mktequsadjaf_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


# 备注: 该表比通联数据字典少了个字段"actpubtime"
def fdmtmaindatapit_define(table_name):

    fdmtmaindatapit_str = {
            "table_name": "fdmtmaindatapit",
            "table_show_name": "财务指标（新）",
            "table_comment": "财务指标（新）-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID",
                 "col_show_name": "通联编制的证券编码，格式是“交易代码.证券市场代码”，如000002.XSHE。可传入证券交易代码使用getSecID接口获取到。",
                 "col_comment": "通联编制的证券编码，格式是“交易代码.证券市场代码”，如000002.XSHE。可传入证券交易代码使用getSecID接口获取到。-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD", "col_show_name": "通联编制的交易市场编码", "col_comment": "通联编制的交易市场编码-描述"},
                {"col_name": "ticker", "col_show_name": "证券在证券市场通用的交易代码。", "col_comment": "证券在证券市场通用的交易代码。-描述"},
                {"col_name": "partyID", "col_show_name": "机构ID", "col_comment": "机构ID-描述"},
                {"col_name": "publishDate", "col_show_name": "发布日期", "col_comment": "发布日期-描述"},
                {"col_name": "endDateRep", "col_show_name": "报告截止日期", "col_comment": "报告截止日期-描述"},
                {"col_name": "endDate", "col_show_name": "截止日期", "col_comment": "截止日期-描述"},
                {"col_name": "isNew", "col_show_name": "end_date是否为最新数据，是为1，否为0",
                 "col_comment": "end_date是否为最新数据，是为1，否为0-描述"},
                {"col_name": "reportType", "col_show_name": "Q1:一季报, S:半年报, Q3:三季报 , A:年报",
                 "col_comment": "Q1:一季报, S:半年报, Q3:三季报 , A:年报-描述"},
                {"col_name": "mergedFlag", "col_show_name": "1是合并，2是母公司", "col_comment": "1是合并，2是母公司-描述"},
                {"col_name": "fiscalPeriod", "col_show_name": "会计区间长度", "col_comment": "会计区间长度-描述"},
                {"col_name": "tFixedAssets", "col_show_name": "固定资产合计", "col_comment": "固定资产合计-描述"},
                {"col_name": "intFreeCl", "col_show_name": "无息流动负债", "col_comment": "无息流动负债-描述"},
                {"col_name": "intFreeNcl", "col_show_name": "无息非流动负债", "col_comment": "无息非流动负债-描述"},
                {"col_name": "intCl", "col_show_name": "带息流动负债", "col_comment": "带息流动负债-描述"},
                {"col_name": "intDebt", "col_show_name": "带息债务", "col_comment": "带息债务-描述"},
                {"col_name": "nDebt", "col_show_name": "净债务", "col_comment": "净债务-描述"},
                {"col_name": "nTanAssets", "col_show_name": "有形净资产", "col_comment": "有形净资产-描述"},
                {"col_name": "workCapital", "col_show_name": "营运资本", "col_comment": "营运资本-描述"},
                {"col_name": "nWorkCapital", "col_show_name": "净营运资本", "col_comment": "净营运资本-描述"},
                {"col_name": "ic", "col_show_name": "投入资本", "col_comment": "投入资本-描述"},
                {"col_name": "tRe", "col_show_name": "留存收益", "col_comment": "留存收益-描述"},
                {"col_name": "grossProfit", "col_show_name": "毛利", "col_comment": "毛利-描述"},
                {"col_name": "opaProfit", "col_show_name": "经营活动净收益", "col_comment": "经营活动净收益-描述"},
                {"col_name": "valChgProfit", "col_show_name": "价值变动净收益", "col_comment": "价值变动净收益-描述"},
                {"col_name": "nIntExp", "col_show_name": "净利息费用", "col_comment": "净利息费用-描述"},
                {"col_name": "ebit", "col_show_name": "息税前利润", "col_comment": "息税前利润-描述"},
                {"col_name": "ebitda", "col_show_name": "息税折旧摊销前利润", "col_comment": "息税折旧摊销前利润-描述"},
                {"col_name": "ebiat", "col_show_name": "息前税后利润", "col_comment": "息前税后利润-描述"},
                {"col_name": "nrProfitLoss", "col_show_name": "非经常性损益", "col_comment": "非经常性损益-描述"},
                {"col_name": "niAttrPCut", "col_show_name": "扣除非经常性损益后的归属于上市公司股东的净利润",
                 "col_comment": "扣除非经常性损益后的归属于上市公司股东的净利润-描述"},
                {"col_name": "fcff", "col_show_name": "企业自由现金流量", "col_comment": "企业自由现金流量-描述"},
                {"col_name": "fcfe", "col_show_name": "股权自由现金流量", "col_comment": "股权自由现金流量-描述"},
                {"col_name": "da", "col_show_name": "折旧与摊销", "col_comment": "折旧与摊销-描述"},
                {"col_name": "rd", "col_show_name": "研发支出合计", "col_comment": "研发支出合计-描述"},
                {"col_name": "rdENiAttrPCut", "col_show_name": "研发支出前利润", "col_comment": "研发支出前利润-描述"},
                {"col_name": "eps", "col_show_name": "每股收益(期末摊薄)", "col_comment": "每股收益(期末摊薄)-描述"},
                {"col_name": "epsCut", "col_show_name": "扣除每股收益(期末摊薄)", "col_comment": "扣除每股收益(期末摊薄)-描述"},
                {"col_name": "basicEps", "col_show_name": "基本每股收益", "col_comment": "基本每股收益-描述"},
                {"col_name": "dilutedEps", "col_show_name": "稀释每股收益", "col_comment": "稀释每股收益-描述"},
                {"col_name": "basicEpsCut", "col_show_name": "扣除基本每股收益", "col_comment": "扣除基本每股收益-描述"},
                {"col_name": "dilutedEpsCut", "col_show_name": "扣除稀释每股收益", "col_comment": "扣除稀释每股收益-描述"},
                {"col_name": "nAssetPs", "col_show_name": "每股净资产", "col_comment": "每股净资产-描述"},
                {"col_name": "tRevPs", "col_show_name": "每股营业总收入", "col_comment": "每股营业总收入-描述"},
                {"col_name": "revPs", "col_show_name": "每股营业收入", "col_comment": "每股营业收入-描述"},
                {"col_name": "opPs", "col_show_name": "每股营业利润", "col_comment": "每股营业利润-描述"},
                {"col_name": "ebitPs", "col_show_name": "每股息税前利润", "col_comment": "每股息税前利润-描述"},
                {"col_name": "ebitdaPs", "col_show_name": "每股EBITDA", "col_comment": "每股EBITDA-描述"},
                {"col_name": "cReserPs", "col_show_name": "每股资本公积", "col_comment": "每股资本公积-描述"},
                {"col_name": "sReserPs", "col_show_name": "每股盈余公积", "col_comment": "每股盈余公积-描述"},
                {"col_name": "reserPs", "col_show_name": "每股公积金", "col_comment": "每股公积金-描述"},
                {"col_name": "rePs", "col_show_name": "每股未分配利润", "col_comment": "每股未分配利润-描述"},
                {"col_name": "tRePs", "col_show_name": "每股留存收益", "col_comment": "每股留存收益-描述"},
                {"col_name": "nCFOperAPs", "col_show_name": "每股经营活动产生的现金流量净额", "col_comment": "每股经营活动产生的现金流量净额-描述"},
                {"col_name": "nCInCashPs", "col_show_name": "每股现金流量净额", "col_comment": "每股现金流量净额-描述"},
                {"col_name": "fcffPs", "col_show_name": "每股企业自由现金流量", "col_comment": "每股企业自由现金流量-描述"},
                {"col_name": "fcfePs", "col_show_name": "每股股东自由现金流量", "col_comment": "每股股东自由现金流量-描述"},
                {"col_name": "grossMargin", "col_show_name": "销售毛利率", "col_comment": "销售毛利率-描述"},
                {"col_name": "npMargin", "col_show_name": "销售净利润率", "col_comment": "销售净利润率-描述"},
                {"col_name": "scRatio", "col_show_name": "销售成本率", "col_comment": "销售成本率-描述"},
                {"col_name": "periodExpTr", "col_show_name": "销售期间费用率", "col_comment": "销售期间费用率-描述"},
                {"col_name": "pCostExp", "col_show_name": "成本费用利润率", "col_comment": "成本费用利润率-描述"},
                {"col_name": "roe", "col_show_name": "净资产收益率(摊薄)", "col_comment": "净资产收益率(摊薄)-描述"},
                {"col_name": "roeA", "col_show_name": "净资产收益率(平均)", "col_comment": "净资产收益率(平均)-描述"},
                {"col_name": "roeW", "col_show_name": "净资产收益率(加权平均)", "col_comment": "净资产收益率(加权平均)-描述"},
                {"col_name": "roeCut", "col_show_name": "净资产收益率(扣除摊薄)", "col_comment": "净资产收益率(扣除摊薄)-描述"},
                {"col_name": "roeCutA", "col_show_name": "净资产收益率ROE(扣除平均)", "col_comment": "净资产收益率ROE(扣除平均)-描述"},
                {"col_name": "roeCutW", "col_show_name": "净资产收益率(扣除加权平均)", "col_comment": "净资产收益率(扣除加权平均)-描述"},
                {"col_name": "roa", "col_show_name": "总资产净利率", "col_comment": "总资产净利率-描述"},
                {"col_name": "roaEbit", "col_show_name": "总资产报酬率", "col_comment": "总资产报酬率-描述"},
                {"col_name": "roic", "col_show_name": "投入资本回报率", "col_comment": "投入资本回报率-描述"},
                {"col_name": "rop", "col_show_name": "人力投入回报率ROP", "col_comment": "人力投入回报率ROP-描述"},
                {"col_name": "faTurnover", "col_show_name": "固定资产周转率", "col_comment": "固定资产周转率-描述"},
                {"col_name": "dayFa", "col_show_name": "固定资产周转天数", "col_comment": "固定资产周转天数-描述"},
                {"col_name": "tfaTurnover", "col_show_name": "固定资产合计周转率", "col_comment": "固定资产合计周转率-描述"},
                {"col_name": "dayTfa", "col_show_name": "固定资产合计周转天数", "col_comment": "固定资产合计周转天数-描述"},
                {"col_name": "caTurnover", "col_show_name": "流动资产周转率", "col_comment": "流动资产周转率-描述"},
                {"col_name": "ncaTurnover", "col_show_name": "非流动资产周转率", "col_comment": "非流动资产周转率-描述"},
                {"col_name": "taTurnover", "col_show_name": "总资产周转率", "col_comment": "总资产周转率-描述"},
                {"col_name": "invenTurnover", "col_show_name": "存货周转率", "col_comment": "存货周转率-描述"},
                {"col_name": "daysInven", "col_show_name": "存货周转天数", "col_comment": "存货周转天数-描述"},
                {"col_name": "nrArTurnover", "col_show_name": "应收票据及应收账款周转率", "col_comment": "应收票据及应收账款周转率-描述"},
                {"col_name": "daysNrAr", "col_show_name": "应收票据及应收账款周转天数", "col_comment": "应收票据及应收账款周转天数-描述"},
                {"col_name": "arTurnover", "col_show_name": "应收账款周转率", "col_comment": "应收账款周转率-描述"},
                {"col_name": "daysAr", "col_show_name": "应收账款周转天数", "col_comment": "应收账款周转天数-描述"},
                {"col_name": "npApTurnover", "col_show_name": "应付票据及应付账款周转率", "col_comment": "应付票据及应付账款周转率-描述"},
                {"col_name": "daysNpAp", "col_show_name": "应付票据及应付账款周转天数", "col_comment": "应付票据及应付账款周转天数-描述"},
                {"col_name": "apTurnover", "col_show_name": "应付账款周转率", "col_comment": "应付账款周转率-描述"},
                {"col_name": "daysAp", "col_show_name": "应付账款周转天数", "col_comment": "应付账款周转天数-描述"},
                {"col_name": "workCapitalTurnover", "col_show_name": "营运资本周转率", "col_comment": "营运资本周转率-描述"},
                {"col_name": "daysWorkCapital", "col_show_name": "营运资本周转天数", "col_comment": "营运资本周转天数-描述"},
                {"col_name": "nWorkCapitalTurnover", "col_show_name": "净营运资本周转率", "col_comment": "净营运资本周转率-描述"},
                {"col_name": "daysWorkCapital2018", "col_show_name": "净营运资本周转天数", "col_comment": "净营运资本周转天数-描述"},
                {"col_name": "operCycle", "col_show_name": "营业周期", "col_comment": "营业周期-描述"},
                {"col_name": "nOperCycle", "col_show_name": "净营业周期", "col_comment": "净营业周期-描述"},
                {"col_name": "currentRatio", "col_show_name": "流动比率", "col_comment": "流动比率-描述"},
                {"col_name": "quickRatio", "col_show_name": "速动比率", "col_comment": "速动比率-描述"},
                {"col_name": "squickRatio", "col_show_name": "保守速动比率", "col_comment": "保守速动比率-描述"},
                {"col_name": "opCl", "col_show_name": "营业利润/流动负债", "col_comment": "营业利润/流动负债-描述"},
                {"col_name": "opTl", "col_show_name": "营业利润/负债合计", "col_comment": "营业利润/负债合计-描述"},
                {"col_name": "assetLiabRatio", "col_show_name": "资产负债率", "col_comment": "资产负债率-描述"},
                {"col_name": "equityRatio", "col_show_name": "产权比率", "col_comment": "产权比率-描述"},
                {"col_name": "tlTeap", "col_show_name": "负债合计/归属于母公司的股东权益", "col_comment": "负债合计/归属于母公司的股东权益-描述"},
                {"col_name": "teapTl", "col_show_name": "股东权益对负债比率", "col_comment": "股东权益对负债比率-描述"},
                {"col_name": "teapID", "col_show_name": "归属于母公司的股东权益/带息债务", "col_comment": "归属于母公司的股东权益/带息债务-描述"},
                {"col_name": "nTanATl", "col_show_name": "有形净资产/负债合计", "col_comment": "有形净资产/负债合计-描述"},
                {"col_name": "nTanAID", "col_show_name": "有形净资产/带息债务", "col_comment": "有形净资产/带息债务-描述"},
                {"col_name": "nTanANd", "col_show_name": "有形净资产/净债务", "col_comment": "有形净资产/净债务-描述"},
                {"col_name": "ebitdaTl", "col_show_name": "息税折旧摊销前利润/负债合计", "col_comment": "息税折旧摊销前利润/负债合计-描述"},
                {"col_name": "ebitdaID", "col_show_name": "息税折旧摊销前利润/带息债务", "col_comment": "息税折旧摊销前利润/带息债务-描述"},
                {"col_name": "cashIcl", "col_show_name": "货币资金/带息流动负债", "col_comment": "货币资金/带息流动负债-描述"},
                {"col_name": "cashCl", "col_show_name": "货币资金/流动负债", "col_comment": "货币资金/流动负债-描述"},
                {"col_name": "nCFOpaCl", "col_show_name": "经营活动现金流量净额/流动负债", "col_comment": "经营活动现金流量净额/流动负债-描述"},
                {"col_name": "nCFOpaLiab", "col_show_name": "经营活动现金流量净额/负债合计", "col_comment": "经营活动现金流量净额/负债合计-描述"},
                {"col_name": "nCFOpaID", "col_show_name": "经营活动现金流量净额/带息债务", "col_comment": "经营活动现金流量净额/带息债务-描述"},
                {"col_name": "nCFOpaNd", "col_show_name": "经营活动现金流量净额/净债务", "col_comment": "经营活动现金流量净额/净债务-描述"},
                {"col_name": "nCFOpaNcl", "col_show_name": "经营活动现金流量净额/非流动负债", "col_comment": "经营活动现金流量净额/非流动负债-描述"},
                {"col_name": "nCFNfaCl", "col_show_name": "非筹资性现金流量净额/流动负债", "col_comment": "非筹资性现金流量净额/流动负债-描述"},
                {"col_name": "nCFNfaLiab", "col_show_name": "非筹资性现金流量净额/负债总额", "col_comment": "非筹资性现金流量净额/负债总额-描述"},
                {"col_name": "nclWc", "col_show_name": "非流动负债与营运资金比率", "col_comment": "非流动负债与营运资金比率-描述"},
                {"col_name": "timesInteEbit", "col_show_name": "EBIT利息保障倍数", "col_comment": "EBIT利息保障倍数-描述"},
                {"col_name": "timesInteEbitda", "col_show_name": "EBITDA利息保障倍数", "col_comment": "EBITDA利息保障倍数-描述"},
                {"col_name": "timesInteCF", "col_show_name": "现金流量利息保障倍数", "col_comment": "现金流量利息保障倍数-描述"},
                {"col_name": "cashRatio", "col_show_name": "现金比率", "col_comment": "现金比率-描述"},
                {"col_name": "nCFOpaDebtDue", "col_show_name": "现金到期债务比", "col_comment": "现金到期债务比-描述"},
                {"col_name": "ltLiabRatio", "col_show_name": "长期负债占比", "col_comment": "长期负债占比-描述"},
                {"col_name": "nrArRecR", "col_show_name": "应收票据及应收账款回款率", "col_comment": "应收票据及应收账款回款率-描述"},
                {"col_name": "nrArR", "col_show_name": "应收票据及应收账款/营业收入", "col_comment": "应收票据及应收账款/营业收入-描述"},
                {"col_name": "arRecR", "col_show_name": "应收账款回款率", "col_comment": "应收账款回款率-描述"},
                {"col_name": "arR", "col_show_name": "应收账款/营业收入", "col_comment": "应收账款/营业收入-描述"},
                {"col_name": "advRR", "col_show_name": "预收款项/营业收入", "col_comment": "预收款项/营业收入-描述"},
                {"col_name": "cfsgsR", "col_show_name": "销售商品提供劳务收到的现金/营业收入", "col_comment": "销售商品提供劳务收到的现金/营业收入-描述"},
                {"col_name": "nCFOpaTr", "col_show_name": "经营活动产生的现金流量净额/营业总收入",
                 "col_comment": "经营活动产生的现金流量净额/营业总收入-描述"},
                {"col_name": "nCFOpaR", "col_show_name": "经营活动产生的现金流量净额/营业收入", "col_comment": "经营活动产生的现金流量净额/营业收入-描述"},
                {"col_name": "nCFOpaOpap", "col_show_name": "经营活动产生的现金流量净额/经营活动净收益",
                 "col_comment": "经营活动产生的现金流量净额/经营活动净收益-描述"},
                {"col_name": "nCFOpaOp", "col_show_name": "经营活动产生的现金流量净额/营业利润", "col_comment": "经营活动产生的现金流量净额/营业利润-描述"},
                {"col_name": "nCFOpaNia", "col_show_name": "经营活动产生的现金流量净额/净利润", "col_comment": "经营活动产生的现金流量净额/净利润-描述"},
                {"col_name": "pFixaODa", "col_show_name": "投资支出/折旧和摊销", "col_comment": "投资支出/折旧和摊销-描述"},
                {"col_name": "cRcvryA", "col_show_name": "全部资产现金回收率", "col_comment": "全部资产现金回收率-描述"},
                {"col_name": "nCFOpaPropt", "col_show_name": "经营活动产生的现金流量净额占比", "col_comment": "经营活动产生的现金流量净额占比-描述"},
                {"col_name": "nCFIaPropt", "col_show_name": "投资活动产生的现金流量净额占比", "col_comment": "投资活动产生的现金流量净额占比-描述"},
                {"col_name": "nCFFaPropt", "col_show_name": "筹资活动产生的现金流量净额占比", "col_comment": "筹资活动产生的现金流量净额占比-描述"},
                {"col_name": "cashMInvRatio", "col_show_name": "现金满足投资比率", "col_comment": "现金满足投资比率-描述"},
                {"col_name": "cashOperRatio", "col_show_name": "现金营运指数", "col_comment": "现金营运指数-描述"},
                {"col_name": "cashDivCover", "col_show_name": "现金股利保障倍数", "col_comment": "现金股利保障倍数-描述"},
                {"col_name": "tRevenueYoy", "col_show_name": "营业总收入同比增长", "col_comment": "营业总收入同比增长-描述"},
                {"col_name": "revenueYoy", "col_show_name": "营业收入同比增长", "col_comment": "营业收入同比增长-描述"},
                {"col_name": "operProfitYoy", "col_show_name": "营业利润同比增长", "col_comment": "营业利润同比增长-描述"},
                {"col_name": "tProfitYoy", "col_show_name": "利润总额同比增长", "col_comment": "利润总额同比增长-描述"},
                {"col_name": "niYoy", "col_show_name": "净利润同比增长", "col_comment": "净利润同比增长-描述"},
                {"col_name": "niAttrPYoy", "col_show_name": "归属于母公司净利润同比增长", "col_comment": "归属于母公司净利润同比增长-描述"},
                {"col_name": "rDExpYoy", "col_show_name": "研发费用同比增长", "col_comment": "研发费用同比增长-描述"},
                {"col_name": "niAttrPCutYoy", "col_show_name": "归属于母公司净利润(扣除)同比增长",
                 "col_comment": "归属于母公司净利润(扣除)同比增长-描述"},
                {"col_name": "tFaYtd", "col_show_name": "固定资产相对年初增长", "col_comment": "固定资产相对年初增长-描述"},
                {"col_name": "roeYoy", "col_show_name": "净资产收益率(摊薄)同比增长", "col_comment": "净资产收益率(摊薄)同比增长-描述"},
                {"col_name": "nCFOpaYoy", "col_show_name": "经营活动产生的现金流量净额同比增长", "col_comment": "经营活动产生的现金流量净额同比增长-描述"},
                {"col_name": "basicEpsYoy", "col_show_name": "基本每股收益同比增长", "col_comment": "基本每股收益同比增长-描述"},
                {"col_name": "dilutedEpsYoy", "col_show_name": "稀释每股收益同比增长", "col_comment": "稀释每股收益同比增长-描述"},
                {"col_name": "nCFOpaPsYoy", "col_show_name": "每股经营活动产生的现金流量净额同比增长",
                 "col_comment": "每股经营活动产生的现金流量净额同比增长-描述"},
                {"col_name": "naPsYtd", "col_show_name": "每股净资产相对年初增长", "col_comment": "每股净资产相对年初增长-描述"},
                {"col_name": "taYtd", "col_show_name": "总资产相对年初增长", "col_comment": "总资产相对年初增长-描述"},
                {"col_name": "naYtd", "col_show_name": "净资产相对年初增长", "col_comment": "净资产相对年初增长-描述"},
                {"col_name": "teAttrPYtd", "col_show_name": "归属于母公司的股东权益相对年初增长", "col_comment": "归属于母公司的股东权益相对年初增长-描述"},
                {"col_name": "tlYtd", "col_show_name": "总负债相对年初增长", "col_comment": "总负债相对年初增长-描述"},
                {"col_name": "cashCeYtd", "col_show_name": "货币资金相对年初增长", "col_comment": "货币资金相对年初增长-描述"},
                {"col_name": "epsYoy", "col_show_name": "每股收益EPS同比增长", "col_comment": "每股收益EPS同比增长-描述"},
                {"col_name": "epsCutYoy", "col_show_name": "扣非后每股收益EPS同比增长", "col_comment": "扣非后每股收益EPS同比增长-描述"},
                {"col_name": "cogsYoy", "col_show_name": "营业成本同比增长", "col_comment": "营业成本同比增长-描述"},
                {"col_name": "grossProfitYoy", "col_show_name": "毛利同比增长", "col_comment": "毛利同比增长-描述"},
                {"col_name": "npMarginYoy", "col_show_name": "销售净利率同比增长", "col_comment": "销售净利率同比增长-描述"},
                {"col_name": "cFrSaleGSYoy", "col_show_name": "销售商品、提供劳务收到的现金同比增长",
                 "col_comment": "销售商品、提供劳务收到的现金同比增长-描述"},
                {"col_name": "cPaidGSYoy", "col_show_name": "购买商品、接受劳务支付的现金同比增长",
                 "col_comment": "购买商品、接受劳务支付的现金同比增长-描述"},
                {"col_name": "cPToForEmplYoy", "col_show_name": "支付给职工以及为职工支付的现金同比增长",
                 "col_comment": "支付给职工以及为职工支付的现金同比增长-描述"},
                {"col_name": "nCFOpaNiaYoy", "col_show_name": "净利润现金含量同比增长", "col_comment": "净利润现金含量同比增长-描述"},
                {"col_name": "cTa", "col_show_name": "货币资金/总资产", "col_comment": "货币资金/总资产-描述"},
                {"col_name": "nrArTa", "col_show_name": "应收票据及应收账款/总资产", "col_comment": "应收票据及应收账款/总资产-描述"},
                {"col_name": "arTa", "col_show_name": "应收账款/总资产", "col_comment": "应收账款/总资产-描述"},
                {"col_name": "repayTa", "col_show_name": "预付账款/总资产", "col_comment": "预付账款/总资产-描述"},
                {"col_name": "invenTa", "col_show_name": "存货/总资产", "col_comment": "存货/总资产-描述"},
                {"col_name": "caTa", "col_show_name": "流动资产/总资产", "col_comment": "流动资产/总资产-描述"},
                {"col_name": "fixedATTa", "col_show_name": "固定资产/总资产", "col_comment": "固定资产/总资产-描述"},
                {"col_name": "tFixedATa", "col_show_name": "固定资产合计/总资产", "col_comment": "固定资产合计/总资产-描述"},
                {"col_name": "intanATa", "col_show_name": "无形资产/总资产", "col_comment": "无形资产/总资产-描述"},
                {"col_name": "ltAmorExpTa", "col_show_name": "长期待摊费用/总资产", "col_comment": "长期待摊费用/总资产-描述"},
                {"col_name": "ncaTa", "col_show_name": "非流动资产/总资产", "col_comment": "非流动资产/总资产-描述"},
                {"col_name": "npApTa", "col_show_name": "应付票据及应付账款/总资产", "col_comment": "应付票据及应付账款/总资产-描述"},
                {"col_name": "apTa", "col_show_name": "应付账款/总资产", "col_comment": "应付账款/总资产-描述"},
                {"col_name": "advRTa", "col_show_name": "预收款项/总资产", "col_comment": "预收款项/总资产-描述"},
                {"col_name": "stBorrTa", "col_show_name": "短期借款/总资产", "col_comment": "短期借款/总资产-描述"},
                {"col_name": "ltBorrTa", "col_show_name": "长期借款/总资产", "col_comment": "长期借款/总资产-描述"},
                {"col_name": "bpTa", "col_show_name": "应付债券/总资产", "col_comment": "应付债券/总资产-描述"},
                {"col_name": "nTanATa", "col_show_name": "有形净资产/总资产", "col_comment": "有形净资产/总资产-描述"},
                {"col_name": "treTa", "col_show_name": "留存收益/总资产", "col_comment": "留存收益/总资产-描述"},
                {"col_name": "teapTa", "col_show_name": "归属于母公司的股东权益/总资产", "col_comment": "归属于母公司的股东权益/总资产-描述"},
                {"col_name": "tseTa", "col_show_name": "所有者权益/总资产", "col_comment": "所有者权益/总资产-描述"},
                {"col_name": "idIc", "col_show_name": "带息债务/投入资本", "col_comment": "带息债务/投入资本-描述"},
                {"col_name": "teapIc", "col_show_name": "归属于母公司的股东权益/投入资本", "col_comment": "归属于母公司的股东权益/投入资本-描述"},
                {"col_name": "clTa", "col_show_name": "流动负债/负债合计", "col_comment": "流动负债/负债合计-描述"},
                {"col_name": "nclTa", "col_show_name": "非流动负债/负债合计", "col_comment": "非流动负债/负债合计-描述"},
                {"col_name": "equMultiplier", "col_show_name": "权益乘数", "col_comment": "权益乘数-描述"},
                {"col_name": "capFixRatio", "col_show_name": "资本固定化比率", "col_comment": "资本固定化比率-描述"},
                {"col_name": "ltDebtCapRatio", "col_show_name": "长期资本负债率", "col_comment": "长期资本负债率-描述"},
                {"col_name": "ltAssetSuitRatio", "col_show_name": "长期资产适合率", "col_comment": "长期资产适合率-描述"},
                {"col_name": "nclTeap", "col_show_name": "非流动负债合计／归属母公司股东的权益", "col_comment": "非流动负债合计／归属母公司股东的权益-描述"},
                {"col_name": "clTeap", "col_show_name": "流动负债合计／归属母公司股东的权益", "col_comment": "流动负债合计／归属母公司股东的权益-描述"},
                {"col_name": "rTr", "col_show_name": "营业收入/营业总收入", "col_comment": "营业收入/营业总收入-描述"},
                {"col_name": "tcogsTr", "col_show_name": "营业总成本/营业总收入", "col_comment": "营业总成本/营业总收入-描述"},
                {"col_name": "cogsTr", "col_show_name": "营业成本/营业总收入", "col_comment": "营业成本/营业总收入-描述"},
                {"col_name": "btaxSurchgTr", "col_show_name": "营业税金及附加/营业总收入", "col_comment": "营业税金及附加/营业总收入-描述"},
                {"col_name": "sellExpTr", "col_show_name": "销售费用/营业总收入", "col_comment": "销售费用/营业总收入-描述"},
                {"col_name": "adminExpTr", "col_show_name": "管理费用/营业总收入", "col_comment": "管理费用/营业总收入-描述"},
                {"col_name": "rDExpTr", "col_show_name": "研发费用/营业总收入", "col_comment": "研发费用/营业总收入-描述"},
                {"col_name": "finanExpTr", "col_show_name": "财务费用/营业总收入", "col_comment": "财务费用/营业总收入-描述"},
                {"col_name": "ailTr", "col_show_name": "资产减值损失/营业总收入", "col_comment": "资产减值损失/营业总收入-描述"},
                {"col_name": "cilTr", "col_show_name": "信用减值损失/营业总收入", "col_comment": "信用减值损失/营业总收入-描述"},
                {"col_name": "opaPTr", "col_show_name": "经营活动净收益/营业总收入", "col_comment": "经营活动净收益/营业总收入-描述"},
                {"col_name": "valChgPTr", "col_show_name": "价值变动净收益/营业总收入", "col_comment": "价值变动净收益/营业总收入-描述"},
                {"col_name": "fvChgGTr", "col_show_name": "公允价值变动收益/营业总收入", "col_comment": "公允价值变动收益/营业总收入-描述"},
                {"col_name": "invIncTr", "col_show_name": "投资收益/营业总收入", "col_comment": "投资收益/营业总收入-描述"},
                {"col_name": "opTr", "col_show_name": "营业利润/营业总收入", "col_comment": "营业利润/营业总收入-描述"},
                {"col_name": "nopgTr", "col_show_name": "营业外收入/营业总收入", "col_comment": "营业外收入/营业总收入-描述"},
                {"col_name": "noplTr", "col_show_name": "营业外支出/营业总收入", "col_comment": "营业外支出/营业总收入-描述"},
                {"col_name": "tpTr", "col_show_name": "利润总额/营业总收入", "col_comment": "利润总额/营业总收入-描述"},
                {"col_name": "itTr", "col_show_name": "所得税/营业总收入", "col_comment": "所得税/营业总收入-描述"},
                {"col_name": "niTr", "col_show_name": "净利润/营业总收入", "col_comment": "净利润/营业总收入-描述"},
                {"col_name": "ebitdaTr", "col_show_name": "EBITDA/营业总收入", "col_comment": "EBITDA/营业总收入-描述"},
                {"col_name": "ebitTr", "col_show_name": "EBIT/营业总收入", "col_comment": "EBIT/营业总收入-描述"},
                {"col_name": "opaPTp", "col_show_name": "经营活动净收益/利润总额", "col_comment": "经营活动净收益/利润总额-描述"},
                {"col_name": "valChgPTp", "col_show_name": "价值变动净收益/利润总额", "col_comment": "价值变动净收益/利润总额-描述"},
                {"col_name": "opTp", "col_show_name": "营业利润/利润总额", "col_comment": "营业利润/利润总额-描述"},
                {"col_name": "nNopiTp", "col_show_name": "营业外收支净额/利润总额", "col_comment": "营业外收支净额/利润总额-描述"},
                {"col_name": "itTp", "col_show_name": "所得税/利润总额", "col_comment": "所得税/利润总额-描述"},
                {"col_name": "niCutNi", "col_show_name": "扣除非经常损益后的归母净利润/归母净利润",
                 "col_comment": "扣除非经常损益后的归母净利润/归母净利润-描述"}
            ]
        }
    define_json = json.dumps(fdmtmaindatapit_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)


'''
备注：fdmtmaindataqpit表含有多个通联字典中不含有的字段，字段统一名称为"新增索引"
其中不含有字段分别是：nIntExp,ebit,ebitda,ebiat,fcff,fcfe,da,basicEps,dilutedEps,basicEpsCut,dilutedEpsCut,nAssetPs,ebitPs,
ebitdaPs,cReserPs,sReserPs,reserPs,rePs,tRePs,fcffPs,fcfePs,roeW,roeCutW,roaEbit,roic,rop,faTurnover,dayFa,tfaTurnover,dayTfa,caTurnover,
ncaTurnover,taTurnover,invenTurnover,daysInven,nrArTurnover,daysNrAr,arTurnover,daysAr,npApTurnover,daysNpAp,apTurnover,daysAp,
workCapitalTurnover,daysWorkCapital,nWorkCapitalTurnover,daysWorkCapital2018,operCycle,nOperCycle,currentRatio,quickRatio,
squickRatio,assetLiabRatio,equityRatio,tlTeap,teapTl,teapID,nTanATl,nTanAID,nTanANd,ebitdaTl,ebitdaID,cashIcl,cashCl,nclWc,
timesInteEbit,timesInteEbitda,timesInteCF,cashRatio,ltLiabRatio,pFixaODa,cashMInvRatio,cashOperRatio,tRevenueYoy,revenueYoy,operProfitYoy,
tProfitYoy,niYoy,niAttrPYoy,rDExpYoy,niAttrPCutYoy,tFaYtd,roeYoy,nCFOpaYoy,basicEpsYoy,dilutedEpsYoy,nCFOpaPsYoy,naPsYtd,taYtd,naYtd,
teAttrPYtd,tlYtd,cashCeYtd,epsYoy,epsCutYoy,cogsYoy,grossProfitYoy,npMarginYoy,cFrSaleGSYoy,cPaidGSYoy,cPToForEmplYoy,nCFOpaNiaYoy,cTa,
nrArTa,arTa,repayTa,invenTa,caTa,fixedATTa,tFixedATa,intanATa,ltAmorExpTa,ncaTa,npApTa,apTa,advRTa,stBorrTa,ltBorrTa,
bpTa,nTanATa,treTa,teapTa,tseTa,idIc,teapIc,clTa,nclTa,equMultiplier,capFixRatio,ltDebtCapRatio,ltAssetSuitRatio,nclTeap,clTeap,ebitdaTr,
ebitTr,
'''
def fdmtmaindataqpit_define(table_name):

    fdmtmaindataqpit_str = {
            "table_name": "fdmtmaindataqpit",
            "table_show_name": "主要财务指标（单季度）",
            "table_comment": "主要财务指标（单季度）-描述",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {"col_name": "secID",
                 "col_show_name": "通联编制的证券编码，格式是“交易代码.证券市场代码”，如000002.XSHE。可传入证券交易代码使用DataAPI.SecIDGet接口获取到。",
                 "col_comment": "通联编制的证券编码，格式是“交易代码.证券市场代码”，如000002.XSHE。可传入证券交易代码使用DataAPI.SecIDGet接口获取到。-描述"},
                {"col_name": "secShortName", "col_show_name": "证券简称", "col_comment": "证券简称-描述"},
                {"col_name": "exchangeCD", "col_show_name": "通联编制的交易市场编码", "col_comment": "通联编制的交易市场编码-描述"},
                {"col_name": "ticker", "col_show_name": "证券在证券市场通用的交易代码。", "col_comment": "证券在证券市场通用的交易代码。-描述"},
                {"col_name": "partyID", "col_show_name": "机构ID", "col_comment": "机构ID-描述"},
                {"col_name": "publishDate", "col_show_name": "发布时间", "col_comment": "发布时间-描述"},
                {"col_name": "endDateRep", "col_show_name": "报告截止时间", "col_comment": "报告截止时间-描述"},
                {"col_name": "endDate", "col_show_name": "截止日期", "col_comment": "截止日期-描述"},
                {"col_name": "isNew", "col_show_name": "是否最新", "col_comment": "是否最新-描述"},
                {"col_name": "reportType", "col_show_name": "报告类型", "col_comment": "报告类型-描述"},
                {"col_name": "mergedFlag", "col_show_name": "合并标志", "col_comment": "合并标志-描述"},
                {"col_name": "fiscalPeriod", "col_show_name": "会计区间", "col_comment": "会计区间-描述"},
                {"col_name": "grossProfit", "col_show_name": "毛利", "col_comment": "毛利-描述"},
                {"col_name": "opaProfit", "col_show_name": "经营活动净收益", "col_comment": "经营活动净收益-描述"},
                {"col_name": "valChgProfit", "col_show_name": "价值变动净收益", "col_comment": "价值变动净收益-描述"},
                {"col_name": "nIntExp", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "ebit", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "ebitda", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "ebiat", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "nrProfitLoss", "col_show_name": "非经常性损益", "col_comment": "非经常性损益-描述"},
                {"col_name": "niAttrPCut", "col_show_name": "扣除非经常性损益后的归属于上市公司股东的净利润",
                 "col_comment": "扣除非经常性损益后的归属于上市公司股东的净利润-描述"},
                {"col_name": "fcff", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "fcfe", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "da", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "rd", "col_show_name": "研发支出合计", "col_comment": "研发支出合计-描述"},
                {"col_name": "rdENiAttrPCut", "col_show_name": "研发支出前利润", "col_comment": "研发支出前利润-描述"},
                {"col_name": "eps", "col_show_name": "每股收益(期末摊薄)", "col_comment": "每股收益(期末摊薄)-描述"},
                {"col_name": "epsCut", "col_show_name": "扣除每股收益(期末摊薄)", "col_comment": "扣除每股收益(期末摊薄)-描述"},
                {"col_name": "basicEps", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "dilutedEps", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "basicEpsCut", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "dilutedEpsCut", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "nAssetPs", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "tRevPs", "col_show_name": "每股营业总收入", "col_comment": "每股营业总收入-描述"},
                {"col_name": "revPs", "col_show_name": "每股营业收入", "col_comment": "每股营业收入-描述"},
                {"col_name": "opPs", "col_show_name": "每股营业利润", "col_comment": "每股营业利润-描述"},
                {"col_name": "ebitPs", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "ebitdaPs", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "cReserPs", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "sReserPs", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "reserPs", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "rePs", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "tRePs", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "nCFOperAPs", "col_show_name": "每股经营活动产生的现金流量净额", "col_comment": "每股经营活动产生的现金流量净额-描述"},
                {"col_name": "nCInCashPs", "col_show_name": "每股现金流量净额", "col_comment": "每股现金流量净额-描述"},
                {"col_name": "fcffPs", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "fcfePs", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "grossMargin", "col_show_name": "销售毛利率", "col_comment": "销售毛利率-描述"},
                {"col_name": "npMargin", "col_show_name": "销售净利润率", "col_comment": "销售净利润率-描述"},
                {"col_name": "scRatio", "col_show_name": "销售成本率", "col_comment": "销售成本率-描述"},
                {"col_name": "periodExpTr", "col_show_name": "销售期间费用率", "col_comment": "销售期间费用率-描述"},
                {"col_name": "pCostExp", "col_show_name": "成本费用利润率", "col_comment": "成本费用利润率-描述"},
                {"col_name": "roe", "col_show_name": "净资产收益率(摊薄)", "col_comment": "净资产收益率(摊薄)-描述"},
                {"col_name": "roeA", "col_show_name": "净资产收益率(平均)", "col_comment": "净资产收益率(平均)-描述"},
                {"col_name": "roeW", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "roeCut", "col_show_name": "净资产收益率(扣除摊薄)", "col_comment": "净资产收益率(扣除摊薄)-描述"},
                {"col_name": "roeCutA", "col_show_name": "净资产收益率ROE(扣除平均)", "col_comment": "净资产收益率ROE(扣除平均)-描述"},
                {"col_name": "roeCutW", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "roa", "col_show_name": "总资产净利率", "col_comment": "总资产净利率-描述"},
                {"col_name": "roaEbit", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "roic", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "rop", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "faTurnover", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "dayFa", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "tfaTurnover", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "dayTfa", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "caTurnover", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "ncaTurnover", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "taTurnover", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "invenTurnover", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "daysInven", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "nrArTurnover", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "daysNrAr", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "arTurnover", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "daysAr", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "npApTurnover", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "daysNpAp", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "apTurnover", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "daysAp", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "workCapitalTurnover", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "daysWorkCapital", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "nWorkCapitalTurnover", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "daysWorkCapital2018", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "operCycle", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "nOperCycle", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "currentRatio", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "quickRatio", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "squickRatio", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "opCl", "col_show_name": "营业利润/流动负债", "col_comment": "营业利润/流动负债-描述"},
                {"col_name": "opTl", "col_show_name": "营业利润/负债合计", "col_comment": "营业利润/负债合计-描述"},
                {"col_name": "assetLiabRatio", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "equityRatio", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "tlTeap", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "teapTl", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "teapID", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "nTanATl", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "nTanAID", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "nTanANd", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "ebitdaTl", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "ebitdaID", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "cashIcl", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "cashCl", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "nCFOpaCl", "col_show_name": "经营活动现金流量净额/流动负债", "col_comment": "经营活动现金流量净额/流动负债-描述"},
                {"col_name": "nCFOpaLiab", "col_show_name": "经营活动现金流量净额/负债合计", "col_comment": "经营活动现金流量净额/负债合计-描述"},
                {"col_name": "nCFOpaID", "col_show_name": "经营活动现金流量净额/带息债务", "col_comment": "经营活动现金流量净额/带息债务-描述"},
                {"col_name": "nCFOpaNd", "col_show_name": "经营活动现金流量净额/净债务", "col_comment": "经营活动现金流量净额/净债务-描述"},
                {"col_name": "nCFOpaNcl", "col_show_name": "经营活动现金流量净额/非流动负债", "col_comment": "经营活动现金流量净额/非流动负债-描述"},
                {"col_name": "nCFNfaCl", "col_show_name": "非筹资性现金流量净额/流动负债", "col_comment": "非筹资性现金流量净额/流动负债-描述"},
                {"col_name": "nCFNfaLiab", "col_show_name": "非筹资性现金流量净额/负债总额", "col_comment": "非筹资性现金流量净额/负债总额-描述"},
                {"col_name": "nclWc", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "timesInteEbit", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "timesInteEbitda", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "timesInteCF", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "cashRatio", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "nCFOpaDebtDue", "col_show_name": "现金到期债务比", "col_comment": "现金到期债务比-描述"},
                {"col_name": "ltLiabRatio", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "nrArRecR", "col_show_name": "应收票据及应收账款回款率", "col_comment": "应收票据及应收账款回款率-描述"},
                {"col_name": "nrArR", "col_show_name": "应收票据及应收账款/营业收入", "col_comment": "应收票据及应收账款/营业收入-描述"},
                {"col_name": "arRecR", "col_show_name": "应收账款回款率", "col_comment": "应收账款回款率-描述"},
                {"col_name": "arR", "col_show_name": "应收账款/营业收入", "col_comment": "应收账款/营业收入-描述"},
                {"col_name": "advRR", "col_show_name": "预收款项/营业收入", "col_comment": "预收款项/营业收入-描述"},
                {"col_name": "cfsgsR", "col_show_name": "销售商品提供劳务收到的现金/营业收入", "col_comment": "销售商品提供劳务收到的现金/营业收入-描述"},
                {"col_name": "nCFOpaTr", "col_show_name": "经营活动产生的现金流量净额/营业总收入",
                 "col_comment": "经营活动产生的现金流量净额/营业总收入-描述"},
                {"col_name": "nCFOpaR", "col_show_name": "经营活动产生的现金流量净额/营业收入", "col_comment": "经营活动产生的现金流量净额/营业收入-描述"},
                {"col_name": "nCFOpaOpap", "col_show_name": "经营活动产生的现金流量净额/经营活动净收益",
                 "col_comment": "经营活动产生的现金流量净额/经营活动净收益-描述"},
                {"col_name": "nCFOpaOp", "col_show_name": "经营活动产生的现金流量净额/营业利润", "col_comment": "经营活动产生的现金流量净额/营业利润-描述"},
                {"col_name": "nCFOpaNia", "col_show_name": "经营活动产生的现金流量净额/净利润", "col_comment": "经营活动产生的现金流量净额/净利润-描述"},
                {"col_name": "pFixaODa", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "cRcvryA", "col_show_name": "全部资产现金回收率", "col_comment": "全部资产现金回收率-描述"},
                {"col_name": "nCFOpaPropt", "col_show_name": "经营活动产生的现金流量净额占比", "col_comment": "经营活动产生的现金流量净额占比-描述"},
                {"col_name": "nCFIaPropt", "col_show_name": "投资活动产生的现金流量净额占比", "col_comment": "投资活动产生的现金流量净额占比-描述"},
                {"col_name": "nCFFaPropt", "col_show_name": "筹资活动产生的现金流量净额占比", "col_comment": "筹资活动产生的现金流量净额占比-描述"},
                {"col_name": "cashMInvRatio", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "cashOperRatio", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "cashDivCover", "col_show_name": "现金股利保障倍数", "col_comment": "现金股利保障倍数-描述"},
                {"col_name": "tRevenueYoy", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "revenueYoy", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "operProfitYoy", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "tProfitYoy", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "niYoy", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "niAttrPYoy", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "rDExpYoy", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "niAttrPCutYoy", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "tFaYtd", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "roeYoy", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "nCFOpaYoy", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "basicEpsYoy", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "dilutedEpsYoy", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "nCFOpaPsYoy", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "naPsYtd", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "taYtd", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "naYtd", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "teAttrPYtd", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "tlYtd", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "cashCeYtd", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "epsYoy", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "epsCutYoy", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "cogsYoy", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "grossProfitYoy", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "npMarginYoy", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "cFrSaleGSYoy", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "cPaidGSYoy", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "cPToForEmplYoy", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "nCFOpaNiaYoy", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "cTa", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "nrArTa", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "arTa", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "repayTa", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "invenTa", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "caTa", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "fixedATTa", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "tFixedATa", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "intanATa", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "ltAmorExpTa", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "ncaTa", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "npApTa", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "apTa", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "advRTa", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "stBorrTa", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "ltBorrTa", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "bpTa", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "nTanATa", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "treTa", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "teapTa", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "tseTa", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "idIc", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "teapIc", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "clTa", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "nclTa", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "equMultiplier", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "capFixRatio", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "ltDebtCapRatio", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "ltAssetSuitRatio", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "nclTeap", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "clTeap", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "rTr", "col_show_name": "营业收入/营业总收入", "col_comment": "营业收入/营业总收入-描述"},
                {"col_name": "tcogsTr", "col_show_name": "营业总成本/营业总收入", "col_comment": "营业总成本/营业总收入-描述"},
                {"col_name": "cogsTr", "col_show_name": "营业成本/营业总收入", "col_comment": "营业成本/营业总收入-描述"},
                {"col_name": "btaxSurchgTr", "col_show_name": "营业税金及附加/营业总收入", "col_comment": "营业税金及附加/营业总收入-描述"},
                {"col_name": "sellExpTr", "col_show_name": "销售费用/营业总收入", "col_comment": "销售费用/营业总收入-描述"},
                {"col_name": "adminExpTr", "col_show_name": "管理费用/营业总收入", "col_comment": "管理费用/营业总收入-描述"},
                {"col_name": "rDExpTr", "col_show_name": "研发费用/营业总收入", "col_comment": "研发费用/营业总收入-描述"},
                {"col_name": "finanExpTr", "col_show_name": "财务费用/营业总收入", "col_comment": "财务费用/营业总收入-描述"},
                {"col_name": "ailTr", "col_show_name": "资产减值损失/营业总收入", "col_comment": "资产减值损失/营业总收入-描述"},
                {"col_name": "cilTr", "col_show_name": "信用减值损失/营业总收入", "col_comment": "信用减值损失/营业总收入-描述"},
                {"col_name": "opaPTr", "col_show_name": "经营活动净收益/营业总收入", "col_comment": "经营活动净收益/营业总收入-描述"},
                {"col_name": "valChgPTr", "col_show_name": "价值变动净收益/营业总收入", "col_comment": "价值变动净收益/营业总收入-描述"},
                {"col_name": "fvChgGTr", "col_show_name": "公允价值变动收益/营业总收入", "col_comment": "公允价值变动收益/营业总收入-描述"},
                {"col_name": "invIncTr", "col_show_name": "投资收益/营业总收入", "col_comment": "投资收益/营业总收入-描述"},
                {"col_name": "opTr", "col_show_name": "营业利润/营业总收入", "col_comment": "营业利润/营业总收入-描述"},
                {"col_name": "nopgTr", "col_show_name": "营业外收入/营业总收入", "col_comment": "营业外收入/营业总收入-描述"},
                {"col_name": "noplTr", "col_show_name": "营业外支出/营业总收入", "col_comment": "营业外支出/营业总收入-描述"},
                {"col_name": "tpTr", "col_show_name": "利润总额/营业总收入", "col_comment": "利润总额/营业总收入-描述"},
                {"col_name": "itTr", "col_show_name": "所得税/营业总收入", "col_comment": "所得税/营业总收入-描述"},
                {"col_name": "niTr", "col_show_name": "净利润/营业总收入", "col_comment": "净利润/营业总收入-描述"},
                {"col_name": "ebitdaTr", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "ebitTr", "col_show_name": "新增索引", "col_comment": "新增索引-描述"},
                {"col_name": "opaPTp", "col_show_name": "经营活动净收益/利润总额", "col_comment": "经营活动净收益/利润总额-描述"},
                {"col_name": "valChgPTp", "col_show_name": "价值变动净收益/利润总额", "col_comment": "价值变动净收益/利润总额-描述"},
                {"col_name": "opTp", "col_show_name": "营业利润/利润总额", "col_comment": "营业利润/利润总额-描述"},
                {"col_name": "nNopiTp", "col_show_name": "营业外收支净额/利润总额", "col_comment": "营业外收支净额/利润总额-描述"},
                {"col_name": "itTp", "col_show_name": "所得税/利润总额", "col_comment": "所得税/利润总额-描述"},
                {"col_name": "niCutNi", "col_show_name": "扣除非经常损益后的归母净利润/归母净利润",
                 "col_comment": "扣除非经常损益后的归母净利润/归母净利润-描述"}
            ]
        }
    define_json = json.dumps(fdmtmaindataqpit_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)



if __name__ == '__main__':

    mktadjfaf_define('mktadjfaf')
    mktadjf_define('mktadjf')
    sectyperel_define('sectyperel')
    equ_define('equ')
    fdmtbsbank2018_define('fdmtbsbank2018')
    fdmtbsindu2018_define('fdmtbsindu2018')
    fdmtbssecu2018_define('fdmtbssecu2018')
    fdmtbsinsu2018_define('fdmtbsinsu2018')
    fdmtbsbank_define('fdmtbsbank')
    fdmtbsindu_define('fdmtbsindu')
    fdmtbsinsu_define('fdmtbsinsu')
    fdmtbssecu_define('fdmtbssecu')
    fdmtcfbank2018_define('fdmtcfbank2018')
    fdmtcfindu2018_define('fdmtcfindu2018')
    fdmtcfinsu2018_define('fdmtcfinsu2018')
    fdmtcfsecu2018_define('fdmtcfsecu2018')
    fdmtcfbank_define('fdmtcfbank')
    fdmtcfindu_define('fdmtcfindu')
    fdmtcfsecu_define('fdmtcfsecu')
    fdmtcfinsu_define('fdmtcfinsu')
    industrystd_define('industrystd')
    equindustry_define('equindustry')
    partyid_define('partyid')
    equdiv_define('equdiv')
    mktequdeval_define('mktequdeval')
    mktlimit_define('mktlimit')
    mktequdind_define('mktequdind')
    equpledge_define('equpledg')
    equstockpledg_define('equstockpledg')
    fdmtmaindatapit_define('fdmtmaindatapit')
    fdmtcfs_define('fdmtcfs')
    fdmte_define('fdmte')
    fdmtmainopern_define('fdmtmainopern')
    fdmtmostditem_define('fdmtmostditem')
    fdmtderpit_define('fdmtderpit')
    mktequfloworder_define('mktequfloworder')
    mktequflow_define('mktequflow')
    mktindustryflow_define('mktindustryflow')
    mktindustryfloworder_define('mktindustryfloworder')
    mktequmf_define('mktequmf')
    fdmtefnew_define('fdmtefnew')
    equholderchgcsf_define('equholderchgcsf')
    mktinstequd_define('mktinstequd')
    fdmtisbank2018_define('fdmtisbank2018')
    fdmtisindu2018_define('fdmtisindu2018')
    fdmtissecu2018_define('fdmtissecu2018')
    fdmtisinsu2018_define('fdmtisinsu2018')
    fdmtisbank_define('fdmtisbank')
    fdmtisindu_define('fdmtisindu')
    fdmtissecu_define('fdmtissecu')
    fdmtisinsu_define('fdmtisinsu')
    equinstssta_define('equinstssta')
    mktblockd_define('mktblockd')
    mktequd_define('mktequd')
    mktequdadjadj_define('mktequdadjadj')
    mktequdadjaf_define('mktequdadjaf')
    equcompproduction_define('equcompproduction')
    mktrankliststocks_define('mktrankliststocks')
    mktranklistsales_define('mktranklistsales')
    equreportpredisclo_define('equreportpredisclo')
    secchghistory_define('secchghistory')
    sechalt_define('sechalt')
    equsharesfloat_define('equsharesfloat')
    equshareschg_define('equshareschg')
    equfreeshares_define('equfreeshares')
    equallot_define('equallot')
    equshten_define('equshten')
    stockfctindiconeday_define('stockfctindiconeday')
    sectips_define('sectips')
    tradecal_define('tradecal')
    workingcal_define('workingcal')
    fdmtcfinduttmpit_define('fdmtcfinduttmpit')
    fdmtisinduttmpit_define('fdmtisinduttmpit')
    mktequwadjaf_define('mktequwadjaf')
    mktequmadjaf_define('mktequmadjaf')
    mktequqadjaf_define('mktequqadjaf')
    mktequaadjaf_define('mktequaadjaf')
    mktequsadjaf_define('mktequsadjaf')
    fdmtmaindatapit_define('fdmtmaindatapit')
    fdmtmaindataqpit_define('fdmtmaindataqpit')
