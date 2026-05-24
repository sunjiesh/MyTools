#!/usr/bin/env python3
"""
RegexTester - 正则表达式测试工具
使用轻量级框架tkinter，支持跨平台
"""

import sys
import re
import platform

try:
    import tkinter as tk
    from tkinter import ttk, messagebox, scrolledtext
except ImportError:
    # 尝试使用Tkinter的备用名称
    try:
        import Tkinter as tk
        from Tkinter import ttk, messagebox, scrolledtext
    except ImportError:
        print("Error: tkinter is not available on this system.")
        print(f"Platform: {platform.system()}")
        sys.exit(1)


class RegexTesterApp:
    """正则表达式测试应用主类"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("RegexTester - 正则表达式测试工具")
        self._setup_ui()
        self._apply_styles()
    
    def _setup_ui(self):
        """初始化UI组件"""
        # 创建主容器
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 配置权重，使文本区域可扩展
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)
        main_frame.rowconfigure(3, weight=1)
        main_frame.rowconfigure(5, weight=1)
        
        # Source 标签和文本框
        ttk.Label(main_frame, text="Source (源文本):").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.text_source = scrolledtext.ScrolledText(
            main_frame, 
            height=8, 
            wrap=tk.WORD
        )
        self.text_source.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # Pattern 标签和文本框
        ttk.Label(main_frame, text="Pattern (正则表达式):").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.text_pattern = scrolledtext.ScrolledText(
            main_frame, 
            height=4, 
            wrap=tk.WORD
        )
        self.text_pattern.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # 选项框架
        options_frame = ttk.LabelFrame(main_frame, text="选项", padding="5")
        options_frame.grid(row=4, column=0, columnspan=2, sticky=tk.W, pady=5)
        
        # 正则表达式选项
        self.var_ignore_case = tk.BooleanVar(value=False)
        self.var_multiline = tk.BooleanVar(value=False)
        self.var_dotall = tk.BooleanVar(value=False)
        
        ttk.Checkbutton(
            options_frame, 
            text="忽略大小写 (IGNORECASE)", 
            variable=self.var_ignore_case
        ).grid(row=0, column=0, padx=5)
        
        ttk.Checkbutton(
            options_frame, 
            text="多行模式 (MULTILINE)", 
            variable=self.var_multiline
        ).grid(row=0, column=1, padx=5)
        
        ttk.Checkbutton(
            options_frame, 
            text="点匹配所有 (DOTALL)", 
            variable=self.var_dotall
        ).grid(row=0, column=2, padx=5)
        
        # 按钮区域
        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(row=6, column=0, columnspan=2, pady=10)
        
        self.btn_run = ttk.Button(btn_frame, text="执行 (Run)", command=self.run_test)
        self.btn_run.pack(side=tk.LEFT, padx=5)
        
        self.btn_clear = ttk.Button(btn_frame, text="清空 (Clear)", command=self.clear_all)
        self.btn_clear.pack(side=tk.LEFT, padx=5)
        
        # Result 标签和文本框
        ttk.Label(main_frame, text="Result (匹配结果):").grid(row=7, column=0, sticky=tk.W, pady=5)
        self.text_result = scrolledtext.ScrolledText(
            main_frame, 
            height=10, 
            wrap=tk.WORD,
            state=tk.DISABLED
        )
        self.text_result.grid(row=8, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
    
    def _apply_styles(self):
        """应用样式配置"""
        style = ttk.Style()
        # 尝试使用系统原生主题
        try:
            style.theme_use('clam')
        except tk.TclError:
            pass
        
        # 配置字体
        font_config = ('Consolas', 10) if platform.system() == 'Windows' else ('Monospace', 10)
        self.text_source.configure(font=font_config)
        self.text_pattern.configure(font=font_config)
        self.text_result.configure(font=font_config)
    
    def run_test(self):
        """执行正则表达式测试"""
        source_text = self.text_source.get("1.0", tk.END).strip()
        pattern_text = self.text_pattern.get("1.0", tk.END).strip()
        
        if not source_text:
            messagebox.showwarning("警告", "请输入 Source (源文本)")
            return
        
        if not pattern_text:
            messagebox.showwarning("警告", "请输入 Pattern (正则表达式)")
            return
        
        try:
            # 构建正则表达式标志
            flags = re.MULTILINE
            if self.var_ignore_case.get():
                flags |= re.IGNORECASE
            if self.var_multiline.get():
                flags |= re.MULTILINE
            if self.var_dotall.get():
                flags |= re.DOTALL
            
            # 编译正则表达式
            compiled_pattern = re.compile(pattern_text, flags)
            
            # 执行匹配
            matches = compiled_pattern.findall(source_text)
            
            # 显示结果
            self._display_results(matches, compiled_pattern, source_text)
            
        except re.error as e:
            messagebox.showerror("正则表达式错误", f"无效的正则表达式:\n{e}")
        except Exception as e:
            messagebox.showerror("错误", f"发生错误:\n{e}")
    
    def _display_results(self, matches, compiled_pattern, source_text):
        """显示匹配结果"""
        self.text_result.config(state=tk.NORMAL)
        self.text_result.delete("1.0", tk.END)
        
        if not matches:
            self.text_result.insert("1.0", "没有找到符合条件的字符串")
        else:
            result_lines = []
            result_lines.append(f"找到 {len(matches)} 个匹配项:\n")
            result_lines.append("=" * 50 + "\n\n")
            
            for i, match in enumerate(matches, 1):
                result_lines.append(f"匹配 #{i}: {repr(match)}\n")
            
            result_lines.append("\n" + "=" * 50 + "\n")
            result_lines.append("详细匹配信息:\n\n")
            
            # 显示匹配位置
            for match in compiled_pattern.finditer(source_text):
                start = match.start()
                end = match.end()
                result_lines.append(f"位置 {start}-{end}: '{match.group()}'\n")
            
            self.text_result.insert("1.0", "".join(result_lines))
        
        self.text_result.config(state=tk.DISABLED)
    
    def clear_all(self):
        """清空所有输入和输出"""
        self.text_source.delete("1.0", tk.END)
        self.text_pattern.delete("1.0", tk.END)
        self.text_result.config(state=tk.NORMAL)
        self.text_result.delete("1.0", tk.END)
        self.text_result.config(state=tk.DISABLED)
        self.var_ignore_case.set(False)
        self.var_multiline.set(False)
        self.var_dotall.set(False)


def main():
    """主函数"""
    root = tk.Tk()
    
    # 设置窗口图标和属性（如果可用）
    try:
        root.title("RegexTester")
    except Exception:
        pass
    
    app = RegexTesterApp(root)
    
    # 设置窗口大小和位置
    window_width = 800
    window_height = 700
    
    # 获取屏幕尺寸
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # 计算居中位置
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    # 运行应用
    root.mainloop()


if __name__ == '__main__':
    main()