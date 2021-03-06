import Function as f;

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] < 6)
         {
            f.SkillWait(cp, 80);

            if (Bring(cp, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill") 
            && Deaths(cp, AtLeast, f.UltimateA[cp], " `UltimateCoolTime"))
            {
               f.Voice_Routine(cp, 5);
               f.wait[cp] = 0;
               f.count[cp] = 0;
               f.loop[cp] = 0;
               f.step[cp] = 310;
               SetDeaths(cp, Subtract, f.UltimateA[cp], " `UltimateCoolTime");
               KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", cp);
            }
            else {
               f.loop[cp] += 1;
            }

         }
         else if (f.loop[cp] == 6)
         {                        
            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }

      }


      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 4)
         {          
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.SquareShape(cp, 1, "40 + 1n Wraith", 50 + 25 * f.loop[cp], 0);
            f.SquareShape(cp, 1, "40 + 1n Zealot", 50 + 25 * f.loop[cp], 0);

            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] < 12)
         {                        
            f.Table_Sin(cp, 22 + 22 * (f.loop[cp] % 4), 200 - 25 * (f.loop[cp] - 4));
            f.Table_Cos(cp, 22 + 22 * (f.loop[cp] % 4), 200 - 25 * (f.loop[cp] - 4));

            f.SquareShape(cp, 1, "40 + 1n Wraith", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp]);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 12)
         {                        
            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }

      }
      else if (f.count[cp] == 2)
      {
         if (f.loop[cp] < 4)
         {       
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.Table_Sin(cp, 22 + 45 * (f.loop[cp] % 4), 75);
            f.Table_Cos(cp, 22 + 45 * (f.loop[cp] % 4), 75);

            f.SquareShape(cp, 1, "40 + 1n Wraith", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 4, "40 + 1n Zealot", f.CosAngle[cp], f.SinAngle[cp]);
            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {         
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;

         }
      }
      else if (f.count[cp] == 3)
      {
         f.SkillEnd(cp);
      }
   }
}