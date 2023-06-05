function flux = heatflow(location,state, temperature, scale_heatflow, trench_length)
%HEATFLOW Summary of this function goes here
%   Detailed explanation goes here
time=round(state.time);
 if ~isnan(state.time)
    flux = location.y;
    z_scale=1;
    %calculate difference until openings of burning chamber and scale heat
    %flow
    dsurf = abs(location.z-trench_length);
    if dsurf <=500
        z_scale=dsurf*0.001+0.5;
    end
    if location.z <=500
        
        z_scale=location.z*0.001+0.5;
    end
    
    try 
        if time == 0
            time = time+1;
        end
        
        flux(:)=temperature(time)*scale_heatflow*z_scale;
        if time > 30*3600
            flux(:)=0;
        end

        return
    end
 else
     flux = nan(1, length(location.x));
 end
end

