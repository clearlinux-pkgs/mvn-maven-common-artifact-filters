#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-maven-common-artifact-filters
Version  : 1.4
Release  : 6
URL      : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-common-artifact-filters/1.4/maven-common-artifact-filters-1.4.jar
Source0  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-common-artifact-filters/1.4/maven-common-artifact-filters-1.4.jar
Source1  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-common-artifact-filters/1.0-alpha-1/maven-common-artifact-filters-1.0-alpha-1.jar
Source2  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-common-artifact-filters/1.0-alpha-1/maven-common-artifact-filters-1.0-alpha-1.pom
Source3  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-common-artifact-filters/1.3/maven-common-artifact-filters-1.3.jar
Source4  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-common-artifact-filters/1.3/maven-common-artifact-filters-1.3.pom
Source5  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-common-artifact-filters/1.4/maven-common-artifact-filters-1.4.pom
Source6  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-common-artifact-filters/3.0.0/maven-common-artifact-filters-3.0.0.jar
Source7  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-common-artifact-filters/3.0.0/maven-common-artifact-filters-3.0.0.pom
Source8  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-common-artifact-filters/3.0.1/maven-common-artifact-filters-3.0.1.jar
Source9  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-common-artifact-filters/3.0.1/maven-common-artifact-filters-3.0.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-maven-common-artifact-filters-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-maven-common-artifact-filters package.
Group: Data

%description data
data components for the mvn-maven-common-artifact-filters package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-common-artifact-filters/1.4
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-common-artifact-filters/1.4/maven-common-artifact-filters-1.4.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-common-artifact-filters/1.0-alpha-1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-common-artifact-filters/1.0-alpha-1/maven-common-artifact-filters-1.0-alpha-1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-common-artifact-filters/1.0-alpha-1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-common-artifact-filters/1.0-alpha-1/maven-common-artifact-filters-1.0-alpha-1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-common-artifact-filters/1.3
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-common-artifact-filters/1.3/maven-common-artifact-filters-1.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-common-artifact-filters/1.3
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-common-artifact-filters/1.3/maven-common-artifact-filters-1.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-common-artifact-filters/1.4
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-common-artifact-filters/1.4/maven-common-artifact-filters-1.4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-common-artifact-filters/3.0.0
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-common-artifact-filters/3.0.0/maven-common-artifact-filters-3.0.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-common-artifact-filters/3.0.0
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-common-artifact-filters/3.0.0/maven-common-artifact-filters-3.0.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-common-artifact-filters/3.0.1
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-common-artifact-filters/3.0.1/maven-common-artifact-filters-3.0.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-common-artifact-filters/3.0.1
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-common-artifact-filters/3.0.1/maven-common-artifact-filters-3.0.1.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-common-artifact-filters/1.0-alpha-1/maven-common-artifact-filters-1.0-alpha-1.jar
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-common-artifact-filters/1.0-alpha-1/maven-common-artifact-filters-1.0-alpha-1.pom
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-common-artifact-filters/1.3/maven-common-artifact-filters-1.3.jar
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-common-artifact-filters/1.3/maven-common-artifact-filters-1.3.pom
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-common-artifact-filters/1.4/maven-common-artifact-filters-1.4.jar
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-common-artifact-filters/1.4/maven-common-artifact-filters-1.4.pom
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-common-artifact-filters/3.0.0/maven-common-artifact-filters-3.0.0.jar
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-common-artifact-filters/3.0.0/maven-common-artifact-filters-3.0.0.pom
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-common-artifact-filters/3.0.1/maven-common-artifact-filters-3.0.1.jar
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-common-artifact-filters/3.0.1/maven-common-artifact-filters-3.0.1.pom
