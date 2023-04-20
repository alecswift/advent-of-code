
function main()
    gen_a = 883
    gen_b = 879
    part1 = 0
    gen_value(gen, factor) = (gen * factor) % 2147483647
    low(gen) = gen & 0x0000FFFF

    part_2_sol = part2(gen_a, gen_b, gen_value, low)
    print(part_2_sol, "\n")

    for _ = 1:40000000
        gen_a = gen_value(gen_a, 16807)
        gen_b = gen_value(gen_b, 48271)

        if low(gen_a) == low(gen_b)
            part1 += 1
        end
    end

    print(part1)

end

function part2(gen_a, gen_b, gen_value, low)
    count = 0

    for _ = 1:5000000
        while gen_a % 4 != 0
            gen_a = gen_value(gen_a, 16807)
        end
        
        while gen_b % 8 != 0
            gen_b = gen_value(gen_b, 48271)
        end

        if low(gen_a) == low(gen_b)
            count += 1
        end
        
        gen_a = gen_value(gen_a, 16807)
        gen_b = gen_value(gen_b, 48271)
    end

    return count
end


main()