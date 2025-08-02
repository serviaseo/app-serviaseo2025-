document.addEventListener('DOMContentLoaded', function() {
    // Form validation
    const forms = document.querySelectorAll('.needs-validation');
    
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });

    // Auto-dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Add animation to table rows
    const tableRows = document.querySelectorAll('tbody tr');
    tableRows.forEach((row, index) => {
        row.style.animationDelay = `${index * 0.1}s`;
    });

    // Navbar scroll effect
    const navbar = document.querySelector('.navbar-modern');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Navbar link hover effect
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('mouseenter', () => {
            link.style.transform = 'translateY(-2px)';
        });
        link.addEventListener('mouseleave', () => {
            link.style.transform = 'translateY(0)';
        });
    });

    // Mobile menu animation
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    
    navbarToggler.addEventListener('click', () => {
        navbarCollapse.classList.toggle('show');
    });

    // Funcionalidad de edición
    document.querySelectorAll('.edit-btn').forEach(button => {
        button.addEventListener('click', function() {
            const row = this.closest('tr');
            row.classList.add('editing');
        });
    });

    // Funcionalidad de cancelar edición
    document.querySelectorAll('.cancel-btn').forEach(button => {
        button.addEventListener('click', function() {
            const row = this.closest('tr');
            row.classList.remove('editing');
        });
    });

    // Funcionalidad de guardar edición
    document.querySelectorAll('.save-btn').forEach(button => {
        button.addEventListener('click', function() {
            const row = this.closest('tr');
            const id = this.dataset.id;
            const nombre = row.querySelector('[name="nombre"]').value;
            const email = row.querySelector('[name="email"]').value;
            const programa = row.querySelector('[name="programa"]').value;

            // Enviar datos al servidor
            fetch(`/editar/${id}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    nombre: nombre,
                    email: email,
                    programa: programa
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Actualizar la vista
                    row.querySelector('.view-mode:nth-child(1)').textContent = nombre;
                    row.querySelector('.view-mode:nth-child(2)').textContent = email;
                    row.querySelector('.view-mode .badge').textContent = programa;
                    row.classList.remove('editing');
                    
                    // Mostrar mensaje de éxito
                    const alert = document.createElement('div');
                    alert.className = 'alert alert-success alert-dismissible fade show';
                    alert.innerHTML = `
                        Registro actualizado exitosamente
                        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                    `;
                    document.querySelector('.card-body').insertBefore(alert, document.querySelector('.table-responsive'));
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error al actualizar el registro');
            });
        });
    });

    // Funcionalidad de eliminar
    document.querySelectorAll('.delete-btn').forEach(button => {
        button.addEventListener('click', function() {
            if (confirm('¿Estás seguro de que deseas eliminar este registro?')) {
                const id = this.dataset.id;
                const row = this.closest('tr');

                fetch(`/eliminar/${id}`, {
                    method: 'POST'
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        row.remove();
                        // Actualizar contador
                        const total = document.querySelector('.badge.bg-primary');
                        total.textContent = `Total: ${parseInt(total.textContent.split(': ')[1]) - 1}`;
                        
                        // Mostrar mensaje de éxito
                        const alert = document.createElement('div');
                        alert.className = 'alert alert-success alert-dismissible fade show';
                        alert.innerHTML = `
                            Registro eliminado exitosamente
                            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                        `;
                        document.querySelector('.card-body').insertBefore(alert, document.querySelector('.table-responsive'));
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('Error al eliminar el registro');
                });
            }
        });
    });
}); 