﻿#pragma checksum "..\..\..\Manager\List_Edit.xaml" "{8829d00f-11b8-4213-878b-770e8597ac16}" "44A7A82238D698F788AEF921F3A39883C0DDD353C205E1C1B01EB004A7A6DD70"
//------------------------------------------------------------------------------
// <auto-generated>
//     이 코드는 도구를 사용하여 생성되었습니다.
//     런타임 버전:4.0.30319.42000
//
//     파일 내용을 변경하면 잘못된 동작이 발생할 수 있으며, 코드를 다시 생성하면
//     이러한 변경 내용이 손실됩니다.
// </auto-generated>
//------------------------------------------------------------------------------

using MahApps.Metro;
using MahApps.Metro.Accessibility;
using MahApps.Metro.Actions;
using MahApps.Metro.Automation.Peers;
using MahApps.Metro.Behaviors;
using MahApps.Metro.Controls;
using MahApps.Metro.Controls.Dialogs;
using MahApps.Metro.Converters;
using MahApps.Metro.IconPacks;
using MahApps.Metro.IconPacks.Converter;
using MahApps.Metro.Markup;
using MahApps.Metro.Theming;
using MahApps.Metro.ValueBoxes;
using StudentCard;
using System;
using System.Diagnostics;
using System.Windows;
using System.Windows.Automation;
using System.Windows.Controls;
using System.Windows.Controls.Primitives;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Ink;
using System.Windows.Input;
using System.Windows.Markup;
using System.Windows.Media;
using System.Windows.Media.Animation;
using System.Windows.Media.Effects;
using System.Windows.Media.Imaging;
using System.Windows.Media.Media3D;
using System.Windows.Media.TextFormatting;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Windows.Shell;


namespace StudentCard {
    
    
    /// <summary>
    /// List_Edit
    /// </summary>
    public partial class List_Edit : MahApps.Metro.Controls.MetroWindow, System.Windows.Markup.IComponentConnector {
        
        
        #line 25 "..\..\..\Manager\List_Edit.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.TextBox TxtStudentId;
        
        #line default
        #line hidden
        
        
        #line 28 "..\..\..\Manager\List_Edit.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.TextBox TxtStudentName;
        
        #line default
        #line hidden
        
        
        #line 33 "..\..\..\Manager\List_Edit.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.TextBox TxtBirthday;
        
        #line default
        #line hidden
        
        
        #line 36 "..\..\..\Manager\List_Edit.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.ComboBox CboMajor;
        
        #line default
        #line hidden
        
        
        #line 41 "..\..\..\Manager\List_Edit.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.TextBox TxtPhoneNum;
        
        #line default
        #line hidden
        
        
        #line 44 "..\..\..\Manager\List_Edit.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.TextBox TxtAddress;
        
        #line default
        #line hidden
        
        
        #line 55 "..\..\..\Manager\List_Edit.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.RadioButton RdoMale;
        
        #line default
        #line hidden
        
        
        #line 56 "..\..\..\Manager\List_Edit.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.RadioButton RdoFemale;
        
        #line default
        #line hidden
        
        
        #line 58 "..\..\..\Manager\List_Edit.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.Button BtnNew;
        
        #line default
        #line hidden
        
        
        #line 59 "..\..\..\Manager\List_Edit.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.Button BtnClose;
        
        #line default
        #line hidden
        
        private bool _contentLoaded;
        
        /// <summary>
        /// InitializeComponent
        /// </summary>
        [System.Diagnostics.DebuggerNonUserCodeAttribute()]
        [System.CodeDom.Compiler.GeneratedCodeAttribute("PresentationBuildTasks", "4.0.0.0")]
        public void InitializeComponent() {
            if (_contentLoaded) {
                return;
            }
            _contentLoaded = true;
            System.Uri resourceLocater = new System.Uri("/StudentCard;component/manager/list_edit.xaml", System.UriKind.Relative);
            
            #line 1 "..\..\..\Manager\List_Edit.xaml"
            System.Windows.Application.LoadComponent(this, resourceLocater);
            
            #line default
            #line hidden
        }
        
        [System.Diagnostics.DebuggerNonUserCodeAttribute()]
        [System.CodeDom.Compiler.GeneratedCodeAttribute("PresentationBuildTasks", "4.0.0.0")]
        [System.ComponentModel.EditorBrowsableAttribute(System.ComponentModel.EditorBrowsableState.Never)]
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Design", "CA1033:InterfaceMethodsShouldBeCallableByChildTypes")]
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Maintainability", "CA1502:AvoidExcessiveComplexity")]
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1800:DoNotCastUnnecessarily")]
        void System.Windows.Markup.IComponentConnector.Connect(int connectionId, object target) {
            switch (connectionId)
            {
            case 1:
            
            #line 11 "..\..\..\Manager\List_Edit.xaml"
            ((StudentCard.List_Edit)(target)).Loaded += new System.Windows.RoutedEventHandler(this.MetroWindow_Loaded);
            
            #line default
            #line hidden
            return;
            case 2:
            this.TxtStudentId = ((System.Windows.Controls.TextBox)(target));
            
            #line 25 "..\..\..\Manager\List_Edit.xaml"
            this.TxtStudentId.KeyDown += new System.Windows.Input.KeyEventHandler(this.TxtStudentId_KeyDown);
            
            #line default
            #line hidden
            return;
            case 3:
            this.TxtStudentName = ((System.Windows.Controls.TextBox)(target));
            
            #line 28 "..\..\..\Manager\List_Edit.xaml"
            this.TxtStudentName.KeyDown += new System.Windows.Input.KeyEventHandler(this.TxtStudentName_KeyDown);
            
            #line default
            #line hidden
            return;
            case 4:
            this.TxtBirthday = ((System.Windows.Controls.TextBox)(target));
            
            #line 33 "..\..\..\Manager\List_Edit.xaml"
            this.TxtBirthday.KeyDown += new System.Windows.Input.KeyEventHandler(this.TxtBirthday_KeyDown);
            
            #line default
            #line hidden
            return;
            case 5:
            this.CboMajor = ((System.Windows.Controls.ComboBox)(target));
            
            #line 36 "..\..\..\Manager\List_Edit.xaml"
            this.CboMajor.KeyDown += new System.Windows.Input.KeyEventHandler(this.CboMajor_KeyDown);
            
            #line default
            #line hidden
            return;
            case 6:
            this.TxtPhoneNum = ((System.Windows.Controls.TextBox)(target));
            
            #line 41 "..\..\..\Manager\List_Edit.xaml"
            this.TxtPhoneNum.KeyDown += new System.Windows.Input.KeyEventHandler(this.TxtPhoneNum_KeyDown);
            
            #line default
            #line hidden
            return;
            case 7:
            this.TxtAddress = ((System.Windows.Controls.TextBox)(target));
            
            #line 44 "..\..\..\Manager\List_Edit.xaml"
            this.TxtAddress.KeyDown += new System.Windows.Input.KeyEventHandler(this.TxtAddress_KeyDown);
            
            #line default
            #line hidden
            return;
            case 8:
            this.RdoMale = ((System.Windows.Controls.RadioButton)(target));
            return;
            case 9:
            this.RdoFemale = ((System.Windows.Controls.RadioButton)(target));
            return;
            case 10:
            this.BtnNew = ((System.Windows.Controls.Button)(target));
            
            #line 58 "..\..\..\Manager\List_Edit.xaml"
            this.BtnNew.Click += new System.Windows.RoutedEventHandler(this.BtnNew_Click);
            
            #line default
            #line hidden
            return;
            case 11:
            this.BtnClose = ((System.Windows.Controls.Button)(target));
            
            #line 59 "..\..\..\Manager\List_Edit.xaml"
            this.BtnClose.Click += new System.Windows.RoutedEventHandler(this.BtnClose_Click);
            
            #line default
            #line hidden
            return;
            }
            this._contentLoaded = true;
        }
    }
}
