// src/types/index.ts

export interface Material {
    id: string;
    name: string;
    unitPrice: number;
    unit: 'm2' | 'm3' | 'kg' | 'item' | 'meter';
  }
  
  export interface Labour {
    id: string;
    role: string;
    hourlyRate: number;
  }
  
  export interface QuoteLineItem {
    id: string;
    description: string;
    quantity: number;
    unitPrice: number;
    total: number;
  }
  
  export interface Quote {
    id: string;
    clientName: string;
    projectTitle: string;
    date: string;
    items: QuoteLineItem[];
    subtotal: number;
    vatRate: number; // e.g., 0.15 for 15% VAT
    vatAmount: number;
    total: number;
  }