@echo off
rem Makefile for Sphinx documentation

set SPHINXBUILD=sphinx-build
set SOURCEDIR=source
set BUILDDIR=build

if "%1" == "" goto help

%SPHINXBUILD% -b %1 %SOURCEDIR% %BUILDDIR%/%1
if errorlevel 1 exit /b 1
goto end

:help
echo.Usage: make.bat [html|dirhtml|singlehtml|pickle|json|htmlhelp|qthelp|devhelp|epub|latex|latexpdf|text|man|texinfo|info|gettext|changes|linkcheck|doctest]
exit /b 1

:end
