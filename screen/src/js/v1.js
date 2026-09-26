(() => {
// --- V1 (OLD) JS LOGIC ---
// Stage 7: Frontend Engineer Interactivity
    document.addEventListener('DOMContentLoaded', () => {

      // 0. Prototype Navigation
      const plumberBtnOld = document.getElementById('plumber-category-btn-old');
        const popularPlumberCardOld = document.getElementById('popular-plumber-card-old');
        if (popularPlumberCardOld) {
          popularPlumberCardOld.addEventListener('click', () => {
            if (window.getIsPlaying && window.getIsPlaying()) {
              window.navigateTo('screen-v1-workerlist');
            }
          });
        }
      if (plumberBtnOld) {
        plumberBtnOld.addEventListener('click', () => {
          if (window.getIsPlaying && window.getIsPlaying()) {
            window.navigateTo('screen-v1-workerlist');
          }
        });
      }

      const workerListCardOld = document.getElementById('workerlist-card-1-old');
      if (workerListCardOld) {
        workerListCardOld.addEventListener('click', () => {
          if (window.getIsPlaying && window.getIsPlaying()) {
            window.navigateTo('screen-v1-worker');
          }
        });
      }

      const backBtnWorkerOld = document.getElementById('back-btn-worker-old');
      if (backBtnWorkerOld) {
        backBtnWorkerOld.addEventListener('click', () => {
          if (window.getIsPlaying && window.getIsPlaying()) {
            window.navigateTo('screen-v1-workerlist');
          }
        });
      }

      // 1. Follow Button Interaction
      const followBtn = document.getElementById('follow-btn-old');
      if (followBtn) {
        let isFollowing = false;
        followBtn.addEventListener('click', () => {
          const rect = followBtn.querySelector('rect');
          const text = followBtn.querySelector('text');
          if (!isFollowing) {
            rect.setAttribute('fill', '#F3F4F6');
            rect.setAttribute('stroke', '#F3F4F6');
            text.setAttribute('fill', '#4B5563');
            text.textContent = 'Following';
            isFollowing = true;
          } else {
            rect.setAttribute('fill', 'none');
            rect.setAttribute('stroke', '#1D4ED8');
            text.setAttribute('fill', '#1D4ED8');
            text.textContent = 'Follow';
            isFollowing = false;
          }
        });
      }

      // 1.5. Dropdown Menu
      const menuBtn = document.getElementById('menu-btn-old');
      const dropdownMenu = document.getElementById('dropdown-menu-old');
      if (menuBtn && dropdownMenu) {
        menuBtn.addEventListener('click', (e) => {
          e.stopPropagation();
          const current = dropdownMenu.getAttribute('display');
          dropdownMenu.setAttribute('display', current === 'none' ? 'block' : 'none');
        });
        document.addEventListener('click', () => {
          dropdownMenu.setAttribute('display', 'none');
        });
      }
      // 2. Tabs Interaction
      const workerSvgOldForTabs = document.getElementById('old-worker-profile-svg');
      const tabsGroup = workerSvgOldForTabs ? workerSvgOldForTabs.querySelector('g[transform="translate(24, 230)"]') : null;
      if (tabsGroup) {
        const tabs = [
          { text: 'Photos', x: 34, width: 76, rx: '-4' },
          { text: 'Reviews', x: 110, width: 85, rx: '68' },
          { text: 'Availability', x: 195, width: 95, rx: '148' },
          { text: 'About', x: 270, width: 70, rx: '235' }
        ];
        
        // Remove existing static rect/text
        tabsGroup.innerHTML = '';
        
        // Rebuild interactive tabs
        let activeBg = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        activeBg.setAttribute('y', '-8');
        activeBg.setAttribute('height', '32');
        activeBg.setAttribute('rx', '16');
        activeBg.setAttribute('fill', '#2563EB');
        tabsGroup.appendChild(activeBg);

        let currentActive = 0;
        
        const tabContents = [
          document.getElementById('tab-content-photos-old'),
          document.getElementById('tab-content-reviews-old'),
          document.getElementById('tab-content-availability-old'),
          document.getElementById('tab-content-about-old')
        ];

        tabs.forEach((tab, index) => {
          let textNode = document.createElementNS('http://www.w3.org/2000/svg', 'text');
          textNode.setAttribute('x', tab.x);
          textNode.setAttribute('y', '13');
          textNode.setAttribute('class', 'font-sans');
          textNode.setAttribute('font-size', '14');
          textNode.setAttribute('font-weight', '600');
          textNode.setAttribute('text-anchor', 'middle');
          textNode.style.cursor = 'pointer';
          textNode.textContent = tab.text;
          
          if (index === currentActive) {
            activeBg.setAttribute('x', tab.rx);
            activeBg.setAttribute('width', tab.width);
            textNode.setAttribute('fill', '#FFFFFF');
          } else {
            textNode.setAttribute('fill', '#6B7280');
          }
          
          textNode.addEventListener('click', () => {
            // Update Background position smoothly
            activeBg.style.transition = 'all 0.3s ease';
            activeBg.setAttribute('x', tab.rx);
            activeBg.setAttribute('width', tab.width);
            
            // Reset all text colors
            tabsGroup.querySelectorAll('text').forEach(t => t.setAttribute('fill', '#6B7280'));
            // Set active text color
            textNode.setAttribute('fill', '#FFFFFF');
            
            // Swap Content Visibility
            tabContents.forEach((tc, i) => {
              if (tc) {
                if (i === index) tc.removeAttribute('display');
                else tc.setAttribute('display', 'none');
              }
            });
          });

          tabsGroup.appendChild(textNode);
        });
      }

      // 3. Image Lightbox
      const lightbox = document.getElementById('lightbox-old');
      const lightboxImg = document.getElementById('lightbox-img-old');
      const lightboxClose = document.getElementById('lightbox-close-old');
      const workerProfileSvgOld = document.getElementById('old-worker-profile-svg');
      const photos = workerProfileSvgOld ? workerProfileSvgOld.querySelectorAll('.photo-thumbnail') : [];
      if (lightbox && lightboxImg && lightboxClose) {
        photos.forEach(photo => {
          photo.addEventListener('click', () => {
            lightboxImg.setAttribute('href', photo.getAttribute('href').split('?')[0]);
            lightbox.removeAttribute('display');
          });
        });
        lightboxClose.addEventListener('click', () => {
          lightbox.setAttribute('display', 'none');
        });
      }

      // 4. Star Rating and Submit Review
      const starsContainer = document.getElementById('review-stars-container-old');
      const reviewInputGroup = document.getElementById('review-input-group-old');
      const submitBtn = document.getElementById('submit-review-btn-old');
      if (starsContainer && reviewInputGroup && submitBtn) {
        const stars = starsContainer.querySelectorAll('.review-star');
        let selectedRating = 0;
        stars.forEach(star => {
          star.addEventListener('click', (e) => {
            selectedRating = parseInt(star.getAttribute('data-rating'));
            stars.forEach(s => {
              const r = parseInt(s.getAttribute('data-rating'));
              if (r <= selectedRating) {
                s.setAttribute('fill', '#F59E0B');
              } else {
                s.setAttribute('fill', 'none');
              }
            });
            reviewInputGroup.removeAttribute('display');
          });
        });

        submitBtn.addEventListener('click', () => {
          // Show new review and shift old ones down
          const newReview = document.getElementById('new-review-block-old');
          const oldReviews = document.getElementById('existing-reviews-old');
          
          newReview.removeAttribute('display');
          oldReviews.setAttribute('transform', 'translate(0, 136)');

          // Update star count in new review visually based on selected
          const newStars = newReview.querySelectorAll('path');
          newStars.forEach((s, i) => {
             if (i < selectedRating) s.setAttribute('fill', '#F59E0B');
             else s.setAttribute('fill', 'none');
          });

          // Reset Input form
          reviewInputGroup.setAttribute('display', 'none');
          stars.forEach(s => s.setAttribute('fill', 'none'));
          selectedRating = 0;
        });
      }

      // 5. Vertical Scrolling Simulation
      const scrollContent = document.getElementById('scrollable-content-old');
      let currentScroll = 0;
      let startY = 0;
      
      const updateScroll = (dy) => {
         currentScroll += dy;
         if (currentScroll > 0) currentScroll = 0;
         if (currentScroll < -600) currentScroll = -600;
         scrollContent.setAttribute('transform', `translate(0, ${currentScroll})`);
      };

      const workerSvg = document.getElementById('old-worker-profile-svg');
      if (workerSvg && scrollContent) {
        workerSvg.addEventListener('wheel', (e) => {
           updateScroll(-e.deltaY);
        });

        workerSvg.addEventListener('touchstart', (e) => {
           startY = e.touches[0].clientY;
        });

        workerSvg.addEventListener('touchmove', (e) => {
           const dy = e.touches[0].clientY - startY;
           startY = e.touches[0].clientY;
           updateScroll(dy);
           e.preventDefault();
        }, { passive: false });

        // Mouse drag-to-scroll for laptops
        let isDragging = false;
        workerSvg.addEventListener('mousedown', (e) => {
           isDragging = true;
           startY = e.clientY;
        });

        window.addEventListener('mousemove', (e) => {
           if (!isDragging) return;
           const dy = e.clientY - startY;
           // Only scroll if moved a bit to avoid jitter
           if (Math.abs(dy) > 1) {
              startY = e.clientY;
              updateScroll(dy);
              e.preventDefault(); // Stop native drag
           }
        });

        const stopDrag = () => {
           isDragging = false;
        };
        
        window.addEventListener('mouseup', stopDrag);
        workerSvg.addEventListener('mouseleave', stopDrag);
      }

      // --- BROADCAST MODAL INTERACTION LOGIC (STAGE 7) ---
      const broadcastFab = document.getElementById('broadcast-fab-old');
      const broadcastModal = document.getElementById('broadcast-modal-old');
      const broadcastDimmer = document.getElementById('broadcast-dimmer-old');
      const closeBroadcastBtn = document.getElementById('close-broadcast-btn-old');
      const broadcastSheet = document.getElementById('broadcast-sheet-old');
      
      const broadcastScrollArea = document.getElementById('broadcast-scroll-area-old');
      const broadcastFooter = document.getElementById('broadcast-footer-old');
      const broadcastSubmitBtn = document.getElementById('broadcast-submit-btn-old');
      
      const radarState = document.getElementById('broadcast-radar-state-old');
      const successState = document.getElementById('broadcast-success-state-old');
      const viewWorkerBtn = document.getElementById('view-assigned-worker-btn-old');

      // Open Modal
      if (broadcastFab && broadcastModal) {
         broadcastFab.addEventListener('click', () => {
            // Reset states
            broadcastScrollArea.setAttribute('display', 'block');
            broadcastFooter.setAttribute('display', 'block');
            radarState.setAttribute('display', 'none');
            successState.setAttribute('display', 'none');
            
            // Show modal
            broadcastModal.setAttribute('display', 'block');
            // Small timeout to allow display:block to paint before transforming
            setTimeout(() => {
               broadcastSheet.setAttribute('transform', 'translate(20, 160)');
            }, 10);
         });
      }

      // Close Modal
      const closeBroadcastModal = () => {
         broadcastSheet.setAttribute('transform', 'translate(20, 812)');
         setTimeout(() => {
            broadcastModal.setAttribute('display', 'none');
         }, 300); // Wait for transition
      };

      if (closeBroadcastBtn) closeBroadcastBtn.addEventListener('click', closeBroadcastModal);
      if (broadcastDimmer) broadcastDimmer.addEventListener('click', closeBroadcastModal);
      if (viewWorkerBtn) viewWorkerBtn.addEventListener('click', closeBroadcastModal);

      // Pill Selection Logic
      const allPills = workerProfileSvgOld ? workerProfileSvgOld.querySelectorAll('.service-pills rect') : [];
      const allPillTexts = workerProfileSvgOld ? workerProfileSvgOld.querySelectorAll('.service-pills text') : [];
      
      allPills.forEach((pill, index) => {
         pill.style.cursor = 'pointer';
         allPillTexts[index].style.cursor = 'pointer';
         
         const handlePillClick = () => {
            // Deselect all
            allPills.forEach((p, i) => {
               p.setAttribute('fill', '#F3F4F6');
               p.removeAttribute('stroke');
               allPillTexts[i].setAttribute('fill', '#6B7280');
               allPillTexts[i].setAttribute('font-weight', '500');
            });
            // Select clicked
            pill.setAttribute('fill', '#EFF6FF');
            pill.setAttribute('stroke', '#2563EB');
            pill.setAttribute('stroke-width', '1.5');
            allPillTexts[index].setAttribute('fill', '#2563EB');
            allPillTexts[index].setAttribute('font-weight', '600');
         };
         
         pill.addEventListener('click', handlePillClick);
         allPillTexts[index].addEventListener('click', handlePillClick);
      });

      // Submit Broadcast Request
      if (broadcastSubmitBtn) {
         broadcastSubmitBtn.addEventListener('click', () => {
            // Hide Form, Show Radar
            broadcastScrollArea.setAttribute('display', 'none');
            broadcastFooter.setAttribute('display', 'none');
            radarState.setAttribute('display', 'block');
            
            // Simulate Network Request (3 seconds)
            setTimeout(() => {
               radarState.setAttribute('display', 'none');
               successState.setAttribute('display', 'block');
            }, 3000);
         });
      }

    });
  
    })();



