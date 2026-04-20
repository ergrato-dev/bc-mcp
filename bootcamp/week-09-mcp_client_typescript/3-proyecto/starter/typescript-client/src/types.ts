// types.ts — Interfaces compartidas del proyecto Library CLI TypeScript

export interface Book {
  id: number;
  title: string;
  author: string;
  year: number;
  isbn?: string | null;
}

export interface BookStats {
  total_books: number;
  books_with_isbn: number;
  average_year: number;
}

export interface OpenLibraryResult {
  title: string;
  author: string;
  year?: number;
  isbn?: string;
}
