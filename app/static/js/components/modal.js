export function initModal() {
    function openExcelModal() {
        document.getElementById('excelModal').style.display = 'block';
    }

    function closeExcelModal() {
        document.getElementById('excelModal').style.display = 'none';
    }

    // Exponer funciones al scope global
    window.openExcelModal = openExcelModal;
    window.closeExcelModal = closeExcelModal;
} 