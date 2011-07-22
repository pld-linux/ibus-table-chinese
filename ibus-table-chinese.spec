%define createdb ibus-table-createdb
Summary:	Chinese input tables for IBus
Summary(zh_CN):	中文码表输入法
Summary(zh_TW):	中文碼表輸入法
Name:		ibus-table-chinese
Version:	1.3.1
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	http://ibus.googlecode.com/files/%{name}-%{version}-Source.tar.gz
# Source0-md5:	63d7dda971e0fd86e7a2d4cbbed779d6
Patch0:		%{name}-no-fedora.patch
URL:		http://code.google.com/p/ibus/
BuildRequires:	cmake >= 2.4
BuildRequires:	ibus-table-devel >= 1.2
Requires:	ibus-table >= 1.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ibus-table-chinese is provides the infrastructure for Chinese input
methods. Input tables themselves are in sub-packages.

%description -l zh_TW
ibus-table-chinese 提供了中文碼表輸入法的基礎架構。
輸入法本身則在子套件裡。

%package array
Summary:	Array input methods
Summary(zh_CN):	行列输入法
Summary(zh_TW):	行列輸入法
License:	Freely redistributable without restriction
Group:		Libraries

%description array
Array input method is a free, open-minded character-structured input
method. Includes: array30: 27489 characters. array30-big: 27489
characters + Unicode ExtB.

%description array -l zh_TW
行列輸入法是一套免費授權、具有開放理念的字根式
中文輸入法，發明人是行列科技負責人廖明德。

行列輸入法除了可以輸入繁體中文和簡體中文之外，
亦可輸入Unicode當中的中日韓統一表意文字。

包含了：
行列30: 27489 字
行列30大字集: 27489 字 + Unicode ExtB.

%package cangjie
Summary:	Cangjie based input methods
Summary(zh_TW):	倉頡輸入法
Summary(zh_CN):	仓颉输入法
License:	Freely redistributable without restriction
Group:		Libraries

%description cangjie
Cangjie based input methods, includes: Cangjie3, Canjie5, and Cangjie
big tables.

%description cangjie -l zh_TW
倉頡以及其衍生輸入法，包含：
倉頡三代、倉頡五代以及倉頡大字集。

%package cantonese
Summary:	Cantonese input methods
Summary(zh_TW):	粵語輸入法
Group:		Libraries

%description cantonese
Cantonese input methods, includes: Cantonese, Hong-Kong version of
Cantonese, and jyutping.

%description cantonese -l zh_TW
粵語輸入法。包含：
廣東拼音、港式廣東話、
以及粵語拼音。

%package easy
Summary:	Easy input method
Summary(zh_CN):	轻松输入法
Summary(zh_TW):	輕鬆輸入法
Group:		Libraries

%description easy
Easy phrase-wise input method.

%description easy -l zh_CN
轻松大词库

%description easy -l zh_TW
輕鬆大詞庫

%package erbi
Summary:	Erbi input method
Summary(zh_CN):	二笔输入法
Summary(zh_TW):	二筆輸入法
License:	Freely redistributable without restriction
Group:		Libraries

%description erbi
Erbi input methods. Includes:
Super Erbi (as erbi)
and Erbi Qin-Song (erbi-qs)

%description erbi -l zh_CN
包含：
超強二笔 (erbi)
以及青松二笔 (erbi-qs)

%description erbi -l zh_TW
包含：
超強二筆 (erbi)
以及青松二筆 (erbi-qs)

%package quick
Summary:	Quick-to-learn input methods
Summary(zh_CN):	速成输入法
Summary(zh_TW):	速成輸入法
License:	Freely redistributable without restriction
Group:		Libraries

%description quick
Quick-to-learn is based on Cangjie input method, but only need
Canjie's first and last word-root to form a character.

Includes: Quick3, Quick5 and Quick-Classic, and Smart Cangjie 6.

%description quick -l zh_TW
速成輸入法，又稱簡易輸入法，為倉頡輸入法之簡化版本。
只取倉頡碼的首尾兩碼，所以一字最長只有兩碼。

包含：
速成三代、速成五代以及速成古典版。

%package scj
Summary:	Smart Cangjie
Summary(zh_CN):	快速仓颉输入法
Summary(zh_TW):	快速倉頡輸入法
Group:		Libraries

%description scj
Smart Cangjie is an improved Cangjie base input method which handles
Cangjie, Quick, Cantonese, Chinese punctuation, Japanese, 3000
frequent words by Hong Kong government, both Traditional and
Simplified Chinese.

This package includes the Smart Cangjie 6.

%description scj -l zh_CN
快速仓颉输入法第六代（快仓六）是一个多功能和多任务的
输入法系统。在功能方面，它不但拥有多种不同版本的仓颉
输入法、速成输入法、广东话输入法、高效率的标点、特殊
符号和数字编码、日文编码、香港政府三千常用字编码、简
码和容错码，而且还能够处理繁体和简体文字。在任务方面
，它不但承袭了传统仓颉的「中文输入、输出、辨识和释义
」等功能，而且还能肩负起促进「资讯科技教育、母语教育
和特殊教育」等多重任务。

%description scj -l zh_TW
快速倉頡輸入法第六代（快倉六）是一個多功能和多任務的
輸入法系統。在功能方面，它不但擁有多種不同版本的倉頡
輸入法、速成輸入法、廣東話輸入法、高效率的標點、特殊
符號和數字編碼、日文編碼、香港政府三千常用字編碼、簡
碼和容錯碼，而且還能夠處理繁體和簡體文字。在任務方面
，它不但承襲了傳統倉頡的「中文輸入、輸出、辨識和釋義
」等功能，而且還能肩負起促進「資訊科技教育、母語教育
和特殊教育」等多重任務。

%package stroke5
Summary:	Stroke 5 input method
Summary(zh_CN):	笔顺五码输入法
Summary(zh_TW):	筆順五碼輸入法
Group:		Libraries

%description stroke5
Stroke 5 input method,

%description stroke5 -l zh_CN
笔顺五码。

%description stroke5 -l zh_TW
筆順五碼。

%package wu
Summary:	Wu pronunciation input method
Summary(zh_CN):	上海吳语注音输入法
Summary(zh_TW):	上海吳語注音輸入法
Group:		Libraries

%description wu
Wu pronunciation input method.
URL: http://input.foruto.com/wu/

%description wu -l zh_CN
上海吳语注音输入法。
URL: http://input.foruto.com/wu/

%description wu -l zh_TW
上海吳語注音輸入法以現代吳語中有代表性的上海吳語（又稱上海話、滬語）
的讀音、詞語為基礎。
本輸入法適用於母語為上海話的用戶，也能作為學習上海話的輔助工具。
URL: http://input.foruto.com/wu/

%package wubi-haifeng
Summary:	Haifeng Wubi input method
Summary(zh_CN):	海峰五笔输入法
Summary(zh_TW):	海峰五筆輸入法
License:	BSD
Group:		Libraries

%description wubi-haifeng
Haifeng Wubi input methods. Current includes: Haifeng Wubi 86.

%description wubi-haifeng -l zh_CN
海峰五笔输入法。包含：海峰五笔86。

%description wubi-haifeng -l zh_TW
海峰五筆輸入法。包含：海峰五筆86。

%package wubi-jidian
Summary:	Jidian Wubi input method
Summary(zh_CN):	极点五笔输入法
Summary(zh_TW):	極點五筆輸入法
License:	Freely redistributable without restriction
Group:		Libraries

%description wubi-jidian
Jidian Wubi input methods. Current includes: Wubi 86.

%description wubi-jidian -l zh_CN
极点五笔输入法。包含：极点五笔86。

%description wubi-jidian -l zh_TW
極點五筆輸入法。包含：五筆86。

%package yong
Summary:	YongMa input method
Summary(zh_CN):	永码输入法
Summary(zh_TW):	永碼輸入法
Group:		Libraries

%description yong
YongMa input method.

%description yong -l zh_CN
永码输入法。

%description yong -l zh_TW
永碼輸入法。

%prep
%setup -q -n %{name}-%{version}-Source
%patch0 -p1

%build
%cmake
%{__make} VERBOSE=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Create indexes
for db in $RPM_BUILD_ROOT%{_datadir}/ibus-table/tables/*.db ; do
	%{_bindir}/ibus-table-createdb -i -n $db
done

%clean
rm -rf $RPM_BUILD_ROOT

%if 0
# no usefull information here
%files
%defattr(644,root,root,755)
%doc RELEASE-NOTES.txt AUTHORS ChangeLog COPYING README
%endif

%files array
%defattr(644,root,root,755)
%{_datadir}/ibus-table/icons/array30.*
%{_datadir}/ibus-table/tables/array30.db
%{_datadir}/ibus-table/icons/array30-big.*
%{_datadir}/ibus-table/tables/array30-big.db

%files cangjie
%defattr(644,root,root,755)
%{_datadir}/ibus-table/icons/cangjie3.*
%{_datadir}/ibus-table/tables/cangjie3.db
%{_datadir}/ibus-table/icons/cangjie5.*
%{_datadir}/ibus-table/tables/cangjie5.db
%{_datadir}/ibus-table/icons/cangjie-big.*
%{_datadir}/ibus-table/tables/cangjie-big.db

%files cantonese
%defattr(644,root,root,755)
%{_datadir}/ibus-table/icons/cantonese.*
%{_datadir}/ibus-table/tables/cantonese.db
%{_datadir}/ibus-table/icons/cantonhk.*
%{_datadir}/ibus-table/tables/cantonhk.db
%{_datadir}/ibus-table/icons/jyutping.*
%{_datadir}/ibus-table/tables/jyutping.db

%files easy
%defattr(644,root,root,755)
%{_datadir}/ibus-table/icons/easy-big.*
%{_datadir}/ibus-table/tables/easy-big.db

%files erbi
%defattr(644,root,root,755)
%{_datadir}/ibus-table/icons/erbi.*
%{_datadir}/ibus-table/tables/erbi.db
%{_datadir}/ibus-table/icons/erbi-qs.*
%{_datadir}/ibus-table/tables/erbi-qs.db

%files quick
%defattr(644,root,root,755)
%{_datadir}/ibus-table/icons/quick3.*
%{_datadir}/ibus-table/tables/quick3.db
%{_datadir}/ibus-table/icons/quick5.*
%{_datadir}/ibus-table/tables/quick5.db
%{_datadir}/ibus-table/icons/quick-classic.*
%{_datadir}/ibus-table/tables/quick-classic.db

%files scj
%defattr(644,root,root,755)
%{_datadir}/ibus-table/icons/scj6.*
%{_datadir}/ibus-table/tables/scj6.db


%files stroke5
%defattr(644,root,root,755)
%{_datadir}/ibus-table/icons/stroke5.*
%{_datadir}/ibus-table/tables/stroke5.db

%files wu
%defattr(644,root,root,755)
%{_datadir}/ibus-table/icons/wu.*
%{_datadir}/ibus-table/tables/wu.db

%files wubi-haifeng
%defattr(644,root,root,755)
%doc tables/wubi-haifeng/COPYING tables/wubi-haifeng/README
%{_datadir}/ibus-table/icons/wubi-haifeng86.*
%{_datadir}/ibus-table/tables/wubi-haifeng86.db

%files wubi-jidian
%defattr(644,root,root,755)
%{_datadir}/ibus-table/icons/wubi-jidian86.*
%{_datadir}/ibus-table/tables/wubi-jidian86.db

%files yong
%defattr(644,root,root,755)
%{_datadir}/ibus-table/icons/yong.*
%{_datadir}/ibus-table/tables/yong.db
