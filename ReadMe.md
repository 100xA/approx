# PDF to Obsidian Vault Summarizer

This project aims to build an intelligent agent that processes PDF documents and transforms them into summarized markdown documents, structured according to your existing Obsidian vault structure.

## Project Overview

The system takes a PDF file as input, extracts its content, and generates a summarized version in markdown format. The summary is then organized to fit seamlessly into your Obsidian vault, maintaining the existing structure and creating relevant connections.

## System Architecture

The system architecture consists of several key components:

1. **PDF Processor**: This module is responsible for reading PDF files and extracting text content. It utilizes the PyPDF2 library to handle various PDF formats and ensure accurate text extraction.

2. **Text Summarizer**: Once the text is extracted, this component processes the content to generate concise summaries. It employs natural language processing techniques to identify key points and themes within the text.

3. **Markdown Formatter**: After summarization, the text is converted into markdown format. This module ensures that the output is compatible with Obsidian's markdown requirements, including proper headings, lists, and links.

4. **Obsidian Vault Integrator**: This component manages the organization of the summarized markdown files within the user's Obsidian vault. It creates a structured folder hierarchy and establishes connections between related notes to enhance navigation and context.

5. **User Interface**: A simple command-line interface allows users to input PDF files and specify their desired output locations within the Obsidian vault. This interface guides users through the process, making it accessible even for those with minimal technical expertise.

Overall, the system is designed to streamline the workflow of converting PDF documents into useful, organized notes that can be easily accessed and referenced within the Obsidian environment.

## System Architecture Diagram

![System Architecture Diagramm](/assets/system_architecture_mermaid.png)